import datetime
import socket
import os
import getpass

if __name__ == "__main__":
    ts = datetime.datetime.now()
    home_dir = os.environ["HOME"]
    user = getpass.getuser()
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    # this is the base for creating logs with this app (can be configured to log SSH requests, file moves, network requests
    print("{}: {}@{} ip: {} home-dir: {}".format(ts, user, hostname, local_ip, home_dir))
    #print("{}: ip: {} home-dir: {} hostname: {}".format(ts, local_ip, home_dir, hostname))

