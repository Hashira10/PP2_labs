movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

# 1 Write a function that takes a single movie and returns True if its IMDB score is above 5.5

'''
def IMDB(m):
    if m["imdb"] > 5.5:
        return True
    else: 
        return False
# chek
print(IMDB(movies[2]))
# 2 Write a function that returns a sublist of movies with an IMDB score above 5.5.

l = []
def subl(m):
    for i in range(len(m)):
        MOVIE_1 = m[i]
        if MOVIE_1["imdb"] > 5.5:
            l.append(MOVIE_1["name"])
    return l
print(subl(movies))


# 3 Write a function that takes a category name and returns just those movies under that category.

def categ(m,c):
    l = []
    for i in range(len(m)):
        MOVIE_1 = m[i]
        if MOVIE_1["category"] == c:
            l.append(MOVIE_1["name"])
    return l
    
print(categ(movies,"Romance"))

# 4 Write a function that takes a list of movies and computes the average IMDB score.

def average(m):
    ans = 0
    for i in range(len(m)):
        movie = m[i]
        ans += movie["imdb"]
    return ans/len(m)
print(average(movies))
'''

# 5 Write a function that takes a category and computes the average IMDB score.

def average_cat(m,cat):
    ans = 0
    cnt = 0
    for i in range(len(m)):
        movie = m[i]
        if movie["category"] == cat:
            ans += movie["imdb"]
            cnt += 1
    return ans/cnt
print(average_cat(movies, "Romance"))
    
