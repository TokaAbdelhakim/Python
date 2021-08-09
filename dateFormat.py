import dateutil.parser as dparser
import datetime
array = ["2010/3/30", "15/12/2016", "8/9/2017", "11-15-2012", "20130720"]
format_array = []
for date in array:
     d = (dparser.parse(date).date())  
     format_array.append( (d.strftime('%d%Y')))

print (format_array)
