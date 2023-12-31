
import os
yes = {'yes','y'}
no = {'no', 'n'}
force = {'f'}

def push():
    while True:
        confirmMessage = input(
            'Please Confirm that you want to push this branch (y or n): ')
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
    elif message == "f":
        os.system("git commit -m \"forced\"")
        os.system("git push")
        print("You have bypassed a commit message. Have a good day!")
        break
    elif message:
        os.system('git commit -m "' + message + '"')
        push()
        break