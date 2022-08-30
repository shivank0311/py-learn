def main():
    a,b = 2,1
    while b< 20:
        print (b,end=" ")
        a,b =b, a*b

if __name__=="__main__" :main()      
