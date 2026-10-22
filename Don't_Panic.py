#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   Don't_Panic.py                                       :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mny-aro- <mny-aro-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/10/22 21:25:51 by mny-aro-            #+#    #+#            #
#   Updated: 2026/10/22 21:33:27 by mny-aro-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys
import math

nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in input().split()]

elevators = {}
for i in range(nb_elevators):
    elevator_floor, elevator_pos = [int(j) for j in input().split()]
    elevators[elevator_floor] = elevator_pos

while True:
    inputs = input().split()
    clone_floor = int(inputs[0])
    clone_pos = int(inputs[1])
    direction = inputs[2]

    if clone_floor == -1:
        print("WAIT")
    elif clone_floor == exit_floor and clone_pos == exit_pos:
        print("WAIT")
    elif clone_floor in elevators and clone_pos == elevators[clone_floor]:
        print("WAIT")
    elif clone_floor == exit_floor:
        if (direction == "RIGHT" and clone_pos < exit_pos) or (direction == "LEFT" and clone_pos > exit_pos):
            print("WAIT")
        else:
            print("BLOCK")
    elif clone_floor in elevators:
        elevator_pos = elevators[clone_floor]
        if (direction == "RIGHT" and clone_pos < elevator_pos) or (direction == "LEFT" and clone_pos > elevator_pos):
            print("WAIT")
        else:
            print("BLOCK")
    else:
        print("BLOCK")
