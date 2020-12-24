import urllib2
import os

output_dir = '/Users/quocdungdang/Project/py_download_img/img/remu-suzumori'
image_url = 'https://javhd.pics/photos/japanese/remu-suzumori/3/remu-suzumori-6.jpg'

# Make output directory if not exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# save path
image_save_path = output_dir + '/' + os.path.basename(image_url)
# Download file from url
# urllib.request.urlretrieve(image_url, image_save_path)

filedata = urllib2.urlopen(image_url)
datatowrite = filedata.read()
 
with open(image_save_path, 'wb') as f:
    f.write(datatowrite)

print(image_save_path)


# import urllib2

# filedata = urllib2.urlopen('http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg')
# datatowrite = filedata.read()
 
# with open('/Users/quocdungdang/Project/py_download_img/img', 'wb') as f:
#     f.write(datatowrite)


