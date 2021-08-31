import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from pymongo import MongoClient

cliente=MongoClient('localhost')
db=cliente['AdquisiciónEntregable045']

col=db['FrutasYVerdurasWon']


opts = Options()
opts.add_argument(
    "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36")

driver=webdriver.Chrome('./chromedriver.exe',options=opts)
driver.get("https://www.wong.pe/")
sleep(random.uniform(11.0,12.0))

Publicidad=driver.find_element(By.XPATH, '//div[@class="slidedown-footer"]/button[@class="align-right secondary slidedown-button"]')
Publicidad.click()
sleep(2)
cookies=driver.find_element(By.XPATH,'//div[@class="swal2-actions"]/button[@class="swal2-confirm swal2-styled"]')
cookies.click()
sleep(2)



Pagina = driver.find_element(By.XPATH, '//div[@class="categsTop"]/div[position()=1]')##322
Pagina.click()


c=0
while c<30:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    sleep(4)
    c=c+1
sleep(random.uniform(10.0,11.0))
Productos = driver.find_elements(By.XPATH, '//li[contains(@layout,"19ccd66b-b568-43cb-a106-b52f9796f5cd")]')
for producto in Productos:
    try:
        Nombre = producto.find_element(By.XPATH, './div[contains(@class,"product-item product-item")]').get_attribute('data-name')
        Marca = producto.find_element(By.XPATH, './div[contains(@class,"product-item product-item")]').get_attribute('data-brand')
        Uri=producto.find_element(By.XPATH, './div[contains(@class,"product-item product-item")]').get_attribute('data-uri')
        Precio = producto.find_element(By.XPATH, './div[contains(@class,"product-item product-item")]//span[@class="product-prices__value product-prices__value--best-price"]').text
        _id=producto.find_element(By.XPATH, './div[contains(@class,"product-item product-item")]').get_attribute('data-sku')
        col.insert_one({
            "_id": _id
        },{
            "$set":{
                "_id":_id,
                "Nombre": Nombre,
                "Marca": Marca,
                "Uri":Uri,
                "2021-08-30" : Precio
            }
        }, upsert=True)
    except: Exception




col=db['CarnesAvesYPescadosWon']
Pagina = driver.find_element(By.XPATH, '//div[@class="categsTop"]/div[position()=2]') ####332
Pagina.click()
sleep(5)

c=0
while c<33:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    sleep(4)
    c=c+1
sleep(random.uniform(10.0,11.0))
Productos = driver.find_elements(By.XPATH, '//li[contains(@layout,"19ccd66b-b568-43cb-a106-b52f9796f5cd")]')
for producto in Productos:
    try:
        Nombre = producto.find_element(By.XPATH, './div[contains(@class,"product-item product-item")]').get_attribute('data-name')
        Marca = producto.find_element(By.XPATH, './div[contains(@class,"product-item product-item")]').get_attribute('data-brand')
        Uri = producto.find_element(By.XPATH, './div[contains(@class,"product-item product-item")]').get_attribute('data-uri')
        Precio = producto.find_element(By.XPATH, './div[contains(@class,"product-item product-item")]//span[@class="product-prices__value product-prices__value--best-price"]').text
        _id=producto.find_element(By.XPATH, './div[contains(@class,"product-item product-item")]').get_attribute('data-sku')
        col.insert_one({
            "_id": _id
        },{
            "$set":{
                "_id":_id,
                "Nombre": Nombre,
                "Marca": Marca,
                "Uri": Uri,
                "2021-08-30" : Precio
            }
        }, upsert=True)
    except: Exception


col=db['AbarrotesWon']

Pagina = driver.find_element(By.XPATH, '//div[@class="categsTop"]/div[position()=3]')#### 2291
Pagina.click()
sleep(5)

c=0
while c<70:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    sleep(4)
    c=c+1
sleep(random.uniform(10.0,11.0))
Productos = driver.find_elements(By.XPATH, '//li[contains(@layout,"19ccd66b-b568-43cb-a106-b52f9796f5cd")]')
for producto in Productos:
    try:
        Nombre = producto.find_element(By.XPATH, './div[contains(@class,"product-item product-item")]').get_attribute('data-name')
        Marca = producto.find_element(By.XPATH, './div[contains(@class,"product-item product-item")]').get_attribute('data-brand')
        Uri = producto.find_element(By.XPATH, './div[contains(@class,"product-item product-item")]').get_attribute('data-uri')
        Precio = producto.find_element(By.XPATH, './div[contains(@class,"product-item product-item")]//span[@class="product-prices__value product-prices__value--best-price"]').text
        _id=producto.find_element(By.XPATH, './div[contains(@class,"product-item product-item")]').get_attribute('data-sku')
        col.insert_one({
            "_id": _id
        },{
            "$set":{
                "_id":_id,
                "Nombre": Nombre,
                "Marca": Marca,
                "Uri": Uri,
                "2021-08-30" : Precio

            }
        }, upsert=True)
    except: Exception

col=db['VinosYLicoresWon']
Pagina = driver.find_element(By.XPATH, '//div[@class="categsTop"]/div[position()=4]')####1635
Pagina.click()
sleep(5)

c=0
while c<70:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    sleep(4)
    c=c+1
sleep(random.uniform(10.0,11.0))
Productos = driver.find_elements(By.XPATH, '//li[contains(@layout,"19ccd66b-b568-43cb-a106-b52f9796f5cd")]')
for producto in Productos:
    try:
        Nombre = producto.find_element(By.XPATH, './div[contains(@class,"product-item product-item")]').get_attribute('data-name')
        Marca = producto.find_element(By.XPATH, './div[contains(@class,"product-item product-item")]').get_attribute('data-brand')
        Uri = producto.find_element(By.XPATH, './div[contains(@class,"product-item product-item")]').get_attribute('data-uri')
        Precio = producto.find_element(By.XPATH, './div[contains(@class,"product-item product-item")]//span[@class="product-prices__value product-prices__value--best-price"]').text
        _id = producto.find_element(By.XPATH, './div[contains(@class,"product-item product-item")]').get_attribute(
            'data-sku')
        col.insert_one({
            "_id": _id
        },{
            "$set":{
                "_id":_id,
                "Nombre": Nombre,
                "Marca": Marca,
                "Uri":Uri,
                "2021-08-30": Precio

            }
        }, upsert=True)
    except: Exception

col=db['LimpiezaWon']
Pagina = driver.find_element(By.XPATH, '//div[@class="categsTop"]/div[position()=5]')####787
Pagina.click()
sleep(5)

c=0
while c<65:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    sleep(4)
    c=c+1
sleep(random.uniform(10.0,11.0))
Productos = driver.find_elements(By.XPATH, '//li[contains(@layout,"19ccd66b-b568-43cb-a106-b52f9796f5cd")]')
for producto in Productos:
    try:
        Nombre = producto.find_element(By.XPATH, './div[contains(@class,"product-item product-item")]').get_attribute('data-name')
        Marca = producto.find_element(By.XPATH, './div[contains(@class,"product-item product-item")]').get_attribute('data-brand')
        Uri = producto.find_element(By.XPATH, './div[contains(@class,"product-item product-item")]').get_attribute('data-uri')
        Precio = producto.find_element(By.XPATH, './div[contains(@class,"product-item product-item")]//span[@class="product-prices__value product-prices__value--best-price"]').text
        _id = producto.find_element(By.XPATH, './div[contains(@class,"product-item product-item")]').get_attribute(
            'data-sku')
        col.insert_one({
            "_id": _id
        },{
            "$set":{
                "_id":_id,
                "Nombre": Nombre,
                "Marca": Marca,
                "Uri":Uri,
                "2021-08-30" : Precio

            }
        }, upsert=True)
    except: Exception

col=db['TecnologiaWon']
Pagina = driver.find_element(By.XPATH, '//div[@class="categsTop"]/div[position()=6]')#### 595
Pagina.click()
sleep(5)

c=0
while c<55:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    sleep(4)
    c=c+1
sleep(random.uniform(10.0,11.0))
Productos = driver.find_elements(By.XPATH, '//li[contains(@layout,"19ccd66b-b568-43cb-a106-b52f9796f5cd")]')
for producto in Productos:
    try:
        Nombre = producto.find_element(By.XPATH, './div[contains(@class,"product-item product-item")]').get_attribute('data-name')
        Marca = producto.find_element(By.XPATH, './div[contains(@class,"product-item product-item")]').get_attribute('data-brand')
        Uri = producto.find_element(By.XPATH, './div[contains(@class,"product-item product-item")]').get_attribute('data-uri')
        Precio = producto.find_element(By.XPATH, './div[contains(@class,"product-item product-item")]//span[@class="product-prices__value product-prices__value--best-price"]').text
        _id = producto.find_element(By.XPATH, './div[contains(@class,"product-item product-item")]').get_attribute(
            'data-sku')
        col.insert_one({
            "_id": _id
        },{
            "$set":{
                "_id":_id,
                "Nombre": Nombre,
                "Marca": Marca,
                "Uri": Uri,
                "2021-08-30": Precio

            }
        }, upsert=True)
    except: Exception
col=db['ElectroHogarWon']
Pagina = driver.find_element(By.XPATH, '//div[@class="categsTop"]/div[position()=7]')#####949
Pagina.click()
sleep(5)

c=0
while c<70:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    sleep(4)
    c=c+1
sleep(random.uniform(10.0,11.0))
Productos = driver.find_elements(By.XPATH, '//li[contains(@layout,"19ccd66b-b568-43cb-a106-b52f9796f5cd")]')
for producto in Productos:
    try:
        Nombre = producto.find_element(By.XPATH, './div[contains(@class,"product-item product-item")]').get_attribute('data-name')
        Marca = producto.find_element(By.XPATH, './div[contains(@class,"product-item product-item")]').get_attribute('data-brand')
        Uri = producto.find_element(By.XPATH, './div[contains(@class,"product-item product-item")]').get_attribute('data-uri')
        Precio = producto.find_element(By.XPATH, './div[contains(@class,"product-item product-item")]//span[@class="product-prices__value product-prices__value--best-price"]').text
        _id = producto.find_element(By.XPATH, './div[contains(@class,"product-item product-item")]').get_attribute(
            'data-sku')
        col.insert_one({
            "_id": _id
        },{
            "$set":{
                "_id":_id,
                "Nombre": Nombre,
                "Marca": Marca,
                "Uri":Uri,
                "2021-08-30": Precio

            }
        }, upsert=True)
    except: Exception
col=db['HogarYBazarWon']
Pagina = driver.find_element(By.XPATH, '//div[@class="categsTop"]/div[position()=8]')##########2161
Pagina.click()
sleep(5)

c=0

while c<70:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    sleep(4)
    c=c+1
sleep(random.uniform(10.0,11.0))
Productos = driver.find_elements(By.XPATH, '//li[contains(@layout,"19ccd66b-b568-43cb-a106-b52f9796f5cd")]')
for producto in Productos:
    try:
        Nombre = producto.find_element(By.XPATH, './div[contains(@class,"product-item product-item")]').get_attribute('data-name')
        Marca = producto.find_element(By.XPATH, './div[contains(@class,"product-item product-item")]').get_attribute('data-brand')
        Uri = producto.find_element(By.XPATH, './div[contains(@class,"product-item product-item")]').get_attribute('data-uri')
        Precio = producto.find_element(By.XPATH, './div[contains(@class,"product-item product-item")]//span[@class="product-prices__value product-prices__value--best-price"]').text
        _id = producto.find_element(By.XPATH, './div[contains(@class,"product-item product-item")]').get_attribute(
            'data-sku')
        col.insert_one({
            "_id": _id
        },{
            "$set":{
                "_id":_id,
                "Nombre": Nombre,
                "Marca": Marca,
                "Uri":Uri,
                "2021-08-30": Precio


            }
        }, upsert=True)
    except: Exception

