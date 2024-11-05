import cohere
from cryptinfluencer.config import COHERE_API_KEY
from cryptinfluencer.prompts import SYSTEM_PROMPT

cohere_client = cohere.ClientV2(COHERE_API_KEY)

def get_llm_response(memory, user_query) :
    response = cohere_client.chat(
    model="command-r-plus-08-2024",
    messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT.format(memory=memory)
            },
            {
                "role": "user",
                "content": f"{user_query}"
            }
        ]
    )

    return response.message.content[0].text