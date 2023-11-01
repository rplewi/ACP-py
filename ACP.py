import os

print("Starting Code...")
os.system('git status')
print('git status')
os.system('git add .')
print('git add .')
message = input('Enter Your Message, Please add quotes to your message:')
os.system('git commit -m ' + message) 
os.system('git push')
print('git push')