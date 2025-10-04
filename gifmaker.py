import imageio
import os
import download
import io
import requests
import datetime

#lastimg = None
#lastpos = None

anim_size = [1800,1300,1181,1169]

key = input('Enter the name of the snapshots you want to download (default: pretoria):\nKey corresponds to the "region" field on archive.snowpity.lol\n: ')
if key == '':
    key = 'pretoria'
    print('Field left empty, defaulting to pretoria')

imageio.plugins.pillow.Image.MAX_IMAGE_PIXELS = 933120000

def get_image(link):
    return requests.get(link).content

def input_integer(question):
    answer = None
    while type(answer) != int:
        answer = input(question)
        try:
            answer = int(answer)
        except ValueError:
            print('What you entered is not a number')
    return answer

test = 0

scale_factor = 10

i = len(download.image_list)
done = False
while not done:
    i -= 1
    entry = download.image_list[i]
    if entry[4] == key:
        done = True
        
        anim_size[0],anim_size[1] = entry[5]*1000, entry[6]*1000
        
        anim_size[2] = int(entry[2])
        anim_size[3] = int(entry[3])

custom_zone = None
while custom_zone != '0' and custom_zone != '1':
    custom_zone = input(f'''
This script will try to download the region at coordinates {anim_size[2]}, {anim_size[3]} and at a width of {anim_size[0]} by {anim_size[1]} pixels.
Enter 0 to leave these values as is or enter 1 to change them.
: ''')

if custom_zone == '1':
    input('''
You will need to enter the 4 coordinates of the top left corner of what you want to download.
These are the same coordinates as those of a blue marble template.
Please note that your drawing must be present on the snapshots you selected for anything to appear.
Again, you can check this is the case through the archive.snowpity.lol website.
(Press Enter to continue)''')

    anim_size[2] = input_integer('Enter 1st coordinate: ')
    anim_size[3] = input_integer('Enter 2nd coordinate: ')
    anim_size[2] += input_integer('Enter 3rd coordinate: ')/1000
    anim_size[3] += input_integer('Enter 4th coordinate: ')/1000

    anim_size[0] = input_integer('\nPlease enter the width of the area you want to download: ')
    anim_size[1] = input_integer('\nPlease enter the height of the area you want to download: ')

min_unix = 0
max_unix = 9999999999
if input_integer('''
By default, this script will use all available snapshots.
Do you want to set a timeframe to generate the gif from?
(Will ask you to enter times in *unix time*. Use a converter online if you need to.)
Enter 1 if yes, enter 0 if no.''') > 0:
    min_unix = input_integer('Unix time to start from (enter 0 to start from the first snapshots): ')
    max_unix = input_integer('Unix time to end at (enter 0 to go until the most recent snapshots): ')
    if max_unix == 0:
        max_unix = 9999999999

delays = []
#delay_overflow = 0
#total_overflow = 0
for entryID in range(len(download.image_list)-1):
    if download.image_list[entryID][4] == key and int(download.image_list[entryID][0]) > min_unix and int(download.image_list[entryID][0]) < max_unix:
        time = (int(download.image_list[entryID+1][0])-int(download.image_list[entryID][0]))//60
        delays.append(time)
if delays == []:
    print("\n\nSomething has gone wrong! This script did not find any images with that satisfy the key and timeframe. If you're seeing this and think this shouldn't happen, please contact thefridgecave on discord and tell him his script is haunted again.")
delays[-1] = 1000
#delays.append(10000)
print(f'\nYou will be downloading {len(delays)} frames.\n')


scale_factor = input_integer('''
Finally, by what factor do you cant this to be scaled down?
For very big images, I recommend entering 10
For smaller images, you can enter 1 to have a full resolution version
As a warning: DO NOT enter 1 if you are downloading very big areas. I have crashed my computer multiple times when trying that. It takes A LOT of memory.
Scale factor you want to use: ''')

anim_size[2] = int((anim_size[2]*1000)//scale_factor)
anim_size[3] = int((anim_size[3]*1000)//scale_factor)
anim_size[0] = anim_size[0]//scale_factor
anim_size[1] = anim_size[1]//scale_factor

print('\n\nAll done! You can now sit back and relax while this script downloads everything.\nPlease note that this will take a while, even moreso if you have bad internet.')

curDelay = 0
with imageio.get_writer('out.gif', mode='I', duration=[*delays], loop=0) as writer:
    for entryID in range(len(download.image_list)):
        entry = download.image_list[entryID]
        if entry[4] == key and int(entry[0]) > min_unix and int(entry[0]) < max_unix:
            alphaimage = imageio.plugins.pillow.Image.open(io.BytesIO(get_image(entry[1]))).convert('RGBA')
            alphaimage = alphaimage.resize((alphaimage.size[0]//scale_factor, alphaimage.size[1]//scale_factor))
            image = imageio.plugins.pillow.Image.new('RGBA', alphaimage.size, (255,255,255))
            image.paste(alphaimage, (0,0), alphaimage)
            fullimg = imageio.plugins.pillow.Image.new('RGBA', (anim_size[0],anim_size[1]), (255,255,255))
            #if lastimg != None:
            #    fullimg.paste(lastimg)
            fullimg.paste(image, (((int(entry[2])*1000)//scale_factor-anim_size[2]),((int(entry[3])*1000)//scale_factor-anim_size[3])))


            writer.append_data(fullimg)
            #lastimg = fullimg
            #lastpos = ((int(entry[2])-anim_size[2]),(int(entry[3])-anim_size[3]))

            print(entry[4], entry[0], delays[curDelay], f"Frame {curDelay+1}/{len(delays)}', f'Snapshot taken at {datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')}")
            curDelay+=1
            test+=1

