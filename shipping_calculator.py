def calculate_shipping(weight_kg, distance_km, express=False):
    base_rate = 2.5
    rate_per_kg = 1.2
    rate_per_km = 0.05
    express_multiplier = 1.8 if express else 1.0
    cost = (base_rate + weight_kg * rate_per_kg + distance_km * rate_per_km)
    return round(cost * express_multiplier, 2)
