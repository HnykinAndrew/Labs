#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
	move_right()
	fill_cell()
	x=1
	k=0
	while wall_is_on_the_right() == False:
		for i in range(x):
			if wall_is_on_the_right() == False:
				move_right()
				k += 1
			if k == x:
				fill_cell()
		k = 0
		x += 1



if __name__ == '__main__':
    run_tasks()
