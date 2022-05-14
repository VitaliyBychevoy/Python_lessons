from controller import create_user_name as cun
from controller import age_user as au
from controller import create_user as cu
from controller import show_user as su

name_1 = cun('rita')
age_1 =au(29)
user_1 = cu(name_1, age_1)
su(user_1)