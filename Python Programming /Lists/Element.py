def BubbleSort(arr) : 
    n = len(arr) 
    for i in range(n-1) : 
        for j in range(0, n-i-1) : 
            if arr[j].number > arr[j+1].number : 
                arr[j], arr[j+1] = arr[j+1], arr[j] #tuple
                
def LinearSearch(arr, x):   
    for i in range(len(arr)): 
        if arr[i].number == x.number: 
            return i   
    return -1

class Element :
    def __init__(self,nu,ab,na) :  # constructor
        self.number = int(nu)
        self.abbrev = ab 
        self.name = na
    def __str__(self):  # string conversion operator
        return str(self.name + '\t' + self.abbrev + '\t' + str(self.number))
        
class PeriodicTable :
    def __init__(self, size):  #constructor
        self.length = size
        self.table = [ ]
    def Reader(self,csvfile):
        csv = open(csvfile)
        for line in csv :
            rline = line.rstrip()  # removes the nl/cr
            cline = rline.split(',')  # returns a list of strings split by a comma
            e = Element(int(cline[0]),cline[1],cline[2])
            self.table.append(e)
    def Output(self) :
        for i in range(0,len(self.table)):
            print(self.table[i]) 
    def Sort(self):
        BubbleSort(self.table)
    def Search(self,e):
        print("Searching for ",e)
        value = LinearSearch(self.table,e)
        if (value != -1):
            print("Element ",e," found")
        else:
            print("Element ",e," not in table")
            
def main():               
    pt = PeriodicTable(120)
    pt.Reader('ptable.csv')
    pt.Output()  # sorted by name
    BubbleSort(pt.table)
    pt.Output()  # sorted by number
    efind = Element(6,'C','Carbon')
    pt.Search(efind)
    
main()

