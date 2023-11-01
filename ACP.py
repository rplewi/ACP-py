# Author: 
# Roman Lewis
#
# Project:
# Add-Commit-Push automation
import subprocess

def git_status():
    try:
        result = subprocess.run(['git', 'status'], capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

def git_add():
    try:
        add = subprocess.run(['git', 'add', '.'], capture_output=True, text=True, check=True)
        print(add.stdout)
    except subprocess.CalledProcessError as e:
        print(f"An error occured: {e}")

def git_message():
    message = input('Enter Your Message: ')
    print(message)
def git_comment():
    try:
        message = input('Enter Your Message: ')
        comment = subprocess.run(['git', 'commit', '-m' '"', + message, '"'], capture_output=True, text=True, check=True)
        print(comment.stdout)
    except subprocess.CalledProcessError as e:
        print(f"An error occured: {e}")

if __name__ == "__main__":
    git_status()
    git_add()
    git_comment()

import os

os.system('git status')
os.system('git add .')
os.system()

