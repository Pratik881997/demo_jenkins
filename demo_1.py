from datetime import datetime
import csv

datetime_d = datetime.now()

print(datetime.now())

file = open("/home/ubuntu/demo_jenkins.csv", mode="a", encoding="utf-8", newline="")

writer = csv.writer(file)

writer.writerow([datetime_d])