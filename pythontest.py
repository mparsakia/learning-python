print("hello world")

# using format option in a simple string 
print ("{}, A computer science portal for geeks."
                        .format("GeeksforGeeks")) 
# The values passed as parameters 
# are replaced in order of their entry 
print ("This is {} {} {} {}"
       .format("one", "two", "three", "four"))   
# Keyword arguments are called 
# by their keyword name 
print("{gfg} is a {0} science portal for {1}"
.format("computer", "geeks", gfg ="GeeksforGeeks")) 
# check the links to read more about formatting (i.e. float, int, hex, octal, bin... etc) and forcing style (right align, etc)
# https://www.geeksforgeeks.org/python-format-function/


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
numbera = 1
while numbera < 7:
	print(numbera, end=" ")
	numbera = numbera + 1
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



# The format_address function separates out parts of the address string into new strings: 
# house_number and street_name, and returns: "house number X on street named Y". The format 
# of the input string is: numeric house number, followed by the street name which may contain numbers,
#  but never by themselves, and could be several words long. For example, "123 Main Street", "1001 1st Ave", or "55 North Center Drive".
def format_address(address_string):
  address = address_string          # Maybe not needed but I dont know if param is const (coming from c++ knowledge)
  sublist = address.split(' ')      # Split the string delim by space, returns list
  housenum = sublist[0]             # The house number (list format)
  housenum = str(housenum)          # Converted to string (verify: print(type(housenum)) Could have chained above, this is clearer for example.
  streetlist = sublist[1:]          # Streetnames, list format still
  streetname = ' '.join([str(x) for x in streetlist])
                                    #line above takes all in sublist[1:] and makes it one long string, adds " " in between the list items
  return f"house number {housenum} on street named {streetname}"
                                    #Using String Literals / Template Literals with 'f' before string.
  
print(format_address("123 Main Street")) # Should print: "house number 123 on street named Main Street"
print(format_address("1001 1st Ave"))
print(format_address("55 North Center Drive"))
input("Press enter to continue.")



# The highlight_word function changes the given word in a sentence to its upper-case version. 
# For example, highlight_word("Have a nice day", "nice") returns "Have a NICE day". 
# Can you write this function in just one line?
def highlight_word(sentence, word):
	return(sentence.replace(word,word.upper()))

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))
input("Press enter to continue.")



# Combine two lists. One list is in reverse order, 'reverse' it to make it correct.
def combine_lists(list1, list2):
  newlist = []
  newlist.extend(list1)
  list2.reverse()      
  newlist.extend(list2)
  return newlist
  
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]
print(combine_lists(Jamies_list, Drews_list))
input("Press enter to continue.")  # prints ['Alice', 'Cindy', 'Bobby', 'Jan', 'Peter', 'Marcia', 'Greg', 'Carol', 'Mike']

# Use a list comprehension to create a list of squared numbers (n*n). 
# The function receives the variables start and end, and returns a list of squares of consecutive numbers 
# between start and end inclusively. For example, squares(2, 3) should return [4, 9].
# Very Helpful Note: https://www.datacamp.com/community/tutorials/python-list-comprehension listcomps are kind of like lambdas in c++
def squares(start, end):
	return [x**2 for x in range(start,end+1)]

print(squares(2, 3)) # Should be [4, 9]
print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# iterate through the keys and values of the car_prices dictionary, printing out some information about each one.
def car_listing(car_prices):
  result = ""
  for key, value in car_prices.items():
    result += str(key) + " costs " + str(value) + " dollars\n"
  return result
  
print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000})) # Prints Kia Soul costs 19000 dollars ... so on
input("Press enter to continue.")



# Taylor and Rory are hosting a party. They sent out invitations, and each one collected responses into dictionaries, 
# with names of their friends and how many guests each friend is bringing. Each dictionary is a partial list, 
# but Rory's list has more current information about the number of guests. Fill in the blanks to combine both dictionaries 
# into one, with each friend listed only once, and the number of guests from Rory's dictionary taking precedence,
# if a name is included in both dictionaries. Then print the resulting dictionary.
def combine_guests(guests1, guests2):
  # Combine both dictionaries into one, with each key listed 
  # only once, and the value from guests1 taking precedence
  g1 = guests1
  g2 = guests2
  g2.update(g1)     #dict1.update(dict2)great function, merges the lists and replaces key:value's of dict1 with dict2 
  return g2

Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}
print(combine_guests(Rorys_guests, Taylors_guests))
input("Press enter to continue.") #{'David': 1, 'Nancy': 1, 'Robert': 4, 'Adam': 2, 'Samantha': 3, 'Chris': 5, 'Brenda': 3, 'Jose': 3, 'Charlotte': 2, 'Terry': 1}



# Use a dictionary to count the frequency of letters in the input string. Only letters should be counted, not blank spaces, 
# numbers, or punctuation. Upper case should be considered the same as lower case. 
# For example, count_letters("This is a sentence.") should return 
# {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}.
from collections import Counter

def count_letters(text):
  return dict(Counter((''.join(c for c in text if c.isalpha()).lower())))
    # What a godline. Let's explain:
    # dict will return a dictionary as requested in the problem
    # Counter is an object/class that will do what it says, count the items and put them in a dictionary, but it returns "Counter({...})"
    # ''.join(c for c in text if c.isalpha()) will strip whitespace and add to a new string if the value "is alpha"
    # remember that c for c in text will iterate through the string and then the .isalpha() only adds it to the new string, if its alphabet only
    # And .lower() will force that entire string lowercase. Remember functions always work from the inside out, so follow the parenthesis!
print(count_letters("AaBbCc")) # Should be {'a': 2, 'b': 2, 'c': 2}
print(count_letters("Math is fun! 2+2=4")) # Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}
print(count_letters("This is a sentence.")) # Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}
input("Press enter to continue.")


