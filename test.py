#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   test.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mny-aro- <mny-aro-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/09/15 15:52:39 by mny-aro-            #+#    #+#            #
#   Updated: 2026/09/15 16:55:58 by mny-aro-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


#=== Level 1 ===

# import sys
# import math

# _sum = input()
# tab_to_sort = _sum.split("+")
# tab_to_sort.sort()
# answer = "+".join(tab_to_sort)
# print(answer)

#=== Level 2 ===

# import sys
# import math

# n = int(input())
# tab: list[int] = []
# for i in range(2, n + 1):
#     if i % 2 == 0:
#         tab.append(i)
# answer = sum(tab)
# print(answer)

#=== Level 3 ===

# import sys
# import math


# n = int(input())
# if n == 0:
#     print("0")
# elif n > 30:
#     print("Steps out of bound")
# else:
#     x, y = (0, 0)
#     for step in input().split():
#         if step == "L":
#             x -= 1
#         if step == "R":
#             x += 1
#         if step == "F":
#             y += 1
#         if step == "B":
#             y -= 1

#     answer = int(math.sqrt((x ** 2) + (y ** 2)))
#     print(answer)

#=== Level 4 ===

# import sys
# import math


# input_string = input()
# dico: dict[str, int] = {}

# for i in input_string:
#     if i not in dico.keys():
#         dico[f"{i}"] = input_string.count(f"{i}")
#     else:
#         continue
# for k, v in dico.items():
#     if v > 0:
#         print(f"{k}" * v, end="")
#     print()
