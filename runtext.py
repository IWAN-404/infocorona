import sys,time

def load(c):
 for s in c + '\n':
  sys.stdout.write(s)
  sys.stdout.flush()
  time.sleep(0.1)
