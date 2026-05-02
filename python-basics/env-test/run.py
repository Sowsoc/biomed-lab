import sys
import platform

print("=== Environment Check ===")
print(f"Python version: {sys.version}")
print(f"Platform: {platform.system()} {platform.release()}")

print("\nEnvironment OK")
