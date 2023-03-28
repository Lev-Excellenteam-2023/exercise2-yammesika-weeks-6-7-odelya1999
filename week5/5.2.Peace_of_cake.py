# -- Peace of cake -- #
def get_recipe_price(prices, optionals=None, **ingredients):
    """
    :param prices: A dictionary of ingredients needed to make a certain recipe.
    :param optionals: A list of components that we will ignore, meaning - we will not buy from them at all.
    :param ingredients: The name of the ingredient and the amount of the ingredient in grams that we would like to buy
    for the recipe.
    :return: Return the final price for buying all ingredients
    """
    final_price = 0
    for product, amount in ingredients.items():
        if not optionals or product not in optionals:
            product_price = prices.get(product)
            total_product_price = product_price * (amount / 100)
            final_price += total_product_price
    return int(final_price)


if __name__ == '__main__':
    # -- Peace of cake -- #
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
    print(get_recipe_price({}))
