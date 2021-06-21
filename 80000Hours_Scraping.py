from selenium import webdriver

# sets up a new firefox profile
fp = webdriver.FirefoxProfile()

# sets the preferences in the profile such that it doesn't confirm download for csv files
fp.set_preference("browser.helperApps.neverAsk.saveToDisk","text/csv")

# use this to set the download folder:
# downloadPath = "home/fakefolder/fakefolder"
# fp.set_preference("browser.download.folderList",2)
# fp.set_preference("browser.download.dir", downloadPath)

# creates a new webdriver using the firefox profile
# must have geckodriver installed
driver = webdriver.Firefox(firefox_profile = fp)

# opens the 80000 hours airtable
driver.get('https://airtable.com/shrD9UEKusc6BYWWc/tbl5zkv6T7WSivZ89')

# finds the three dots, which when clicked allows for the file to be downloaded
dots = driver.find_element_by_xpath("//div[@class='pointer darken1-hover rounded flex items-center animate focus-visible viewMenuButton mx1']")

# clicks on the three dots
dots.click()

# finds the download button
download = driver.find_element_by_xpath("//li[@class='py1 px1-and-half text-size-default items-center pointer width-full flex']")

# clicks on the download button
download.click()

# TODO: make generalizable to all airtables
