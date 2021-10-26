#import modules
import rpa as r
import pandas as pd

#read the excel file and store in dataframe variable df
df= pd.read_excel('challenge.xlsx')

#start the tagUI process
r.init()

#open the website
r.url('http://www.rpachallenge.com/')
r.wait(10)
#click on start button
r.click('//button[text()="Start"]')

#data entry operations
for index,row in df.iterrows():
    r.type('//input[@ng-reflect-name="labelFirstName"]',row['First Name'])
    r.type('//input[@ng-reflect-name="labelLastName"]',row['Last Name '])
    r.type('//input[@ng-reflect-name="labelCompanyName"]',row['Company Name'])
    r.type('//input[@ng-reflect-name="labelRole"]',row['Role in Company'])
    r.type('//input[@ng-reflect-name="labelAddress"]',row['Address'])
    r.type('//input[@ng-reflect-name="labelEmail"]',row['Email'])
    r.type('//input[@ng-reflect-name="labelPhone"]',str(row['Phone Number']))
    r.click('//input[@value="Submit"]')

#screenshot of webpage

r.snap('/html/body/app-root/div[2]','results.png')

#stop the tagui process
r.close()



    

