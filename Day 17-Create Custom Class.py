# Class is a Blueprint
# 通常class的名稱都要使用大寫(PascalCase)。
# 例如: 'C'ar'C'am'P'ulley
class User:
    def __init__(self, user_id, username):
        # Constructor 建構屬於自己的class。
        # initialize 初始化class內的內容。
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        
    def follow(self, user):
        user.followers += 1
        self.following += 1


# 當使用User class時，要記得設定user_1.id的值、username的parameter。
user_1 = User("001", "Dawei")
user_2 = User("002", "jack")

# 印出user_1 的followers and following number.
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)

# 印出user_2 的followers and following number.
print(user_2.followers)
print(user_2.following)



# 1. 建立 attribute
# user_1.username = "Dawei"
# user_1.id = "001"

# 2. 印出 attribute
# print(user_1.id)       # 則印出 001。
# print(user_1.username) # 印出 Dawei





