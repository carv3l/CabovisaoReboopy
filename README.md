# CabovisaoReboopy


Python Script to automate the task of rebooting Cabovisão Router Sagemcom F@st 3184 and  F@st 3284, as Nowo is kinda crappy

Currently only for linux





## Raspbian
Notes:
Steps to make it work on raspbian

Install chromium webdriver

```bash
sudo apt-get install chromium-chromedriver
```

In scripty.py change in line 59

```python
driver = webdriver.Firefox(executable_path="./drivers/geckodriver")
```
To

```python
driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
```
## TODO List

Finish Bash:

Logs Creation

Scanning OS

Scanning Browsers from that OS

Download Webdriver accordingly

