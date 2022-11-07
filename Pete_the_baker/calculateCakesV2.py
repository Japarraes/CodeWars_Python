def cakes(recipe, available):
    
    try:
        return min([available[a]//recipe[a] for a in recipe])
    except:
        return 0