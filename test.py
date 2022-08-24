import time


def countdown(): 

    start_time = time.time()
    while True:
    
        if time.time()-start_time == 1:
            print ("3...")
        if time.time() -start_time== 2:
            print ("2...") 
        if time.time() - start_time== 3:
            print ("1...")
        if time.time() -start_time == 4:
            print ("GO!")
            break


countdown ()