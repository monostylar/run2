import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyperclip
import random

# Fungsi untuk membuka ChromeDriver yang sudah ada di sistem
def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    return driver

# Fungsi untuk membaca email dari file bb.txt
def get_emails():
    with open("bb.txt", "r") as file:
        emails = file.readlines()
    return [email.strip() for email in emails]

# Fungsi untuk menghasilkan 5 digit huruf random dan 5 digit angka random
def random_site_name():
    letters = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
    numbers = ''.join(random.choices('0123456789', k=5))
    letters2 = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
    return f"{letters}-{numbers}-{letters2}"

# Main function to handle the automation
def signup_process(email):
    driver = get_driver()
    
    # Buka halaman Netlify Sign Up
    driver.get("https://app.netlify.com/signup")
    time.sleep(5)

    # Klik tombol "Sign up with Bitbucket"
    bitbucket_button = driver.find_element(By.XPATH, "//button[@name='bitbucket']")
    bitbucket_button.click()
    time.sleep(15)

    # Masukkan email dari file bb.txt
    email_input = driver.find_element(By.ID, "username")
    email_input.send_keys(email)
    email_input.send_keys(Keys.ENTER)
    time.sleep(5)

    # Masukkan password
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("giatuye123")
    password_input.send_keys(Keys.ENTER)
    time.sleep(5)

    # Klik "Continue without two-step verification"
    skip_2step_button = driver.find_element(By.XPATH, "//span[text()='Continue without two-step verification']")
    skip_2step_button.click()
    time.sleep(7)

    # Klik "Grant access"
    grant_access_button = driver.find_element(By.XPATH, "//button[@type='submit' and @name='action' and @value='approve']")
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

    # Kembali ke tab utama
    driver.switch_to.window(driver.window_handles[0])

    # Masukkan site name dengan format random
    site_name_input = driver.find_element(By.ID, "nf_field_2e2b40b1-cda7-4efa-b9ec-181254eb6009")
    site_name = random_site_name()
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

    # Tutup browser
    driver.quit()

# Baca daftar email dari file bb.txt dan ulangi proses untuk setiap email
emails = get_emails()
for email in emails:
    signup_process(email)
    time.sleep(5)
