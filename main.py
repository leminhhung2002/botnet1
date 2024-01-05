# -*- coding: utf-8 -*-
import base64
import re

from platform import system
from os import system as cmd

filePath = input( "Enter Batch File Path You Want To Encrypt:" )
with open(filePath, "r", encoding='utf-8') as subject:
    batchLines = subject.readlines()

result = open("result.bat", "w", encoding='utf-8')
result.close()
result = open("result.bat", "a", encoding='utf-8')
result.write("setlocal EnableDelayedExpansion\n")

countLines = 0

for bline in batchLines:
    if re.search("%", bline) and bline.count("%") == 2:
        newline = bline.replace("%", "%%")
        bline = "cmd /c " + newline
        batchLines[countLines] = bline
    countLines += 1
countLines = 0

for bline in batchLines:
    if bline[0] == ':':
        cani = False


def kodOlustur():
    global result
    for batch in batchLines:
        for line in batch:
            if line == '':
                continue
            elif line == '\n':
                continue
            elif line == '>':
                continue
            elif line == '<':
                continue
            if line == '%':
                cmd = ''
            elif line == '>':
                cmd = ''
            else:
                lineb = line.encode("utf-8")
                ln64b = base64.b64encode(lineb)
                ln64 = ln64b.decode('utf-8')
                ln64 = ln64.replace('=', '')
                cmd = ("set {}={}".format(ln64, line))
                result.write(cmd)
                result.write('\n')
    
    result.close()
    
    with open("result.bat", "r", encoding='utf-8') as rread:
        rlines = rread.readlines()
        dlines = set(rlines)
        with open("result.bat", "w", encoding='utf-8') as result:
            result.write("@echo off\n")
        result = open("result.bat", "a", encoding='utf-8')
        for i in dlines:
            result.write(i)
    
    result.write("cls\n")


def encodeIt():
    global result
    for batch in batchLines:
        if batch[0] == ':':
            cani = False
        else:
            cani = True
        if cani == False:
            result.write(batch)
            continue
        for line in batch:
            if line == '%':
                ln64 = '%'
            else:
                lineb = line.encode('utf-8')
                ln64b = base64.b64encode(lineb)
                ln64 = ln64b.decode('utf-8')
                ln64 = ln64.replace('=', '')
            if ln64 == 'Cg':
                exc = '\n'
            # elif ln64 == 'JQ':
            #     exc = ''
            elif ln64 == 'Pg':
                exc = '>'
            elif ln64 == 'Jg':
                exc = '&'
            elif ln64 == 'PO':
                exc = '<'
            elif ln64 == 'Ipq':
                exc = '!'
            else:
                if ln64 != '%':
                    exc = "%" + ln64 + "%"
                else:
                    exc = "%"
    
            result.write(exc)


kodOlustur()
encodeIt()
result.close()

with open("result.bat", "rb") as batbytes:
    bb = batbytes.read().hex()
add = 'fffe0d0a'
with open("result.bat", "wb") as batg:
    batg.write(bytes.fromhex(add + bb))

print("Encrypted Batch File Saved in 'result.bat'!")