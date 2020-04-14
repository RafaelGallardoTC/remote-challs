#! /usr/bin/python
import	sys

# !!! A lot of work left. It doesn´t handle files.
# !!! Errors with big chunks of code.

# Reading the first line and splitting it. Assuming predefined format.
# Transforming first line to int value's array.
# Handling some posible errors.

def	fit_books():
	for line in sys.stdin:
		shelfs = line.split()
		break
	try:
		shelfs = list(map(int, shelfs))
	except:
		print(sys.argv[0] + ": Can't read file")
		exit(-1)

	# Reading rest of lines.
	# Transforming each line to int value's array.
	# Handling some posible errors.

	coll_values = []
	for line in sys.stdin:
		coll_values.append(line.split(' ', 1)[0])
	try:
		coll_values = list(map(int, coll_values))
	except:
		print(sys.argv[0] + ": Can't read file")
		exit(-1)

	# Comparing values. First it compares the sum of the collection with
	# the min value of the shelf and return result.
	# If more than on shelf is needed we sort the list from min to max and
	# parse the list. It compares the sum of the first value of the list with the second,
	# the third, etc, if no result, adds the first value to a tmp_sum variable and keep comparing
	# the sum of first and second plus the third, four, etc. Keeps until find result.

	coll_sum = 0
	for values in coll_values:
		coll_sum += values
	result = 0
	if (min(coll_values) >= coll_sum):
		result = 1
	else:
		shelfs.sort()
		tmp_sum = 0
		idx = 0
		for i in shelfs[:-1]:
			idx += 1
			for j in shelfs[idx:]:
				if ((tmp_sum + i + j) >= coll_sum):
					result += idx
					break
			if ((tmp_sum + i + j) >= coll_sum):
				break
			tmp_sum += i
	if (result > 0):
		print(result)
	elif (result <= 0):
		print(sys.argv[0] + ": Not enough space in the given shelves")


if __name__ == "__main__":
	fit_books()
