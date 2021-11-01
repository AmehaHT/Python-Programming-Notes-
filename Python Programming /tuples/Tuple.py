import collections

def TupleAssign():
    (x,y,z) = ("python", "is", "Number 1")
    return x,y,z
    
def TupleMinMax(tup):
    mn = min(tup)
    mx = max(tup)
    return mn,mx
    
def TupleIndex(tup,val):
    y = tup.index(val)
    return y
     
def TupleLen(tup):
    y = len(tup)
    return y 
    
def TupleStr(s):
    ts = tuple(s)
    return ts
    
def TupleStar(tup):
    tuple2 = tup*3
    return tuple2
    
def TuplePartition(s):
    print(s)
    tuplef = s.partition("g")
    tupler = s.rpartition("g")
    return tuplef,tupler
    
def TupleJoin(tup):
    tuple2 = "--HiDeeHo--".join(tup)
    return tuple2
    
def TuplePoint(p):
    x = p[0]
    y = p[1]
    return x,y

def TupleAlphabet(tup):
    alist = []
    for i in range(len(tup)):
        alist.insert(i,chr(tup[i]+ord('a')))
    return alist
  
def sortLength(words):
    t = []
    for word in words:
        t.append((len(word), word))
    t.sort(reverse=True)
    res = []
    for length, word in t:
        res.append((length,word))
    return res

def namedTupleEx():
    Planet = collections.namedtuple('Planet',['name','distance','mass']) 
    earth = Planet('Earth',1.0,1.0) 
    mars = Planet('Mars',1.52,0.107)
    mercury = Planet('Mercury',0.39,0.055)
    venus = Planet('Venus',0.72,0.815)
    [print ("index[",i,"]\t",mars[i]) for i in range(len(mars))]
    print ("The planet name using keyname is : ",end ="") 
    print (mercury.name) 
    print ("The planet distance using getattr() is : ",end ="") 
    print (getattr(venus,'distance'))     
    print ("All the fields of the planet are: ") 
    print (earth._fields) 

college = ("De", "Anza", "College")
evens = (2,4,6,8,10)
numbers = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)
pl = "Python Language"
tuple1 = (44,22,13,22,45,555,32,33)
sentence = ("The","quick","brown","fox","jumps","over","the","lazy","poodle")

t = TupleAssign()
print(t)
print(*t)

print('-'*25)
t = TupleMinMax(tuple1)
print(t)
print("min = ",t[0],"\tmax = ",t[1])

print('-'*25)
value = 555
t = TupleIndex(tuple1,value)
print("the value of ",value," is at index ", t)
print('-'*25)

t = TupleLen(tuple1)
print("The length of tuple1 is ",t)
print('-'*25)

t = TupleStr("python")
print(t)
print(*t)
print('-'*25)

t = TupleStar(numbers)
print(t)
print(*t)
print('-'*25)

t = TuplePartition(pl)
print(t[0])
print(t[1])
print('-'*25)

print(college)
t = TupleJoin(college)
print(t)
print('-'*25)

pointx,pointy = TuplePoint((123,234))
print("{0}X, {1}Y".format(pointx,pointy))
print('-'*25)

alphabet = TupleAlphabet(numbers)
print(alphabet)
print(*alphabet)
print('-'*25)

t = sortLength(sentence)
for length,word in t:
    print("length = {0}\tword = {1}".format(length,word))
    
namedTupleEx()