


# coding = utf-8



from handle.register_handle import RegisterHandle

class RegisterBusiness():
    def __init__(self,driver):
        self.register_h = RegisterHandle(driver)

    def user_base(self,email,name,password,code):
        self.register_h.send_user_email(email)
        self.register_h.send_user_name(name)
        self.register_h.send_user_password(password)
        self.register_h.send_user_code(code)
        self.register_h.click_register_button()
        
    # 检测是否有注册按钮 如果没有注册按钮 返回true 证明登录成功
    def register_success(self):
        if  self.register_h.get_register_text() == None:
            return True
        else:
            False


    #执行操作
    #邮箱错误
    def register_email_error(self,email,name,password,code):
        self.user_base(email,name,password,code)
        if self.register_h.get_user_text('user_email_error','请输入有效的电子邮件地址') == None:
            print('邮箱检验失败')
            return True
        else:
            return False

    #name错误
    def register_name_error(self,email,name,password,code):
        self.user_base(email,name,password,code)
        if self.register_h.get_user_text('user_name_error','字符长度必须大于等于4，一个中文字算2个字符') == None:
            print('输入了正确的用户名格式，用户名检验失败')
            return True
        else:
            return False

    #password错误
    def register_password_error(self,email,name,password,code):
        self.user_base(email,name,password,code)
        if self.register_h.get_user_text('password_error','最少需要输入 5 个字符') == None:
            print('密码检验失败')
            return True
        else:
            return False
    
    #验证码错误
    def register_code_error(self,email,name,password,code):
        self.user_base(email,name,password,code)
        if self.register_h.get_user_text('code_text_error','验证码错误') == None:
            print('密码检验失败')
            return True
        else:
            return False

    def register_function(self,email,username,password,code,assertCode,assertText):
        self.user_base(email,username,password,code)
        if self.register_h.get_user_text(assertCode,assertText) == None:
            print('密码检验失败')
            return True
        else:
            return False
    

        
