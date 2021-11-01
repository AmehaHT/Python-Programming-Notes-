class CaesarCypher:
    def __init__(self):
        self.encrypt = ""
        self.offset = 0
    def getOffset(self):
        return self.offset
    def setOffset(self,offset):
        self.offset = offset
    def Encrypt(self,text):
        self.encrypt = ""
        for c in text:
            if c != str(' ')[0]:
                ec = chr(ord(c)+self.offset)
                self.encrypt += str(ec)[0]
            else:
                self.encrypt += str(' ')[0]
        return self.encrypt

class ASCII_Table():
    def __init__(self):
        print("Ascii Table")
        print("Numeric\tCharacter")
    def Table(self):
        for i in range(1,128):
            print(i,'\t'*2,chr(i))

class Distance:
    def __init__(self):
        self.kilofactor = 1.609344
        self.meters = 1000
        self.centimeters = 100
        self.milefactor = 0.6213712
        self.feet = 5280
        self.inches = 12      
    def Metric(self,miles):
        kilometers = miles * self.kilofactor
        meters = kilometers * self.meters
        centimeters = meters * self.centimeters
        print("Miles to kilometers ",kilometers,'\tmeters',meters,'\tcentimeters',centimeters)
    def English(self,kilometers):
        miles = kilometers * self.milefactor
        feet = miles * self.feet
        inches = feet * self.inches
        print("Kilometers to miles",miles,'\tfeet',feet,'\tinches',inches)

class Time:
    def __init__(self,value):
        self.age = value
    def Years(self):
        return self.age
    def Months(self):
        return self.age * 12
    def Days(self):
        return self.Months() * 365
    def Hours(self):
        return self.Days() * 24
    def Minutes(self):
        return self.Hours() * 60
    def Seconds(self):
        return self.Minutes() * 60
    def Output(self,caption,value):
        print(caption,value)

def Age(years) :
    age = Time(years)
    months = age.Months()
    days = age.Days()
    hours = age.Hours()
    minutes = age.Minutes()
    seconds = age.Seconds()
    age.Output("Age = ",age.Years())
    age.Output("Months = ",months)
    age.Output("Days = ",days)
    age.Output("Hours = ",hours)
    age.Output("Minutes = ",minutes)
    age.Output("Seconds = ",seconds)
    
def DistanceTime(lightYr):
    #distance light travels in a second (km)
    lightseconds = 299792
    lightTime = Time(lightseconds).Seconds()
    # fastest rocket 430000/hr
    rockethourseconds = 430000 /60 /60
    rocketTime = Time(rockethourseconds).Seconds()
    timedistance = lightYr * lightTime / rocketTime
    return timedistance

years = int(input("Enter your age: "))
age = Age(years)
print('*'*50)
print("Years = ",DistanceTime(4.3))
print('*'*50)
distance = Distance()
metric = distance.Metric(100)
print("Metric: ",metric)
english = distance.English(100)
print("English: ",english)
print(50*'-')
ascii = ASCII_Table()
ascii.Table()
print(50*'-')
text = "THE QUICK BROWN FOX JUMPED OVER THE LAZY POODLE"
offset = 3
caesar = CaesarCypher()
caesar.setOffset(offset)
encrypted = caesar.Encrypt(text)
print(encrypted)
caesar.setOffset(-offset)
decrypted = caesar.Encrypt(encrypted)
print(decrypted)

