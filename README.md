# Python logical expressions

## Description

In this exercise, we will practice some more on complex logical expressions.

##

## Collection Basic

## List

A list is a built-in data structure that represents an ordered collection of items. Lists can be stored in variables just like Strings can. For example to store a list of car brands you could create a variable `car_brands` with a list of brands like `'BMW'`, `'Audi'`, and `'Volkswagen'`. This translates to the following code:

```python
car_brands = ['BMW', 'Audi', 'Volkswagen']
```

Elements in this list can be accessed by zero-based, numbered indices. For example `car_brands[0]` would return `BMW`.

To work with all elements in a list you can loop over its elements and for example print them like this:

```python
for brand in car_brands:
  print(brand)
```

Lists can also be altered. Elements can be added using the `append` method:

```python
car_brands.append('Volvo')
```

Using indices elements can also be removed from a list again using the `pop` method:

```python
car_brands.pop(0)
```


## Dictionary

A dictionary is a built-in data structure that represents a collection of key-value pairs. Dictionaries (also called dicts) of course can also be stored in variables. For example let's store fruits, grouped by their color:

```python
fruits = {
  'red': ['apple', 'cherry', 'strawberry'],
  'orange':['orange', 'mango', 'peach'],
  'yellow': ['banana', 'lemon']
}
```

Elements in this dictionary can be accessed by keys which are Strings. For example all red fruits can be accessed using `fruits['red']`. The nested value `apple` could be accessed using `fruits['red'][0]`.

To add an element to or update one in a dictionary you can use the key syntax as well or use the `update` method:

```python
fruits['green'] = ['watermelon']
fruits.update({'green': ['watermelon']})
```

To remove an element from a dictionary one can use the `pop` method with a specified key. For example to remove all yellow fruits:

```python
fruits.pop('yellow')
```

You can also loop over dictionaries like you can loop over lists using the `items` method:

```python
for color, colored_fruits in fruits.items()
  print(color + ' fruits:')
  for fruit in colored_fruits:
    print('- ' + fruit)
```

##

## Tasks

###

### Task 1:

We will now use the following list of users in a blog site:

```
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
```

Define a function named `has_hits` with one required parameter as a `String` containing the name of the author we want to query.

The function will return a Boolean (strictly of type `Boolean`) indicating if that author has any hit article.

> An article is a hit if it has more than 1000 reads.

Use the following test cases:

```
print("Clark", has_hits("Clark"))
print("Peter", has_hits("Peter"))
print("Samantha", has_hits("Samantha"))
print("Mathilda", has_hits("Mathilda"))
print("Mario", has_hits("Mario"))
```
- Your result should look like this:

```
Clark False
Peter False
Samantha True
Mathilda False
Mario False
```

###

### Task 2:

Using the same list of users, now define a function named `author_average_reads` with one required parameter as a `String` containing the name of the author we want to query.

The function will return an `Integer` representing the average amount of reads an author has in all its `Published` articles.

> You may use multiple conditionals in `if ... elif ...` structures.

> You will have to take into account that Reviewers' items do not have a "reads" key. Their average amount should be 0.

> You will also have to take into account Authors with an empty list of items.

> And also make sure the function does not return an error if we type the name of an author that does not exist.

> Remember to base the calculation only on the articles with the `status` set to `Published`.

Use the following test cases:

```
print("Clark", author_average_reads("Clark"))
print("Peter", author_average_reads("Peter"))
print("Samantha", author_average_reads("Samantha"))
print("Mathilda", author_average_reads("Mathilda"))
print("Mario", author_average_reads("Mario"))
```
- Your result should look like this:

```
Clark 0
Peter 0
Samantha 1740
Mathilda 0
Mario 0
```

###

### Task 3:

Using the same list of users, now define a function named `author_is_popular` with one required parameter as a `String` containing the name of the author we want to query.

The function will return a `Boolean` (strictly a type `Boolean`) indicating if the average number of reads of all `Published` articles of a particular author is greater than 1000.

> You are NOT allowed to use any `if` conditionals except when checking for the `Published` flag.

> You are not allowed to use the `author_average_reads` function from the previous exercise.


Use the following test cases:

```
print("Clark", author_is_popular("Clark"))
print("Peter", author_is_popular("Peter"))
print("Samantha", author_is_popular("Samantha"))
print("Mathilda", author_is_popular("Mathilda"))
print("Mario", author_is_popular("Mario"))
```
- Your result should look like this:

```
Clark False
Peter False
Samantha True
Mathilda False
Mario False
```
