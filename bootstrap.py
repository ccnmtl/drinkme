#!/usr/bin/env python
import os
import sys
import subprocess
import shutil

pwd = os.path.abspath(os.path.dirname(__file__))
vedir = os.path.abspath(os.path.join(pwd,"ve"))

if os.path.exists(vedir):
    shutil.rmtree(vedir)

virtualenv_support_dir = os.path.abspath(os.path.join(pwd, "requirements", "virtualenv_support"))

ret = subprocess.call(["python2.5", "virtualenv.py", 
                       "--extra-search-dir=%s" % virtualenv_support_dir,
                       "--never-download",
                       vedir])
if ret: exit(ret)

# Let's also bake in an assertion that setuptools 0.6c8 is the installed and active version,
# to be extra safe, and to be a little bit self-documenting
ret = subprocess.call([os.path.join(vedir, 'bin', 'python2.5'),
                       "-c",
                       "import pkg_resources as pkr; assert pkr.get_distribution('setuptools').version=='0.6c8'"])
if ret: exit(ret)
    
ret = subprocess.call([os.path.join(vedir, 'bin', 'pip'), "install",
                       "-E", vedir,
                       "--enable-site-packages",
                       "--index-url=''",
                       "--requirement",os.path.join(pwd,"requirements/apps.txt")])
if ret: exit(ret)

ret = subprocess.call([os.path.join(vedir, 'bin', 'pip'), "install",
                       "-E", vedir,
                       "--enable-site-packages",
                       "--index-url=''",
                       "--requirement",os.path.join(pwd,"requirements/phasetwo.txt")])
if ret: exit(ret)

