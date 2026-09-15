#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   The_Descent.py                                       :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mny-aro- <mny-aro-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/09/15 15:32:18 by mny-aro-            #+#    #+#            #
#   Updated: 2026/09/15 15:47:34 by mny-aro-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys
import math


while True:
    test: list[int] = []
    for i in range(8):
        mountain_h = int(input())
        test.append(mountain_h)
    to_destroy_index = test.index(max(test))
    print(to_destroy_index)
    test.pop(to_destroy_index)
