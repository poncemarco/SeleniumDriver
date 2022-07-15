from selenium import webdriver
from selenium.webdriver.common.by import By


selenium_path = "C:\\Users\\Enrique M\\OneDrive\\Documentos\\Marco\\Web Development\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=selenium_path)
web = "https://www.python.org/"

driver.get(url=web)

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")


# Create an event dictionary
events = {}
for n in range(len(event_times)):
    events[n]= {
        "time": event_times[n].text,
        "name": event_names[n].text
    }

print(events)
driver.quit()
