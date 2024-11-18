#!/usr/bin/python
import sys, os, re

path = sys.argv[1]
regex = re.compile(r"^-\s*\[.*\]\((.*)\)\s*")
if os.path.isfile(path):
    with open(path, 'r', encoding='utf-8') as file:
        modified_lines = []
        startofTOC = False
        for line_number, line in enumerate(file, start=1):
            match = regex.search(line)
            if not startofTOC:
                if match:
                    startofTOC = True
                    processText = f"""
```{{tocTree}}
:maxdepth: 4
:caption: Table of Contents

"""
                    modified_lines.append(processText + match.group(1) + "\n")
                else:
                    modified_lines.append(line)
            else:
                if match:
                    modified_lines.append(match.group(1) + "\n")
        # Add end
        modified_lines.append(r"```")
        with open(path, 'w', encoding='utf-8') as file:
            # Write all modified lines back to the file
            file.writelines(modified_lines)

