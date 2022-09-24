def main():
    f= open("line.txt" , "r")
    for line in f.readlines():
        print (line, end=" ")

if __name__=="__main__" : main()