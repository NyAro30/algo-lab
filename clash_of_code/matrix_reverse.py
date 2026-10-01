#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   matrix_reverse.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mny-aro- <mny-aro-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/10/01 17:59:06 by mny-aro-            #+#    #+#            #
#   Updated: 2026/10/01 18:01:05 by mny-aro-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

h = int(input())
w = int(input())

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

for i in range(h):
    print('O'*w)
