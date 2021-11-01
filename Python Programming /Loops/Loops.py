def whileForwards() :
    i = 0
    while i < 10 :
        print ("iteration ",i)
        i += 2

def whileBackwards() :
    i = 10
    while i > 0 :
        print ("iteration ",i)
        i -= 2

def forwards() :
    for i in range(0,10,2) :
        
        print("iteration ",i)

def backwards() :
    for i in range(10,0,-2) :
        print("iteration ",i)

def FileReader(s):
    file = open(s)
    for line in file:
        line = line.rstrip()  #removes line feed
        print(line)
    file.close()

whileForwards()
whileBackwards()
forwards()
backwards()
FileReader("Speech.txt")
