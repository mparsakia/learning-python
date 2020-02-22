print("hello world")


# Complete the function by filling in the missing parts. The color_translator function receives the name of a color, 
# then prints its hexadecimal value. Currently, it only supports the three additive primary colors (red, green, blue), 
# so it returns "unknown" for all other colors.
def color_translator(color):
	if color == "red":
		hex_color = "#ff0000"
	elif color == "green":
		hex_color = "#00ff00"
	elif color == "blue":
		hex_color = "#0000ff"
	else:
		hex_color = "unknown"
	return hex_color

print(color_translator("blue")) # Should be #0000ff
print(color_translator("yellow")) # Should be unknown
print(color_translator("red")) # Should be #ff0000
print(color_translator("black")) # Should be unknown
print(color_translator("green")) # Should be #00ff00
print(color_translator("")) # Should be unknown
input("Press enter to continue.")



# Students in a class receive their grades as Pass/Fail. Scores of 60 or more (out of 100) mean that the grade is "Pass". 
# For lower scores, the grade is "Fail". In addition, scores above 95 (not included) are graded as "Top Score".
def exam_grade(score):
	if (score > 95):
		grade = "Top Score"
	elif (score <= 95 and score >=60):
		grade = "Pass"
	else:
		grade = "Fail"
	return grade

print(exam_grade(65)) # Should be Pass
print(exam_grade(55)) # Should be Fail
print(exam_grade(60)) # Should be Pass
print(exam_grade(95)) # Should be Pass
print(exam_grade(100)) # Should be Top Score
print(exam_grade(0)) # Should be Fail
input("Press enter to continue.")



# Complete the body of the format_name function. 
# This function receives the first_name and last_name parameters and then returns a properly formatted string.
# Specifically:
# If both the last_name and the first_name parameters are supplied, the function should return:
# "Name: last_name, first_name"
# If only one name parameter is supplied (either the first name or the last name) , the function should return:
# "Name: name"
# Finally, if both names are blank, the function should return the empty string:
# ""
def format_name(first_name, last_name):
  if (first_name == ""):
    if(last_name == ""):
      return ""
  if (first_name):
    if(last_name):
      return "Name: " + last_name + ", " + first_name
  if (first_name == ""):
    if(last_name):
      return "Name: " + last_name
  if (last_name == ""):
    if(first_name):
      return "Name: " + first_name

print(format_name("Ernest", "Hemingway"))
# Should be "Name: Hemingway, Ernest"
print(format_name("", "Madonna"))
# Should be "Name: Madonna"
print(format_name("Voltaire", ""))
# Should be "Name: Voltaire"
print(format_name("", ""))
# Should be ""
input("Press enter to continue.")



# The longest_word function is used to compare 3 words. It should return the word with the most number of characters 
# (and the first in the list when they have the same length). Fill in the blank to make this happen.
def longest_word(word1, word2, word3):
	if len(word1) >= len(word2) and len(word1) >= len(word3):
		word = word1
	elif len(word1) <= len(word2) and len(word2) >= len(word3):
		word = word2
	else:
		word = word3
	return(word)

print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))
input("Press enter to continue.")



# The fractional_part function divides the numerator by the denominator, and returns just the fractional part 
# (a number between 0 and 1). Complete the body of the function so that it returns the right number. 
# Note: Since division by 0 produces an error, if the denominator is 0, the function should 
# return 0 instead of attempting the division.
def fractional_part(numerator, denominator):
  if (denominator == 0):
    return 0
  else:
    return (numerator / denominator) - int(numerator/denominator)

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0
input("Press enter to continue.")


# Basic while loop example
number = 1
while number < 7:
	print(number, end=" ")
	number = number + 1
input("Press enter to continue.")


# Iterating a string / for in loop
def show_letters(word):
	for x in word:
		print(x)
# Should print one line per letter
show_letters("Hello")
input("Press enter to continue.")


# Complete the function digits(n) that returns how many digits the number has. 
# For example: 25 has 2 digits and 144 has 3 digits. 

def digits(n):
	count = 0
	if n == 0:
	  return 1;
	while (n):
		count += 1
		n = int(n / 10)
	return count

print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1
input("Press enter to continue.")

#This function prints out a multiplication table (for in range(start,stop,step)) & offset "stop+1" 
# multiplication_table(1, 3) = {[1,2,3],[4,5,6],[7,8,9]}
def multiplication_table(start, stop):
	for xi in range(start,stop+1):
		for yi in range(start,stop+1):
			print(str(xi*yi), end=" ")
		print()

multiplication_table(1, 3)
input("Press enter to continue.")
# Should print the multiplication table shown above


#The counter function counts down from start to stop when start is bigger than stop, and counts up from start to stop otherwise.
def counter(start, stop):
	x = start
	if start > stop:
		return_string = "Counting down: "
		while x >= stop:
			return_string += str(x)
			if x > stop:
				return_string += ","
			x = x-1
	else:
		return_string = "Counting up: "
		while x <= stop:
			return_string += str(x)
			if x < stop:
				return_string += ","
			x = x + 1
	return return_string

print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"
input("Press enter to continue.")



# The loop function is similar to range(), but handles the parameters somewhat differently: 
# it takes in 3 parameters: the starting point, the stopping point, and the increment step. 
# When the starting point is greater than the stopping point, it forces the steps to be negative. 
# When, instead, the starting point is less than the stopping point, it forces the step to be positive. 
# Also, if the step is 0, it changes to 1 or -1. The result is returned as a one-line, space-separated string of numbers. 
# For example, loop(11,2,3) should return 11 8 5 and loop(1,5,0) should return 1 2 3 4. 

def loop(start, stop, step):
	return_string = ""
	if step == 0:
		step = 1;
	if start > stop:
		step = abs(step) * -1
	else:
		step = abs(step)
	for count in range(start,stop,step):
		return_string += str(count) + " "
	return return_string.strip()

print(loop(11,2,3)) # Should be 11 8 5
print(loop(1,5,0)) # Should be 1 2 3 4
print(loop(-1,-2,0)) # Should be -1
print(loop(10,25,-2)) # Should be 10 12 14 16 18 20 22 24 
print(loop(1,1,1)) # Should be empty
input("Press enter to continue.")




