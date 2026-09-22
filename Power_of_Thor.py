#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   Power_of_Thor.py                                     :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mny-aro- <mny-aro-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/09/22 16:30:22 by mny-aro-            #+#    #+#            #
#   Updated: 2026/09/22 16:33:41 by mny-aro-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys, math


light_X, light_Y, initial_TX, initial_TY = [int(i) for i in input().split()]

thor_X = initial_TX
thor_Y = initial_TY


while True:
    remainingTurns = int(input())
    
    direction_X: str = ""
    direction_Y: str = ""

    if thor_Y > light_Y:
        direction_Y += "N"
        thor_Y -= 1
    elif thor_Y < light_Y:
        direction_Y += "S"
        thor_Y += 1
    if thor_X > light_X:
        direction_X += "W"
        thor_X += 1
    elif thor_X < light_X:
        direction_X += "E"
        thor_X -= 1
    
    print(direction_Y + direction_X)
