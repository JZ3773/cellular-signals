import json
import requests
import datetime

#The user should enter his/her username and password where "Username" and "Password" are written
URL = "https://Username:Password@electrosense.org/api/spectrum/aggregated"

#The parameters should be changed by the user to whatever sensor, timespan, and frequencies are being looked at
PARAMS = {'sensor': 202481597925725, 'timeBegin': 1596474000, 'timeEnd': 1596480000, 'freqMin': 780000000,'freqMax': 800000000, 'aggFreq': 100000, 'aggTime': 60, 'aggFun': "MAX"}
response=requests.get(url=URL, params = PARAMS)
values=json.loads(response.text)["values"]

#Creating a file
myfile = open("mydata.csv", "w+")

#Writing out all of the frequencies (in MHz)
myfile.write(",") #This comma alligns the frequencies with their correct values
freq=PARAMS["freqMin"]
while freq<=PARAMS["freqMax"]:
	myfile.write(f'{freq/1000000},')
	freq+=PARAMS["aggFreq"]
myfile.write("\n")

#Writing out dB values for each frequency at each time
time = PARAMS["timeBegin"]
for valuearray in values:
	myfile.write(datetime.datetime.fromtimestamp(time).strftime('%c'))
	myfile.write(",")
	time+=PARAMS["aggTime"]
	for sound in valuearray:
		myfile.write(f"{sound},")
	myfile.write("\n")
myfile.close()

#Once this is all done, open in Excel, highlight everything, insert an area chart, and select one of the charts under "3D"