import random
pas=''
for x in range(11): #Количество символов (11)
    pas = pas + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ')) #Символы, из которых будет составлен пароль
print('Your password is: ', pas)