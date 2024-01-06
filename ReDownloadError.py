from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os
from filemanager import File


class ErrorDownload:

    def __init__(self) -> None:
        pass

    def txt_json(self) -> list:
        txt = File.Text.read("test.txt")
        links = txt.split("\n")
        return links

    def Download(self):
        links = self.txt_json()
        dir_path = r"D:\Abhay\archieve\Dictionary"
        option = webdriver.ChromeOptions()
        
        pref = {
        'download.default_directory':dir_path,
        'safebrowsing.enabled':'false',
        'plugins.always_open_pdf_externally':True
        }
        
        option.add_experimental_option('prefs',pref)
        
        driver = webdriver.Chrome(options=option)

        for link in links:

            driver.get(link)
            time.sleep(5)

            while True:

                filesinFolder = os.listdir(dir_path)
                index = 0
                unconfirm = 0
                files_count = 0
                minused = False

                for f in filesinFolder:

                    if "unconfirmed" in f.lower() or ".crdownload" in f.lower():
                        unconfirm = index
                    else:
                        index += 1
                    files_count += 1

                check = files_count 
                
                
                if "unconfirmed" in filesinFolder[unconfirm].lower() or ".crdownload" in filesinFolder[unconfirm].lower():
                    if minused == False:
                        files_count -= 1
                        minused = True
                    else:
                        pass
                else:
                    files_count += 1

                if files_count <= check:
                    print("Waiting To Complete the download : ",filesinFolder[unconfirm])
                    time.sleep(30)
                else:
                    print("Download Completed ")
                    break



d = ErrorDownload()
d.Download()