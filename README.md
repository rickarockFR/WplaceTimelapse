# WplaceTimelapse

So, you want to create a timelapse from the [Wplace snaphot browser](https://archive.snowpity.lol)'s snapshots? Well, now you can!

Depending on what you download, it may take a while. To generate the full pretoria timelapse on my 500mb connection, it takes me around 2 hours!

Also, because of the way the snapshot bucket works, **making a gif out of only a small area still requires downloading the entire snapshot!**

Currently, the script allow you to:
- Decide which snapshot name to download from (check snapshot region on the snapshot viewer)
- Crop the gif to a specific part using wplace coordinates and the width / height
- Which timeframe to download snapshots from (using unix time, [you can use this converter](https://www.unixtimestamp.com/))
- What factor to downscale the image by (heavily recommended for big pieces, as this takes up a lot of memory)

Instructions in the script should be very clear

# How to use
You will need to have [Python 3](https://www.python.org/downloads/), with the [Pillow](https://pypi.org/project/pillow/) and [ImageIO](https://pypi.org/project/imageio/) libraries. [(Here's how to download packages on Python)](https://packaging.python.org/en/latest/tutorials/installing-packages/)

You will need both the download.py and gifmaker.py files in the same folder, which you can download [here](scripts.zip)

How to run the script on Windows: (if you are on linux, I assume you know how to use python)  
Open 
