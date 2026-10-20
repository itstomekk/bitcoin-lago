#!/usr/bin/env python3
"""Start a local HTTP server and run QA + thumbnail generation against it."""
import os, sys, time, threading, subprocess
from http.server import HTTPServer, SimpleHTTPRequestHandler

ROOT = r"C:\Users\Lenovo\Hermes\projects\websites\bitcoin-lake-guatemala"
os.chdir(ROOT)
PORT = 18432

srv = HTTPServer(("127.0.0.1", PORT), SimpleHTTPRequestHandler)
t = threading.Thread(target=srv.serve_forever, daemon=True)
t.start()
print(f"Server started on 127.0.0.1:{PORT}", flush=True)

# Verify server works
import urllib.request
try:
    r = urllib.request.urlopen(f"http://127.0.0.1:{PORT}/", timeout=5)
    assert r.status == 200
    print("Server verified OK", flush=True)
except Exception as e:
    print(f"Server verification failed: {e}", flush=True)
    srv.shutdown()
    sys.exit(1)

# 1) Generate thumbnails (needs images served)
print("=== Generating thumbnails ===", flush=True)
ret = subprocess.run(
    [sys.executable, "qa/make_thumbs.py", f"http://127.0.0.1:{PORT}/"],
    cwd=ROOT, capture_output=True, text=True, timeout=120
)
print(f"make_thumbs exit: {ret.returncode}", flush=True)
if ret.stdout: print(ret.stdout[-500:], flush=True)
if ret.stderr: print("STDERR:", ret.stderr[-300:], flush=True)

# 2) Run variant QA for all finished designs
print("=== Running variant QA (a,c,d,ac,ad,cd) ===", flush=True)
ret = subprocess.run(
    [sys.executable, "qa/run_qa_variants.py", f"http://127.0.0.1:{PORT}/", "qa/.cache/shots-local", "a,c,d,ac,ad,cd"],
    cwd=ROOT, capture_output=True, text=True, timeout=300
)
print(f"run_qa_variants exit: {ret.returncode}", flush=True)
if ret.stdout: print(ret.stdout[-2000:], flush=True)
if ret.stderr: print("STDERR:", ret.stderr[-500:], flush=True)

# 3) Run baseline QA
print("=== Running baseline QA ===", flush=True)
ret = subprocess.run(
    [sys.executable, "qa/run_qa.py", f"http://127.0.0.1:{PORT}/", "qa/.cache/shots-qa"],
    cwd=ROOT, capture_output=True, text=True, timeout=300
)
print(f"run_qa exit: {ret.returncode}", flush=True)
if ret.stdout: print(ret.stdout[-2000:], flush=True)
if ret.stderr: print("STDERR:", ret.stderr[-500:], flush=True)

srv.shutdown()
print("Server stopped", flush=True)
