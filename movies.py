# create empty list
movies=[]


# create main loop
def menu():
    print("===The Movie List App by Heidi Bada===")
    
    user_input = input("\nEnter 'a' to add a movie, 'l' to list your movies, 'f' to find a movie, and 'q' to quit: ")
 
    while user_input !='q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movie(movies)
        elif user_input == 'f':
            find_movie()
        else:
            print("Thanks for using this app")
 
        user_input = input("\nEnter 'a' to add a movie, 'l' to list your movies, 'f' to find a movie, and 'q' to quit: ")
 
def add_movie():
    name = input("\nEnter the name of the movie: ")
    review = input("Add your review: ")
    rating = input("Enter your rating, 0 to 5: ")
 
    movies.append({
        'name': name,
        'review': review,
        'rating': rating
    })
    

def show_movie(movies_list):
    for movie in movies_list:
        show_movie_details(movie)

 
def show_movie_details(movie):
    print(f"\nName:{movie['name']}")
    print(f"Review:{movie['review']}")
    print(f"Rating:{movie['rating']}")


def find_movie():
    print('\nYou can search for name, review, or rating.')
    find_by = input("What property do you want to search by? ")
    looking_for = input("\nWhat are you searching for? ")
    found_movies = find_by_attribute(movies, looking_for, lambda x: x[find_by])
    show_movie(found_movies)

 
def find_by_attribute(items, expected, finder):
    found = []
    for i in items:
        if finder(i) == expected:
            found.append(i)
    return found
 
 
menu()
