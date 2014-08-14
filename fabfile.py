from fabric.api import *

env.user = 'admin'

# TODO put host here
env.hosts = []

def pack():
    local('python setup.sdist --formats=gztar', capture=False)

def deploy():

    pack()

    dist = local('python setup.py --fullname', capture=True).strip()
    put('dist/{}.tar.gz'.format(dist), '/tmp/test.provserver.tar.gz')
    run('mkdir /tmp/test.provserver')
    with cd('/tmp/test.provserver'):
        run('tar xzf /tmp/test.provserver.tar.gz')
        run('/var/www/test.provserver/env/bin/python setup.py install')
    run('rm -rf /tmp/test.provserver /tmp/test.provserver.tar.gz')
    run('touch /var/www/provserver.wsgi')
