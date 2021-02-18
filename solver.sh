#!/bin/bash

cd solver
python3 array_to_clingo.py
clingo *.lp 0 > output
python3 clingo_to_array.py
