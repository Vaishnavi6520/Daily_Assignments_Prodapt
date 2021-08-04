import timeit
def printnumbers():
    for n in range(1000):
        pass
# mycode='''
# a=10
# if(a<15):
#     pass
# '''
# print(timeit.timeit(stmt=mycode))
print(timeit.timeit(printnumbers,number=100000))