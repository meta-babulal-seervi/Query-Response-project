from together import Together
import os 
from dotenv import load_dotenv
import realTimellm

load_dotenv()  

api_Key = os.getenv("API_KEY")  
client = Together(api_key=api_Key)


def classify_intent(user_input):
    categories = {
        "rental": "rental_trends",
        "lease": "rental_trends",
        "price": "purchase_price",
        "buy": "purchase_price",
        "climate": "climate",
        "weather": "climate",
        "ROI": "financial_analysis",
        "payback": "financial_analysis",
        "legal": "legal_guidelines",
        "law": "legal_guidelines",
        "translate": "document_translation",
        "interpret": "document_translation",
        "fun": "location_activities",
        "things to do": "location_activities"
    }
    for keyword, category in categories.items():
        if keyword.lower() in user_input.lower():
            return category
    return "other"




def getResponse(user_input):
    intent = classify_intent(user_input)

    # Determine if real-time data is needed
    real_time_categories = [
        "rental_trends", "purchase_price", "climate",
        "legal_guidelines", "location_activities"
    ]
    needs_real_time = intent in real_time_categories 
    if needs_real_time:
        # Use Perplexity to get real-time info
        real_time_info = realTimellm.get_live_data_with_perplexity(user_input ,client)

        # Final prompt to LLaMA with context
        enhanced_prompt = f"""
            As a professional real estate agent, your job is to assist clients with insightful, data-informed responses.

            ---

            **Client's Inquiry:**  
            \"\"\"{user_input}\"\"\"

            **Relevant Real-Time Data (e.g., market trends, weather, nearby amenities):**  
            {real_time_info}

            ---

            Using the above information, craft a clear and concise response in **Markdown**. Be friendly, professional, and informative. 
            Tailor the answer as if you're guiding a client who is considering buying, selling, or renting a property. Provide helpful
            context and actionable advice where possible.
            """

    else:
        enhanced_prompt = f"""
            You are a helpful and professional real estate agent assisting a client.

            Client's Question:  
            {user_input}

            Please respond clearly and concisely as if you're guiding a home buyer or renter. Use any relevant real-time information if available.

            Format your answer in **Markdown**.
            """


    # Final response from LLaMA
    response = client.chat.completions.create(
        # model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
        model="meta-llama/Llama-Guard-4-12B",
        messages=[{"role": "user", "content": enhanced_prompt}]
    )

    return response.choices[0].message.content.strip()
