#!/usr/bin/python3
"""Module to compress files
"""
from fabric.api import *
from datetime import datetime
import os


env.hosts = ["ubuntu@34.73.252.190", "ubuntu@54.198.140.74"]


def do_deploy(archive_path):
    """Method to deploy files
    """
    if not os.path.exists(archive_path):
        return False

    else:
        try:
            name = archive_path.split("/")[1][:-4]
            put(archive_path, '/tmp')
            run("mkdir -p /data/web_static/releases/{}".format(name))
            command = "tar -xzf /tmp/{}.tgz -C ".format(name)
            command += "/data/web_static/releases/{}".format(name)
            run(command)
            run("rm /tmp/{}.tgz".format(name))
            command = "mv /data/web_static/releases/{}/".format(name)
            command += "web_static/* /data/web_static/releases/{}".format(name)
            run(command)
            run("rm -rf /data/web_static/releases/{}/web_static".format(name))
            run("rm -rf /data/web_static/current")
            command = "ln -s /data/web_static/releases/{}/ ".format(name)
            command += "/data/web_static/current"
            run(command)
            return True
        except Exception as err:
            return False
