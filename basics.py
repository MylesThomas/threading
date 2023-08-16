import threading
import time

def func():
    print('ran')
    time.sleep(1)
    print('done')
    
# x = threading.Thread(target=func, args=(4, ))
print(threading.active_count()) # 1
x = threading.Thread(target=func)
print(threading.active_count()) # 1
x.start()

print(threading.active_count()) # 2