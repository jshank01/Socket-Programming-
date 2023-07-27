
from socket import *
import os
import sys
import struct
import time
import select
import binascii

ICMP_ECHO_REQUEST = 8
MAX_HOPS = 30
TIMEOUT = 2.0
TRIES = 2
# The packet that we shall send to each router along the path is the ICMP echo
# request packet, which is exactly what we had used in the ICMP ping exercise.
# We shall use the same packet that we built in the Ping exrcise
def checksum(string):
    # In this function we make the checksum of our packet
    sum = 0
    countTo = (len(string) // 2) * 2

    count = 0
    while count < countTo:
        thisVal = ord(string[count + 1]) * 256 + ord(string[count])
        sum = sum  + thisVal
        sum = sum & 0xffffffff
        count = count + 2
    if countTo < len(string):
        sum = sum + ord(string[len(string)-1])
        sum = sum & 0xffffffff
    sum = (sum >> 16) + (sum & 0xffff)
    sum = sum + (sum >> 16)
    answer = ~sum
    answer = answer & 0xffff
    answer = answer >> 8 | (answer << 8 & 0xff00)
    return answer

def build_packet():
    # In the sendOnePing() method of the ICMP Ping exercisse, firstly the header of our
    # packet to be sent was made, secondly the checksum was appened to the header and 
    # then finally the complete packet tat we build in the Ping exercise

    # Make the header in a similar way to the ping exercise.
    # Append checksum to the header.

    # Don't send the packet yet , just return the final packet in this function.

    # So the function ending looks like this

    packet = header + data 
    return packet

def get_route(hostname): 
    timeLeft = TIMEOUT
    for tt1 in range(1,MAX_HOPS):
        for tries in range(TRIES):
            destAddr = gethostbyname(hostname)
            mySocket.setsockopt
