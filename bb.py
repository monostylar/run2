from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
import string

# Konfigurasi driver
driver = webdriver.Chrome()  # Menggunakan ChromeDriver yang ada di sistem

# Fungsi untuk menghasilkan nama acak
def generate_random_site_name(length=8):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

# Fungsi untuk signup dan login Bitbucket
def signup_process(email):
    # Buka halaman signup Netlify
    driver.get("https://app.netlify.com/signup")
    time.sleep(5)

    # Klik tombol "Sign up with Bitbucket"
    bitbucket_button = driver.find_element(By.XPATH, "//button[@name='bitbucket']")
    bitbucket_button.click()
    time.sleep(15)

    # Input email yang diambil dari file
    email_input = driver.find_element(By.ID, "username")
    email_input.send_keys(email)
    email_input.send_keys(Keys.ENTER)
    time.sleep(5)

    # Isi password
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("giatuye123")
    password_input.send_keys(Keys.ENTER)
    time.sleep(5)

    # Klik tombol "Continue without two-step verification"
    continue_without_2fa = driver.find_element(By.XPATH, "//span[text()='Continue without two-step verification']")
    continue_without_2fa.click()
    time.sleep(7)

    # Klik tombol "Grant access"
    grant_access_button = driver.find_element(By.XPATH, "//button[@name='action' and @value='approve']")
    grant_access_button.click()
    time.sleep(5)

    # Input nama situs menggunakan elemen berdasarkan atribut `name="siteName"`
    driver.find_element(By.NAME, "siteName").click()
    site_name = generate_random_site_name()  # Menghasilkan nama situs acak
    driver.find_element(By.NAME, "siteName").send_keys(site_name)  # Memasukkan nama situs acak yang dihasilkan
    driver.find_element(By.NAME, "siteName").send_keys(Keys.ENTER)
    time.sleep(5)

    # Buka link Netlify team sites
    modified_email = email.split('+')[1].split('@')[0]
    driver.get(f"https://app.netlify.com/teams/{modified_email}/sites")
    time.sleep(5)

    # Membuka halaman logout Atlassian/Bitbucket
    driver.get("https://id.atlassian.com/logout?continue=https%3A%2F%2Fbitbucket.org%2Faccount%2Fsignout%2F&prompt=none")
    time.sleep(5)

    # Klik tombol Log out di halaman Atlassian
    logout_button = driver.find_element(By.XPATH, "//span[text()='Log out']")
    logout_button.click()
    time.sleep(5)

    # Lanjutkan dengan proses login ke Bitbucket
    username_input = driver.find_element(By.ID, "username")
    username_input.send_keys("geivux1+fatiscent@outlook.com")
    username_input.send_keys(Keys.ENTER)
    time.sleep(3)

    # Isi password untuk Bitbucket
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("AyLevy123@")
    password_input.send_keys(Keys.ENTER)
    time.sleep(5)

# Membaca file bb.txt
with open('bb.txt', 'r') as file:
    emails = file.readlines()

# Loop melalui setiap email
for email in emails:
    email = email.strip()  # Menghapus spasi atau newline di awal/akhir email
    signup_process(email)

# Tutup browser setelah selesai
driver.quit()
