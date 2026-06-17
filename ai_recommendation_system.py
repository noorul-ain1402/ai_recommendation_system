movies = {
    "Action": [
        {"name": "War", "actor": "Hrithik Roshan"},
        {"name": "Pathaan", "actor": "Shah Rukh Khan"},
        {"name": "Singham", "actor": "Ajay Devgn"}
    ],

    "Romance": [
        {"name": "Dilwale Dulhania Le Jayenge", "actor": "Shah Rukh Khan"},
        {"name": "Veer-Zaara", "actor": "Shah Rukh Khan"},
        {"name": "Jab We Met", "actor": "Shahid Kapoor"}
    ],

    "Comedy": [
        {"name": "3 Idiots", "actor": "Aamir Khan"},
        {"name": "Bhool Bhulaiyaa", "actor": "Akshay Kumar"},
        {"name": "Hera Pheri", "actor": "Akshay Kumar"}
    ],

    "Drama": [
        {"name": "Taare Zameen Par", "actor": "Aamir Khan"},
        {"name": "Dangal", "actor": "Aamir Khan"},
        {"name": "Chhichhore", "actor": "Sushant Singh Rajput"}
    ],

    "Thriller": [
        {"name": "Drishyam", "actor": "Ajay Devgn"},
        {"name": "Andhadhun", "actor": "Ayushmann Khurrana"},
        {"name": "Kahaani", "actor": "Vidya Balan"}
    ]
}

history = []

print("=" * 65)
print("      AI BOLLYWOOD MOVIE RECOMMENDATION SYSTEM")
print("=" * 65)

user_name = input("Enter your name: ")

print(f"\nWelcome {user_name}!")
print("Let's find the perfect Bollywood movie for you!")

while True:

    print("\n" + "=" * 65)
    print("1. Get Movie Recommendations")
    print("2. View Recommendation History")
    print("3. Exit")
    print("=" * 65)

    option = input("Choose an option (1-3): ")

    if option == "1":

        print("\nAvailable Genres:")
        for genre in movies:
            print("•", genre)

        genre_choice = input("\nEnter your favorite genre: ").title()

        if genre_choice in movies:

            favorite_actor = input(
                "Enter your favorite Bollywood actor (optional): "
            ).title()

            print("\nAnalyzing your preferences...")
            print("Generating recommendations...\n")

            recommendations = []

            score = 100

            for movie in movies[genre_choice]:

                match_score = score

                if favorite_actor == movie["actor"].title():
                    match_score += 25

                recommendations.append(
                    (movie["name"], movie["actor"], match_score)
                )

                score -= 10

            recommendations.sort(
                key=lambda x: x[2],
                reverse=True
            )

            print("⭐ Recommended Movies ⭐\n")

            rank = 1

            for movie, actor, score in recommendations:

                print(f"{rank}. {movie}")
                print(f"   Lead Actor : {actor}")
                print(f"   Match Score : {score}%")
                print("-" * 40)

                history.append(movie)

                rank += 1

        else:
            print("Invalid genre selected!")

    elif option == "2":

        print("\nYour Recommendation History")
        print("-" * 40)

        if len(history) == 0:
            print("No recommendations yet.")

        else:
            for i, movie in enumerate(history, start=1):
                print(f"{i}. {movie}")

    elif option == "3":

        print("\nThank you for using the Bollywood Recommendation System!")
        print("Visit again for more movie suggestions. 🎬")
        break

    else:
        print("Invalid option. Please choose between 1 and 3.")