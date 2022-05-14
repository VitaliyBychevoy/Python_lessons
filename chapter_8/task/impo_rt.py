import controller as con

name_1 = con.create_user_name('konstantin')
age_1 = con.age_user(23)
user_1 = con.create_user(name_1, age_1)
con.show_user(user_1)