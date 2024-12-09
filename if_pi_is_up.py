#!/usr/bin/env python3
import os
import subprocess
def ping_host(ip):
    # Run the ping command
    output = subprocess.run(
        ['ping', '-c', '1', ip],    # For Linux/Unix/Mac
        # ['ping', '-n', '1', ip],  # For Windows, use this line instead
        stdout=subprocess.DEVNULL,  # Suppress output
        stderr=subprocess.DEVNULL   # Suppress error messages
    )
    return output.returncode  # Return the returncode of the command

def main():
    ip = "192.168.32.198"
    # Call ping_host and get the return code
    ping_result = ping_host(ip)
    
    if ping_result == 0:
        print(f" {ip}")
        # FTP credentials and host
    else:
        print(f" ")
 

if __name__ == "__main__":
    main()
