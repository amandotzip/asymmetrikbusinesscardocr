# Business Card Parser OCR
Programming challenge to parse data from a screenshot of a business card

# Requirements
Must be compiled and run via Python3

Required external packages (all quick pip installs)
* requests
* lxml
* pandas
* re

# Usage
Simply compile and run using python with your argument being the text file you wish to parse

You run python <address of business card parser file\> <text input file\>

For Example on Windows: 
    
    python .\BusinessCardParser.py .\examples\\01.txt 

Or for help:

    python .\BusinessCardParser.py -h

To test functionality, input via text file and run:

    Bobby Builder
    test@work.com
    1234567890

Then rearrange the order of the fields in any order and compare to see that the output is always the same.
# Error Handling
* Fields that are never provided will remain "N/A". 
* Too few or too many arguments won't be allowed.

# The thought process behind parsing
This was an interesting coding challenge. Initially one would assume that regex string validation would be adequate to parse all 3 fields, but the ambiguity of the real world makes that difficult. 

Patterns of data were considered when parsing:

All emails:
* Could have a name and a phone number within themselves
* Always have an @ and a .domain

All phone numbers:
* Had 10 or greater numbers
* Were indiscernable from a fax number

All names:
* Could be literally anything without numbers

## Dealing with names
Regex was used to handle the average case of phone numbers and emails, but names proved to be challenging. Anything could be a name. By definition "Software Engineer" and "Asymmetric Building" both qualify as a name, although a peculiar one. The approach I took was to data scrape the top 50 most common names in the US and compare those first names to the information provided. In a realistic setting, a software would have trouble distinguishing "Software Engineering" from an actual name, but this approach was the most practical and yielded the best results. There is still the matter that people may have infinitely many nicknames for each name, but that isn't in the scope of this program.
