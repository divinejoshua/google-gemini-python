from google import genai
from decouple import config

client = genai.Client(api_key=config("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Explain how AI works in a few words"
)
print(response.text)