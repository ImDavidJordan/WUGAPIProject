import urllib2
import json
import csv
import time
#import winsound

loc = [\
  'GH/Accra.json',\
  'DE/Burghausen.json',\
  'AR/Buenos-Aires.json',\
  'IN/Chennai.json',\
  'CN/Lengshuijiang.json',\
  'PE/Lima.json',\
  'GB/London.json',\
  'MX/Mexico_City.json',\
  'RU/Moscow.json',\
  'CA/Nanaimo.json',\
  'ES/Pamplona.json',\
  'AU/Perth.json',\
  'NC/Cary.json',\
  'zmw:00000.1.78486.json',\
  'UZ/Tashkent.json',\
  'GR/Thessaloniki.json',\
  'PL/Gliwice.json'\
]
out = open( 'DavidJordanWeatherUngergroundOutput.csv', 'wb' )
writer = csv.writer( out )
writer.writerow(['City', 'Min 1', 'Max 1','Min 2', 'Max 2','Min 3', 'Max 3','Min 4', 'Max 4','Min 5', 'Max 5']) 
i=1
j=0

link='http://api.wunderground.com/api/d6f2280b946748c1/forecast10day/conditions/q/{}'
for i in loc:
    newlink = link.format(i)
    #print newlink
    h = urllib2.urlopen(newlink)
    njson_string = h.read()
    nparsed_json = json.loads(njson_string)

    #City
    print nparsed_json[u'current_observation'][u'display_location'][u'city']
    city= str(nparsed_json[u'current_observation'][u'display_location'][u'city'])
    rows=[city]
   
    #Getting the minimum and maximum temperature for each of the 5 days
    while j <5:
        #Low Temperature
        #print nparsed_json[u'forecast'][u'simpleforecast'][u'forecastday'][j][u'low'][u'celsius']
        low= str(nparsed_json[u'forecast'][u'simpleforecast'][u'forecastday'][j][u'low'][u'celsius'])
        
        #Error Checking
        print str(nparsed_json[u'forecast'][u'simpleforecast'][u'forecastday'][j][u'low'][u'celsius'])

        #High Temperature
        #print nparsed_json[u'forecast'][u'simpleforecast'][u'forecastday'][j][u'high'][u'celsius']
        high= str(nparsed_json[u'forecast'][u'simpleforecast'][u'forecastday'][j][u'high'][u'celsius'])

        #Error Checking
        #print str(nparsed_json[u'forecast'][u'simpleforecast'][u'forecastday'][j][u'high'][u'celsius'])

        #Appending the next observation for output
        rows.append(low)
        rows.append(high)

        j=j+1

    #Error checking
    #print rows
    #print njson_string

    writer.writerow(rows)
    j=0
    time.sleep(7)



out.close()
print 'Code finished executing'
#winsound.Beep(500,5000)
