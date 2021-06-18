'''
Bobby chapa
Port Scanner (Assignment-9) from Chapter 2
Python 3
6/18/2021
'''

import argparse
import socket

def main():
    parser = argparse.ArgumentParser(description='-t <target host> -p <target port>')
    
    parser.add_argument('-t', dest='targetHost', type=str, help='specify target host')
    parser.add_argument('-p', dest='targetPort', type=str, help='specify target port[s] separated by comma')

    args = parser.parse_args()

    targetHost = args.targetHost
    targetPorts = args.targetPort.split(',')

    # Test user input and then call portScan function
    if (targetHost == None) | (targetPorts[0] == None):
        print('[-] You must specify a target host and port[s].')
    else:
        for p in targetPorts:
            print(portScan(targetHost, p))
 
    return

def portScan(t,p):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    portStatus = ''

    if sock.connect_ex((t,int(p))):
        portStatus = str(p)+ ' Closed '
    else:
        portStatus = str(p)+ '***[OPEN]***'

    return portStatus


if __name__ == '__main__':
	main()
