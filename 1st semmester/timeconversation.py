def timeConversion(s):
    listHour = s.split(":")
    if listHour[0][0] == '0':
        hour = eval(listHour[0][1])
        if listHour[2][2:4] == 'PM':
            if hour <= 12:
                hour = hour+12
                if hour >= 24:
                    hour = hour - 24
                if hour <12:
                    hour = '0'+str(hour)
        elif listHour[2][2:4] == 'AM':
            if hour >= 12:
                hour = hour-12
                if hour >= 24:
                    hour = hour - 24
                if hour < 12:
                    hour = '0'+str(hour)
            elif hour <= 12:
                hour = '0' + str(hour)
        return str(hour)+":"+ str(listHour[1])+":" + str(listHour[2][:2]) 
    else:
        hour = eval(listHour[0])
        if listHour[2][2:4] == 'PM':
            if hour <= 12:
                hour = hour+12
                if hour >= 24:
                    hour = hour - 24
                if hour <12:
                    hour = '0'+str(hour)
        elif listHour[2][2:4] == 'AM':
            if hour >= 12:
                hour = hour-12
                if hour >= 24:
                    hour = hour - 24
                if hour < 12:
                    hour = '0'+str(hour)
            elif hour <= 12:
                hour = '0' + str(hour)
        return str(hour)+":"+ str(listHour[1])+":" + str(listHour[2][:2])

def main():
    inputStr = input()
    print(timeConversion(inputStr))
main()