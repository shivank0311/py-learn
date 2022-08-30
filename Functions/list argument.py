def main():
    testfunc(1,2,3,10,11,12,13)
def testfunc(one,two,three,*args):
    print(one,two,three)
    for n in args: print (n,end=" ")

if __name__=="__main__" :main()    
