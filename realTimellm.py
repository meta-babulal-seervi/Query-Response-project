# ---  Get real-time data from Perplexity if needed ---
def get_live_data_with_perplexity(user_input , client):
    prompt = f"""
        You are an AI assistant acting as a knowledgeable real estate agent with access to real-time information.

        Client's Question:  
        \"\"\"{user_input}\"\"\"

        Use current market data, weather, local amenities, or property listings—whichever is relevant—to answer clearly and professionally. Add any insights that could help the client make a decision.

        Respond in **Markdown** format.
        """

    response = client.chat.completions.create(
        model="perplexity-ai/r1-1776",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()