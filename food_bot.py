import requests

class FoodRecommendationBot:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_recommendations(self, query, number=5):
        url = f"https://api.spoonacular.com/food/products/search?query={query}&number={number}&apiKey={self.api_key}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if 'products' in data:
                recommendations = [product['title'] for product in data['products']]
                return recommendations
            else:
                return []
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return []

if __name__ == "__main__":
    api_key = 'b8e473f0c34d4f858e1785a7bd4d1126'  # Replace with your actual API key
    bot = FoodRecommendationBot(api_key)

    print("Bot: Hi there! I'm your Enhanced Conversation Bot.")
    print("Bot: You can ask me for food recommendations or chat about anything.")
    print("Bot: Feel free to say 'recommendation' or 'food' to get started.")
    print("Bot: Type 'exit' to quit the bot.")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ['hi', 'hello', 'hey']:
            print("Bot: Hello! How can I assist you today?")
        elif 'who are you' in user_input.lower():
            print("Bot: I'm your Food Recommendation Bot. I can help you discover delicious food options.")
        elif 'why' in user_input.lower():
            print("Bot: I'm here to make your food choices easier and more enjoyable.")
        elif 'how are you' in user_input.lower():
            print("Bot: I'm just a bot, but thanks for asking!")
        elif 'thanks' in user_input.lower():
            print("Bot: You're welcome! If you need more help, just let me know.")
        elif 'welcome' in user_input.lower():
            print("Bot: Thank you! Let's get started.")
        elif user_input.lower() == 'exit':
            print("Bot: Exiting the bot. Goodbye!")
            break
        elif 'recommendation' in user_input.lower() or 'food' in user_input.lower():
            print("Bot: Sure! Let me find some food recommendations for you.")
            query = input("Bot: What type of food are you looking for? ")
            recommendations = bot.get_recommendations(query)
            if recommendations:
                print("Bot: Here are some recommendations for you:")
                for idx, title in enumerate(recommendations, 1):
                    print(f"{idx}. {title}")
            else:
                print("Bot: Sorry, I couldn't find any recommendations for that.")
        else:
            print("Bot: Sorry, I'm not programmed to chat about that. Let's talk about food recommendations!")
