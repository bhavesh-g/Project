# Project
### Dependencies
- Python 3
- Scrapy

### Important Instructions
- The output file name must not be changed, default is '**output.json**'
- The output file will be stored at '**data/output.json**' only, please don't try to change it.
- The logfile will be in the same directory named **logs.txt**

### Usage:
- Clone the repository 
- open cmd and navigate to this directory
- type this command **_scrapy runspider extractor.py -o data/output.json --logfile logs.txt_**
- read the onscreen instruction carefully.
- enter the website starting URL to start scraping desired text, (without 'www')
- after finishing the scraping, check **data/output.json**, for output as specified in the challenge.

### Key Points:
- This program outputs the result in specified format i.e JSON only.
- The JSON file has its contents in Unicode strings.
- All the indic fonts such as Hindi, Tamil, Bengali etc. can be scraped easily and stored in unicoded strings
- To read the JSON contents exactly, just print it out in Python interpretor or copy the contents and use a free service like [https://codebeautify.org/jsonviewer]

### Testing_sample_outputs
Here the JSON files named **testing_output1.json** and **testing_output2.json** were tested by me, as specified in the challenge.

- Starting website URL for **testing_output1.json** is https://magazine.iit.edu
- Starting website URL for **testing_output2.json** is http://dustyfeet.com

## Contact:
If any problem occurs, please feel free to contact me at:
- Email : guptabhavesh6@gmail.com
I would be happy to debug it or help with anything.

# Thank You
