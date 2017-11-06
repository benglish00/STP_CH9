import os
import csv

#set a path and filename
pathname = os.path.join("C:\\","Users", "Brian", "OneDrive", "Data", "FPGA_Sensor_Test")
filename = os.path.join(pathname,"st.txt")
csvname = os.path.join(pathname,"st.csv")
print(filename)

#Write a file to the path\filename
with open(filename,"w") as f:
    f.write("Hi from Python!")

with open(filename,"r") as f:
    print(f.read())

with open(csvname, "w", newline='') as f:
    w = csv.writer(f,
                   delimiter = ",")
    w.writerow(["one",
                "two",
                "three"])
    w.writerow(["four",
                "five",
                "six"])

with open(csvname, "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))

#Challenge 1. Find a file and print its contents
calData = os.path.join(pathname, "Cal1430.csv")
with open(calData, "r") as data:
    Cal1430 = csv.reader(data, delimiter=",")
    for row in Cal1430:
        print(",".join(row))




