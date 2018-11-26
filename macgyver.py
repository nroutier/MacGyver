#! /usr/bin/env python3
# coding: utf-8

with open("level.txt", "r") as level:
	lab_structure = []
	for row in level:
		lab_row = []
		for char in row:
			if char != "\n":
				lab_row.append(char)
		lab_structure.append(lab_row)

print(lab_structure)