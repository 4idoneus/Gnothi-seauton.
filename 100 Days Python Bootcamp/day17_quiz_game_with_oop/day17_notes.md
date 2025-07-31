Classes in python usually  name like this: FirstName ---> This called PascalCase.

Camel case is different from pascal when you're first naming something first word's first letter is lower after that the other words first letter should be written with upper case. We don't usually use camelCase in python.

Snake case is the casing system we all love and use. snake_case. This is mostly used when we are naming variables or functions.

### Constractor
A part of the class creation that tell u s about the class objects requirements like when we crate a user it should have name, id, mail ect.
This is also knows as initializing. Which basically means when start this object have these.
To create constractor we use special function " \_\_init__(self)"
    
```
def __init__(self):
    #initialise attributes
--------------------------------------------------------
class Game:    
    def __init__(self -> object itself, atribute1 -> what we want to have in this object, attribute2 ...)
        self.attribute1 = attribute1
        self.attribute2 = attribute2
            .
            .
            .
        #You can add as many things you want.

game_1 = Game("001","Baldur'Gate 3", ...)
game_2 = Game("002", "Expedition 33", ...)
```

You can also set some attributes to the default so when we create an object and the attribute that object is not something we can give from the start.
```
class Game:    
def __init__(self -> object itself, attribute1, attribute2)
    self.attribute1 = attribute1
        self.attribute2 = attribute2
        self.attribute3 = 0
        
``` 

#### Example from the class
```    
class User:
    def __init__(self,user_id, username):
        print("A new user being created...")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        
    def follow(self,user):
        user.followers += 1
        self.following += 1

user_1 = User("001","Ai")
user_2 = User("002","Le")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
```
#### Two Different ways to write same code but what is their differences?
```
for question in question_data:
    question_bank.append(Question(question_data[i]["text"],question_data[i]["answer"]))
```
This is the first code. I wrote this to get the text and its answer's from a list which store these as a dictionary.

- Extracts text and answer,
- Creates a Question object,
- And fills question_bank with them.
>There is way compact way to write this:
> ```
> question_bank = [Question(q["text"], q["answer"]) for q in question_data]
> ```
>

This is another way to write it:
```
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)
```
They do the same job so what is their differences:

| Feature     | 	Long Version                            | Compact Version             |
|-------------|------------------------------------------|-----------------------------|
| Readability | 	👍 Easy to read, great for beginners    | 👎 Less readable if complex |
| Efficiency  | 	👎 Slightly slower (usually negligible) | 👍 Often faster             |
| Flexibility | 👍 Easy to expand with logic             | 👎 Hard to expand cleanly   |
| Best for    | Complex logic, learning                  | Simple transformations      |
##### Which is the preferred way?
- For simple operations, the compact version is generally preferred by experienced Python developers because it's clean and efficient.

    ✅ Use list comprehension when:

    - You're just transforming data from one format to another.

    - No extra logic (like conditionals or logging) is needed.

- For more complex logic, the long version is preferred.

    ✅ Use the long version when:

    - You need to add conditions (if/else).

    - You want to handle exceptions or log values.

    - Readability is more important than brevity.