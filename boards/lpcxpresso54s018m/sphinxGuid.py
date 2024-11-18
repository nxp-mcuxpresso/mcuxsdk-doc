#!/usr/bin/python
import sys, os, re

rootpath = sys.argv[1]
if not os.path.isdir(rootpath):
    print("Not valid folder")
    sys.exit(0)

regex = re.compile(r"\s+{#\w*-[0-9a-fA-F\-]*}")
for root, dirs, files in os.walk(rootpath):
    for path in files:
        if re.search(".*.md$", path):
            targetPath = os.path.join(root, path)
            modified_lines = []
            needModify = False
            with open(targetPath, 'r', encoding='utf-8') as file:
                for line_number, line in enumerate(file, start=1):
                    # Search for the pattern in the current line
                    match = regex.search(line)
                    if match:
                        line = regex.sub('', line)
                        if not needModify:
                            needModify = True
                    modified_lines.append(line)
            if needModify:
                print(f"process {path}")
                with open(targetPath, 'w', encoding='utf-8') as file:
                    # Write all modified lines back to the file
                    file.writelines(modified_lines)
