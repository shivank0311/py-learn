def main():
    choices= dict(
        one="first",
        two="second",
        three="third",
        four="fourth"
    )
    v= "seven"
    print(choices .get(v, "other"))

if __name__=="__main__": main()    