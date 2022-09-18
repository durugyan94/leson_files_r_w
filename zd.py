import os
from os.path import join
cook_book = {} 
dishes = []
person_count = None


def get_shop_list_by_dishes(dishes, person_count):
    dishes_dict = {}
    for dishe in dishes:
        if dishe in cook_book:
            for ingredients in cook_book[dishe]:
                quantity_1 = (ingredients["quantity"] * person_count)
                dishes_dict.update({ingredients["ingredient_name"]:{"quantity":quantity_1, "measure":ingredients["measure"]}})
    return dishes_dict


with open ("cook.txt", "r", encoding="utf-8") as cook_list: 
    for line in cook_list: 
        cook_dict = {line.strip():[]} 
        cook_count = cook_list.readline() 
        for i in range(int(cook_count)): 
            emp = cook_list.readline() 
            ingredient_name, quantity, measure = emp.split(" | ") 
            employee = {"ingredient_name": ingredient_name, "quantity": int(quantity), "measure": measure.strip()} 
            cook_dict[line.strip()].append(employee) 
        cook_list.readline() 
        cook_book.update(cook_dict) 

print(get_shop_list_by_dishes(["Омлет", "Фахитос"], 3))


content = []

for root, dirs, files in os.walk('c:/Netology/leson_files_r_w/dz_'):
    lln = 0
    for file in files:
        with open(join(root, file), "r", encoding="utf-8") as f:
            raw = f.read()
            ln = len(raw)
            new_raw = f"{file}\n{ln}\n{raw.strip()}\r"
            if ln > lln:
                content.append(new_raw)
            else:
                content.insert(0, new_raw)
            lln = ln

with open('c:/Netology/leson_files_r_w/1_2_3.txt', 'w', encoding="utf-8") as f:
    f.write(" ".join(content))