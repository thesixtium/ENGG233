def All_uppercase(string):
    returnString = ""
    for i in string:
        if 97 <= ord(i) <= 122:
            returnString += chr(ord(i)-32)
        else:
            returnString+=i
    return returnString

def main():
    s = "I am Happy to See You."
    capstr = All_uppercase(s)
    print(capstr)

if __name__ == '__main__':
    main()