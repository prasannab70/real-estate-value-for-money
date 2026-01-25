def estimate_price(city, state):
    base_price = 5000
    return base_price + (len(city) * 100) + (len(state) * 150)
