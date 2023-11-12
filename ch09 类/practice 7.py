# Yu Junming
# 12/11/2023
# chapter 9 类  practice 7
# 《Python编程从入门到实践》


class User:
    """模拟一个用户类。"""

    def __init__(self, first_name, last_name, age):
        """初始化描述用户的属性。"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        """描述用户的信息。"""
        print(f"\n{self.first_name} {self.last_name} is {self.age} years old.")

    def greeting_user(self):
        """问候用户。"""
        print(f"Hi, {self.first_name.title()} {self.last_name.title()}!")

    def increment_login_attempts(self):
        """将登录次数增加一次。"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """将登录次数重置为0。"""
        self.login_attempts = 0


class Admin(User):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print("The admins' privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


admin_rr = Admin('Junming', 'Yu', 23)
admin_rr.show_privileges()
