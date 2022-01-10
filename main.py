from selenium import webdriver
from selenium.webdriver.common.by import By

####################################################
#CHANGE POINTS
startPoint = "54.34958325688697, 18.64803248596945"
endPoint = "54.349768349180636, 18.65767397279539"
####################################################


#Static
URL = f"https://www.google.pl/maps/dir/{startPoint.replace(' ','')}/{endPoint.replace(' ','')}/"
CHROMEPATHWIN = "ChromeDriver/chromedriver_win32/chromedriver.exe"

#Open Chrome
driver = webdriver.Chrome(CHROMEPATHWIN)
driver.get(URL)

#Click accept button
acceptButton = driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div/div/button/span')
acceptButton.click()

#First route
try:
    firstTime = driver.find_element(By.XPATH,'//*[@id="section-directions-trip-0"]/div/div[1]/div[1]/div[1]/span[1]').text
    firstRouteTittle = driver.find_element(By.XPATH,'//*[@id="section-directions-trip-title-0"]/span').text
    firstRouteDescription = driver.find_element(By.XPATH,'//*[@id="section-directions-trip-0"]/div/div[1]/div[3]/span[1]/span[1]/span[2]').text
except:
    try:
        firstTime = driver.find_element(By.XPATH,'//*[@id="section-directions-trip-0"]/div/div[3]/div[1]/div[1]').text
        firstRouteTittle = driver.find_element(By.XPATH,'//*[@id="section-directions-trip-title-0"]/span').text
        firstRouteDescription = "its really close"
    except:
        pass

#Second route
try:
    secondTime = driver.find_element(By.XPATH,'//*[@id="section-directions-trip-1"]/div/div[1]/div[1]/div[1]/span[1]').text
    secondRouteTittle = driver.find_element(By.XPATH,'//*[@id="section-directions-trip-title-1"]/span').text
    secondRouteDescription = driver.find_element(By.XPATH,'//*[@id="section-directions-trip-1"]/div/div[1]/div[3]/span[1]/span[1]/span[2]').text
except:
    try:
        secondTime = driver.find_element(By.XPATH,'//*[@id="section-directions-trip-1"]/div/div[3]/div[1]/div[1]').text
        secondRouteTittle = driver.find_element(By.XPATH,'//*[@id="section-directions-trip-title-1"]/span').text
        secondRouteDescription = "its really close"
    except:
        pass

#Get name of source and destination
sourcePoint = driver.find_element(By.XPATH,'//*[@id="sb_ifc50"]/input').get_attribute("aria-label")
destinationPoint = driver.find_element(By.XPATH,'//*[@id="sb_ifc51"]/input').get_attribute("aria-label")


#Show all data
#Source and destination
print("From:",sourcePoint.replace('Punkt początkowy ',''))
print("To:",destinationPoint.replace('Miejsce docelowe ',''))

#Trip1 details
try:
    print("First time: ",firstTime)
    print("First trip via: ",firstRouteTittle)
    print("First trip description: ",firstRouteDescription)
except:
    print("No route could be found")

#Trip2 details
try:
    print("Second time: ",secondTime)
    print("Second trip via: ",secondRouteTittle)
    print("Second trip description: ",secondRouteDescription)
except:
    pass

#Print url to fast access
print(URL)

#Close Chrome app
driver.close()