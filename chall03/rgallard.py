#! /usr/bin/python
import	sys

#A lot missing, but it´ll get some updates :)

##Snail Sort
##<1-9 squared_rows...>

def 	SnailSort(my_list):

	output = []
	if len(my_list) == 0 or len(my_list) > 21:
		print("<1-9 squared_rows...>")
		return

	row_s = 0
	row_end = len(my_list) - 1
	col_s = 0
	col_end = len(my_list[0]) - 1

	for i in my_list:
		if (i.isdigit() == False):
			print("<1-9 squared_rows...>")
			return


	# Adding first full row to output.
	while row_s <= row_end and col_s <= col_end:
		for i in range(col_s, col_end+1):
			output.append(my_list[row_s][i])
		row_s += 1

	#Second part. Taking top-right values from sub_arrays.
		for i in range(row_s, row_end+1):
			output.append(my_list[i][col_end])
		col_end -= 1

	#Bottom part.
		if row_s <= row_end:
			for i in range(col_end, col_s-1, -1):
				output.append(my_list[row_end][i])
			row_end -= 1

		if col_s <= col_end:
			for i in range(row_end, row_s-1, -1):
				output.append(my_list[i][col_s])
		col_s += 1

	print(', '.join(output))
	return output

SnailSort(sys.argv[1:])
