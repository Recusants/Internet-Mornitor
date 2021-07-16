import os
import csv
from datetime import datetime



ip = "216.58.223.142"
status = 'Booting'
new_status = None

def csv_update(date, time, status):
	now = datetime.now()
	csv_name = str(now.strftime("%m_20%y_logs")) + ".csv"
	data = [(date, time, status)]
	with open(csv_name, "a") as fp:
	    writer = csv.writer(fp, delimiter=",")
	    writer.writerows(data)
	    fp.close()

while True:
	now = datetime.now()
	date = now.strftime("%d/%m/%y")
	time = now.strftime("%H:%M")
	response = os.popen(f"ping {ip}").read()
	if "Received = 4" in response:
		if new_status != status:
			print(time)
			print(status)
			csv_update(date, time, status)
			new_status = status
		status = 'Upp'
		print(status)

	else:
		if new_status != status:
			print(time)
			print(status)
			csv_update(date, time, status)
			new_status = status
		status = 'Down'
		print(status)



