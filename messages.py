import re, os

import calendar, datetime

# weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# days = calendar.Calendar(firstweekday=0).monthdatescalendar(2015, 11)
# for week in days:
#     for d in week:
#         if d.day != 0:
#             print(str(d) + str(calendar.day_name[d.weekday()]))
#

if not os.path.exists("texts"):
    os.makedirs("texts")


#this populates the vector days
days = {}
thisDate = ""
with open("texts.txt" ,encoding='utf-8', errors='ignore') as file_in:
        file_lines = []
        lines = file_in.readlines()
        for line in lines:
            date = re.match('[0-9]{4}-[0-9]{2}-[0-9]{2}', line)
            if date:
                date = date.group(0)
                days[date] = days.get(date,0)
                thisDate = date
            if date is None:
                if line != 'Tifa Almeida\n' and line != "Trenton Adam Hyer\n":
                    days[thisDate] = days.get(thisDate, 0) + 1

#create a dictionary for each weekday, adding the number of texts sent in that day
weekdays = {}
for k in sorted(days):
    k2 = k.split('-')
    weekday = calendar.weekday(int(k2[0]),int(k2[1]),int(k2[2]))
    wd = calendar.day_name[weekday]
    weekdays[wd] = weekdays.get(wd, 0) + int(days[k])
print(weekdays)


#write out to a .csv in the format: one column for each month, inside of it one row for each day
results = open('texts/results2.csv', 'w+')
# for w in calendar.day_name:
#     results.write(str(w) + ',' + str(weekdays[w]) + '\n')
# for w in days:
#     results.write(str(w) + "," + str(days[w]) + '\n')

#write out the weekdays totals separated by month
weekday_month = {}
for k in sorted(days):
    k2 = k.split('-')
    weekday = calendar.weekday(int(k2[0]),int(k2[1]),int(k2[2]))
    wd = calendar.day_name[weekday]
    weekdays[wd] = weekdays.get(wd, 0) + int(days[k])
print(weekdays)