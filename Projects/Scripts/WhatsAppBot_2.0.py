from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import datetime
import time
import openpyxl as excel

driver = webdriver.Chrome("/home/rishav/Downloads/Compressed/chromedriver")
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 10)
wait5 = WebDriverWait(driver, 5)


def read_contacts(fileName):
    lst = []
    file = excel.load_workbook(fileName)
    sheet = file.active
    first_col = sheet['A']
    for cell in range(len(first_col)):
        contact = str(first_col[cell].value)
        contact = "\"" + contact + "\""
        lst.append(contact)
    return lst


targets = read_contacts("contacts.xlsx")

print(targets)
