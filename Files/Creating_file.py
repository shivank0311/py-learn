def main():
    infile= open("line.txt", "r")
    outfile= open ("new.txt","w")
    for line in infile:
        print(line,file=outfile, end= "")
    print("done.") 

if __name__=="__main__": main()