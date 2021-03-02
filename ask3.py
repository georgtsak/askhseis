import datetime
import urllib2
import json
now = datetime.datetime.now()
print ("Twrinh hmeromhnia kai wra : ")
("%Y-%m-%d %H:%M:%S")
now_date = now.strftime("%Y-%m-%d %H:%M:%S")

for i in range(31):
    date_str= now.strftime("%d-%m-%Y")
    url ='https://api.opap.gr/draws/v3.0/1100/draw-date/%Y/2021-02-03/1100'
    req = urllib2.Request(url)
    response = urllib2.urlopen(req) 
    data = response.read()
    dataDict = json.loads(data)
    response.close()
    
