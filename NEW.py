import os
yes = {'yes','y'}
no = {'no', 'n'}

print("Starting Code...")
print('git status')
os.system('git status')
print('git add .')
os.system('git add .')
while True:
    message = input('Enter Your Message: ')
    if not message:
        print('Please enter a valid message')
        continue

    os.system('git commit -m ' + message) 

    confirmMessage = input('Please Confirm that you want to push this branch (y or n): ' )
    if confirmMessage in yes:
        print()
        print('git push')
        os.system('git push')
        break #Ends code here
    elif confirmMessage in no:
        print()
        print('You have cancelled this push')
        break #Ends code here
    else:
        print()
        print('Please enter a valid answer, and try again')