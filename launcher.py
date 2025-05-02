import platform
import importlib

arch = platform.machine()
if 'aarch64' in arch:
    print("Detected 64-bit system. Running 64-bit module...")
    ap = importlib.import_module("ap_64bit")
elif 'arm' in arch:
    print("Detected 32-bit system. Running 32-bit module...")
    ap = importlib.import_module("ap_32bit")
else:
    print("Unsupported architecture:", arch)
    exit()

ap.main()
