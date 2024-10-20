from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import string
import pyperclip

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

    # Login kembali dengan email dan password baru
    email_input = driver.find_element(By.ID, "username")
    email_input.send_keys("geivux1+fatiscent@outlook.com")
    email_input.send_keys(Keys.ENTER)
    time.sleep(3)

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("AyLevy123@")
    password_input.send_keys(Keys.ENTER)
    time.sleep(5)
    
    # Kembali ke halaman tim Netlify
    driver.get(f"https://app.netlify.com/teams/{modified_email}/sites")
    time.sleep(5)

    # Klik "Import from Git"
    import_git_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Import from Git')]")
    import_git_button.click()
    time.sleep(3)

    # Klik tombol Bitbucket untuk mengimpor proyek
    bitbucket_button = driver.find_element(By.XPATH, "//button[contains(@class, 'btn-tertiary') and contains(@class, 'tw-px-4')]")
    bitbucket_button.click()
    time.sleep(5)

    # Masukkan site name dengan format random
    site_name_input = driver.find_element(By.NAME, "siteName")  # Menggunakan atribut name yang lebih generik
    site_name = generate_random_site_name()
    site_name_input.send_keys(site_name)
    site_name_input.send_keys(Keys.ENTER)
    time.sleep(7)

    # Lanjutkan ke langkah deploy dan copy title
    driver.find_element(By.CSS_SELECTOR, "#deploys-secondary-nav-item .tw-transition").click()
    time.sleep(5)

    driver.find_element(By.CSS_SELECTOR, ".btn-secondary:nth-child(1) > .tw-flex").click()
    time.sleep(5)

    driver.find_element(By.CSS_SELECTOR, ".card:nth-child(8) .btn").click()
    time.sleep(5)

    # Masukkan title dan copy
    title_input = driver.find_element(By.NAME, "title")
    title_input.send_keys("asc")
    title_input.send_keys(Keys.ENTER)
    time.sleep(5)

    # Klik tombol copy dan ambil teks yang disalin
    driver.find_element(By.CSS_SELECTOR, ".tw-relative:nth-child(1) > .btn .scalable-icon").click()
    time.sleep(1)

    copied_text = pyperclip.paste()
    print(f"Copied text: {copied_text}")

# Membaca file bb.txt
with open('bb.txt', 'r') as file:
    emails = file.readlines()

# Loop melalui setiap email
for email in emails:
    email = email.strip()  # Menghapus spasi atau newline di awal/akhir email
    signup_process(email)

# Tutup browser setelah selesai
driver.quit()
