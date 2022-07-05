from selenium import webdriver
from selenium.webdriver.common.by import By
import codecs

####################################################
#CHANGE POINTS
startPoint = "54.349755317206004, 18.652511907042967"
endPoint = "54.31822735730348, 18.551403358929083"
txtFileLocation = r"C:\MichalDurlak\result.txt"
htmlFileLocation = r"C:\MichalDurlak\result.html"
####################################################


#Save to file
##txt file
f = open(txtFileLocation, "w")
##html file
htmlFile = codecs.open(txtFileLocation, "w", "utf-8-sig")
##basic html scripts start
htmlFile.write("<!DOCTYPE html> \n <html lang=\"en\"> \n <head> \n  <style> \n body {background-color: #1c1c1c; \n color: white;} \n </style> \n <meta charset=\"UTF-8\"> \n <title>GoogleTripToWork</title> \n </head> \n <body> \n")

#Static
URL = f"https://www.google.pl/maps/dir/{startPoint.replace(' ','')}/{endPoint.replace(' ','')}/"
CHROMEPATHWIN = "ChromeDriver/chromedriver_win32/chromedriver.exe"

#Open Chrome

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=CHROMEPATHWIN, options=options)

# driver = webdriver.Chrome(CHROMEPATHWIN)
driver.get(URL)
#Click accept button

try:
    acceptButton = driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div/div/button/span')
    acceptButton.click()
except:
    pass

#First route
try:
    firstTime = driver.find_element(By.XPATH,'//*[@id="section-directions-trip-0"]/div/div[1]/div[1]/div[1]/span[1]').text
    firstRouteTittle = driver.find_element(By.XPATH,'//*[@id="section-directions-trip-title-0"]/span').text
    firstRouteDescription = driver.find_element(By.XPATH,'//*[@id="section-directions-trip-0"]/div/div[1]/div[3]/span[1]/span[1]/span[2]').text
    ## Write to text file
    f.write("Czas dojazdu: " + firstTime+"\n ")
    f.write("Trasa: " + firstRouteTittle+"\n")
    f.write("Opis trasy: " + firstRouteDescription+"\n")
    ## Write to html file
    htmlFile.write("<h1> Czas dojazdu: <b> " + firstTime+"</b></h1> \n <br>")
    htmlFile.write("Trasa: " + firstRouteTittle+"\n <br>")
    htmlFile.write("Opis trasy: " + firstRouteDescription+"\n <br>")

except:
    try:
        firstTime = driver.find_element(By.XPATH,'//*[@id="section-directions-trip-0"]/div/div[3]/div[1]/div[1]').text
        firstRouteTittle = driver.find_element(By.XPATH,'//*[@id="section-directions-trip-title-0"]/span').text
        firstRouteDescription = "its really close"
        ## Write to text file
        f.write("Czas dojazdu: " + firstTime+"\n")
        f.write("Trasa: " + firstRouteTittle+"\n")
        f.write("Opis trasy: " + firstRouteDescription+"\n")
        ## Write to html file
        htmlFile.write("Czas dojazdu:  <b>" + firstTime + "</b> \n <br>")
        htmlFile.write("Trasa: " + firstRouteTittle + "\n <br>")
        htmlFile.write("Opis trasy: " + firstRouteDescription + "\n <br>")

    except:
        pass

#Second route
try:
    secondTime = driver.find_element(By.XPATH,'//*[@id="section-directions-trip-1"]/div/div[1]/div[1]/div[1]/span[1]').text
    secondRouteTittle = driver.find_element(By.XPATH,'//*[@id="section-directions-trip-title-1"]/span').text
    secondRouteDescription = driver.find_element(By.XPATH,'//*[@id="section-directions-trip-1"]/div/div[1]/div[3]/span[1]/span[1]/span[2]').text
    ## Write to text file
    f.write("Czas dojazdu: " + secondTime+"\n")
    f.write("Trasa: " + secondRouteTittle+"\n")
    f.write("Opis trasy: " + secondRouteDescription+"\n")
    ## Write to html file
    htmlFile.write("Czas dojazdu: <b>" + secondTime+"</b>\n <br>")
    htmlFile.write("Trasa: " + secondRouteTittle+"\n <br>")
    htmlFile.write("Opis trasy: " + secondRouteDescription+"\n <br>")

except:
    try:
        secondTime = driver.find_element(By.XPATH,'//*[@id="section-directions-trip-1"]/div/div[3]/div[1]/div[1]').text
        secondRouteTittle = driver.find_element(By.XPATH,'//*[@id="section-directions-trip-title-1"]/span').text
        secondRouteDescription = "its really close"
        ## Write to text file
        f.write("Czas dojazdu: " + secondTime+"\n")
        f.write("Trasa: " + secondRouteTittle+"\n")
        f.write("Opis trasy: " + secondRouteDescription+"\n")
        ## Write to html file
        htmlFile.write("Czas dojazdu: <b>" + secondTime + "</b> \n <br>")
        htmlFile.write("Trasa: " + secondRouteTittle + "\n <br>")
        htmlFile.write("Opis trasy: " + secondRouteDescription + "\n <br>")

    except:
        pass

#Get name of source and destination
sourcePoint = driver.find_element(By.XPATH,'//*[@id="sb_ifc50"]/input').get_attribute("aria-label")
destinationPoint = driver.find_element(By.XPATH,'//*[@id="sb_ifc51"]/input').get_attribute("aria-label")
## Write to text file
f.write("Z punktu: " + sourcePoint+"\n")
f.write("Do punktu: " + destinationPoint+"\n")
## Write to html file
htmlFile.write(sourcePoint+"\n <br>")
htmlFile.write(destinationPoint+"\n <br>")

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
driver.quit()

##basic html scripts stop
htmlFile.write("\n </body> \n </html>")
#close files
f.close()
htmlFile.close()

quit()