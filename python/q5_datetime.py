# Hint:  use Google to find python function
from datetime import datetime

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015' 

def date_dff(start, stop):
  return datetime.strptime(stop, '%m-%d-%Y') - datetime.datetime.strptime(start, '%m-%d-%Y')

#937 days

####b)  
date_start = '12312013'  
date_stop = '05282015'  

def date_dff(start, stop):
  return datetime.strptime(stop, '%m%d%Y') - datetime.datetime.strptime(start, '%m%d%Y')

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

#513 days

def date_dff(start, stop):
  return datetime.strptime(stop, '%d-%b-%Y') - datetime.datetime.strptime(start, '%d-%b-%Y')

#7850 days 

