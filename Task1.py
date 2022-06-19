# func creates new list. each item in func param will be will be sqared and then appended to new_list. function returns sorted new list.
def order_and_square(list_of_nums):
    new_list = []
    for i in list_of_nums:
        i = i * i
        new_list.append(i)
    return sorted(new_list)

print(order_and_square([2, 1, 10, 5]))
