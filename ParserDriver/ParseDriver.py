#!/usr/bin/python
import subprocess
import re

out = subprocess.Popen(["python.exe", "../s2protocol/s2protocol.py", "../s2protocol/Sequencer LE.SC2Replay",
                        "--trackerevents"],stdout=subprocess.PIPE)
output_list = out.stdout.readlines()
# for i in output_list:
#     if i != '\n':
#         print i,

concat_list = ''.join(output_list).split("{")
bornList = []
buildList = []
for str in concat_list:
    if "SUnitBornEvent" in str:
        bornList.append(str)
for str in concat_list:
    if "SUnitInitEvent" in str:
        buildList.append(str)

for i in buildList:
    if i != '\n':
        print "element:",i
