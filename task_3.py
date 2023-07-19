#Task 3:
users = [
    {
        "name": "Clark",
        "type": "Publisher",
        "items": [
            {
                "title": "The ABC of Blockchain",
                "status": "Draft",
                "reads": 10
            }
        ]
    },
    {
        "name": "Peter",
        "type": "Publisher",
        "items": []
    },
    {
        "name": "Samantha",
        "type": "Publisher",
        "items": [
            {
                "title": "The ABC of JavaScript",
                "status": "Published",
                "reads": 3254
            },
            {
                "title": "The XYZ of JavaScript",
                "status": "Published",
                "reads": 226
            }
        ]
    },
    {
        "name": "Mathilda",
        "type": "Reviewer",
        "items": [
            {
                "title": "The ABC of Blockchain",
                "status": "Pending"
            }
        ]
    }
]
# define a function named author_is_popular with one required parameter as a String containing the name of the author we want to query.

#The function will return a Boolean (strictly a type Boolean) indicating if the average number of reads of all Published articles of a particular author is greater than 1000.

#You are NOT allowed to use any if conditionals except when checking for the Published flag.

#You are not allowed to use the author_average_reads function from the previous exercise.


def author_is_popular(author):
    for user in users:
        if user["name"] == author:
            if user["type"] == "Publisher":
                published_items = [item["reads"] for item in user["items"] if item.get("status") == "Published"]
                if len(published_items) == 0:
                    return False
                else:
                    average_reads = sum(published_items) / len(published_items)
                    return average_reads > 1000
    return False  # Return False if the author doesn't exist

#Use the following test cases:

print("Clark", author_is_popular("Clark"))
print("Peter", author_is_popular("Peter"))
print("Samantha", author_is_popular("Samantha"))
print("Mathilda", author_is_popular("Mathilda"))
print("Mario", author_is_popular("Mario"))