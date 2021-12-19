## Session 2

### Git concepts review

- Remote repositories, fetch, pull
- Fork, contribution workflow
- Merge conflict

## Session 3

### Algorithmization

- approaches:
  - top-down
    - split the assignment into general steps
    - split each step into more and more concrete steps
    - when there is an obvious implementation for a step, write it down
  - bottom-up
    - find a specific example of input that is complex enough
    - write down the concrete steps that **I** would do to solve the problem for a specific input
    - find patterns in the steps/operations, e.g. introduce loops (while, for), helper functions, ...
- demo: binary search
- task: 12 days of Christmas

#### Binary search

Given an ordered list and an item X to find, check the middle item
of the list - if X is bigger, search in the right half, if X is smaller,
search in the left half, otherwise return the current item.

##### Top-down

1. General
   1. Read inputs.
   2. Find the midpoint of the list.
   3. Compare with input item.
   4. Depending on the result of the comparison: return, or go to step 2.
2. More specific
   1. def binary_search(xs, x)
   2. midpoint = len(xs) // 2
   3. current_item = xs\[midpoint]
   4. if current_item > x: return binary_search(???)
   5. elif current_item < x: return binary_search(???)
   6. else: return midpoint
3. Final code
4. ...debugging, etc.

##### Bottom-up

xs = \[1, 2, 3, 4, 5, 8, 9]
x = 8

1. midpoint_idx = 3, midpoint_item = 4
2. 8 > 4 => right sublist (start = 4, end = 6; xs = \[_, _, _, _, 5, 8, 9])
3. midpoint_idx = 5, midpoint_item = 8
4. 8 == 8 => return midpoint

##### Demo

xs = [1, 2, 3, 4, 5, 8, 9, 9]
x = 8
n = ?  =>  n = 4

1) xs = [1, 2, 3, 5, 8, 9, 9]

   x?
2) xs = [----------, 8, 9, 9]

   x?
3) xs = [----------, 8, ----]

   x?

Equivalent:
xs = [1, 2, 3, 5, 8, 9, 9]

xs =           5,
2,          9,
[1,    3,    8,    9]

### Data structures

- concept
- linked list (concept, demo, task: length)
- stack (concept, demo: single parentheses, task: multiple parentheses)
- queue (concept, demo: Queue + stdin, task: two Queues (L/R) + stdin)
- tree (concept, demo: creation, task: find

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
