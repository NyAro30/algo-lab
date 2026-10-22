#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   code_vs_zombie.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mny-aro- <mny-aro-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/09/15 15:04:05 by mny-aro-            #+#    #+#            #
#   Updated: 2026/09/22 09:52:24 by mny-aro-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import math

while True:
    x, y = [int(i) for i in input().split()]
    
    human_count = int(input())
    humans = {}
    for i in range(human_count):
        human_id, human_x, human_y = [int(j) for j in input().split()]
        humans[human_id] = (human_x, human_y)
    
    zombie_count = int(input())
    zombies = []
    for i in range(zombie_count):
        zombie_id, zombie_x, zombie_y, zombie_x_next, zombie_y_next = [int(j) for j in input().split()]
        zombies.append({
            'id': zombie_id,
            'x': zombie_x,
            'y': zombie_y,
            'next_x': zombie_x_next,
            'next_y': zombie_y_next
        })

    target_x, target_y = x, y
    best_urgency = float('inf')

    for zombie in zombies:
        min_dist_to_human = float('inf')
        for h_id, (h_x, h_y) in humans.items():
            dist_z_h = math.hypot(zombie['x'] - h_x, zombie['y'] - h_y)
            if dist_z_h < min_dist_to_human:
                min_dist_to_human = dist_z_h

        turns_before_kill = min_dist_to_human / 400.0
        dist_ash_z = math.hypot(x - zombie['next_x'], y - zombie['next_y'])
        
        turns_to_reach = (dist_ash_z - 2000) / 1000.0
        if turns_to_reach < 0:
            turns_to_reach = 0

        if turns_to_reach <= turns_before_kill:
            if turns_before_kill < best_urgency:
                best_urgency = turns_before_kill
                target_x, target_y = zombie['next_x'], zombie['next_y']

    if target_x == x and target_y == y and len(zombies) > 0:
        target_x, target_y = zombies[0]['next_x'], zombies[0]['next_y']

    print(f"{target_x} {target_y}")
