#!/usr/bin/python
import subprocess
import s2Parser
import s2ListConverter
[a, b] = s2Parser.s2parser("Sequencer LE.SC2Replay")
gamespeed = 1.666666
convList = s2ListConverter.listconverter(a, gamespeed)
convList.extend(s2ListConverter.listconverter(b, gamespeed))

for i in convList:
    if i != '\n':
        print "element:",i

#22.4 ticks per second

