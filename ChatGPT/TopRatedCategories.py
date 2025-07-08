reviews = [
    {"name": "Joe's Pizza", "category": "Food", "rating": 4},
    {"name": "Sally's Sushi", "category": "Food", "rating": 5},
    {"name": "Taco Town", "category": "Food", "rating": 3},
    {"name": "Techy Spa", "category": "Wellness", "rating": 5},
    {"name": "Relax n’ Go", "category": "Wellness", "rating": 4},
    {"name": "BoxFit", "category": "Fitness", "rating": 4},
]


def top_rated_businesses(reviews):
    result_dictionary = {}

    for review in reviews:
        category_entry = result_dictionary.get(review["category"])
        if not category_entry or review["rating"] > category_entry["rating"]:
            result_dictionary[review["category"]] = review

    result = {}

    for result_entry in result_dictionary.values():
        result[result_entry["category"]] = result_entry["name"]

    return result


def top_rated_businesses_better(reviews):
    result = {}

    for review in reviews:
        category = review["category"]

        if category not in result or review["rating"] > result[category]["rating"]:
            result[category] = review

    return {category: entry["name"] for category, entry in result.items()}


print(top_rated_businesses(reviews))
print(top_rated_businesses_better(reviews))
