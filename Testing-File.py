import os

print("Starting Code...")
os.system('git status')
os.system('git add .')
message = input('Enter Your Message: ')
os.system('git commit -m ' + message) 
os.system('git push')