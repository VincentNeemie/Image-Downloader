import os
import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


# selenium options
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
#put your selenium data directory here so that chrome can save the cookies
#if you dont have one, create one and put the path 
#download the webdriver from https://chromedriver.chromium.org/downloads
userdatadir = ""
options.add_argument(f"user-data-dir={userdatadir}")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
try:
    driver = webdriver.Chrome(options=options)
except:
    print("Couldn't find the selenium userdata, please put the correct userdata in the userdatadir variable")
    exit()
def imagemain():
    
    pinterestimage = (By.XPATH, '//*[@class="hCL kVc L4E MI"]')
    # pinterest hwa kVc MIw L4E = videos
    # open pinterest and get the images
    while True:
        inputname = input("Enter the name: ")
        driver.get(f'https://pinterest.com/search/pins/?q={inputname}')

        # make a directory in the folder Images with the name of the inputname
        def makefolder():
            try:
                os.mkdir(f"{inputname}")
            except:
                print('Folder already exists')
        makefolder()
        
        imagelists = []
        error_count = 0

        # get the images
        def lookforimages():
            nonlocal error_count
            images = driver.find_elements(By.XPATH, '//*[@class="hCL kVc L4E MIw"]')
            # for each element in the images list get the src and print it
            for image in images:
                # try to get the image src
                try:
                    newimage = image.get_attribute('src')
                    print(newimage)

                    # if newimage is not in the imagelist add it and download it to the folder Images
                    if newimage not in imagelists:
                        imagelists.append(newimage)
                        urllib.request.urlretrieve(newimage, f"{inputname}\\" + newimage.split('/')[-1])
                        
                    else:
                
                        print('Image Already Downloaded')
                        error_count += 1
                        if error_count >= 500:
                            choice = input("Error count reached 100, what do you want to do?\n1. Restart\n2. Quit?\n3. Continue\n")
                            if choice == "1":
                                imagemain()
                            if choice == '2':
                                
                                exit()
                            else:
                                error_count = 0
                                continue

                except:
                    print('Error')
                    error_count += 1
                    if error_count >= 500:
                        choice = input("Error count reached 100, what do you want to do?\n1. Restart\n2. Quit?\n3. Continue\n")
                        if choice == "1":
                            imagemain()
                        if choice == '2':
                            
                            exit()
                        else:
                            error_count = 0
                            continue

        def pagedown():
            body = driver.find_element(By.CSS_SELECTOR, 'body')
            body.send_keys(Keys.PAGE_DOWN)

        while True:
            lookforimages()
            pagedown()

imagemain()