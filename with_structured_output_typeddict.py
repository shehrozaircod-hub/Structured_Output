from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = ChatOpenAI(model_name="gpt-5")


# schema
class Review(TypedDict):
    summary: str
    sentiment: str

structured_model = model.with_structured_output(Review)


result = structured_model.invoke(""""
                      The hardware is great, but the software feels bloated. There are
                      too many pre-installed apps that I never use, and
                      they just take up space and slow down the system. I wish there
                      was a way to customize the software more to my liking.
                      """)

print(result)
print(f"Summary: {result['summary']}")
print(f"Sentiment: {result['sentiment']}")