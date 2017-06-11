import sys
import json
from collections import defaultdict
from Classes import customer,siteVisit,image,order
from datetime import datetime, timedelta
import calculate 

#command line arguments
#First argument provides X customers
#Second argument provides file name
if len(sys.argv)!=3:
	print 'Please provide two arguments which are  count of customers and file name'
	exit(1)
file_Name=sys.argv[2]
top_Customer=int(sys.argv[1])

#Dicionary to store each customer information
dict={}

if top_Customer <0:
	print 'Please provide a valid customer count'
	exit(1)

#parsing the JSON file 
with open (file_Name) as file:
	data=json.load(file)

#calling the Ingest method in calculate 
dict=calculate.Ingest(data,dict)
#calling Analytical Method in calculate
calculate.topXSimpleLTVCustomers(top_Customer,dict)
