print(bytes(str(18),'utf-8'))
print(bytes([255]))
arrayOfBytes = [bytes("Wheel Speed",'utf-8'), bytes("Ride Height",'utf-8'), bytes("Temperature",'utf-8')]
print(arrayOfBytes[1])
print(len(arrayOfBytes[0]))


myDict = {}
myDict["NEW THING"] = [12]
print(myDict)