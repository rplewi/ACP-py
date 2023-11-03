import os
yes = {'yes','y'}
no = {'no', 'n'}

print("Starting Code...")
print('git status')
os.system('git status')
print('git add .')
os.system('git add .')
message = input('Enter Your Message, Please add quotes to your message: ')
os.system('git commit -m ' + message) 
confirmMessage = input('Please Confirm that you want to push this branch (y or n): ' )
choice = raw_input().lower()
if choice in yes:
    print('git push')
    os.system('git push')
elif choice in no:
    print('You have cancelled this push')
else:
    print('Please select and actual answer')