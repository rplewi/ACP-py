
import os
yes = {'yes', 'y'}
no = {'no', 'n'}
force = {'f'}


def push():
    while True:
        if confirmMessage in yes:
            print()
            print('git push')
            os.system('git push')
            break
        elif confirmMessage in no:
            print()
            print('You have cancelled this push')
            break
        else:
            print()
            print('Please enter a valid answer, and try again')


print("Starting Code...")
print('git status')
os.system('git status')
print('git add .')
os.system('git add .')

while True:
    message = input('Enter Your Message or f to bypass confirmation: ')
    if not message:
        print('Please enter a valid message')
        continue
    elif message:
        os.system('git commit -m "' + message + '"')
        confirmMessage = input(
            'Please Confirm that you want to push this branch (y or n): ')
        push()
        break
