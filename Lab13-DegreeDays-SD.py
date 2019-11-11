#Lab13-DegreeDays-SD.py
#Stephen Davies
#heating and cooling days

def main():
    HeatDay = 0
    CoolDay = 0
    CAvg = 0
    HAvg = 0
    #make the user input a intial temp value
    print("Welcome to a program that will find the number of hot days and the number of cool days, the program"
          "will do this by the user inputting numbers until a number greater than 150 or less than 150 is entered")
    temp = eval(input("input an initial daily temperature: "))
    while temp >= -150 and temp <= 150:
        #processing if value is greater than 150 or less than -150
        #if value fits conditionals then it moves through the while loop
        if temp < 60:
            HeatDay = HeatDay + (temp - 60)
            HeatDay = HeatDay
            HAvg = HAvg + 1
            HAvg = HAvg
        #anaylizes if it is a Heat Day
        elif temp > 80:
            CoolDay = CoolDay + (temp - 80)
            CoolDay = CoolDay
            CAvg = CAvg + 1
            CAvg = CAvg
        #anaylizes if it is a Cool Day
        #end if-elif
        temp = eval(input("input another daily temperature: "))
        #makes user input another temp to be evaulated
    print('Average of Heat Days in temperature is', abs(HeatDay), "with the total number of Heat Days being", HAvg)
    print("Average of Cool Days in temperature is", abs(CoolDay), "with the total number of Cool Days being", CAvg)
    #end while
#end main


main()