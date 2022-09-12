def main():
    print("this is function.py file")
    for i in inclusive_range(5, 25,1):
        print (i, end=" ")

def inclusive_range (*args):
    numargs=len(args)
    if numargs<1 : raise typeerror ("require at least one argument")   
    elif numargs==1:
        stop=args[0]
        start=0
        step=1
    elif numargs==2:
        (start,stop)=args
    elif numargs==3:
        (start,stop, step)=args
    else: raise typeerror("inclusive_range require at least 3 argument,got {}".format(numargs))
    i = start
    while i <= stop:
        yield i
        i += step

if __name__=="__main__": main()



