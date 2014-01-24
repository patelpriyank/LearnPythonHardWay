the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print("number> %d" %number)

#build an empty list
elements = []

#use build in range() function ot loop through numbers.
#NOTE: range() function only does numbers from the first to the last, not including the last
for i in range(0, 10):
    elements.append(i) #build in append() function for list

print("Total elements: %d" %len(elements))

counter = 0
for i in elements:
    if counter == len(elements)-1:
        print("Last element: %d" %counter)
    else:
        print("Element: %d, Next element: %d" %(i, elements[counter+1]))

    counter += 1
