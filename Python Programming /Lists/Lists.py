def Alphabet():
    alist = []
    for i in range(0,26):
        alist.append(chr(ord('A')+i))
    print(alist)
    alist.reverse()
    print(alist)

def Planets() :
    plist = ['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune']
    dlist = [0.4,0.7,1.0,1.5,5.2,9.5,19.2,30.0]
    print("Original: ",plist)
    for p in plist:
        print(p,end = '\t')
    print()
    for i in range(len(plist)):
        print("Planet = ",plist[i],"\tDistance (AU): ",dlist[i])
    #
    # https://solarsystem.nasa.gov/planets/dwarf-planets/ceres/overview/
    plist.insert(4,"Ceres")
    print("Inserting middle: ",plist)
    #
    # https://solarsystem.nasa.gov/planets/dwarf-planets/pluto/overview/
    plist.insert(len(plist),'Pluto')
    print("Inserting end: ",plist)
    #
    # http://web.gps.caltech.edu/~mbrown/sedna/
    plist.append('Sedna')
    print("Appending: ",plist)
    #
    plist.sort()
    print("Sorted: ",plist)
    #
    print("Length = ",len(plist))
    print("Minimum = ",min(plist))
    print("Maximum = ",max(plist))
    print("Done")
    

def PrintNumbers() :
    numbers = []
    for i in range(0,10):
        numbers.insert(i,i+1)
    print('original list')
    for j in range(0,10):
        print(numbers[j])
    for k in range(1,10,2):
        numbers.remove(k)
    print('odd removed')
    for l in range(0,len(numbers)):
        print(numbers[l])
    print('printed using -index')
    index = -1
    for m in range(0,len(numbers)):
        print(numbers[index])
        index -= 1
    #
    print(6 in numbers)
    print(7 in numbers)
    nulist = numbers
    nulist[2] = 111
    print(nulist)
    print(numbers)
    
Alphabet()
Planets()
PrintNumbers()
