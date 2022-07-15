"""Python program to have interaction with webpages"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

selenium_path = "C:\\Users\\Enrique M\\OneDrive\\Documentos\\Marco\\Web Development\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=selenium_path)
web = "https://en.wikipedia.org/wiki/Main_Page"
# driver.get(url=web)


# Get the number of articles available in Wikipedia
# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# print(article_count.text)

# ######### Click on links ############
# all_portals = driver.find_element(By.LINK_TEXT, "Talk")
# all_portals.click()

# ------------------ Type on search boxes ---------

# search = driver.find_element(By.NAME, "search")
# search.send_keys("python")
# search.send_keys(Keys.ENTER)


# ----------------- Fill a form ----------
url = "http://secure-retreat-92358.herokuapp.com/"
driver.get(url=url)
f_name = driver.find_element(By.NAME, "fName")
l_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")

f_name.send_keys("Marco")
l_name.send_keys("Ponce")
email.send_keys("maarco.app98@gmail.com")

button = driver.find_element(By.CSS_SELECTOR, ".btn")
button.click()





#driver.quit()
