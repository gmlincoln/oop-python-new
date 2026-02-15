class User:
    def login(self):
        print("User Logged In")


class Admin(User):
    def delete_user(self):
        print("User Deleted")


admin = Admin()
admin.login()
admin.delete_user()

