#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   reverse.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mny-aro- <mny-aro-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/10/01 17:45:44 by mny-aro-            #+#    #+#            #
#   Updated: 2026/10/01 17:47:11 by mny-aro-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys
import math

sentence = input()

#expected output:
#    "life is beautiful -> efiL si lufituaeb"

print(" ".join(word[::-1] for word in sentence.split(" ")))