import sys
import os
if sys.platform.startswith("linux"):
    print("linux")
elif os.name == "nt":
    print("windows")