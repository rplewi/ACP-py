import os

print("Starting Code...")
print('git status')
os.system('git status')
print('git add .')
os.system('git add .')
message = input('Enter Your Message, Please add quotes to your message:')
os.system('git commit -m ' + message) 
print('git push')
os.system('git push')