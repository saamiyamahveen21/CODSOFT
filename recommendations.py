
# ---------------- DATASET ----------------
movies = {
    # 🎬 HOLLYWOOD
    "Avengers": (["Action", "Adventure", "Sci-Fi"], 95),
    "Iron Man": (["Action", "Sci-Fi"], 90),
    "Titanic": (["Romance", "Drama"], 92),
    "The Notebook": (["Romance", "Drama"], 88),
    "John Wick": (["Action", "Thriller"], 93),
    "Fast & Furious": (["Action", "Cars"], 89),
    "Interstellar": (["Sci-Fi", "Drama"], 97),
    "The Conjuring": (["Horror", "Thriller"], 91),
    "Jumanji": (["Adventure", "Comedy"], 87),
    "Deadpool": (["Action", "Comedy"], 94),
    "Inception": (["Sci-Fi", "Thriller"], 98),
    "The Dark Knight": (["Action", "Crime", "Drama"], 99),
    "Avatar": (["Sci-Fi", "Adventure", "Fantasy"], 96),

    # 🇮🇳 BOLLYWOOD
    "3 Idiots": (["Comedy", "Drama", "Education"], 96),
    "Dangal": (["Sports", "Drama", "Biography"], 95),
    "PK": (["Comedy", "Drama", "Satire"], 94),
    "Taare Zameen Par": (["Drama", "Family", "Education"], 97),
    "Kabir Singh": (["Romance", "Drama"], 89),
    "Zindagi Na Milegi Dobara": (["Adventure", "Comedy", "Drama"], 93),
    "Chennai Express": (["Comedy", "Action", "Romance"], 88),
    "Drishyam": (["Thriller", "Crime", "Mystery"], 95),
    "Uri: The Surgical Strike": (["Action", "War", "Thriller"], 96),
    "Shershaah": (["Action", "Biography", "War"], 94),

    # 🇮🇳 TOLLYWOOD
    "RRR": (["Action", "Drama", "Historical"], 98),
    "Pushpa: The Rise": (["Action", "Crime", "Drama"], 94),
    "Pushpa 2": (["Action", "Crime", "Thriller"], 97),
    "Baahubali: The Beginning": (["Action", "Drama", "Fantasy"], 96),
    "Baahubali 2": (["Action", "Drama", "Fantasy"], 99),
    "Arjun Reddy": (["Romance", "Drama"], 90),
    "Sita Ramam": (["Romance", "Drama", "War"], 95),
    "Jersey": (["Sports", "Drama"], 92),
    "Eega": (["Fantasy", "Action", "Drama"], 91),
    "Akhanda": (["Action", "Drama", "Mythology"], 93)
}

# ---------------- USER HISTORY ----------------
user_history = ["Avengers", "RRR", "Interstellar"]

# ---------------- INPUT ----------------
def get_user_preferences():
    print("\n🎬 NETFLIX STYLE RECOMMENDER")
    print("=" * 50)

    print("\n💡 Enter genres")
    print("Use space, comma, or +")
    print("Example: Action Comedy Drama\n")

    prefs = input("👉 Your preferences: ").lower()

    if not prefs.strip():
        return ["Action"]

    prefs = prefs.replace("+", " ")
    prefs = prefs.replace(",", " ")

    return [g.title() for g in prefs.split() if g.strip()]

# ---------------- RECOMMENDATION ENGINE ----------------
def recommend_movies(user_prefs):
    results = []

    for movie, (genres, rating) in movies.items():

        match_count = 0
        matched_genres = []

        for g in genres:
            if g.lower() in [x.lower() for x in user_prefs]:
                match_count += 1
                matched_genres.append(g)

        if match_count > 0:

            final_score = match_count + (rating / 100)

            results.append({
                "movie": movie,
                "genres": genres,
                "matched": matched_genres,
                "score": final_score,
                "rating": rating
            })

    results.sort(key=lambda x: x["score"], reverse=True)

    return results

# ---------------- EXPLANATION ----------------
def explain(matched):
    if not matched:
        return ""
    return f"💡 Because you liked {', '.join(matched)}"

# ---------------- MAIN ----------------

def main():

    while True:
        user_prefs = get_user_preferences()

        print("\n🍿 ANALYZING YOUR TASTE...")
        print("🔍 Building recommendations...\n")

        results = recommend_movies(user_prefs)

        print("\n" + "=" * 60)
        print("🎬 YOUR NETFLIX-STYLE RECOMMENDATIONS")
        print("=" * 60)

        if not results:
            print("😕 No matches found. Try different genres!")
        else:
            for r in results[:7]:
                print(f"\n🎥 {r['movie']}")
                print(f"   ⭐ Genres: {', '.join(r['genres'])}")
                print(f"   🎯 Score: {r['score']:.2f}")
                print(f"   ⭐ IMDb Rating: {r['rating']}/100")
                print(f"   {explain(r['matched'])}")
                print("-" * 60)

        print("\n📌 Previously watched:")
        for m in user_history:
            print(f"   ✔ {m}")

        # 🔁 ASK USER TO CONTINUE
        again = input("\n🔄 Do you want to try again? (yes/no): ").lower()

        if again not in ["yes", "y"]:
            print("\n👋 Thanks for using Movie Recommender!")
            break

# ---------------- RUN ----------------
if __name__ == "__main__":
    main()