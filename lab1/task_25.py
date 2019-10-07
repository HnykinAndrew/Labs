#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():
	move_right(1)
	move_down(1)
	def shape():
		fill_cell()
		for i in range(2):
			move_down()
			fill_cell()
		move_right()
		move_up()
		fill_cell()
		for i in range(2):
			move_left()
			fill_cell()
		move_up()
	for i in range(4):
		shape()
		move_right(5)
	shape()


if __name__ == '__main__':
    run_tasks()
