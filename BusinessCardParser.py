
import requests
import lxml.html as lh
import pandas as pd
import re
import sys
from ContactInfo import ContactInfo

class BusinessCardParser:
    parsedName = "N/A"
    parsedPhoneNumber = "N/A"
    parsedEmail = "N/A"
  

    if len(sys.argv) == 1 or len(sys.argv) > 2:
        print("Too few or too many arguments. Try \"python BusinessCardParser -h\" for help")
        sys.exit()
    elif sys.argv[1] == "-h":
        helpString = """Usage:
    Windows: 
        python .\BusinessCardParser.py <file>
    Linux:
        python BusinessCardParser.py <file>
    Example: 
        python .\BusinessCardParser.py .\examples\\01.txt

[file]: Address of text file you wish to parse

Business Card Parser OCR

    Takes contact information data as .txt files, then parses them for name, phone number, and email, then
    prints parsed data."""
        print(helpString)
        sys.exit()
    with open(sys.argv[1], 'r') as file:
        file_contents = file.read()
        

    
    lines = file_contents.split('\n')

    #email is the most "flexible" in formatting to parse, so we parse and remove it first
    #if a valid email is found, save and remove
    for item in lines:
        if re.search("^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$", item) != None:
            parsedEmail = item
            lines.remove(item)

    #Removes fax numbers since we're looking for phone numbers
    for item in lines:
        if ("fax" or "Fax" or "FAX") in item:
            print(item)
            lines.remove(item)
    #if string has 10 or more digits, it must be either a phone # or email, and we've already handled email
    for item in lines:
        # if line has 10 digits or greater, investigate if number
        digitCount = 0
        for i in item:
            if i.isdigit():
                digitCount += 1
        if digitCount >= 10:
            #strip away all non digits since this must be a phone number
            phoneDigits = re.compile(r'\d+(?:\.\d+)?')
            phoneDigitsList = phoneDigits.findall(item)
            #concatenate digits to complete number
            parsedPhoneNumber = ""
            for i in phoneDigitsList:
                parsedPhoneNumber += i
            lines.remove(item)
        #if phone number is valid via regex, store and consume
        elif re.search("^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$", item) != None:
            parsedPhoneNumber = item
            lines.remove(item)


    #Data scraping top 50 most common names in order to parse names from Business Cards
    #Names will be stored in topNames
    URL = "https://www.ssa.gov/oact/babynames/decades/century.html"
    page = requests.get(URL)
    doc = lh.fromstring(page.content)
    tr_elements = doc.xpath('//tr')

    topNames=[]
    i=0
    #In each element e in tr elements, then each tr tag in elements, extract the name then add to the
    #topNames list
    for e in tr_elements:
        for t in e:
            i+=1
            name=t.text_content()
            if len(name) > 0 and not name[0].isdigit():
                topNames.append((name))
                #Manually adding nicknames for the top 20 most popular names
                if (name == "Michael"):
                    topNames.append(("Mike"))
                if (name == "Nicholas"):
                    topNames.append(("Nick"))
                if (name == "Joseph"):
                    topNames.append(("Joe"))

    #Tidying data
    topNames = topNames[7:len(topNames)-1]
    #If name is found in top 50 names, store and consume the value
    for item in lines:
        if item.split()[0] in topNames:
            parsedName = item
            lines.remove(item)

    contact = ContactInfo(parsedName, parsedPhoneNumber, parsedEmail)
    print(contact)