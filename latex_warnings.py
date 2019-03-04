#!/usr/bin/env python3

import sys
import os
import subprocess
import re

re_warning = re.compile("Warning|Error")
re_path = re.compile("(\\./.*?\\.(pygtex|pygstyle|tex|pdf|png|toc|sty|w18))")

cmd = sys.argv[1:]

print("Wrapper script executes: {}".format(cmd))

env = os.environ.copy()
env["max_print_line"] = "10000"

process = subprocess.Popen(cmd,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT,
                           env=env)

output = []
for line in iter(process.stdout.readline, b''):
    clean_line = line.decode("utf-8", "backslashreplace")
    output.append(clean_line)
    print(clean_line.strip()),

process.stdout.close()
returncode = process.wait()

print("---Warnings and Errors ---------------------------------------------------------")

last_file = None
current_file = "asdf"
for line in output:
    for m in re_path.findall(line):
        last_file_candidate = "File {}".format(m[0])
        #print("[" + last_file_candidate + "]")
        if last_file_candidate.endswith(".tex"):
            last_file = last_file_candidate

    if re_warning.search(line):
        if current_file != last_file:
            print(last_file)
            current_file = last_file
        print("  " + line.strip()),

exit(returncode)
