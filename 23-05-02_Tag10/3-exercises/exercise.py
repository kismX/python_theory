print('----------EXERCISE-----------------')
import datetime 

def get_user_age(date_of_birth):
    
    dob_2 = datetime.datetime.strptime(date_of_birth, "%d-%m-%Y")
    date_now = datetime.datetime.now()
    age = (date_now - dob_2).days / 365.2425
    return int(age)


print(get_user_age())







