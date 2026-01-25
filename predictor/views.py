from django.shortcuts import render
from .models import Place
from .pricing import estimate_price

BHK_FACTOR = {1:0.9, 2:1.0, 3:1.15, 4:1.3}

def value_for_money(request):
    results = []
    predicted_price = None
    cities, prices = [], []

    if request.method == "POST":
        state = request.POST["state"].title()
        city = request.POST["city"].title()
        area = int(request.POST["area"])
        bhk = int(request.POST["bhk"])

        place = Place.objects.filter(state=state, city=city).first()
        if not place:
            place = Place.objects.create(
                state=state,
                city=city,
                price_per_sqft=estimate_price(city, state)
            )

        factor = BHK_FACTOR.get(bhk, 1.0)
        predicted_price = int(area * place.price_per_sqft * factor)

        all_places = Place.objects.filter(state=state)
        avg_price = sum(p.price_per_sqft for p in all_places) / len(all_places)

        for p in all_places:
            total = int(area * p.price_per_sqft * factor)
            score = round((avg_price - p.price_per_sqft)/avg_price, 2)
            results.append({
                "city": p.city,
                "price_per_sqft": p.price_per_sqft,
                "total_price": total,
                "value_score": score
            })
            cities.append(p.city)
            prices.append(total)

    return render(request, "value.html", {
        "results": results,
        "predicted_price": predicted_price,
        "cities": cities,
        "prices": prices
    })
