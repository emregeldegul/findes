#!/usr/bin/env python3
from argparse import ArgumentParser
from os import name, walk, path

bold, underline, endcolor = "\033[1m", "\033[4m", "\033[0m"
green, blue, yellow, red = "\033[92m", "\033[94m", "\033[93m", "\033[91m"
cantOpen = []

flag = "\np -> Search Files Path"
flag += "\nc -> Search File Contents"
flag += "\nd -> Specify output type"
flag += "\nn -> Specify Number of Unreadable Files"

def logo():
    print("--==["+bold+blue+"nickname"+endcolor+"] [ MuReCoder")
    print("--==["+bold+yellow+"MyGitHub"+endcolor+"] [ http://github.com/MuReCoder")
    print("--==["+bold+green+"software"+endcolor+"] [ Findes / Searcher v2")
    print("-"*50)

def usage():
    text1 = "\n\t"+"Detailed Help\t >> "+bold+green+"es@coderlab "+blue+"~ $"+endcolor+" findes -h"
    text2 = "\n\t"+"Example\t\t >> "+bold+green+"es@coderlab "+blue+"~ $"+endcolor+" findes -s 'Search word' -d 'directory' -t 'scan type'"
    return text1+text2

def pathScan(fPath, str, typ, op):
    payload = ""
    if "m" in typ:
        if str in fPath:
            payload = fPath
        else:
            payload = None
    else:
        if str.lower() in fPath.lower(): payload = fPath
        else: payload = None

    if payload != None:
        if "d" in typ:
            payload = bold+yellow+"[p] "+endcolor+payload
        else:
            payload = payload

        if op != None:
            if op in payload:
                return None
            else:
                return payload
        else: return payload
    else:
        return None

def fileScan(rFile, str, typ):
    try: read = open(rFile).read()
    except:
        cantOpen.append(rFile)
        return None
    if "m" in typ:
        if str in read:
            payload = rFile
        else:
            payload = None
    else:
        if str.lower() in read.lower(): payload = rFile
        else: payload = None

    if payload != None:
        if "d" in typ:
            payload = bold+yellow+"[f] "+endcolor+payload
            return payload
        else:
            return payload
    else:
        return None

def scan(str, dic, typ, op):
    for directory, folders, files in walk(dic):
        for file in files:
            if "p" in typ:
                result = pathScan(path.join(directory, file), str, typ, op)
                if  result != None:
                    print(result)
            if "c" in typ:
                result = fileScan(path.join(directory, file), str, typ)
                if  result != None:
                    print(result)


def main():
    if name != "posix": print ("This Program Just For Linux!"), quit()
    parser = ArgumentParser(usage = usage())
    parser.add_argument("-s", type = str, help = "String You Are Lookings For")
    parser.add_argument("-d", type = str, help = "Directory You Want to Scan (Default: '/')")
    parser.add_argument("-p", type = str, help = "Word to Ignore")
    parser.add_argument("-t", type = str, help = "Additional Flags (p, c, d, n, m) || "+flag)
    flags = parser.parse_args()

    if flags.s == None or flags.s == "":
        logo()
        print("usage:"+usage())
        quit()
    if flags.d == None or flags.d == "": flags.d = "/"
    if flags.t == None or flags.t == "": flags.t = "p"

    scan(flags.s, flags.d, flags.t, flags.p)

    if "n" in flags.t:
        print(bold+red+"\n\nTotal Can't Open File: "+endcolor+str(len(cantOpen)))
        for i in cantOpen:
            print(i)


if __name__ == '__main__':
    main()
