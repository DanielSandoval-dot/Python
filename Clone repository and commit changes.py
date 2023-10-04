# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 21:29:39 2023

@author: Daniel Sandoval
"""
#Work with F9 to run each line of code at a time and have time to copy the file to the local folder

import git

remoteurl = "git@github.com:DanielSandoval-dot/Python.git"  # SSH URL
localfolder = r"C:\Users\danie\Files_to_commit"

# Clone the repository
myrepo = git.Repo.clone_from(remoteurl, localfolder)

# Copy the file that you want to commit now and run the next file

# file_to_upload = "String practice.py"  # Replace with new name
# file_to_upload = "Boolean statements.py"
# file_to_upload = "Clone repository and commit changes.py"
# file_to_upload = "Clone repository.py"
# file_to_upload = "DataFrame individual practice.py"
# file_to_upload = "DataFrame_pandas.py"
# file_to_upload = "Dictionary.py"
# file_to_upload = "Generators.py"
# file_to_upload = "if_while_for statements.py"
# file_to_upload = "List comprenhension.py"
# file_to_upload = "Mutability of strings and lists.py"
# file_to_upload = "Other exercises.py"
file_to_upload = "Turtle module.py"

myrepo.index.add([file_to_upload]) # Adding the file to the repository

myrepo.index.commit("Added file: " + file_to_upload) # Commit the changes

origin = myrepo.remote()# Push the changes to the remote repository
origin.push()
