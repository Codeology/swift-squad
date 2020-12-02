# swift-squad
Image processing! \
Ali Matsumoto &amp; Kyle Hua, Fall 2020

## Setup
Install necessary dependencies: 
- `pip install flask`
- `pip install flask_restful`
Run:
- `python3 run.py`
- werkzeug

This backend handles all of the k-means clustering and image processing logic required of 
its corresponding <a href="https://github.com/Codeology/swift-squad-frontend">Frontend</a>.<br><br>
The two 'starter' folders (HTTP and Backend) contain old demo/curriculum content.

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

To test run.py:
- Start the server: python3 run.py 
While server is running, in a new terminal:
- GET: curl http://127.0.0.1:5000/endpoint
- POST: curl http://127.0.0.1:5000/endpoint

Thank you to <a href="https://levelup.gitconnected.com/better-restful-image-transfer-multipart-uploads-with-python-flask-swift-38a34d4e6e1f">this</a> blog post for the help :) 
