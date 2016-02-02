#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fabric.api import run
from fabric.context_managers import env
from fabric.context_managers import cd
from fabric.operations import put
import time
from fabric.contrib.project import rsync_project
env.hosts = ['10.13.25.2','10.13.25.3','10.13.25.4']
env.user = 'root'
env.parallel = True


def backup():
	with cd("/data/cds/source/trunk/"):
		run("pwd")
		run("tar -Jcvf bak/cdscp_`date +%Y%m%d`.tar.xz cdscp")

def svnup():
	with cd("/data/cds/source/trunk/cdscp/"):
		run("pwd")
		run("svn update")

def restart():
	with cd("/root/"):
		run("pwd")
		run("service nginx stop")
		run("ps -ef | grep nginx")
		time.sleep(5)
		run("service nginx start")
		run("ps -ef | grep nginx")
def upload():
	put('zookeeper-3.4.7.tar.gz','/root')
def rsync():
	rsync_project('/root/zookeeper-3.4.7.tar.gz','/root/zookeeper-3.4.7.tar.gz')	
