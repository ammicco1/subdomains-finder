#!/usr/bin/python3

import sys, getopt, subprocess

def __Usage__():
    print("""Usage: python3 main.py [option] <hostname>
    Options: 
    - [-f | --file FILE] Select an input file list of subdomains.
    - [-h | --help] Display this help.
    - [-n | --number] Select a subset of subdomains.
    - [-o | --output] Send output to a file.
""")

def __ping(hostname):
    response = subprocess.run(["ping", "-c", "1", hostname], stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)
       
    return response.returncode

try:
    opts, args = getopt.getopt(sys.argv[1:], "f:hn:o:", ["file=", "help", "number=", "output="])
except: 
    print("Error in argv parsing")
    __Usage__()
    exit()

out = False
filename = ""

for opt, arg in opts: 
    if opt in ["-h", "--help"]:
        __Usage__()
        exit()
    if opt in ["-f", "--file"]:
        filename = arg
    if opt in ["-o", "--output"]: 
        out = True
        outfile = arg
        of = open(outfile, "w")
    if opt in ["-n", "--number"]:
        m = arg

if len(args) == 0:
    __Usage__()
    exit()

hostname = args[0]

if filename != "":
    f = open(filename, "r")
    i = 0

    for index, subdomains in enumerate(f):
        i += 1

        sub = subdomains.replace("\n", "");

        if __ping(sub + "." + hostname) == 0:
            s = sub + "." + hostname + " is up"
        else:
            s = sub + "." + hostname + " is down"

        if out:
            of.write(s)
            of.write("\n")
        else:
            print(s)

        if i == int(m):
            break

    f.close()
else:
    if __ping(hostname) == 0:
        print(f"{hostname} is up")
    else:
        print(f"{hostname} is down")
    

if out: 
    of.close()
