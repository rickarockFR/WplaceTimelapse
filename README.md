# WplaceTimelapse

So, you want to create a timelapse from the [Wplace snaphot browser](https://archive.snowpity.lol)'s snapshots? Well, now you can!

Depending on what you download, it may take a while. To generate the full pretoria timelapse on my 500mb connection, it takes me around 2 hours!

Also, because of the way the snapshot bucket works, **making a gif out of only a small area still requires downloading the entire snapshot!**

Currently, the script allow you to:
- Decide which snapshot name to download from (check snapshot region on the snapshot viewer)
- Crop the gif to a specific part using wplace coordinates and the width / height
- Which timeframe to download snapshots from (using unix time, [you can use this converter](https://www.unixtimestamp.com/))
- What factor to downscale the image by (heavily recommended for big pieces, as this takes up a lot of memory)
- And, most obviously, **generate a gif from which options you chose! yay!!!**

Instructions when running the script should be very clear, please tell me if they aren't.

# How to use

You can download the necessary files [here](https://github.com/rickarockFR/WplaceTimelapse/raw/refs/heads/main/scripts.zip).

You will need to have [Python 3](https://www.python.org/downloads/), with the Pillow and ImageIO libraries. You can download these by either running the "requirements.bat" file, or getting them manually by following [this tutorial](https://packaging.python.org/en/latest/tutorials/installing-packages/).

You can run the script on Windows by running the "launch.bat" file.  
If you're on Linux, I assume you don't need help running a ***python script***.
