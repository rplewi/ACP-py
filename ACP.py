import os
yes = {'yes','y'}
no = {'no', 'n'}

print("Starting Code...")
print('git status')
os.system('git status')
print('git add .')
os.system('git add .')
try:
    message = input('Enter Your Message: ')
    os.system('git commit -m ' + message) 
    if not message:
        raise ValueError()
    confirmMessage = input('Please Confirm that you want to push this branch (y or n): ' )
    if confirmMessage in yes:
        print()
        print('git push')
        os.system('git push')
    elif confirmMessage in no:
        print()
        print('You have cancelled this push')
    else:
        print()
        print('Please select and actual answer, and restart')
except:
    print()
    print('error, please make sure you add a comment, and try again.')
