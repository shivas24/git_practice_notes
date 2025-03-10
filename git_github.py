# -*- coding: utf-8 -*-
"""Git_Github.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VZ8gLGeVoZESOgCQ1omJ2F2ah31PwJTO
"""



"""**Git**

Git is a version cotrol system to track the changes in

**Functioning**

* Track the history
* collaborate

**Github**

* It is a repository (normally know as folder) which can be used to store and manage the code

* Create a first repository
* Create a README.md . it contains all our project details
* Make first commit


**Git & How to Setup Git**
We need to install Git in our local system and need to run with various commands.

3 tools available

1. Microsoft Vsual Studio COde
2. Gitbash for WIndows OS
3. Terminal Mac

Install any of above software tools. now check **git --version**


"""

# To check the version of git
!git --version

"""**CLONE & STATUS**

  Local server is laptop/PC  
  Remote server is Github Repository (Github folder)

  **CLONE** command is used to store data from gthub repository to our local machine
Command is git clone github repository address
"""

# CLone
!git clone https://github.com/shivas24/working.git

ls -a  # list hidden files  , # ls list files

cd working

!git status

!git commit -m "deleted"

!git status

!git add .

!git commit -m "update"

!git remote -v

!git remote set-url origin https://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@github.com/shivas24/working.git

!git remote -v

!git clone https://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@github.com/shivas24/working.git

!git fetch

!git status

!git clone https://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@github.com/shivas24/working.git

"""GIT COMMANDS

usage:
git [--version] [--help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           [--super-prefix=<path>] [--config-env=<name>=<envvar>]
           <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)

   **clone**     Clone a repository into a new directory
   
   **init**     Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)

   **add**       Add file contents to the index

   **mv**        Move or rename a file, a directory, or a symlink

   **restore**   Restore working tree files

   **rm**        Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   
   **bisect**    Use binary search to find the commit that introduced a bug
   
   **diff**      Show changes between commits, commit and working tree, etc
   
   **grep**      Print lines matching a pattern
   
   **log**       Show commit logs
   
   **show**      Show various types of objects
   
   **status**    Show the working tree status

grow, mark and tweak your common history
   
   **branch**    List, create, or delete branches
   
   **commit**    Record changes to the repository

   **merge**     Join two or more development histories together
  
   **rebase**    Reapply commits on top of another base tip
   
   **reset**     Reset current HEAD to the specified state
   
   **switch**    Switch branches
   
   **tag**       Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   
   **fetch**     Download objects and refs from another repository
   
   **pull**      Fetch from and integrate with another repository or a local branch
   
   **push**      Update remote refs along with associated objects

   **Origin**    Which is the by default repository on github.

   **Main/Master** by default repository on client side either laptop/PC

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
See 'git help git' for an overview of the system.
"""

!git

!git diff

"""**Different types of status in git**

* UNTRACKED   . if any changes made to local files git is not unaware of this..that measn there is no updation in github repository in remote server
* MODIFIED   If any changes made in local server
* STAGED  If any changes made are added ready to be committed
* ADD    Adds to changed files and moves to stage and ready to be commit in git or github repository
* COMMIT committing to git remote repository
* PUSH coomand to push from our local system to github rp



"""

!git config --global user.name "shivas24"
!git config --global user.email "shivasunkaranam@gmail.com"
!git config --global color.ui auto

!git config user.name

# Add changes or files ready to commit on github remote respository

#!git add Index.html  #Make it ready to Add Index.html and which is ready for commit in github rp
#!git add . # We can use this function to add all modified files or created files at once without mention the file names

"""** INIT Command**

* init used to create new git repository
* git remote add origin link
* git remote -v (verifying remote
* git branch   to checkbranch
* git branch -M main     to rename branch
* git push origin main

"""

!git remote -v

!git branch

!git branch -M new

!git remote -v

!git push -u origin new

!git remote -v

!git branch -r

!git reset -url https://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@github.com/shivas24/working.git
!git push -u origin main



"""**WORK FLOW**

**Local Git**

Gthub repo
>>clone

>>chaanges

>>add

>> commit

>> push
"""



"""**BRANCH COMMANDS**
* git branch
> to check branch
* git branch -M main
> to rename branch
* git checkout <.branchname..>
> to navigate branch
* git checkout -b <..newbranch name..>
> create new branch
* git branch -d <..branch_name..>
> to delete branch
* git diff <..branch Name..>
> compare between between current branch and mentioned branch
* git merge <..branchname..>
> merges 2 branches
**UNDO CHANGES**
* Staged CHanges  (means **git add filename** or **git add .**)
> git reset filename  (for specified filename)

  > git reset  (for all staged files)

* For committed changes (**git commit -m "ddd"**)
> git reset HEAD~1
> for undo change of latest commit

> for multiple commits
> git reset <..commit hashcode..>
>>
eg..commit 94e5ba5be30c902a4b391c46faee226a1465e859
Author: shXXXX <XXXXXXXaranam@gmail.com>
Date:   Sat Sep 2 13:51:14 2023 +0530

>>deleted
>> git reset 94e5ba5be30c902a4b391c46faee226a1465e859

> to remove that commit from inside our vscode

>> git reset --hard <<hashcode>>


**FORK**
>>To create same repository which was already created by someother or simply saying that copy ther entire repository into our repository..so that we can use the code for any changes

>> PULL to create ask access the code download request









"""