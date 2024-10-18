
def find_common_element(list1, list2):
    common_elements = list(set(list1) & set(list2)) # set is a module that intersects both lists and combines common elements. Is used in tuples and list
    return common_elements

lista = [1, 2, 3, 4, 5]
listb = [1, 3, 6,8, 9]
results = find_common_element(lista, listb)
print(results)