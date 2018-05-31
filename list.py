import sys
import json

def open_shopping_list():
    try:
        with open('shopping_list.json', 'r') as list_file:
            shopping_list = json.load(list_file)
    except:
        shopping_list = {"items":{}, "menu":{}}

    return shopping_list

def open_recipe_book():
    try:
        with open('recipe_book.json', 'r') as recipe_book_json:
            recipe_book = json.load(recipe_book_json)
    except:
        recipe_book = {}
    return recipe_book

def create_list():
    shopping_list = {"items":{}, "menu":{}}
    with open('shopping_list.json', 'w') as list_file:
        json.dump(shopping_list, list_file)

def add_to_list(item, quantity=None):
    shopping_list = open_shopping_list()
    if quantity is None:
        quantity = 1
    try:
        shopping_list["items"][item] = quantity + shopping_list["items"][item]
    except:
        shopping_list["items"][item] = quantity
    with open('shopping_list.json', 'w+') as list_file:
        json.dump(shopping_list, list_file)

def remove_from_list(item, quantity=None):
    shopping_list = open_shopping_list()
    try:
        if (quantity is None) or (quantity > shopping_list["items"][item]):
            del shopping_list["items"][item]
        else:
            shopping_list["items"][item] = shopping_list["items"][item] - quantity
    except:
        return
    with open('shopping_list.json', 'w+') as shopping_list_json:
        json.dump(shopping_list, shopping_list_json)


def create_recipe(name):
    recipe_book = open_recipe_book()
    new_recipe = {}
    while True:
        ingredient = input("Add ingredient: ")
        if ingredient == "":
            break
        else:
            try:
                quantity = input("How many? ")
            except:
                quantity = 1
            new_recipe[ingredient] = int(quantity)

    print(new_recipe)
    recipe_book[name] = new_recipe
    print(recipe_book)
    print(type(recipe_book))
    with open('recipe_book.json', 'w+') as recipe_book_json:
        json.dump(recipe_book, recipe_book_json)

def add_recipe_to_list(name):
    shopping_list = open_shopping_list()
    recipe_book = open_recipe_book()
    if recipe_book == {}:
        return
    shopping_list["items"] = {key : shopping_list["items"].get(key, 0) + recipe_book[name].get(key,0) 
        for key in set(shopping_list["items"]) | set(recipe_book[name])}
    try:
        shopping_list["menu"][name] = shopping_list["menu"][name] + 1 
    except:
        shopping_list["menu"][name] = 1 
    with open('shopping_list.json', 'w+') as shopping_list_json:
        json.dump(shopping_list, shopping_list_json)

def remove_recipe_from_list(name):
    shopping_list = open_shopping_list()
    recipe_book = open_recipe_book()
    if recipe_book == {}:
        return
    try:
        shopping_list["menu"][name] = shopping_list["menu"][name] - 1 
        shopping_list["items"] = {key : shopping_list["items"].get(key, 0) - recipe_book[name].get(key,0) 
                for key in set(shopping_list["items"]) | set(recipe_book[name])}
    except:
        return
    for key in set(shopping_list["items"]):
        if shopping_list["items"][key] < 1:
            del shopping_list[key]
    if shopping_list["menu"][name] == 0:
        del shopping_list["menu"][item]
    with open('shopping_list.json', 'w+') as shopping_list_json:
        json.dump(shopping_list, shopping_list_json)
    

def delete_recipe(name):
    recipe_book = open_recipe_book()
    try:
        del recipe_book[name]
    except:
        return
    with open('recipe_book.json', 'w+') as recipe_book_json:
        json.dump(recipe_book, recipe_book_json)


#create a new list
if sys.argv[1] == "clear":
    create_list()

#add to list, optionally with a quantity
elif sys.argv[1] == "add":
    if len(sys.argv) > 3:
        add_to_list(sys.argv[3], int(sys.argv[2]))
    else:
        add_to_list(sys.argv[2])

#remove from list, optionally with a quantity
elif sys.argv[1] == "remove":
    if len(sys.argv) > 3:
        remove_from_list(sys.argv[3], int(sys.argv[2]))
    else:
        remove_from_list(sys.argv[2])

#add a recipe to the list
elif sys.argv[1] == "add-recipe":
    add_recipe_to_list(sys.argv[2])

#remove a recipe from the list
elif sys.argv[1] == "remove-recipe":
    remove_recipe_from_list(sys.argv[2])

#create a new recipe
elif sys.argv[1] == "create-recipe":
    create_recipe(sys.argv[2])

#delete a recipe
elif sys.argv[1] == "delete-recipe":
    delete_recipe(sys.argv[2])

