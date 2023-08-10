my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(f"Lista initiala este: {my_list}")
my_list_sorted = my_list
my_list_sorted.sort()
print(f"Lista sortate ascendent este: {my_list_sorted}")
my_list_sorted.sort(reverse=True)
print(f"Lista sortate descendent este: {my_list_sorted}")
my_list_sliced = my_list_sorted[:10:2]
print(f"Elementele pare din lista sunt: {my_list_sliced}")
my_list_sliced = my_list_sorted[1:10:2]
print(f"Elementele impare din lista sunt: {my_list_sliced}")
my_list_sliced = my_list_sorted[1:10:3]
print(f"Elementele multipli de 3 din lista sunt: {my_list_sliced}")
