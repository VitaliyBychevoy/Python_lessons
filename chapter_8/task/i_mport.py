import controller

name_user_1 = controller.create_user_name('vasia')
age_1 = int(controller.age_user(32))
user_1 = controller.create_user(name_user_1, age_1)
controller.show_user(user_1)
print("\n")
name_user_2 = controller.create_user_name('tolik')
age_2 = int(controller.age_user(24))
user_2 = controller.create_user(name_user_2, age_2)
controller.show_user(user_2)
print("\n")
name_user_3 = controller.create_user_name('maria')
age_3 = int(controller.age_user(28))
user_3 = controller.create_user(name_user_3, age_3)
controller.show_user(user_3)
print("\n")
name_user_4 = controller.create_user_name('anton')
age_4 = int(controller.age_user(30))
user_4 = controller.create_user(name_user_4, age_4)
controller.show_user(user_4)


