__author__ = 'student'
import sys
import subprocess
p = subprocess.getoutput("{} ./adventure.py < solutions.txt".format(sys.executable))
print(p)