def interCookie(mode):
    #0 doesn't return a value, 1 does.
    with open('cookies.txt', 'r') as fileContent:
        contents = fileContent.read()
        #print(contents)
        #this works thus far
        if mode == 0:
            return contents
        print(contents)
        
class setUp:
   def initx2():
       comp = interCookie(0)
 
runStart = setUp
interCookie(1)
print("ReadCookies")
runStart.initx2

