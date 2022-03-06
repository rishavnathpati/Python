from selenium import webdriver

driver = webdriver.Chrome("/home/rishav/Downloads/Compressed/chromedriver")
driver.get("https://web.whatsapp.com/")
input("Enter anything after scanning QR code")

name = input("Enter the name of user or group : ")
user = driver.find_element_by_xpath("//span[@title = \"{}\"]".format(name))
print(user)

msg = input("Enter your message : ")

count = int(input("Enter the count : "))

user.click()

msg_box = driver.find_element_by_class_name('_2S1VP')

for i in range(count):
    driver.find_element_by_class_name('_2WovP').send_keys(msg)
    driver.find_element_by_class_name('_35EW6').click()
