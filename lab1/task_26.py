#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
	move_right(1)
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

	for j in range(4):
		for i in range(9):
			shape()
			move_right(5)
		shape()
		move_down(4)
		move_left(35)
	for i in range(9):
		shape()
		move_right(5)
	shape()
	move_left(36)


if __name__ == '__main__':
    run_tasks()
