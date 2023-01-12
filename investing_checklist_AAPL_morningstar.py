from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from pprint import pprint
options = Options()

# set headless = true so it does not load browser
options.headless = True

# driver = webdriver.Chrome(options=options, executable_path="PATH_TO_CHROMEDRIVER")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.morningstar.com/stocks/xnas/aapl/valuation")

# sleep to let the javascript to load
time.sleep(2)

# # print the page source
# print(driver.page_source)

# pe

# key statistics
ks = dict()
element = driver.find_elements(By.CLASS_NAME, 'dp-pair')
for e in element:
    elem = e.find_elements(By.TAG_NAME, 'div')
    ks[elem[0].text]=elem[1].text

#find and click the button for ROE 5 year average
button = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/div[3]/div/main/div/div/div[1]/section/sal-components/div/sal-components-stocks-valuation/div/div[2]/div/div/div[1]/div[1]/div/div/div/button[3]')
driver.execute_script('arguments[0].click();', button)
time.sleep(2)
data = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/div[3]/div/main/div/div/div[1]/section/sal-components/div/sal-components-stocks-valuation/div/div[2]/div/div/div[4]/div/div/div/div/div[1]/table/tbody/tr[7]/td[13]')
roe5Year = data.text

#find and click the button for 5Y Net income growth rate, 10Y Revenue Growth Rate, 10Y EPS Growth Rate
button1 = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/div[3]/div/main/div/div/div[1]/section/sal-components/div/sal-components-stocks-valuation/div/div[2]/div/div/div[1]/div[1]/div/div/div/button[2]')
driver.execute_script('arguments[0].click();', button1)
time.sleep(2)
fiveYearNetIncomeGrowthRate = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/div[3]/div/main/div/div/div[1]/section/sal-components/div/sal-components-stocks-valuation/div/div[2]/div/div/div[3]/div/div/div/div/div/div[1]/table/tbody/tr[14]/td[11]')
fiveYearNetIncomeGrowthRate = fiveYearNetIncomeGrowthRate.text
tenYearRevenueGrowthRate = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/div[3]/div/main/div/div/div[1]/section/sal-components/div/sal-components-stocks-valuation/div/div[2]/div/div/div[3]/div/div/div/div/div/div[1]/table/tbody/tr[5]/td[11]')
tenYearRevenueGrowthRate = tenYearRevenueGrowthRate.text
tenYearEPSGrowthRate = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/div[3]/div/main/div/div/div[1]/section/sal-components/div/sal-components-stocks-valuation/div/div[2]/div/div/div[3]/div/div/div/div/div/div[1]/table/tbody/tr[20]/td[11]')
tenYearEPSGrowthRate = tenYearEPSGrowthRate.text

#scrape marketcap
button2 = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/div[3]/div/div[3]/nav/ul/li[1]/a/span')
driver.execute_script('arguments[0].click()', button2)
time.sleep(2)
marketCap = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[2]/div[3]/div/main/div/div/div[1]/section[1]/div/div[2]/div[2]/ul/li[7]/span[2]/span')

#PRINT RESULTS
print('============================================================')
print('Market Capilization (Recommened: > 500M):    ' + marketCap.text)
print('P/E Ratio (Recommended: < 15):   ' + ks['Price/Earnings'])
print('P/B Ratio (Recommended: < 1.5):  ' + ks['Price/Book'])
print('Current Ratio (Reccomended: > 1.5):  ' + ks['Current Ratio*'])
print('Debt/Equity (Reccomended: < 0.5):    ' + ks['Debt/Equity*'])
print('5 Year ROE (Reccommended: > 8%):    ' + roe5Year)
print('5 Year Net Income Growth Rate (Recommended: > 5%):   ' + fiveYearNetIncomeGrowthRate)
print('10 Year Revenue Growth Rate (Recommended: > 5%):    ' + tenYearRevenueGrowthRate)
print('10 Tear EPS Growth Rate (Recommended: > 5%):    ' + tenYearEPSGrowthRate)
print('Interest Coverage (Recommended: > 6.0, 8.0):    ' + ks['Interest Coverage'])
print('============================================================')
# for e in roeYear0:
#     print(e.text)

# # # pprint(roeYear0)

# # for r in roeYear0:
# #     r.find_element
driver.quit()