# ASP Sudoku Solver

## About The Project
Sudoku solver written in *clingo* (Answer Set Programming).

## Getting Started

Clone the project locally.</br>

## Prerequisites

*clingo* must be installed on the machine:</br>
To check if *clingo* is installed, run:</br>
`which clingo`</br>
If there is no output, run:</br>
`sudo apt install gringo`</br>
Or the equivalent for your distribution.</br>

`solver.sh` must have run permissions.</br>
Run `chmod +x solver.sh`

## Usage

For the following problem:</br>
![alt text](figures/problem.png "Problem")</br>

1. Edit `problem.py` with an array representing the game:</br>
```
problem = [
    [0,0,0,9,2,0,0,0,0],
    [0,0,9,0,0,1,0,0,0],
    [2,0,6,0,0,0,8,0,0],
    [9,1,0,0,0,0,0,0,7],
    [0,0,7,5,0,8,0,0,0],
    [6,8,0,0,9,0,0,5,0],
    [0,3,0,0,0,5,0,7,0],
    [0,0,0,0,3,0,0,0,2],
    [0,0,0,0,1,0,0,0,0]
]
```

2. Run `./solver.sh` and it will print the solution.</br>
```
[8, 7, 1, 9, 2, 6, 3, 4, 5]
[3, 4, 9, 8, 5, 1, 7, 2, 6]
[2, 5, 6, 4, 7, 3, 8, 9, 1]
[9, 1, 5, 3, 4, 2, 6, 8, 7]
[4, 2, 7, 5, 6, 8, 9, 1, 3]
[6, 8, 3, 1, 9, 7, 2, 5, 4]
[1, 3, 2, 6, 8, 5, 4, 7, 9]
[5, 9, 8, 7, 3, 4, 1, 6, 2]
[7, 6, 4, 2, 1, 9, 5, 3, 8]
```
Which represents the following:
![alt text](figures/solution.png "Solution")</br>

If the game has no solution it will print:</br>
`Unsatisfiable.`

## Built With

* [clingo](https://potassco.org/)

## Authors

* **João Bordalo** - *Initial work* - [jbordalo](https://github.com/jbordalo)