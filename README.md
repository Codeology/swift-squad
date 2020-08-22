# swift-squad
Image processing! \
Ali Matsumoto &amp; Kyle Hua, Fall 2020

## Setup
### To clone this repo locally:
* open the terminal
* cd into the directory where you want the project to
 live
* run `git clone https://<your github username>:<your github password>@github.com/codeology/swift-squad.git`
* if you're unfamiliar with git, let us know! we'll give you resources so that you're caught up for the project

## Setting up the backend
Our API is made from Python and the Flask-RESTful framework, which allows us to define API routes we hit from the frontend.
Code for the API is located in the 'api' directory of this repo.
1. Enter the API directory: `cd api` 
2. Set up a virtual environment (this allows you to install libraries without affecting code outside this project): 
`python3 -m venv venv/`
3. Activate your venv: `source venv/bin/activate`
4. Install Flask and Flask-RESTful within your venv: `pip install -r requirements.txt`
5. Add the venv to your .gitignore: open your gitignore and add the line `/api/venv/*`
    - while you're at it, ignore any other files specific to your local machine 

## What the heck is git? 
Welcome to our version control system! If you're familiar with git/github, you can skip this section.

When you cloned this repo locally, a Git repository was created. This allows you to execute a bunch 
of different commands to keep track of your versions and let us collaborate! 

When you work on a git project, you `add` files to a `commit` and `push` that commit to a remote `branch` so other 
people can see it. To obtain other people's work in your local repo, you `pull` their work. 

Here's how that works: 
* Make sure you're up to date on everyone's code: from your `master` branch, run `git pull`
    * You can make sure you're on `master` by running `git branch` - it'll display every branch you've created locally, 
    and there will be a star next to the current one
    * If you aren't on master, run `git checkout master` to switch.  
* To create a branch to work on, run `git checkout -b <branch name>` in the terminal 
* On github, in the remote repo, click the little `branch` icon that (probably) says `master` and type in the same branch
name you're working with locally. Click `create branch <name>` (it should have a little footnote that says `from master`)
* Work on your code! Periodically, you'll want to make a commit to save your work. To do this, run `git add <file>` for any
files you've changed. Once all files are included, run `git commit -m "<a message that describes your commit>"`. Now you've
saved a snapshot of your work in case something happens!
* Once you've completed whatever you're working on, commit one more time, then run `git push origin <branch name>`. Now 
your code is on the github version of your branch, and we can merge it into master or work with it collaboratively!
