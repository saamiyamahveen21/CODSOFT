from datetime import datetime

def get_response(msg):

    msg = msg.lower()

    # 👋 Greetings
    greetings = ["hi", "hello", "hey"]

    if any(word in msg for word in greetings):
        return "Hello 👋 Welcome to AFS Diner 🇮🇳🍽️"

    # 📋 Menu with Prices
    elif "menu" in msg:
        return """
🍽️ OUR MENU 🍽️

🍛 BIRYANI
1. Chicken Biryani → ₹299
2. Mutton Biryani → ₹399
3. Egg Biryani → ₹229
4. Paneer Biryani → ₹249
5. Veg Biryani → ₹199

🍗 MAIN COURSE
6. Butter Chicken → ₹349
7. Kadai Chicken → ₹329
8. Paneer Butter Masala → ₹259
9. Dal Tadka → ₹179

🍚 RICE & NOODLES
10. Fried Rice → ₹199
11. Jeera Rice → ₹149
12. Hakka Noodles → ₹189

🍕 FAST FOOD
13. Pizza → ₹299
14. Burger → ₹179
15. Shawarma → ₹149
16. Momos → ₹129
17. Sandwich → ₹139
18. French Fries → ₹119
19. Tacos → ₹229

🍝 ITALIAN
20. White Sauce Pasta → ₹239
21. Red Sauce Pasta → ₹229
22. Garlic Bread → ₹129

🥤 DRINKS & DESSERTS
23. Cold Coffee → ₹149
24. Milkshake → ₹169
25. Lassi → ₹99
26. Cappuccino → ₹149
27. Green Tea → ₹89
28. Soft Drinks → ₹59
29. Chocolate Cake → ₹179
30. Ice Cream → ₹99
"""

    # 🍛 Biryani Pattern Matching
    elif "biryani" in msg:

        if "chicken" in msg:
            return "🍛 Chicken Biryani costs ₹299"

        elif "mutton" in msg:
            return "🥘 Mutton Biryani costs ₹399"

        elif "egg" in msg:
            return "🥚 Egg Biryani costs ₹229"

        elif "paneer" in msg:
            return "🧀 Paneer Biryani costs ₹249"

        elif "veg" in msg:
            return "🥦 Veg Biryani costs ₹199"

        else:
            return """
We have these biryanis 🍛

1. Chicken Biryani → ₹299
2. Mutton Biryani → ₹399
3. Egg Biryani → ₹229
4. Paneer Biryani → ₹249
5. Veg Biryani → ₹199
"""

    # 💰 Food Price Pattern Matching
    food_prices = {
        "butter chicken": "🍗 Butter Chicken costs ₹349",
        "chicken 65": "🍢 Chicken 65 costs ₹249",
        "fried rice": "🍚 Fried Rice costs ₹199",
        "noodles": "🍜 Hakka Noodles cost ₹189",
        "pizza": "🍕 Pizza costs ₹299",
        "burger": "🍔 Burger costs ₹179",
        "shawarma": "🌯 Shawarma costs ₹149",
        "momos": "🥟 Momos cost ₹129",
        "sandwich": "🥪 Sandwich costs ₹139",
        "fries": "🍟 French Fries cost ₹119",
        "tacos": "🌮 Tacos cost ₹229",
        "naan": "🫓 Butter Naan costs ₹49",
        "paneer butter masala": "🍛 Paneer Butter Masala costs ₹259",
        "kadai chicken": "🥘 Kadai Chicken costs ₹329",
        "dal tadka": "🍲 Dal Tadka costs ₹179",
        "jeera rice": "🍚 Jeera Rice costs ₹149",
        "salad": "🥗 Caesar Salad costs ₹159",
        "white sauce pasta": "🍝 White Sauce Pasta costs ₹239",
        "red sauce pasta": "🍝 Red Sauce Pasta costs ₹229",
        "garlic bread": "🧀 Garlic Bread costs ₹129",
        "cold coffee": "🥤 Cold Coffee costs ₹149",
        "milkshake": "🧋 Milkshake costs ₹169",
        "lassi": "🥛 Lassi costs ₹99",
        "cake": "🍰 Chocolate Cake costs ₹179",
        "ice cream": "🍨 Ice Cream costs ₹99",
        "cappuccino": "☕ Cappuccino costs ₹149",
        "green tea": "🍵 Green Tea costs ₹89",
        "soft drink": "🥤 Soft Drinks cost ₹59",
        "soft drinks": "🥤 Soft Drinks cost ₹59"
    }

    for food, response in food_prices.items():
        if food in msg:
            return response

    # 🛵 Ordering
    order_words = ["order", "buy"]

    if any(word in msg for word in order_words):
        return """
You can order food in 3 ways 😊

1. Official Restaurant Website 🌐
2. Swiggy 🛵
3. Zomato 🍽️
"""

    # 🍽️ Table Booking
    booking_words = ["book", "table", "reservation"]

    if any(word in msg for word in booking_words):
        return """
🍽️ Table Booking Available!

📞 Call us at: +91 98765 43210
🕒 Booking Time: 10 AM - 11 PM
👨‍👩‍👧 Family tables available
"""

    # 🕒 Restaurant Timings
    timing_words = ["timing", "timings", "open", "closing", "hours"]

    if any(word in msg for word in timing_words):
        return """
🕒 AFS Diner Timings

🍽️ Monday - Friday : 10 AM - 11 PM
🍽️ Saturday - Sunday : 9 AM - 12 AM

✅ Dine-In Available
✅ Online Orders Available
"""

    # ⏰ Current Time
    if "time" in msg:
        return "⏰ Current time is " + datetime.now().strftime("%H:%M:%S")

    # 😊 Thanks
    thank_words = ["thank", "thanks"]

    if any(word in msg for word in thank_words):
        return "You're welcome 😊"

    # 👋 Bye
    bye_words = ["bye", "exit"]

    if any(word in msg for word in bye_words):
        return "Thanks for visiting AFS Diner ❤️"

    # ❌ Default Response
    else:
        return f"Sorry 😅 {msg.title()} is currently not available at AFS Diner."