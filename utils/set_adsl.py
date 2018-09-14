#!/bin/env python
import sys
import socket
import time
from urllib.request import urlopen

# set html header
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"}


def test_interface():
    try:
        rslt = urlopen("http://members.3322.org/dyndns/getip")
        html = rslt.read()
        ret_ip = html.rstrip()
        print("return ip=%s" % (ret_ip))
        return True
    except Exception as FF:
        print("Test interface error, exit ... \n")
        return

    # set interface


def set_interface(ip):
    true_socket = socket.socket

    def bind_socket(*arg1, **arg2):
        sock = true_socket(*arg1, **arg2)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((ip, 0))
        return sock

    socket.socket = bind_socket
    print("virtual ip: %s" % (ip))
    n = 6
    while 1:
        n -= 1
        if n <= 0:
            sys.exit(1)
        is_success = test_interface()
        if not is_success:
            time.sleep(2)
            continue
        else:
            break


if __name__ == "__main__":
    # parse args
    set_interface(sys.argv[1])
