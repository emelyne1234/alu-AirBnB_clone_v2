#!/usr/bin/python3
"""deletes out-of-date archives"""

import os
from fabric.api import *

env.hosts = ['54.225.38.130', '18.207.143.154']


def do_clean(number=0):
    """deletes outdates"""


    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
