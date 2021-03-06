# Christopher Geier (cpg3rb)
import math
import webbrowser
import urllib.request


def distance_between(lat_1, lon_1, lat_2, lon_2):
    '''Uses the "great circle distance" formula and the circumference of the earth
    to convert two GPS coordinates to the miles separating them'''
    lat_1, lon_1 = math.radians(lat_1), math.radians(lon_1)
    lat_2, lon_2 = math.radians(lat_2), math.radians(lon_2)
    theta = lon_1 - lon_2
    dist = math.sin(lat_1)*math.sin(lat_2) + math.cos(lat_1)*math.cos(lat_2)*math.cos(theta)
    dist = math.acos(dist)
    dist = math.degrees(dist)
    dist = dist * 69.06         # 69.09 = circumference of earth in miles / 360 degrees

    return dist

file = urllib.request.urlopen('http://cs1110.cs.virginia.edu/files/wendys.csv').read().decode('utf-8').splitlines()
loc_list = []
for line in range(0,len(file)):
    loc_list.append(file[line].split(','))

latitude = str(input('Enter a latitude: '))
longitude = str(input('Enter a longitude: '))

min_dist = None
min_wendys = ''
for wendys_coord in loc_list:
    distance = distance_between(float(latitude), float(longitude), float(wendys_coord[1]), float(wendys_coord[0]))
    if min_dist is None:
        min_dist = distance
        closest_wendys = str(wendys_coord[0]) + ',' + str(wendys_coord[1])
    elif distance <= min_dist:
        min_dist = distance
        closest_wendys = str(wendys_coord[1]) + ',' + str(wendys_coord[0])

url = 'http://maps.google.com/maps?q=' + closest_wendys
webbrowser.open(url)
