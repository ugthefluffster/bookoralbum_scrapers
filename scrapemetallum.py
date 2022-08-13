from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

url = 'https://www.metal-archives.com/search/advanced/searching/bands?bandName=&genre=power+metal&country=&yearCreationFrom=&yearCreationTo=&bandNotes=&status=&themes=&location=&bandLabelName=#bands'
driver = webdriver.Firefox()
driver.get(url)
driver.implicitly_wait(5)
next = driver.find_elements(By.XPATH, '//*[@id="searchResultsBand_next"]')[0]
bandlist = []

for i in range(0,15):
    bandno = 1
    while bandno < 201:
        for i in range(0, 5):
            try:
                driver.implicitly_wait(5)
                bandname = driver.find_elements(By.XPATH, '/html/body/div/div[3]/div/div[1]/div/div/div/div/div[5]/table/tbody/tr['+str(bandno)+']/td[1]/a')
                bandlist.append(bandname[0].text)
                print(bandname[0].text)
                bandno += 1
            except:
                continue
            else:
                break
    next.click()


f = open('C:/Users/PCP/Desktop/game/bandlist.txt', "w", encoding="utf-8")
f.write(str(bandlist))
f.close()


