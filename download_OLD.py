import requests
import xml.etree.ElementTree as ET
import PIL.Image as Image
from os.path import isfile

def save_image(path, link, data):
    imagedata = requests.get(link)
    with open('backups/'+path+'.png', 'wb') as f:
        f.write(imagedata.content)
        f.close()
    with open('backups/'+path+'.txt', 'w') as f:
        f.write(data)
        f.close()


data = requests.get('https://objects.hydn.us/wplace-archive/')

root = ET.fromstring(data.content)

filename = ''
lastmodified = ''
fullname = ''

image_list = []

for child in root:
    for child2 in child:
        if "key" in child2.tag.lower():
            #print (child2.text)
            filename = child2.text
            print(filename)
        if 'LastModified' in child2.tag:
            #print(child2.text)
            lastmodified = child2.text
    if filename != '':
        fullname = filename
        filename = filename.replace('.png','')
        filename = filename.replace('full/','')
        filename = filename.split('-')
        #filename[1] = filename[1]+'.png'

        lastmodified = lastmodified.replace('Z','')
        lastmodified = lastmodified.split('T')

        #print(fullname)
        #print(filename[1])
        #print(filename[2], filename[3])
        #print(lastmodified[0], lastmodified[1])

        #if isfile(f'backups/{filename[1]}.png') and isfile(f'backups/{filename[1]}.txt'):
        #    print("exists lol")
        #    with open(f'backups/{filename[1]}.txt', 'w') as f:
        #        f.write(f'{filename[2]};;;{filename[3]};;;{filename[0]}')
        #else:
        #    save_image(filename[1], f'https://objects.hydn.us/wplace-archive/{fullname}', f'{filename[2]};;;{filename[3]};;;{filename[0]}')
        image_list.append([filename[1], f'https://objects.hydn.us/wplace-archive/{fullname}', filename[2], filename[3], filename[0]])
        
        

    #print()
    filename = ''
    lastmodified = ''

image_list.sort(key=lambda tup: tup[0])
