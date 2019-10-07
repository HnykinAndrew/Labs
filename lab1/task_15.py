#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
	if wall_is_on_the_left() == True:
		if wall_is_above() == True:
			while wall_is_on_the_right() == False:
				move_right()
			while wall_is_beneath() == False:
				move_down()
		else:
			while wall_is_on_the_right() == False:
				move_right()
			while wall_is_above() == False:
				move_up()
	else:
		if wall_is_above() == True:
			while wall_is_on_the_left() == False:
				move_left()
			while wall_is_beneath() == False:
				move_down()
		else:
			while wall_is_on_the_left() == False:
				move_left()
			while wall_is_above() == False:
				move_up()


if __name__ == '__main__':
    run_tasks()
