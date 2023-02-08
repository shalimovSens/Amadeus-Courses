'''
Файл с дополнительными функциями
'''
from typing import Optional
from django.core.exceptions import ValidationError

def handle_special_task(form) -> Optional[dict]:
    if form:
        form.username = 'Абдула'
        form.save
        context = {
            'form': form
            }
        return context
    return None

def check_username_chars(username:str, *, char_code:int=177) -> None:
    # в перспективе можно заменить регуляркой
    if username.isalnum():
        for char in set(username):
            if ord(char) > char_code:
                raise ValidationError('Используйте латинские буквы!')
    else:
        raise ValidationError('Используйте цифры от 0-9, "_" и "-".')
    
def check_password_correct(password:str, confirm_password:str) -> None:
    MIN_PASSWORD_LENGTH = 12
    PASSWORD_COMPLEXITY = 5
    error_message = ''
    if password != confirm_password:
        error_message = 'Пароли не совпадают!'
    
    if len(password) < MIN_PASSWORD_LENGTH:
        error_message = 'Слишком короткий пароль!'
    
    if len(set(password)) < PASSWORD_COMPLEXITY:
       error_message = 'Пароль слишком простой!'
    
    if password.isalpha() or password.isdigit():
        error = ['Цифры от 0-9', 'минимум одну сточную и одну заглавную букву']
        error_message = f'Пароль должен содеражать {error[password.isdigit()]}'
        
    if not is_password_contains_upper_lower_letters(password):
        error = ['строчную букву', 'заглавную букву']
        # error[test_arg.index(0)] очень не читаемо, переделать логику
        error_message = f'пароль должен соджержать {error[0]} и {error[1]}'  
        
    if error_message:
        raise ValidationError('Пароли не совпадают!')
    
def is_password_contains_upper_lower_letters(password:str) -> bool:
    test_arg = [0, 0]
    for char in set(password):
        if 'a' <= char.lower() <= 'z':
            if char.isupper():
                test_arg[1] = 1
            else:
                test_arg[0] = 1
    return sum(test_arg) == 2