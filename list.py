import sys
import json

def open_shopping_list():
    try:
        with open('shopping_list.json', 'r') as list_file:
            shopping_list = json.load(list_file)
    except:
        shopping_list = {}

    return shopping_list

def open_recipe_book():
    try:
        with open('recipe_book.json', 'r') as recipe_book_json:
            recipe_book = json.load(recipe_book_json)
    except:
        recipe_book = {}
    return recipe_book

def create_list():
    shopping_list = {}
    with open('shopping_list.json', 'w') as list_file:
        json.dump(shopping_list, list_file)

def add_to_list(item, quantity=None):
    shopping_list = open_shopping_list()
    if quantity is None:
        quantity = 1
    shopping_list[item] = int(quantity)
    with open('shopping_list.json', 'w+') as list_file:
        json.dump(shopping_list, list_file)

def create_recipe(name):
    recipe_book = open_recipe_book()
    new_recipe = {}
    while True:
        ingredient = input("Add ingredient: ")
        if ingredient == "":
            break
        else:
            try:
                quantity = int(input("How many? "))
            except:
                quantity = 1
            print(quantity)
            print(type(quantity))
            new_recipe[ingredient] = quantity

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
    shopping_list_new = {key : shopping_list.get(key, 0) + recipe_book[name].get(key,0) 
            for key in set(shopping_list) | set(recipe_book[name])}
    with open('shopping_list.json', 'w+') as shopping_list_json:
        json.dump(shopping_list_new, shopping_list_json)

def delete_recipe(name):
    recipe_book = open_recipe_book()
    try:
        del recipe_book[name]
    except:
        return
    with open('recipe_book.json', 'w+') as recipe_book_json:
        json.dump(recipe_book, recipe_book_json)


if sys.argv[1] == "clear":
    create_list()
elif sys.argv[1] == "add":
    add_to_list(sys.argv[3], sys.argv[2])
elif sys.argv[1] == "add-recipe":
    add_recipe_to_list(sys.argv[2])
elif sys.argv[1] == "create-recipe":
    create_recipe(sys.argv[2])
elif sys.argv[1] == "delete-recipe":
    delete_recipe(sys.argv[2])

