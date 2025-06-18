
import random 

com_num=random.randint(1,100)

print("*--------------------------------------*")
print("|                                      |")
print("| Welcome to the Number guessing game! |")
print("|  **********************************  |")
print("*--------------------------------------*")
print('')
print('Coumputer has guessed number between 1 and 100, Can you guess the Number ?')
print('')
print('You get 10 tries , All The Best! :)')
print('')

i=10
while i>0:
    user_num=int(input('Enter your guess between 1 and 100:'))
    if user_num>100:
        print('')
        print(f'The number {user_num} is greater than 100, Please enter a number between 1 and 100')
    elif user_num>com_num:
        print('')
        print(f'Your guessed number {user_num} is greater than the actual number')
        i-=1
        print(f'Remaning tires :{i}')
        
    elif user_num<com_num:
        print('')
        print(f'Your gussed number {user_num} is lesser than the actual number')
        i-=1    
        print(f'Remaning tires :{i}')
        
    elif user_num==com_num:
        print('')
        if i== 10:
            print(f'Congrats the number is {user_num} and you got it Right in "{11-i}" try!!')
        else:
            print(f'Congrats the number is {user_num} and you got it Right in "{11-i}" tries!!')
        break
print('*------------*')    
print('|GAME OVER !!|')
print('*------------*')    
