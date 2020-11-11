#!/usr/bin/python

from recipe import Recipe
from datetime import datetime


class Book:
    def __init__(self, name, recipes_list):
        if ((isinstance(name, str) is False) or
           (isinstance(recipes_list, dict) is False)):
            raise TypeError("Type Error")
        self.name = name
        self.last_update = datetime.now()
        self.creation_update = datetime.now()
        self.recipes_list = recipes_list

    def get_recipe_by_name(self, name):
        for i in self.recipes_list.values():
            for rec in i:
                if rec.name == name:
                    print(str(rec))
                    return rec
        print("Recipe not found.")

    def get_recipes_by_types(self, recipe_type):
        if recipe_type in ['starter', 'lunch', 'dessert']:
            for i in self.recipes_list[recipe_type]:
                print(i.name)
            return
        print("Invalid type.")

    def add_recipe(self, recipe):
        if isinstance(recipe, Recipe) is False:
            print("Invalid recipe")
            return
        if recipe.recipe_type not in self.recipes_list.keys():
            print("Invalid type")
            return
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now()
