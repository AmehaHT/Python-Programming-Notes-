
class Element :
    def __init__(self,nu,ab,na) :  # constructor
        self.number = int(nu)
        self.abbrev = ab 
        self.name = na
    def __str__(self):  # string conversion operator
        return str(self.name + '\t' + self.abbrev + '\t' + str(self.number))
    def __lt__(self,right): # less-than operator
        print(str(self.number) + "__lt__" + str(right.number))
        return self.number < right.number
    def __eq__(self,right):  # equality operator
        print(str(self.number) + "__eq__" + str(right.number))
        return self.number == right.number
    def __add__(self,right):
        print(str(self.number) + "__add__" + str(right.number)) 
        return self.number + right.number
        
class PeriodicList :
    def __init__(self, size):  #constructor
        self.length = size
        self.table = [ ]
    def __getitem__(self,index):
        return self.table[index]
    def Reader(self,csvfile):
        csv = open(csvfile)
        for line in csv :
            rline = line.rstrip()
            cline = rline.split(',')
            e = Element(int(cline[0]),cline[1],cline[2])
            self.table.append(e)
    def Output(self) :
        for i in range(0,len(self.table)):
            print(self.table[i]) 
    def Sort(self):
        self.table.sort()
    def Search(self,e):
        print("Searching for ",e)
        if e in self.table:
            print("Found: ",self.table[self.table.index(e)])
        else:
            print("Not Found")
    def Plus(self,e,f):
        i = e + f
        print(str(e) + '\t' + str(f) + ' = ' + str(self.table[i]))
            
def main():               
    pt = PeriodicList(120)
    pt.Reader('PeriodicTable.csv')
    pt.Output()  # sorted by name
    pt.Sort()
    pt.Output()  # sorted by number
    efind = Element(80,"Hg","Mercury")
    pt.Search(efind)
    pt.Plus(pt[0],pt[7])
    
     
    
if __name__=="__main__":
    main()

