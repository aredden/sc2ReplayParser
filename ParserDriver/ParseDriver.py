#!/usr/bin/python
import subprocess
import Parser
import s2ListConverter
[a,b] = Parser.s2parser("Sequencer LE.SC2Replay")

convList = s2ListConverter.listconverter(a)
convList.extend(s2ListConverter.listconverter(b))

for i in convList:
    if i != '\n':
        print "element:",i

#22.4 ticks per second

