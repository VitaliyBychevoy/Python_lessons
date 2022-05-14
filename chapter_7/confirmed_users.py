#Начинаем с двух списков: пользователей для проверки
# и пустого списка для хранения проверенных пользователей.
unconfirmed_users = ['alice', 'brian', 'candace']
confirm_user = []

#Проверяем каждого пользователя, пока остаются непроверенные
# пользователи. Каждый пользователь, прошедший проверку,
# перемещается в список проверенных.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirm_user.append(current_user)

#Вывод всех проверенных пользователей.
print("\nThe following users have been confirmed:")
for confirm_user in confirm_user:
    print(confirm_user.title())