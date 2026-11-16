#Assigning the data types to variables

integer_var = 10                            #integer
print(integer_var)          

float_var = 10.5                            #Float
print(float_var)

string_var = "Hello, Machela!"           #string
print(string_var)

bool_var = True                             #Boolean
print(bool_var)

list_var = [1,2,3,4,5]                      #List
print(list_var)

dict_var = {"name": "John", "age": "30"}    #dictionary
print(dict_var)

#string operations
uppercase_string = string_var.upper()
concatenated_string = string_var + "How are you?"

#List operations
list_length = len(list_var)       #Get the lenght of the list
list_sum = sum(list_var)          #sum of list elements
list_var.append(6)               #Add an element to the list

#Dictionary operations
dict_keys = dict_var.keys()            #Get the keys of the dictionary
dict_values = dict_var.values()        #Get the values of the dictionary
dict_var["city"] = "Pretoria"          #Add a new key-value pair to the dictionary

print("Uppercase String:", uppercase_string)
print("concatenated string:", concatenated_string)
print("Length of the list:", list_length)
print( "sum oof the list:",list_sum)
print("dictionary keys:",dict_keys)
print("dictionary values:",dict_values)
print("dictionary variables:", dict_var)

#Artihmetic operations
sum_result = integer_var + float_var 
diff_result = integer_var - 5
mult_result = integer_var * 2
div_result = integer_var / 2
mod_result = integer_var % 3
expo_result = integer_var ** 2

#comparison operations
is_equal = integer_var == float_var
is_greater = integer_var > 5
is_less =float_var <20

#Logical operations
and_result = bool_var and (integer_var > 5)          #Logical AND
or_result = bool_var or (integer_var < 5)              #Logical OR
not_result = not bool_var                               #Logical NOT

print(sum_result)
print(diff_result)
print(mult_result)
print(div_result)
print(mod_result)
print(expo_result)
print(is_equal)
print(is_greater)
print(is_less)
print(and_result)
print(or_result)
print(not_result)