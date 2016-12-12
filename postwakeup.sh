#!/bin/zsh
# 1. open a problem
# 2. ...
problem=$(python3 ${0:a:h}/get_and_delete.py ~/n/problems.list)
echo $problem
xdg-open $problem

