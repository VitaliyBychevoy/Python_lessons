from controller import create_user_name
from controller import age_user
from controller import create_user
from controller import show_user

name_1 = create_user_name('pasha')
age_1 = age_user(32)
user_1 = create_user(name_1, age_1)
show_user(user_1)
