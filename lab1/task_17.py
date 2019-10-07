#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_27():
	while wall_is_above() == False and cell_is_filled() == False:
		move_up()
	move_right()
	if cell_is_filled() == False:
		move_left(2)

if __name__ == '__main__':
    run_tasks()
