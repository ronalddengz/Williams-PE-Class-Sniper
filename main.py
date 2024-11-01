url = 'https://sarah.williams.edu/psp/cs92prd/EMPLOYEE/SA/c/WMS_SS_STU_MENU.WMS_SS_PE_REG.GBL?FolderPath=PORTAL_ROOT_OBJECT.CO_EMPLOYEE_SELF_SERVICE.HCCC_ENROLLMENT.WMS_SS_PE_REG&IsFolder=false&IgnoreParamTempl=FolderPath,IsFolder'

username = input("Username (without williams.edu): ") 
email = username + "@williams.edu"
password = input("Password: ")

okta = input("Verification via code or push notification? (1/2) ")
class_id = f"WMS_M166_WK_SELECT${int(input('Class number (see classes.txt for class numbers): ')) - 1}"

browser = webdriver.Firefox()
browser.get(url)
sleep(1)
browser.find_element(By.ID, "identifierId").send_keys(email)

WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "identifierNext")))
browser.find_element(By.ID, "identifierNext").click()

WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "input28")))
browser.find_element(By.ID, "input28").send_keys(username)

WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button")))
browser.find_element(By.CSS_SELECTOR, ".button").click()

WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "input60")))
browser.find_element(By.ID, "input60").send_keys(password)

WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button")))
browser.find_element(By.CSS_SELECTOR, ".button").click()

if(okta == 1):
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.authenticator-row:nth-child(1) > div:nth-child(2) > div:nth-child(2) > a:nth-child(1)")))
    browser.find_element(By.CSS_SELECTOR, "div.authenticator-row:nth-child(1) > div:nth-child(2) > div:nth-child(2) > a:nth-child(1)").click()

else:
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.authenticator-row:nth-child(2) > div:nth-child(2) > div:nth-child(2) > a:nth-child(1)")))
    browser.find_element(By.CSS_SELECTOR, "div.authenticator-row:nth-child(2) > div:nth-child(2) > div:nth-child(2) > a:nth-child(1)").click()   

WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.ID, "userid")))
browser.find_element(By.ID, "userid").send_keys(username)
browser.find_element(By.ID, "pwd").send_keys(password)
browser.find_element(By.CSS_SELECTOR, ".ps-button").click()

print("Now we wait... Don't close out of this program or that window!")

while True:
    try:
        WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.ID, class_id)))
        browser.find_element(By.ID, class_id).click()
        break
    
    except:
        sleep(1)
        browser.refresh()
