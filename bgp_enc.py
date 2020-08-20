import os
import subprocess
import fnmatch
import time

qp =27

#enc = True
enc = False
dec = True
#dec = False

if enc == True:
    for root, dirs, files in os.walk("../vimeo_septuplet/sequences/", topdown=False):
        for name in files:
            if fnmatch.fnmatch(name, 'im1.png'):
                cmd = "bpgenc -f 444 -m 9 " + root + '/' + name + " -o " + root + '/' + "im1_QP" + str(qp) + ".bgp -q " + str(qp)
                #os.system(cmd)
                print(cmd)
                subprocess.Popen(cmd, shell=True)
                time.sleep(0.01)

if dec == True:
    for root, dirs, files in os.walk("../vimeo_septuplet/sequences/", topdown=False):
        for name in files:
            if fnmatch.fnmatch(name, "im1_QP" + str(qp) + ".bgp"):
                cmd = "bpgdec " + root + '/' + name + " -o " + root + '/' + "im1_bpg444_QP" + str(qp) + ".png"
                #os.system(cmd)
                print(cmd)
                subprocess.Popen(cmd, shell=True)
                time.sleep(0.001)
