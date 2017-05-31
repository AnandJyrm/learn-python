#! /usr/bin/python
import re
import subprocess
import time
import sys
import signal

interface = ""
fh = open("stat.txt", 'w')


def signal_handler(sig, frame):
    global fh
    fh.close()
    print "\nStopping Interface Monitor"
    sys.exit(0)


def write_stat():
    global interface, fh
    fh.write(str(time.strftime("%H:%M:%S")))
    fh.write("\t")
    output_string = subprocess.check_output(["ifconfig", interface])
    fh.write(str(re.findall("RX bytes:([0-9]*)", output_string)[0]))
    fh.write("\t")
    fh.write(str(re.findall("TX bytes:([0-9]*)", output_string)[0]))
    fh.write("\n")


def main():
    global interface, fh
    signal.signal(signal.SIGINT, signal_handler)
    output_string = subprocess.check_output(["ifconfig"])
    interfaces = re.findall("([a-zA-Z0-9]*) *Link encap:", output_string)
    if len(sys.argv) == 1:
        print "Interface List: " + " ".join(interfaces)
        interface = str(raw_input("Which Interface do you want to monitor: "))
    else:
        interface = sys.argv[1]
    if interface not in interfaces:
        print "Invalid interface. Quiting"
        exit()
    print "Monitoring \'%s\'. Check stat.txt for RX, TX bytes. Ctrl C to stop." % interface
    while 1:
        write_stat()
        time.sleep(3)

if __name__ == "__main__":
    main()
