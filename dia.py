def dia(w):
    for i in range(1, w):
        print((w-i)*" " + i*"*")
    for i in range(w):
        print(i*" " + (w-i)*"*")
 
#dia(5)
dia(30)