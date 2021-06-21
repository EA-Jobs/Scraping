from selenium import webdriver

# must have the geckodriver downloaded
driver = webdriver.Firefox()

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

# TODO: find way to confirm download, and move download to folder
