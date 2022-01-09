## Session 2

### Git concepts review

- Repository

  - Remote repository (GitHub, GitLab)
    - Main Repo:
      - zarybnicky/SDAPython-7 = writable only by owner (zarybnicky)
    - Fork = copy of the main repo:
      - StingrayCZ/SDAPython-7 = writable only by owner (StingrayCZ)
  - Local repository (files on disk)
    - `git clone https://github.com/zarybnicky/SDAPython-7.git` => local clone of the repo
- "Remote" (`git remote -v`) = reference to a remote repository by URL

  - "origin" - where was this repo cloned from
  - "upstream" - where was "origin" forked from
- `git push`, `git fetch`, (`git pull`)

  - "push" = upload local commits to a remote repo
  - "fetch" = download commits from a remote repo
  - ("pull" = fetch + rebase/merge)
  - "Sync Fork"
    - `git fetch upstream`
    - `git rebase upstream`
- "Pull Request" (PR)

## Session 3

### Algorithmization

- approaches:
  - top-down
    - split the **whole problem** into **general steps leading to the solution**, or into **smaller subproblems**
    - split each step/subprobleme into more and more concrete steps
    - when there is an obvious implementation for a step, write it down
  - bottom-up
    - find a **specific example** of input that is complex enough
    - write down the concrete steps that **I** would do to solve the problem for a specific input
    - find patterns in the steps/operations, e.g. introduce loops (while, for), helper functions, ...
  - divide and conquer
    - find the closest subproblem
    - do the minimum to reduce the problem to a subproblem
    - n! = n * (n - 1)!
- demo: binary search
- task: 12 days of Christmas


#### Prime factors

##### Top-down

General steps:

- Find a prime number,
- Check if the number is divisible.
- If divisible, n is a prime factor, check again
- If not divisible, look for next prime

More specific:

- "is divisible" == "n % p == 0"
- "find a prime number" == "The Sieve of Eratosthenes"

##### Bottom-up

- n=54
- 54 % 2 = 0, is divisible => 2 is a prime factor
- 54 / 2 = 27
- 27 % 2 = 1, is not divisible => 2 is not a prime factor
- next prime = 3
- 27 % 3 = 0, is divisible => 3 is a prime factor
- 27 / 3 = 9
- 9 % 3 = 0, is divisible => 3 is a prime factor
- 9 / 3 = 3
- 3 % 3 = 0, is divisible => 3 is a prime factor
- 3 / 3 = 1, we are done
- => prime factors are 2, 3, 3, 3

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
  - "... is a data organization, management, and storage format that enables efficient access and modification."
  - Opaque object, that provides a set of operations (that comprise the API, "rozhraní")
- you already know some: set, dict, list

#### Linked List

- composed of nodes: one node is one unit of the entire list
- one node (jeden uzel) = jeden článek řetězu
- node is composed of two slots: one slot for data, one slot for a pointer to the next node
- `[1, 2, 3] : list`
- `( 1, -> )   ->   ( 2, -> )  ->  ( 3, NULL ) : linked list`

  class LinkedListNode
  def __init__(self, data, next):
  self.data = data
  self.next = next

  class TreeNode:
  def __init__(self, data, left, right):
  self.data = data
  self.left = left
  self.right = right

  three = LinkedList(3, None)
  two = LinkedList(2, three)
  one = LinkedList(1, two)
  list = one
  while list is not None:
  print(list.data)
  list = list.next

  list = [1, 2, 3]
  for item in list:
  print(item)

#### Stack

concept, demo: single parentheses, task: multiple parentheses)

#### Queue

concept, demo: Queue + stdin, task: two Queues (L/R) + stdin)

#### Tree

concept, demo: creation, task: find

## Session 4

### Gridworld
- TKinter
- Gridworld
- Fork & play, WASD
- Pathfinding = tree search
  - Natural, strategies

### BFS
= queue

list, deque, timeit

### DFS
= stack

list, deque, timeit

### Dijkstra
= Prio Q

tree, heap, min-heap, heapq

## Session 5

### Review
- Virtualenv
- Git
- GitHub
- Algorithmization
- Recursion

### Practical
- refactoring
- linters
- documentation

### Sorting

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
