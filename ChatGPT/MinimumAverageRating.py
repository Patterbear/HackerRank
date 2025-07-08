reviews = [
    {"name": "Joe's Pizza", "rating": 4},
    {"name": "Joe's Pizza", "rating": 5},
    {"name": "Taco Town", "rating": 2},
    {"name": "Taco Town", "rating": 3},
    {"name": "BoxFit", "rating": 5},
    {"name": "BoxFit", "rating": 5},
    {"name": "BoxFit", "rating": 4},
]

min_avg_rating = 4.5


def popular_businesses(reviews, min_avg_rating):
    business_ratings = {}

    for review in reviews:
        if not business_ratings.get(review["name"]):
            business_ratings[review["name"]] = [review["rating"]]
        else:
            business_ratings[review["name"]].append(review["rating"])

    suitable_businesses = []

    for business, ratings in business_ratings.items():
        if (sum(ratings) / len(ratings)) > min_avg_rating:
            suitable_businesses.append(business)


    return suitable_businesses



print(popular_businesses(reviews, min_avg_rating))