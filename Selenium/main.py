from selenium import webdriver

chrome_driver_path = "Users\Dhanesh\Desktop\PycharmProjects\Development\chromedriver"

driver = webdriver.Chrome()

driver.get("https://www.python.org/")

search_bar = driver.find_elements("q")
print(search_bar.driver)

driver.quit()