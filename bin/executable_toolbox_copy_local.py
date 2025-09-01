#!/usr/bin/env python3
import os
import re
import sys

def main():
    input = sys.argv[1]
    pattern = re.compile(r"\/usr")
    local_path = os.path.expanduser("~/.local")
    replaced = pattern.sub(local_path, input)
    print(f"Copying {input} to {replaced}")
    try:
        os.makedirs(os.path.dirname(replaced), exist_ok=True)
        with open(input, 'rb') as src_file:
            with open(replaced, 'wb') as dest_file:
                dest_file.write(src_file.read())
        print(f"Successfully copied to {replaced}")
    except Exception as e:
        print(f"Error copying file: {e}")

if __name__ == "__main__":
    main()
    if len(sys.argv) != 2:
        print("Usage: copy_local.py <path_to_file>")
        sys.exit(1)
