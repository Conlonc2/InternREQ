# This repo is no longer maintained!

# CSC-330---GearGrinders

# Authors of InternREQ  
  Tom Birmingham    
  Christopher Conlon  
  Davis Jaekle             
  Dan Glinski  
  Mohamad Maarouf  

    
  # Flask structure we are working with

  |  
  |-|InternREQ (project's root level)  
  |-|.git (This file should not be touched it was created with 'git init')  
  |-|.gitignore (This file will contain files we dont want git to track for us i.e.: pythons cached forms)  
  |-|flaskr.py (For routing and other python functions if we need to add more python files they go in this level of the project)  
  |-|static  
  |-----| Any resources (i.e. image files, .css files, and anything you are not sure where to put, probably goes here)   
  |-|templates  
  |-----| All html files and files that can be considered a route in flask  
  |-|modules  
  |-----| python files that our server will import(i.e.: Flask forms that we create)  
  
  # Steps for working with a repo  
    
    1) Make sure you have git installed on what ever machine you wish to use. 
        If you do not have git go here: [git](https://git-scm.com) and download.  

    2) Set git up by typing the following commands in the command line:   
            git config --global user.name "Enter Username Here"  
            git config --global user.email johndoe@example.com  

     These steps are required so we know who is adding what and, git usually won't allow 
     you to push files without this step.  
       
  2.5) Test your variabels by typing  
            git config --list  
    
# Getting the repo on local machine  
    1) Open up the command line  
    2) cd into the folder you want to store this repo 
    5) Now in the open command line type "git clone [https://github.com/scsu-csc330-400/gear-grinders-test.git]". Press enter  
    6) Make sure the folder is now on your computer and start hacking away!  
      
  # Branching  
    1) Open terminal/cmd  
    2) Make sure your in the proper git repository  
    3) Type "git checkout -b <NAME YOUR BRANCH>"  
    This creates a new branch and moves you into it. Step 3 is shorthand for
    --> "git branch <NAME BRANCH HERE>"
    --> "git checkout <SAME BRANCH NAME HERE>"

  # Adding changes to github  
    1) Make edits to the project  
    2) git add < enter files that have been updated and need to be staged >  
    3) git commit -m "Enter message that tells us what you did"  
    4) git push <REMOTE NAME> <BRANCH NAME>   
  
  # Pulling/Pushing new changes  
    For this step you need to understand one thing, this is that you will be pulling from this exact address:  
      -->[https://github.com/scsu-csc330-400/gear-grinders-test]  
    To do this you will use the command: 
        -->git pull [https://github.com/scsu-csc330-400/gear-grinders-test.git] exactly as written  
      
    However to push changes to your repo you will use "git push <REMOTE NAME> <BRANCH NAME>  
    --> Remote name will be origin if you used "git clone <YOUR REPO>"  
      
# Wrapping it up  
  After following these steps you should have a local version of this project and be able to create pull requests so we can merge your edits with the main project. If you have any questions still please feel free to ask.  
