# Entry point
# AI Written

import os
import subprocess
import sys

# 1. Define the path to your actual project file
target_script = os.path.join("src", "MyLibrary.py")

# 2. Collect all arguments passed to this script (excluding the script name itself)
# sys.argv[1:] captures everything after 'python run.py'
passed_args = sys.argv[1:]

# 3. Construct the full command
# We use sys.executable to ensure we use the same Python version
command = [sys.executable, target_script] + passed_args

# 4. Execute
try:
    subprocess.run(command)

except KeyboardInterrupt:
    print("\nAborted by user! (Note: from entry point aka main.py")
    exit(0)  # Exit with a success code, not an error.
