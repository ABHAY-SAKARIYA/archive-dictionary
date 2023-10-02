from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from time import sleep
from filemanager import File
import os

class dictionary:

    def __init__(self) -> None:
        pass

    def filterData(self) -> None:
        data = File.Csv.read(filename="data.csv")
        
        revisedData = []
        count = 1
        for index,row in data.iterrows():
            if row["mediatype"] == "texts":
                if "dictionary" in row["title"].lower():
                    if str(row["language"]).lower() == "english" or str(row["language"]).lower() == "hindi" or str(row["language"]).lower() == "gujarati" or str(row["language"]).lower() == "sanskrit" or str(row['language']).lower() == "eng":
                        createLink = f"http://archive.org/download/{row['identifier']}"
                        revisedData.append(createLink)
                        count+=1
                else:
                    continue
            else:
                continue
        print(count)
        try:
            File.Json.write(filename="downloadLink.json",data=revisedData)
            print("Saved To File1")
        except TypeError as e:
            print(e)

        

    # pdfs found with download link 31079 
    def download(self) -> None:

        links = File.Json.read(filename="downloadLink.json")
        op = webdriver.ChromeOptions()
        p = {
            "download.default_directory":r"D:\Abhay\archieve\Dictionary\28-09-23-dictionary", 
        "safebrowsing.enabled":"false",
        "plugins.always_open_pdf_externally": True
        }
        op.add_experimental_option("prefs", p)
        driver = webdriver.Chrome(options=op)

        sleep(30)
        count = 0			

        for link in links[6:10:1]:  

            driver.get(link)
            soup = BeautifulSoup(driver.page_source,"html.parser")

            sleep(5)
            clickCount = 0
            try:
                for data in soup.select("pre a"):
                    pdf = data.text

                    if clickCount == 0:
                        if ".pdf" in pdf or ".rar" in pdf:
                            driver.find_element(By.XPATH,f"//a[@href='{data.get('href')}']").click()
                            clickCount+=1
                        else:
                            pass
                    else:
                        pass

                sleep(10)

                dir_path = r"D:\Abhay\archieve\Dictionary\28-09-23-dictionary"
                stop = True
                while stop == True:

                    filesinfolder = os.listdir(dir_path)
                    index = 0
                    unconfirm = 0
                    file_count = 0
                    minused = False

                    for f in filesinfolder:

                        if "unconfirmed" in f.lower():
                            unconfirm = index
                        else:
                            index+=1
                        file_count+=1
                    
                    check = file_count
                    print(f"FileName : {filesinfolder[unconfirm]}")

                    if "unconfirmed" in filesinfolder[unconfirm].lower():
                        if minused == False:
                            file_count-=1
                            minused = True
                        else:
                            pass
                    else:
                        file_count+=1

                    print(f"Range Of File Found : {check}\nRange Of File - Unconfirmed File : {file_count}")
                    if file_count <= check:
                        sleep(20)
                    else:
                        stop = False

                print(f"Files Downloaded : {count}")
                count+=1
            except:
                File.Text.write(filename="DownloadError.txt",data=link)


obj1 = dictionary()
obj1.download()
# obj1.filterData()