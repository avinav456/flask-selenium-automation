import os, subprocess, time, socket, contextlib
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def wait_for_port(host, port, timeout=20.0):
    start = time.time()
    while time.time() - start < timeout:
        with contextlib.closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
            s.settimeout(1)
            if s.connect_ex((host, port)) == 0:
                return  True
        time.sleep(0.2)
    raise RuntimeError("Server did not start on time")

@pytest.fixture(scope="session", autouse=True)
def server():
    p = subprocess.Popen(
        ["python", "app.py"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT,
        start_new_session=True
    )
    try:
        wait_for_port("127.0.0.1", 5000, timeout=20)
        yield
    finally:
        try:
            p.terminate()
            p.wait(timeout=5)
        except Exception:
            try:
                p.kill()
            except Exception:
                pass
        time.sleep(0.5)

@pytest.fixture
def driver():
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--disable-gpu")
    with webdriver.Chrome(options=opts) as d:
        d.set_window_size(1280, 900)
        yield d
