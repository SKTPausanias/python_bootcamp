#!/usr/bin/python

import sys

cookbook = {'sandwich': {'ingredients': ["ham", "bread", "cheese", "tomatoes"], 'meal': 'lunch', 'prep_time': '10'},
                'cake': {'ingredients': ["flour", "sugar", "eggs"], 'meal': 'dessert', 'prep_time': '60'},
                'salad': {'ingredients': ["avocado", "arugula", "tomatoes", "spinach"], 'meal': 'lunch', 'prep_time': '15'}
}

def print_menu():
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")


def add_recipe(recipe_name, ingredients, meal_type, prep_time):
    cookbook[recipe_name] = {}
    cookbook[recipe_name]['ingredients'] = ingredients
    cookbook[recipe_name]['meal'] = meal_type
    cookbook[recipe_name]['prep_time'] = prep_time


def print_recipe(recipe_name):
    bol = False
    for i in cookbook:
        if (i == recipe_name):
            print("Recipe for", recipe_name + ":\n")
            print("Ingredients list:", cookbook[i]['ingredients'])
            print("To be eaten for", cookbook[i]['meal'] + ".")
            print("Takes", cookbook[i]['prep_time'], "minutes of cooking.\n")
            bol = True
    if bol is False:
        print("\nCant find that recipe!\n")


def delete_recipe(recipe_name):
    bol = False
    for i in cookbook:
        if (i == recipe_name):
            bol = True
            break
    if bol is True:
        print("\nrecipe deleted!\n")
        del cookbook[i]
    else:
        print("\nCant find that recipe!\n")


def print_cookbook():
    for i in cookbook:
        print_recipe(i)


while 1:
    print_menu()
    n = input(">> ")
    if n == '1':
        name, ingr, meal_type, prep_time = input("enter details <name>(example->salad) <ingr>(example->['ham','cheese']) <meal_type>(example->lunch) <prep_time>(example->10) ").split()
        add_recipe(name, ingr, meal_type, prep_time)
    elif n == '2':
        name = input("enter recipe name to delete >> ")
        delete_recipe(name)
    elif n == '3':
        name = input("enter recipe name to print >> ")
        print_recipe(name)
    elif n == '4':
        print_cookbook()
    elif n == '5':
        print("\nCookbook closed")
        sys.exit(0)
    else:
        print("\nThis option does not exist, please type the corresponding number.")
        print("To exit, enter 5.\n")
