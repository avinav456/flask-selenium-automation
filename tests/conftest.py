import os, subprocess, time, signal, socket, contextlib, random, string
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

BASE_URL = os.environ.get("BASE_URL", "http://127.0.0.1:5000")

def wait_for_port(host, port, timeout=10.0):
    start = time.time()
    while time.time() - start < timeout:
        with contextlib.closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
            sock.settimeout(1)
            if sock.connect_ex((host, port)) == 0:
                return True
        time.sleep(0.2)
    raise RuntimeError("Server did not start on time")

@pytest.fixture(scope="session", autouse=True)
def server():
    env = os.environ.copy()
    env["FLASK_ENV"] = "testing"
    p = subprocess.Popen(["python", "app.py"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, env=env)
    try:
        wait_for_port("127.0.0.1", 5000, timeout=15)
        yield
    finally:
        if p.poll() is None:
            if os.name == "nt":
                p.terminate()
            else:
                os.killpg(os.getpgid(p.pid), signal.SIGTERM) if hasattr(os, "getpgid") else p.terminate()
        time.sleep(1)

@pytest.fixture
def driver():
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    with webdriver.Chrome(options=opts) as d:
        d.set_window_size(1280, 900)
        yield d

def rand_email():
    suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return f"user_{suffix}@example.com"

@pytest.fixture
def test_user():
    return {"name": "Test User", "email": rand_email(), "password": "Passw0rd!"}
