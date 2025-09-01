#!/usr/bin/env python3
import os
import argparse
import re

def main(input_path, container_name):
    with open(input_path, 'r') as file:
        content = file.read()

    pattern = re.compile(r"\/usr")
    local_path = os.path.expanduser("~/.local")
    replaced = pattern.sub(local_path, input_path)
    print(f"Processing {input_path} to {replaced}")

    with open(replaced, 'w') as file:
        for line in content.splitlines():
            if line.startswith("Exec="):
                original = line.split("=")[1]
                file.write(f"Exec=/usr/bin/toolbox run -c {container_name} {original}\n")
            elif line.startswith("TryExec="):
                file.write(f"TryExec=/usr/bin/toolbox\n")
            else:
                file.write(line + "\n")

if __name__ == "__main__":
    args = argparse.ArgumentParser(description="Process a .desktop file to modify Exec paths.")
    args.add_argument("input", help="Path to the .desktop file to process.")
    args.add_argument("container", help="Container name to use in the Exec command.")
    parsed_args = args.parse_args()
    main(parsed_args.input, parsed_args.container)

