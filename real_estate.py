def calculate_sqm_price(price, area):
    return price / area

apartments = [
    {"price": 15000, "area": 50},
    {"price": 60000, "area": 50},
    {"price": 62500, "area": 50},
    {"price": 84500, "area": 65},
    {"price": 850000, "area": 100}
]

# Faza 1: Calibrarea radarului (pe date sterile)
apartments.sort(key=lambda x: calculate_sqm_price(x["price"], x["area"]))
core = apartments[1:-1]

clean_prices = []
for apt in core:
    clean_prices.append(calculate_sqm_price(apt["price"], apt["area"]))

area_average = sum(clean_prices) / len(clean_prices)
alert_threshold = area_average * 0.8
overpriced_threshold = area_average * 1.2

print(f"Area average: {area_average} EUR/sqm")
print(f"Alert threshold: {alert_threshold} EUR/sqm\n")

# Faza 2: Scanarea pieței (pe baza de date completă)
underpriced_apartments = []
overpriced_apartments = []

for apt in apartments:
    sqm_price = calculate_sqm_price(apt["price"], apt["area"])
    
    if sqm_price < alert_threshold:
        underpriced_apartments.append(apt)
        print(f"ALERT: OPPORTUNITY - {sqm_price} EUR/sqm")
    elif sqm_price > overpriced_threshold:
        overpriced_apartments.append(apt)
        print(f"ALERT: OVERPRICED - {sqm_price} EUR/sqm")
    else:
        print(f"NORMAL - {sqm_price} EUR/sqm")