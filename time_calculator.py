def add_time(start, duration, dayofweek=None):
    start = start.replace(':', ' ')
    start = start.split(' ')
    
    duration = duration.split(':')

    startHour = int(start[0])
    startMin = int(start[1])
    startAPM = start[2]

    durHour = int(duration[0])
    durMin = int(duration[1])

    endHour = startHour + durHour
    endMin = startMin + durMin

    # variable to hold the times of change from AM to PM or
    # PM to AM
    countAPM = 0

    # if startHour != 12 and endHour >= 12:
    #     countAPM += 1

    # if minute is more than 60, subtract that and add into hour
    while True:
        if endMin >= 60:
            endMin -= 60
            endHour += 1
        else:
            break

    # if hour is more than 12, subtract that by 12
    while True:
        if endHour > 12:
            endHour -= 12
            countAPM += 1
        elif startHour != 12 and endHour == 12:
            countAPM += 1
            break
        else:
            break

    endAPM = ""
    # evaluate if it is AM or PM
    # if countAPM is odd, AM is changed to PM or vice versa
    if countAPM % 2 != 0:
        if startAPM == "PM":
            endAPM = "AM"
        elif startAPM == "AM":
            endAPM = "PM"
    else:
        endAPM = startAPM

    countdayAPM = 0
    # see how many days have passed by seeing the AM and PM
    # change. If PM is changed to AM, one day has passed.
    if startAPM == "AM" and countAPM >= 1:
        # when AM is changed to PM, it is the same day
        countdayAPM = countAPM
    elif startAPM == "PM" and countAPM >= 1:
        # when PM is changed to AM, one more day passed
        countdayAPM = countAPM + 1
    
    # count the days by counting how many times AM and PM switched
    day = countdayAPM // 2

    
    
    # put a "0" in front if it is single digit
    endMinstr = ""
    if endMin <= 9:
        endMinstr = "0" + str(endMin)
    else:
        endMinstr = str(endMin)

    daystr = ""
    if day == 1:
        daystr = " (next day)"
    elif day >= 2:
        daystr = " (" + str(day) + " days later)"

    # calculate the day of the week
    if dayofweek is not None:
        dayofweek = dayofweek.capitalize()
        daylist = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        daynum = daylist.index(dayofweek)  # 0 is monday, 1 is tuesday, etc
        daynum += day
        daynum = daynum % 7 # 7 days in a week
        endday = daylist[daynum]

    if dayofweek is None:
        new_time = str(endHour) + ":" + endMinstr + " " + endAPM + daystr
    else:
        new_time = str(endHour) + ":" + endMinstr + " " + endAPM + ", " + endday + daystr

    return new_time