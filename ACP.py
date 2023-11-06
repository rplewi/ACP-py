
import os
yes = {'yes', 'y'}
no = {'no', 'n'}
force = {'f'}

print("Starting Code...")
print('git status')
os.system('git status')
print('git add .')
os.system('git add .')
while True:
    message = input('Enter Your Message or f to bypass confirmation: ')
    os.system('git commit -m "' + message + '"') 
    if not message:
        print('Please enter a valid message')
        continue
    elif message in force:
        push()

    confirmMessage = input('Please Confirm that you want to push this branch (y or n): ' )

def push():
    if confirmMessage in yes:
        print()
        print('git push')
        os.system('git push')
    elif confirmMessage in no:
        print()
        print('You have cancelled this push')
    else:
        print()
        print('Please enter a valid answer, and try again')