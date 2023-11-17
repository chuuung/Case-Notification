
# Case Notification for Facebook Tsing-Chiao Group
Utilized web crawler(selenium and beautifulsoup) to scrape information on Facebook.   
If get matched post, it will notify user by Line Notify API.  

## Open Browser
use chromedriver to open chrome broswer and redirect to facebook

```python
options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values':
        {
            'notifications': 2
        }
}
options.add_experimental_option('prefs', prefs)
options.add_argument("disable-infobars")

driver = webdriver.Chrome(options = options)
driver.maximize_window()
url = 'https://www.facebook.com'
driver.get(url)
```
## Login Facebook
login automation

```python
username = # your account
password = # your passwordd

elem = driver.find_element_by_id("email")
elem.send_keys(username)
elem = driver.find_element_by_id("pass")
elem.send_keys(password)        

elem.send_keys(Keys.RETURN)
time.sleep(5)

url = # the url of page
driver.get(url)
time.sleep(5)
```

## Line Notify API
```python
headers = {
"Authorization": "Bearer " + "3FmmROfkHGiz4kUdSVNWF3uyuj35gZaHriNnLntlXzv",
"Content-Type": "application/x-www-form-urlencoded"
}
params = {"message": "有 【"+ j + "】 案件了 快打開FB!!!!!! "}

r = requests.post("https://notify-api.line.me/api/notify",
            headers=headers, params=params)
#                     print(r.status_code)  #200

if r.status_code == 200:
    print("Found !! ", j)
    flag = 1
```