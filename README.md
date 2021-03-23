# itdashboard_project
Python, RPA Framework


### Challenge

Your challenge is to automate the process of extracting data from [**itdashboard.gov**](http://itdashboard.gov/).

- The bot should get a list of agencies and the amount of spending from the main page
    - Click "**DIVE IN"** on the homepage to reveal the spend amounts for each agency
    - Write the amounts to an excel file and call the sheet "**Agencies**".
- Then the bot should select one of the agencies, for example, National Science Foundation (this should be configured in a file or on a Robocloud)
- Going to the agency page scrape a table with all "**Individual Investments**" and write it to a new sheet in excel.
- If the "**UII**" column contains a link, open it and download PDF with Business Case (button "**Download Business Case PDF**")
- Your solution should be submitted and tested on [**Robocloud**](https://cloud.robocorp.com/).
- Store downloaded files and Excel sheet to the root of the `output` folder

Please leverage pure python using the **[rpaframework](https://rpaframework.org/)** for this exercise

**Bonus**: We are looking for people that like going the extra mile if time allows or if your curiosity gets the best of you 😎

Extract data from PDF. You need to get the data from **Section A** in each PDF. Then compare the value "**Name of this Investment**" with the column "**Investment Title**", and the value "**Unique Investment Identifier (UII)**" with the column "**UII**"



###################################################################################################
Solution deploying using **Windows 10** and **Chrome 87.0.4280.88** 


### Tech 
* python 3.9
* rpaframework 7.4.2


#### Installation.Build And Run
https://cloud.robocorp.com/

