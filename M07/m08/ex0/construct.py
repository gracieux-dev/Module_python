import site
import sys
import os

in_venv = sys.prefix != sys.base_prefix

if in_venv:
    print("MATRIX STATUS: Welcome to the construct")
else:
    print("MATRIX STATUS: You're still plugged in")
print(f"Current Python: {sys.executable}")
print(f"Virtual Environment: {os.environ.get("VIRTUAL_ENV")}\n")

if not in_venv:
    print()
    print("WARNING: You are in the global environment!")
    print("The machines can see everything you install.\n")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\\Scripts\\activate # On Windows\n")
    print("Then run this program again.")
if in_venv:
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.\n")
    print(f"Package installation path:")
    print(site.getsitepackages()[0])
