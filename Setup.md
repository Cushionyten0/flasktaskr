#####PIP
pip3 install numpy (Install specific package)
pip3 install numpy==1.10.1 (Install Specific version of a package)
pip3 uninstall numpy (To uninstall package)
(When working with pip on UNIX might need to put sudo before the command)
pip freeze > requirements.txt

#####VIRTUALENV
pyvenv-3.5 env (Creates a new dir called env and makes a virtualenv in it)
UNIX: source env/bin/activate (To activate env)
Windows: env\scripts\activate
deactivate env (To deactivate the environment)

######GIT
git config --global user.name "FIRST_NAME LAST_NAME"
git config --global user.email "MY_NAME@example.com"

git init (Initializes a local repo)
touch README.md (Make an outlook of your project)
git add -A (Add all files in the repo to staging)
git commit -m "NAME OF THE COMMIT" (To add project to the repo)
_Before next command go to github and make a new repo_
git remote add origin https://github.com/<USERNAME>/name_of_the_repo.git
git push origin master

Once all the setup is done:
git add -A
git commit -am 'message'
git push origin master

#####COVERAGE
coverage run test.py
coverage report --omit=../env/*
coverage html --omit=../env/*

######NOSETEST
nosetests --with-coverage --cover-erase --cover-package=project (Doesn't always work)
python -m nose --with-coverage --cover-erase --cover-package=project (Works)
