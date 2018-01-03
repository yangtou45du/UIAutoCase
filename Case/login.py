from Common.Login import Login
from Util.write_fail_log import write_fail_log
from Util.write_pass_log import write_pass_log
import time
class login:
    def __init__(self):
        pass
    def assert_suc(self,dict,exception):
        self.driver = Login().login(dict)
        nowtime=str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
        try:
            texts = self.driver.find_element_by_link_text("设置").text
            self.driver.implicitly_wait(5)
            if exception in texts:
                write_pass_log(nowtime + " right username and passwd case pass!!!" + "\n")
            else:
                write_fail_log(nowtime + " right username and passwd case  fail!!! error is" + "\n")
        except Exception as e:
            print(nowtime+" right username and passwd case  fail!!! error is" +str(e) +"\n")
        time.sleep(3)
        self.driver.close()
    # def assert_fail(self,dict,exception):
    #     self.driver=Login().login(dict)
f=login()
dict={"username":"13730687504","passwd":123456}
f.assert_suc(dict,"设置")