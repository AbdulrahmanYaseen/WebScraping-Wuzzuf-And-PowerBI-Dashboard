# Web Scrape Wuzzuf For a Job Title and Get a Dashboard Of Your Own

### The following libraries are expected to be used in this project:

- Selenium 
- Beautifulsoup
- requests
- zip_longest

> Actually only one of Selenium or Beautifulsoup could have done the job but I used both of them for learning purpose

### Perquisites:

- Run Cmd and run the following(install needed libraries):
  - "pip install selenium"
  - "pip install requests"
  - "Pip install beautifulsoup4"

- Download chrome driver from selenium from here: https://www.selenium.dev/downloads/  under browsers section
> for windows only 32bit is available, but there is no problem with using it on 64bit machine

### How it works:
- Enter the required data here which are basically:
  - the title you want to get the data about
  - the path where your downloaded driver is saved at
  - the path where you want to save the scraped data 

![1](https://user-images.githubusercontent.com/77448625/126833930-a6a7212f-c0f1-46f5-afce-e8c93d570a83.jpg)

- The code simply uses beautifulsoup for scraping the search pages, each page holds around 15 search results, so with beautifulsoup I only scraped the "surface" info like job title, link, location, and company name
- For inner pages -the jobs- I used selenium to iterate through each page and scrape the desired data by it's X_Path, you will actually see the chrome driver iterating through each page, which takes a long time of course based on how many search results you have.

![Untitled](https://user-images.githubusercontent.com/77448625/126835823-5570c169-53da-4ffc-b6e1-03b8f3abfc9b.gif)


- Last, we zip all the gathered data into csv file and save it, the last cell is to make sure all lists are the same length in other words the data for each record represents the jo title in front of it, no shifting happened or anything

### The Dashboard:
- You can Download the pbix file from the files upove
- First: Change the datasource to your saved file, apply and you are good to go



