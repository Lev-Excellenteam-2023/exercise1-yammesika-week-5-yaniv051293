def get_recipe_price(prices, optionals=[], **kwargs):
    """
    calculate the price of the recipe
    :param prices: dictionary of the prices of ingredients (for 100 gram)
    :param optionals: list of ingredients not need to buy
    :param kwargs: args -the ingredients and they weight
    :return:
    """
    sum = 0
    for key, value in kwargs.items():
        if key not in optionals:
            price = prices[key] * (value / 100)
            sum += price
    return sum


def main():
    assert (get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100) == 44)
    assert (get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300) == 54)
    assert (get_recipe_price({}) == 0)
    print("All work good")


if __name__ == '__main__':
    main()