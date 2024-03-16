#List and operations
ages = [39, 30, 27, 18]

print(ages)
print(type(ages))

##Return elemnt in n position
print(f'Age in position 2 is {ages[1]}')

##Append element to the end of the list
ages.append(15)

##Remove element 15 from list - Remove the first element 
ages.remove(15)

##Remove all elements from list
#ages.clear()

if 15 in ages:
    ages.remove(15)
    print(ages)

ages.insert(0,20)

new_ages = [20,39,18]

##Extend the list by appending all the items from the iterable
ages.extend(new_ages)

ages_next_year = [(age + 1) for age in ages]
print(ages_next_year)

ages_next_year_if_age_greather_than_21 = [(age + 1) for age in ages if age > 21]
print(ages_next_year_if_age_greather_than_21)

def visualize_len_list(list_parameter):
    print(len(list_parameter))

visualize_len_list(ages_next_year)