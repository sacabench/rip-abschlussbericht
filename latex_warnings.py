#!/usr/bin/env python3

import sys
import os
import subprocess
import re

re_warning = re.compile("Warning|Error")
re_path = re.compile("\\./.*?\\.tex")

cmd = sys.argv[1:]

process = subprocess.Popen(cmd,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT,
                           env={ "max_print_line": "10000" })

output = []
for line in iter(process.stdout.readline, b''):
    clean_line = line.decode("utf-8", "backslashreplace")
    output.append(clean_line)
    print(clean_line.strip()),

process.stdout.close()
returncode = process.wait()

for line in output:
    for m in re_path.findall(line):
        print("File {}".format(m))

    if re_warning.match(line):
        print(line.strip()),

exit(returncode)
