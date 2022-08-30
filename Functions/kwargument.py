def main():
    testfunc(5,6,7,8,9,10,one=1,two=2,three=3)
def testfunc(first,second,third,*args,**kwargs):
    for k in kwargs: print (k,kwargs[k])

if __name__=="__main__" :main()    

