from filelock import FileLock
import time

subor_lock = FileLock('databaza/TOVAR_LOCK.txt')

subor_lock.acquire()
with open('databaza/TOVAR.txt', 'r') as f:
    lines = f.readlines()

# remove the last line from the list of lines
lines = lines[:-1]

# remove the newline character from the last line
last_line = lines[-1].rstrip()
lines[-1] = last_line

# write the modified list of lines back to the file
with open('databaza/TOVAR.txt', 'w') as f:
    f.writelines(lines)
time.sleep(10)  
subor_lock.release()