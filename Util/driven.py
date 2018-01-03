from Util.read_excel import Excel
import sys,time
from Util.get_dc import get_dc
from Util.write_fail_log import write_fail_log
from Util.write_pass_log import write_pass_log

class Driven:
    #实现数据驱动
    def driven_it(self):
        ex=Excel()
        table=ex.read_it("C:\\Users\\Administrator\\PycharmProjects\\Undunion\\Test_Date\\Testdata.xlsx")
        i=1
        for rownum in range(1,table.nrows):
            print("\n##### start Test Case"+str(i)+"  ####")
            #获取行数据为列表形式
            list=table.row_values(rownum)
            print(list)
            #动态导入包
            __import__('Case.'+list[1])
            #  #导入模块
            module=sys.modules['Case.'+list[1]]
            # #根据list[0]获取类
            c=getattr(module,list[1])
            # #实例化对象
            obj=c()
            # #根据list[1]获取方法
            mtd=getattr(obj,list[2])
            try:
                dict=get_dc(list[3])
                mtd(dict,list[4])
            except Exception as e:
                write_fail_log(" error :"+str(e)+"\n")
            print("##### stop Test Case"+str(i)+"  ####\n")
            time.sleep(3)
            i+=1


            # if list[6]=="":
            #     try:
            #         mtd(list[2],rownum)
            #     except:
            #         write_fail_log(" error....."+str(rownum)+"\n")
            # else:
            #     try:
            #         dict=get_dc(list[3])
            #         mtd(dict,list[7],rownum)
            #     except:
            #         write_fail_log(" error....."+str(rownum)+"\n")
            #



dr=Driven()
dr.driven_it()
