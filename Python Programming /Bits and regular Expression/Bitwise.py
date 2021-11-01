def AndTable():
    print("\nAnd Table")
    print("\tfalse\ttrue")
    print("false\t",(0 & 0),'\t',(1 & 0))
    print("true\t",(1 & 0),'\t',(1 & 1))
    
def OrTable():
    print("\nOr Table")
    print("\tfalse\ttrue")
    print("false\t",(0 | 0),'\t',(1 | 0))
    print("true\t",(1 | 0),'\t',(1 | 1))

def XorTable():
    print("\nXor Table")
    print("\tfalse\ttrue")
    print("false\t",(0 ^ 0),'\t',(1 ^ 0))
    print("true\t",(1 ^ 0),'\t',(1 ^ 1))

def BitwiseAND(x,y):
    return x & y

def BitwiseOR(x,y):
    return x | y

def BitwiseNOT(x):
    return ~x

def BitwiseXOR(x,y):
    return x ^ y

def RightShift(x,y):
    return x >> y

def LeftShift(x,y):
    return x << y

AndTable()
OrTable()
XorTable()
print(BitwiseAND(15,7))
print(BitwiseOR(15,7))
print(BitwiseNOT(15))
print(BitwiseXOR(15,7))
print(RightShift(16,2))
print(LeftShift(16,2))
