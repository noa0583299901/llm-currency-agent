import os
from dotenv import load_dotenv
from smolagents import OpenAIModel, ToolCallingAgent, CodeAgent, DuckDuckGoSearchTool, FinalAnswerTool, tool
from datetime import date


load_dotenv()


@tool
def get_today_date() -> str:
    """Returns today's date in a readable format."""
    return str(date.today())

@tool
def search_exchange_rate(currency_pair: str, target_date: str) -> str:
    """
    Searches for the exchange rate of a currency pair on a specific date.
    Args:
        currency_pair: The pair to look for (e.g., 'USD to ILS').
        target_date: The date to check for the rate.
    """
    search = DuckDuckGoSearchTool()
   
    query = f"exchange rate {currency_pair} on {target_date}"
    return search.forward(query)

@tool
def calculate_conversion(amount: float, rate: float, fee_percentage: float) -> float:
    """
    Calculates the final amount after conversion and fees.
    Args:
        amount: The original amount in source currency.
        rate: The exchange rate found.
        fee_percentage: The bank fee (e.g., 2.5).
    """
    total_before_fee = amount * rate
    total_after_fee = total_before_fee * (1 - (fee_percentage / 100))
    return round(total_after_fee, 2)

final_answer = FinalAnswerTool()


all_tools = [final_answer, get_today_date, search_exchange_rate, calculate_conversion]


model = OpenAIModel(model_id="gpt-4.1-mini") 


agent_code = CodeAgent(model=model, tools=all_tools, max_steps=10)
agent_tools = ToolCallingAgent(model=model, tools=all_tools, max_steps=10)


prompt = """
Step-by-step task:
1. Find out today's date.
2. Search for the current USD to ILS exchange rate for this specific date.
3. Extract the numeric rate from the search results.
4. Using the calculation tool, find how many ILS I will get for 500 USD with a 2.5% fee.
"""



print("--- Running CodeAgent ---")
agent_code.run(prompt)

print("\n--- Running ToolCallingAgent ---")
agent_tools.run(prompt)