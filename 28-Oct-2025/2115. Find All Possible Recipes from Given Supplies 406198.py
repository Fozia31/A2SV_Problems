# Problem: 2115. Find All Possible Recipes from Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/description/

from typing import List

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # Initialize a set with available supplies
        can_make = set(supplies)
        progr = True

        while progr:
            progr = False  
            for i in range(len(recipes)):
                if recipes[i] in can_make:
                    continue
                
                all_ingredient = True
                for ingredient in ingredients[i]:
                    if ingredient not in can_make:
                        all_ingredient = False  
                        break  

                if all_ingredient:  
                    can_make.add(recipes[i])
                    progr = True  

        answer = []
        for i in range(len(recipes)):
            if recipes[i] in can_make:
                answer.append(recipes[i])

        return answer
