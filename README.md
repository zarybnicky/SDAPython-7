## Linux commands - in Git Bash, Linux servers, desktops
- ls [DIR]         - LiSt directory    ("dir" in cmd.exe)
- cd [DIR]         - Change Directory  ("cd"  in cmd.exe)
- mkdir \<DIR> - MaKe DIRectory
- cp \<PATH> \<PATH> - CoPy
- mv \<PATH>        - MoVe
- rm \<PATH>        - ReMove file      (irreversible, not in Trash)
- rm -r \<PATH>     - ReMove directory (-r == --recursive)
- "." = current directory
- ".." = parent directory
- \<TAB> to auto-complete one option
- \<TAB>\<TAB> to list options if more than one
- \<UP> = previous command
- \<DOWN> = next command

## Git commands in terminal
- git init [DIR]
- git add [FILE] ...
- git log
- git commit -m "Commit message"
- git push
- git pull

## Jupyter Lab
In Git Bash,
0. cd [DESIRED DIR]
1. pip install jupyterlab
2. jupyter-lab
3. ... (browser opens, do some work)
4. Ctrl-C in Git Bash to quit

## Fork a repository & sync a fork
1. git clone [YOUR FORK]
2. git remote add upstream [ORIGINAL REPO]
3. git pull upstream master
4. git rebase upstream/master
