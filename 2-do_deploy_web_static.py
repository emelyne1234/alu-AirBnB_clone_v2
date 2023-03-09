#!/usr/bin/python3
"""fabric script that distributes an archive to my web"""


from os.path import exists
from fabric.api import put, run, env


env.hosts = ['54.225.38.130', '18.207.143.154']


def do_deploy(archive_path):
    """returns false if the file at the path archive doesn't exist"""
    if not exists(archive_path):
        return False

    try:
        filename = archive_path.split("/")[-1]
        dirname = filename.split(".")[0]


        Test_dir = "/data/web_static/releases/"

        put(archive_path, '/tmp/')

        run('mkdir -p {}{}/'.format(Test_dir, dirname))

        run('tar -xzf /tmp/{} -C {}{}/'.format(filename, Test_dir, dirname))

        run('rm /tmp/{}'.format(filename))

        run('mv {0}{1}/web_static/* {0}{1}/'.format(Test_dir, dirname))

        run('rm -rf {}{}/web_static'.format(Test_dir, dirname))

        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(Test_dir, dirname))

        return True
    except:
        return False

