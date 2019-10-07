#!/usr/bin/python3

from pyrob.api import *


@task

def task_5_10():
	fill_cell()
	while wall_is_beneath() == False:
		while wall_is_on_the_right() == False:
			fill_cell()
			move_right()
		fill_cell()
		if wall_is_beneath() == False:
			move_down()
			while wall_is_on_the_left() == False:
				fill_cell()
				move_left()
			fill_cell()
		else:
			while wall_is_on_the_left() == False:
				move_left()


if __name__ == '__main__':
    run_tasks()
