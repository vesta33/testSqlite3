__author__ = 'anastassias'
import HTML
import sqlite3
import re
import datetime
from urllib.request import urlopen
import types

f = open('links.html','w')

message = """<html>
<head></head><body>"""

conn = sqlite3.connect('main.db')
c = conn.cursor()
c.execute("SELECT from_dispname,body_xml,timestamp FROM Messages WHERE body_xml LIKE '<a href%' ")
test = c.fetchall()
#print (test)
x = []
for i in range(len(test)):
        linktext =  str(test[i])
        val1 = linktext.split(', ')[0][2:-1]
        val2 = (re.findall('\"([^$]*)\"', linktext))
        extractLink = (val2[0])
        extractTime = (linktext.split(', ')[2][0:-1])

        htmlFile = urlopen(extractLink)
        html = htmlFile.read()
        regexp_link = '''<title>(.*)</title>'''
        pattern = re.compile(regexp_link)
        links = re.findall(pattern, str(html))
        print(links)
        if len(links) != 0:
            a = list((
                val1,
                ("""<a href=""" +  extractLink + """ target="_blank"> """ + links[0] + """</a>"""),
                datetime.datetime.fromtimestamp(
                  int(extractTime)
                    ).strftime('%d.%m.%Y')
                ))
            x.append(a)
print(x)
conn.close()

htmlcode = HTML.table(x,
    header_row=['Person', 'URL',   'Date'])
message2 ="""
</body>
</html>"""

f.write(message)
f.write(htmlcode)
f.write(message2)
f.close()