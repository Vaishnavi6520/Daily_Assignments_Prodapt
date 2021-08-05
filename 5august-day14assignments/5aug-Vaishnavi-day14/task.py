import threading
start=2
end=500
def primeNumbers(start,end):
    for i in range(start,end+1):
        if i>1:
            for j in range(2,i):
                if (i%j)==0:
                    break
            else:
                print(i)

t1=threading.Thread(target=primeNumbers,args=(start,end)) # create a thread

t1.start()

t1.join()

print("Done!")
# printNumbers()