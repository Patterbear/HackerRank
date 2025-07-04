def matchingStrings(stringList, queries):
    results = []

    for query in queries:
        results.append(stringList.count(query))

    return results
