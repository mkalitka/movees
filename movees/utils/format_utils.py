def format_movie(movie):
    movie = movie["movie"]
    people = ""
    for person in movie["people"]:
        people += f"{person['name']} as {person['role']}, "
    people = people[:-2]
    if people == "":
        return f"    {movie['title']} ({movie['year']})"
    return f"    {movie['title']} ({movie['year']}) by {people}"


def format_person(person):
    person = person["person"]
    output = f"    {person['name']}:"
    if len(person["movies"]) == 0:
        output += "\n        No movies."
    else:
        for movie in person["movies"]:
            output += f"\n        {movie['title']} ({movie['year']}) as {movie['role']}"
    return output
