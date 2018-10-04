#string

s = "I am a string."
print(type(s))	#will say string

#boolean

yes = True	#Boolean True
print(type(yes))

no = False	#Boolean False
print(type(no))

#list -- ordered and changeable

alpha_list = ["a", "b", "c"]	#list initialization
print(type(alpha_list))		#will say tuple
print(type(alpha_list[0]))	#will say string
alpha_list.append("d")		#will add "d" to the list
print(alpha_list)			#will print list

#Tuple

alpha_tuple = ["a", "b", "c"]	#tuple initialization
print(type(alpha_tuple))	#will say tuple

try:						#attempt to follow the line
	alpha_tuple = "d"		#wont work and will raise TypeError
except TypeError:			#when we get a type error
	print("We can't add elements to tuples!")	#print this message
print(alpha_tuple)			#will print tuple