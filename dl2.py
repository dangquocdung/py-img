import requests
import os

dvs = ['iori-kogawa']
for dv in dvs:
    
    output_dir = '/Users/quocdungdang/Project/py_download_img/img/' + str(dv)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for x in range(1, 95):

        for y in range(1, 13):

            url = 'https://javhd.pics/photos/japanese/' + str(dv) + '/' + str(x) + '/' + str(dv) + '-' + str(y) + '.jpg'

            # save path
            image_save_path = output_dir + '/' + str(x) + '-' + os.path.basename(url)

            print('Beginning file download with requests')

            r = requests.get(url)

            content_length_s = r.headers.get('content-length')

            

            if content_length_s > 10000:

                with open(image_save_path, 'wb') as f:
                    f.write(r.content)

                # Retrieve HTTP meta-data
                print(r.status_code)
                print(r.headers['content-type'])
                print(r.headers['content-length'])
                print(r.encoding)
                print(image_save_path)
            else:
                break