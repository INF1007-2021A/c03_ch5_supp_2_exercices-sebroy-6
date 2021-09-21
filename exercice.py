#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def get_num_letters(text):
	nb_letters = 0
	for letter in text:
		if letter.isalnum():
			nb_letters += 1

	return nb_letters

def get_word_length_histogram(text):
	length_list = 0
	histogram = []

	for word in text.split():  # Find the length of our list
		if get_num_letters(word) > length_list:
			length_list = get_num_letters(word)

	for i in range(length_list + 1):  # create the list with the right length
		histogram.append(0)

	for word in text.split():  # Add a point to the correct position in the histogram
		histogram[get_num_letters(word)] += 1

	return histogram

def format_histogram(histogram):
	histogram.pop(0)
	formated_histogram = ""
	ROW_CHAR = "*"
	for i, number in enumerate(histogram):
		if i + 1 < 10:
			formated_histogram += " "
		formated_histogram += str(i + 1) + " " + (ROW_CHAR * number) + "\n"
	return formated_histogram

def format_horizontal_histogram(histogram):
	BLOCK_CHAR = "|"
	LINE_CHAR = "¯"
	Max_histo = max(histogram)
	result = ""

	for i in range(1, Max_histo + 1):
		for position, number in enumerate(histogram):
			if number >= Max_histo:
				result += BLOCK_CHAR
			else:
				result += " "
		Max_histo -= 1
		result += "\n"

	for i in range(0, len(histogram) + 1):
		result += LINE_CHAR

	return str(result)


if __name__ == "__main__":
	spam = "Stop right there criminal scum! shouted the guard confidently."
	eggs = get_word_length_histogram(spam)
	print(eggs, "\n")
	print(format_histogram(eggs), "\n")
	print(format_horizontal_histogram(eggs))
