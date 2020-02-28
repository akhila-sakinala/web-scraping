# web-scraping
Web scraping using python 

## Packages-needed
pip install -r requirements.txt

### Requirements needed
Steps
1) Create virtual environment
    a) pip install virtualenv 
    b) virtualenv env_name  
    c) source virtualenv_name/bin/activate

2) Installing required packages
    a) install all packages required , follow command in 'packages-needed' block.

3) Create a src folder
    a) create a src folder as starting point
    b) Create a .py file like main.py 

4) Need to specify path for chromedriver 
    a) export PATH = $PATH:/path/to/webdriver/:/path/to/your/python/folder
    b) export PYTHONPATH = $PYTHONPATH:/path/to/webdriver/:/path/to/your/python/folder

#### Code walk-through
Steps 
1) Packages block 
    a) In this block we specify required packages .

2) Main block 
    a) Main block contains the actual code
        -> Open the webdriver 
        -> Search for required webpage to make web scraping  ( in this application i used www.amazon/laptops )
        -> Parse the content using beautifulSoup 
        -> Store required data into datatypes
        -> Store data in csv file for easy reading 

##### Cheat sheet 
CMD : pip install selenium  - To install selenium , selenium is used to access webdriver
CMD : pip install beautifulSoup4 - To install beautifulSoup4 is user to parse html code
Cmd : pip install pandas - to install pandas is used to frame date
CMD : whereis chromedriver  -  To get path for chrome driver 

You can skip using virtual environment if needed 
Check for supported versions
Install chromewebdriver which supports your current browser

python main.py 

All Done .





