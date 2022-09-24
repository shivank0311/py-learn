import sys

def main():
    print("python version {}.{}. {}".format(*sys.version_info))
    print(sys.platform)

    import datetime
    now=datetime.datetime.now()
    print (now)
    print (now.year, now.month , now.day , now.time , now.hour , now.minute, now.second , now.microsecond)

if __name__=="__main__": main()    