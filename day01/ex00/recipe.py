#!/usr/bin/python

class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time,
                 ingredients, description, recipe_type):
        if ((isinstance(name, str) is False) or
           (isinstance(cooking_lvl, int) is False) or
           (isinstance(cooking_time, int) is False) or
           (isinstance(ingredients, list) is False) or
           (isinstance(description, str) is False) or
           (isinstance(recipe_type, str) is False)):
            raise TypeError("Type Error")
        for i in ingredients:
            if isinstance(i, str) is False:
                raise TypeError("Type Error")
        if (not name or not recipe_type or '' in ingredients):
            raise Exception("empty string")
        if (cooking_lvl < 1 or cooking_lvl > 5):
            raise Exception("invalid cooking_lvl")
        if (cooking_time < 1):
            raise Exception("invalid cooking time")
        if (recipe_type != "starter" and recipe_type != "lunch" and recipe_type != "dessert"):
            raise Exception("invalid recipe type")
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        txt = ""
        txt += self.name + " (" + self.recipe_type + ") : " + self.description
        txt += " | cooking level = " + str(self.cooking_lvl) + " | cooking time "
        txt += str(self.cooking_time) + " | necessary ingredients : "
        for i in self.ingredients:
            txt += i + " "
        return txt
