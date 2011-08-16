#def run_unit_tests(pusher):
#    codir = pusher.checkout_dir()
#    (out,err) = pusher.execute("pushd %s && nosetests && popd" % codir)
#    return ("OK" in err,out,err)

def post_rsync(pusher):
    """ need to restart apache2 """
    (out,err) = pusher.execute(["ssh","monty.ccnmtl.columbia.edu","/var/www/drinkme/init.sh","/var/www/drinkme/"])
    (out4,err4) = pusher.execute(["ssh","monty.ccnmtl.columbia.edu","/bin/ln","-s","/usr/lib/python2.5/site-packages/PIL","/var/www/drinkme/working-env/lib/python2.5/"])
    (out3,err3) = pusher.execute(["ssh","monty.ccnmtl.columbia.edu","/bin/ln","-s","/usr/lib/python2.5/site-packages/PIL.pth","/var/www/drinkme/working-env/lib/python2.5/"])    
    (out2,err2) = pusher.execute(["ssh","monty.ccnmtl.columbia.edu","sudo","/usr/bin/supervisorctl","restart","drinkme"])
    out += out4 + out3 + out2
    err += err4 + err3 + err2
    return (True,out,err)  
