def English2Metric(miles):
    kilometers = miles * 1.609344
    meters = kilometers * 1000
    centimeters = meters * 100
    print("Miles to kilometers ",kilometers,'\t',meters,'\t',centimeters)

def InputYears():
    age = input("Enter your age: ")
    return int(age)

def Years(number):
    return number * 365

def Months(number):
    return number * 12

def Days(number):
    return number * 365

def Hours(number):
    return number * 24

def Minutes(number):
    return number * 60

def Seconds(number):
    return number * 60

def Output(caption,value):
    print(caption,value)
        
def LightYearsSpeed(lightYr,speedHr):
    #distance light travels in a year (miles)
    lightseconds = 186282
    lightminutes = Seconds(lightseconds)
    lighthours = Minutes(lightminutes)
    lightdays = Hours(lighthours)
    lightyears = Years(lightdays)
    rocketday = Hours(speedHr)
    rocketyear = Years(rocketday)
    #fastest rocket to LightYear destination
    timedistance = lightYr * lightyears / rocketyear
    return timedistance

def Age() :
    age = InputYears()
    months = Months(age)
    days = Days(months)
    hours = Hours(days)
    minutes = Minutes(hours)
    seconds = Seconds(minutes)
    Output("Age = ",age)
    Output("Months = ",months)
    Output("Days = ",days)
    Output("Hours = ",hours)
    Output("Minutes = ",minutes)
    Output("Seconds = ",seconds)
    
Age()
English2Metric(100)
Output("Years to Alpha Centauri = ",LightYearsSpeed(4.3,450000))
    
