from filelock import FileLock
import time
from tkinter.messagebox import showinfo

subor_lock = FileLock('databaza/TOVAR_LOCK.txt')
print('snazim sa dostat do suboru')
timeout=1
subor_lock.acquire(timeout)
if TimeoutError:
    print('subor pouziva iny modul')
    #showinfo(title='INFO', message='subor pouziva iny modul')
print('som vnutri suboru')
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

subor_lock.release()