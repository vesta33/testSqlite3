__author__ = 'anastassias'
import sqlite3
import datetime
import time
import sys

skypeName = input("Enter name in form Mari Maasikas: ")
if not skypeName:
    print ("!!!Please start again and provide a first and the last names!!!")
    sys.exit("Input is incorrect")

skypeDate = input("Enter date in form 2014-11-11: ")
if not skypeDate:
    print ("!!!Please start again and provide a date your are looking for!!!")
    sys.exit("Input is incorrect")

skypeDay = str(int(time.mktime(datetime.datetime.strptime(skypeDate, "%Y-%m-%d").timetuple())))[0:5]

conn = sqlite3.connect('main.db')
c = conn.cursor()
skypeD = skypeDay + '%'
t = (skypeD, skypeName,)
c.execute("SELECT body_xml FROM Messages WHERE timestamp LIKE ? AND from_dispname=?", t)
print(c.fetchall())

conn.close()

"""
print(
    datetime.datetime.fromtimestamp(
        int("1415951287")
    ).strftime('%Y-%m-%d %H:%M:%S')
)

#from http://stackoverflow.com/questions/9637838/convert-string-date-to-timestamp-in-python
s = "2014-11-14 09:43:47"
print (int(time.mktime(datetime.datetime.strptime(s, "%Y-%m-%d %H:%M:%S").timetuple())))

a = "2014-11-13"
print (int(time.mktime(datetime.datetime.strptime(a, "%Y-%m-%d").timetuple())))
"""