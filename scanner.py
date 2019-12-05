#!/usr/bin/python

import time
import argparse
from socket import *

def connScan(tgtHost, tgtPort, format):
    connSkt = socket(AF_INET, SOCK_STREAM)
    connSkt.settimeout(5)
    res = connSkt.connect_ex((tgtHost, tgtPort))
    connSkt.close()

    pl = "      "
    for i in range(len(str(tgtPort))):
        pl = pl[:-1]
    if res is 0:
        if format:
            print("Port", tgtPort, pl, "is open")
        else:
            print(str(tgtPort) + ",open")
        return True
    else:
        if format:
            print("Port", tgtPort, pl, "is closed")
        else:
            print(str(tgtPort) + ",closed")
        return False

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", help="The victims ip address")
    parser.add_argument("--port", help="A specific port for checking")
    parser.add_argument("--portF", help="A file for the ports")
    parser.add_argument("--format", help="true for beautiful output. Default: true")
    args = parser.parse_args()

    if not args.ip:
        print("please use --ip <ip address> to set the address")
        exit(0)
    if not args.port and not args.portF:
        print("please use --port <port> or --portF <file> to set the address")
        exit(0)
    if not args.format:
        format = True
    else:
        if args.format == "true":
            format = True
        else:
            format = False
    
    if format:
        print("Starting Port Scanner")

    try:
        ip = gethostbyname(args.ip)
    except gaierror:
        if format:
            print("IP Adress not found!")
            exit(0)
    if args.port:
        ports = args.port.split(",")
    else:
        ports = []
        try:
            with open(args.portF) as f:
                line = f.readline()
                while line:
                    ports.append(line)
                    line = f.readline()
        except FileNotFoundError:
            if format:
                print("File", args.portF, "not found")
                exit(0)

    if format:
        print("Checking ports for " + args.ip)

    opened = 0
    closed = 0

    for i in ports:
        try:
            if connScan(ip, int(i), format):
                opened = opened+1
            else:
                closed = closed+1
        except ValueError:
            if format:
                print("Could not parse port " + i)

    if format:
        print("Check finished:", opened, "open Ports,", closed, "closed Ports")

if __name__ == '__main__':
    main()