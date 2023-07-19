#Task 2:
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
#define a function named author_average_reads with one required parameter as a String containing the name of the author we want to query.

#The function will return an Integer representing the average amount of reads an author has in all its Published articles.

#You may use multiple conditionals in if ... elif ... structures.

#You will have to take into account that Reviewers' items do not have a "reads" key. Their average amount should be 0.

#You will also have to take into account Authors with an empty list of items.

#And also make sure the function does not return an error if we type the name of an author that does not exist.

#Remember to base the calculation only on the articles with the status set to Published.

def author_average_reads(author):
    for user in users:
        if user["name"] == author:
            if user["type"] == "Publisher":
                published_items = [item["reads"] for item in user["items"] if item.get("status") == "Published"]
                if len(published_items) == 0:
                    return 0
                else:
                    return sum(published_items) // len(published_items)
            elif user["type"] == "Reviewer":
                return 0
    return 0  # Return 0 if the author doesn't exist

#Use the following test cases:
print("Clark", author_average_reads("Clark"))
print("Peter", author_average_reads("Peter"))
print("Samantha", author_average_reads("Samantha"))
print("Mathilda", author_average_reads("Mathilda"))
print("Mario", author_average_reads("Mario"))