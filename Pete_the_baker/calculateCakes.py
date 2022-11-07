def cakes(recipe, available):
    
    cakes = -1

    for key_recipe in recipe:
        
        value_recipe = recipe.get(key_recipe)
        value_ingredient = available.get(key_recipe, -1)

        # Verify if there are enough quantity of each ingredients
        if (value_recipe > value_ingredient):
            return 0

        # Obtein how many times recipe is in ingredients
        if (value_recipe > 0):
            ratio = value_ingredient // value_recipe
            if (cakes < 0):
                cakes = ratio
            else:
                cakes = min(cakes, ratio)
    
    return cakes