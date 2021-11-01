import re

address = "<De Anza College>,<12250 Stevens Creek Blvd>,<Cupertino>,<95014>,<864-5300>"

morse = ".--. -.-- - .... ---','-.'"
letters = ['P','Y','T','H','O','N']
    
def RemoveAlphabetic(target):
    print("\D - RemoveAlphabetic")
    numbers = re.sub(r'\D',"",target)
    return numbers

def RemoveNumbers(target):
    print("\d - RemoveNumbers")
    alphabetic = re.sub(r'\d',"",target)
    return alphabetic

def RemoveAlphaNumeric(target):
    print("\w - RemoveAlphaNumeric")
    alphabetic = re.sub(r'\w',"",target)
    return alphabetic
    
def RemovePunctuation(target):
    print("\W - RemovePunctuation")
    alphabetic = re.sub(r'\W',"",target)
    return alphabetic

def RemoveSpaces(target):
    print("\s - RemoveSpaces")
    alphabetic = re.sub(r'\s',"",target)
    return alphabetic

def RemoveNonSpaces(target):
    print("\S - RemoveNonSpaces")
    alphabetic = re.sub(r'\S',"",target)
    return alphabetic

def RemoveNonVowels(target):
    print("[aeiouAEIOU] - RemoveNonVowels")
    nvowelsregex = re.compile(r'[aeiouAEIOU]*')
    vlist = nvowelsregex.findall(target)
    return vlist

def RemoveVowels(target):
    print("[^aeiouAEIOU] - RemoveVowels")
    vowelsregex = re.compile(r'[^aeiouAEIOU]')
    nvlist = vowelsregex.findall(target)
    return nvlist

def RemoveCommas(target):
    print("[^,]* - RemoveCommas")
    commaregex = re.compile(r'[^,]*')
    clist = commaregex.findall(target)
    return clist

def SubstituteLetter(target,letter,substitute):
    print("Substitute")
    regex = re.compile(r''+letter)
    elist = regex.sub(substitute,target)
    print(elist)

def SearchWord(target,word):
    print("SearchWord")
    regex = re.compile(r''+word)
    find = regex.search(target)
    return find

def MatchPattern(target,pattern):
    print("MatchPattern")
    regex = re.compile(r''+pattern)
    found = regex.search(target)
    return found

def MatchPhone(target):
    m = re.compile(r'''(
                    (\d{3}) # first 3 digits
                    (\s|-|\.) # separator
                    (\d{4}) # last 4 digits
                    )''', re.VERBOSE)
    found = m.findall(target)
    return found

def Splitter(target):
    # \s is whitespace
    # {4} is up to 4
    print("splitter")
    regex = re.compile(r'[\s{4}]*')
    mlist = regex.split(target)
    print(mlist)
    
def isRegexPhone(text):
    # /d is number
    print('non-regex phone number')
    phone = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    number = phone.search(text) 
    if number != None:
        return number.group()
    else:
        return "not found"
    
def Counter(text,pat):
    print('counter')
    pattern = re.compile(pat)
    matcher = pattern.findall(text)
    count = len(matcher)
    return count
    
def isPhoneNumber(text):
    print('non-regex phone number')
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

print(isPhoneNumber('408-864-5300'))
print(isPhoneNumber('408-BOB-5300'))
print(isRegexPhone('My number is 408-864-5300.'))
print(isRegexPhone('My number is 408-BOB-5300.'))
print(MatchPhone(address))
print(MatchPattern(address,'\d{3}-\d{4}'))
print(Counter('elephant',r'[^e]*e'))
print(RemoveAlphabetic(address))
print(RemoveNumbers(address))
print(RemovePunctuation(address))
print(RemoveAlphaNumeric(address))    
print(RemoveVowels(address))
print(RemoveNonVowels(address))
print(RemoveCommas(address))
print(RemoveSpaces(address))
print(RemoveNonSpaces(address))
print(Splitter(morse))
print(SubstituteLetter(address,'e','E'))
print(SearchWord(address,'Anza'))
