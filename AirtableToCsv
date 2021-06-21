from selenium import webdriver
import time

# finds the dots button
def findDots(driver):
    # Occasionally simply entering the code in the try section will return an error
    # this is because the page ins't loaded yet
    # so when this happens, this function recursively calls itself again until it works
    try:
        dots = driver.find_element_by_xpath("//div[@class='pointer darken1-hover rounded flex items-center animate focus-visible viewMenuButton mx1']")
    except:
        time.sleep(3)
        dots = findDots()
    return dots

# finds the download button
def findDownload(driver):
    # Occasionally simply entering the code in the try section will return an error
    # this is because the page ins't loaded yet
    # so when this happens, this function recursively calls itself again until it works
    try:
        download = driver.find_element_by_xpath("//li[@class='py1 px1-and-half text-size-default items-center pointer width-full flex']")
    except:
        time.sleep(3)
        download = findDownload()
    return download

# downloads airtable as csv, and saves to downloadPath
def downloadAirtableCsv(link, downloadPath):
    # creates a new firefox profile
    fp = webdriver.FirefoxProfile()

    # sets the preference of the profile to not ask user to confirm the download of csv files
    fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv")

    # sets the preference of the profile to download files to custom path, then tells it
    # the custom path is downloadPath
    fp.set_preference("browser.download.folderList",2)
    fp.set_preference("browser.download.dir", downloadPath)

    # instantiates the firefox driver with the profile set up above
    # be sure geckodriver is installed
    driver = webdriver.Firefox(firefox_profile = fp)

    # loads the airtable link in the driver
    driver.get(link)
    
    # finds the three dots, which when clicked allows for the file to be downloaded
    #dots = findDots()
    dots = findDots(driver)
    
    # clicks on the three dots
    dots.click()
    
    # finds the download button
    download = findDownload(driver)
    
    # clicks on the download button
    download.click()

# testing on New York EA's job board
# downloadAirtableCsv("https://airtable.com/shrFYOsnjlMnTTvAa/tblbKsEIEUb1q9zQ0", "/home/d0themath/scraper")

# TODO: figure out how to determine when the file is downloaded, then close window afterwards.
