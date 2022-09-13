


# coding = utf-8

import sys
sys.path.append('F:/selenium_python/Imooc_selenium')
from util.excel_util import ExcelUtil
from keywordselenium.actionMethod import ActinoMethod

class KeywordCase:
    def run_main(self):  
        self.action_method = ActinoMethod()      
        handle_excel = ExcelUtil('F:/selenium_python/Imooc_selenium/config/key_word.xls')
        case_lines = handle_excel.get_lines()           # 拿到行数
        if case_lines:
            for i in range(1,case_lines):               # 循环行数，去执行每一行的case
                is_run = handle_excel.get_col_value(i,3)
                if is_run == 'yes':                     # 判断是否执行
                    method = handle_excel.get_col_value(i,4)              #拿到执行方法（第i行，第5列的元素）
                    send_value = handle_excel.get_col_value(i,5)          #拿到输入数据
                    handle_value = handle_excel.get_col_value(i,6)        #拿到操作值
                    except_result_method = handle_excel.get_col_value(i,7)  #拿到预期结果方法 
                    except_result = handle_excel.get_col_value(i,8)         #拿到预期结果值
                    self.run_method(method,handle_value,send_value)
                    if except_result != '':
                        except_value = self.get_except_result_value(except_result)
                        print('______》',except_result_method)
                        print('______>>',except_value)
                        if except_value[0] == 'text':
                            result = self.run_method(except_result_method)  
                            if except_value[1] in result:
                                handle_excel.write_value(i,'pass')
                            else:
                                handle_excel.write_value(i,'failed')
                        elif except_value[0] == 'element':
                            result = self.run_method(except_result_method,except_value[1])
                            if result:
                                handle_excel.write_value(i,'failed')
                            else:
                                handle_excel.write_value(i,'pass')
                    else:
                        print('期望结果为空 ')      

    #获取预期结果值
    def get_except_result_value(self,data):
        return data.split("=")

    # 再操作值中 输入数据                    
    def run_method(self,method,handle_value='',send_value=''):        
        method_value = getattr(self.action_method,method)      # getattr(object, name[, default])函数用于返回一个对象属性值。
        # if send_value:
        #     method_value(handle_value,send_value)
        # elif send_value == '' and handle_value == '':
        #     method_value()
        # else:
        #     method_value(handle_value)

        if send_value == '' and handle_value != '':
            result = method_value(handle_value)
        elif send_value != '' and handle_value != '':
            result = method_value(handle_value,send_value)
        elif send_value != '' and handle_value =='':
            result = method_value(send_value)
        else:
            result = method_value()
        return result

    
            #判断是否有输入数据
                # 执行方法（输入数据，操作元素）
            #没有输入数据
                # 执行方法（操作元素）
keywordcase = KeywordCase()
keywordcase.run_main()