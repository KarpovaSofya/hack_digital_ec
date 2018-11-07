from db_users import*

db = 'users'

print('Я - деканат-бот - приветствую вас!')
inp = input('вход или регистрация? ')
if inp == 'регистрация':
	u_id = input('введите ваш id: ') #потом не вводим
	name = input('введите ваше имя: ')
	adm = input('вы сотрудник деканата? (да\нет): ')
	if adm == 'да':
		adm_acc = 1
		group = 'None'
	else:
		adm_acc = 0
		group = input('введите вашу группу: ')
	add_new_user(db, u_id, name, group, adm_acc)#доделать если такой пользователь есть
else:
	u_id = input('введите ваш id: ') #потом не вводим
	name = input('введите ваше имя: ')
	if user_in_base(db,u_id):
		print('Вход выполнен');
	else:
		print('Такого пользователя нет! Попробуйте найти ошибку или пройдите регистрацию!')
		inp = input('вход или регистрация? ')
#сделать цикл пока регистрация или вход не выполнен