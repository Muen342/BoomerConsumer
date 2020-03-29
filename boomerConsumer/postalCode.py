#'pip install requests BeatifulSoup' is required for this script
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import math
import requests
from itertools import cycle
import traceback
from lxml.html import fromstring
import time
import json

def nearestPostalCode():
    return "hello world"


def my_function():
    print("Hello World")

def testFunc():
    raw_html = open('contrived.html').read()
    html = BeautifulSoup(raw_html, 'html.parser')
    for p in html.select('p'):
        if p['id'] == 'walrus':
            print(p.text)

# def parsePostal(postalCode): 
#     url = "http://www.zip-codes.com/canadian/postal-code.asp?postalcode=" + postalCode.lower().replace(" ", "")
#     raw_html = simple_get(url)
    
#     if raw_html is not None:
#         raw_text = ''
#         html =  BeautifulSoup(raw_html, 'html.parser')
#         for td in html.select('td'):
#             raw_text += td.text
        
#         lat_split = raw_text.lower().split('latitude')
#         lat_split = lat_split[2].split('elevation')[0]
#         latitude =  lat_split.split(':')[1].split('longitude')[0]
#         longitude = lat_split.split('longitude:')[1]

#         print("latitude: " + latitude)
#         print("longitude: " + longitude)

#         lat_long_list = [float(latitude), float(longitude)]
#         return lat_long_list

           
#     else:
#         print("No data found for that postal code")
#         return [None,None]

#https://geocoder.ca/?locate=l8v4x5&geoit=XML&json=1

def parsePostal(postalCode):
    time.sleep(2)
    print(postalCode) 
    url = r"https://geocoder.ca/?locate=" + postalCode.lower().replace(" ", "") + r"&geoit=XML&json=1"
    
    try:
        response = requests.get(url)
    except:
        print("Skipping. Connnection error")
        return [None, None]
    #print(response.json())
    data = response.json()
    data = json.dumps(data)
    #print(data)
    latitude = data.split('longt')[1].split('": "')[1].split('",')[0]
    longitude = data.split('latt')[1].split('": "')[1].split('"}')[0]
    #print('latitude: ' + latitude)
    #print('longitude: ' + longitude)
    return [float(latitude), float(longitude)]
def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    #time.sleep(5)
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None



def complex_get(url):
    #print("called simpleget")
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    proxies = get_proxies()
    proxy_pool = cycle(proxies)
    proxy = next(proxy_pool)
    #try:
    
    for i in range(1,len(proxies)):
        
        #Get a proxy from the pool
        proxy = next(proxy_pool)
        print("Request #%d"%i)
        try:
            response = get(url, proxies={"http": proxy, "https": proxy})
            #print(response.json())
            #print(response.content)
            if(is_good_response(response)):
                if('elevation' in response.content):   
                    print('good request')
                    return response.content
                else: print('Bad Request')
            else: print('bad request')
        except:
            #Most free proxies will often get connection errors. You will have retry the entire request using another proxy to work. 
            #We will just skip retries as its beyond the scope of this tutorial and we are only downloading a single url 
            print("Skipping. Connnection error")
    
    return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    print(e)    

def get_proxies():
    proxies = []
    with open("http_proxies.txt") as file_in:
        lines = []
        for line in file_in:
            lines.append(line.replace('\n',''))
    proxies = lines
    return proxies

def get_postalCodes():
    postalCodes = []
    with open("postalcodes.txt") as file_in:
        lines = []
        for line in file_in:
            lines.append(line.replace('\n',''))
    postalCodes = lines
    return postalCodes

def getDistFromLatLon(lat1,lon1,lat2,lon2): #in km
    R = 6371 # Radius of the earth in km
    dLat = deg2rad(lat2-lat1)  # deg2rad below
    dLon = deg2rad(lon2-lon1)
    a = math.sin(dLat/2) * math.sin(dLat/2) + math.cos(deg2rad(lat1)) * math.cos(deg2rad(lat2)) * math.sin(dLon/2) * math.sin(dLon/2) 
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a)) 
    d = R * c # Distance in km
    return round(d,2)


def deg2rad(deg):
    return deg * (math.pi/180)

def populateDist(postalCode, codeList):
    lat_lon_list = parsePostal(postalCode)
    lat1 = lat_lon_list[0]
    lon1 = lat_lon_list[1]
    #i = 0
    print(codeList[1])
    distList = []
    for lat_lon in codeList[1]:
        print(lat_lon)
        distList.append(getDistFromLatLon(lat1, lon1, lat_lon[0], lat_lon[1]))
    print(distList)
    
    codeList.append(distList)
    return codeList


postal_code_list = [get_postalCodes(), []]

for code in postal_code_list[0]:
    var = parsePostal(code)
    postal_code_list[1].append(var)



postal_code_list = populateDist('l5k2m3',postal_code_list)

print(postal_code_list)

objList = []

for idx in range(len(postal_code_list[1])):
    obj = [postal_code_list[0][idx], postal_code_list[1][idx], postal_code_list[2][idx]]
    objList.append(obj)

print(objList)
objList =  sorted(objList, key=lambda x: x[2])
print("")
print(objList)
print("")
print(objList[0]) #closest location

# indices = len
# indices.sort(key = lol[1].__getitem__)
# for i, sublist in enumerate(lol):
#   lol[i] = [sublist[j] for j in indices]
