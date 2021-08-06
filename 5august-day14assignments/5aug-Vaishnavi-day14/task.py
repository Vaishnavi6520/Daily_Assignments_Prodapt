import threading,logging

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

def palindrome(start,end):
    for num in range(start, end + 1):
        temp = num
        reverse = 0
    
        while(temp > 0):
            Reminder = temp % 10
            reverse = (reverse * 10) + Reminder
            temp = temp //10

        if(num == reverse):
            print("%d " %num, end = '  ')

try:
    t1=threading.Thread(target=primeNumbers,args=(start,end)) # create a thread
    t2=threading.Thread(target=palindrome,args=(start,end)) # create a thread

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done!")
except:
    logging.error("Wrong Input")
finally:
    print("Completed!")
