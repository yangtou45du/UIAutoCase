from selenium import webdriver


class setup:
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http://stg-firm.ichengke.cn")
        self.driver.maximize_window()
        # self.driver.implicitly_wait(30)

# f=setup()

