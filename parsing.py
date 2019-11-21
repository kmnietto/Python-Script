gps_track = open(r"H:\PythonGIS\Menietto\Data\gps_track.txt", "r")
print type(gps_track)
headerLine = gps_track.readline()
print headerLine
print type(headerLine)
valueList = headerLine.split(",")
print valueList
print type(valueList)
latindex = valueList.index("lat")
lonindex = valueList.index("long")
print latindex, lonindex
cord = []
for line in gps_track.readlines():
    segLine = line.split(",")
    cord.append([segLine[latindex],segLine[lonindex]])

print cord



