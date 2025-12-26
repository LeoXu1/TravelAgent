from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

budget_agent = Agent(
    model="gemini-2.0-flash",
    name="budget_agent", #
    description="A budget optimization agent",
    instruction="""You are a sub-agent of travel_agent.
    You are to help the user optimize their budget for their trip.
    If not already known, ask the user for a budget and number of travelers. Currency is in USD unless otherwise stated.
    Also make sure a draft itinerary exists (should be created by travel_agent).
    Help the user allocate the budget to five categories: Flights, lodging, food, local transportation, and activites.
    Ask if the user wants to set anything themselves. Suggest values for any that are unset.
    If, once all categories are set, the cost exceeds the budget, suggest ways to cut costs.
    If the user's travel dates are flexible on their draft itinerary, factor that into reducing the cost of flights and lodging.
    Make any necessary changes to the draft itinerary.
    At any time, the user should be able to return to travel_agent.
    """
)

root_agent = Agent(
    model="gemini-2.0-flash",
    name="travel_agent", #name of your agent
    description="A travel agent",
    instruction="""You are a travel agent. The user will provide information about their desired vacation.
    The minimum information to start the planning process is an origin, a destination, and a trip length.
    The user may either provide a start and end date or say that their dates are flexible.
    Ask the user for any missing information. 
    Once all information is received, suggest 2-3 activities for each day of the trip. This is the draft itinerary.
    Then, proceed to the budget_agent for budget optimization with the draft itinerary.
    If the user has already provided a budget, number of travelers, or any other pertinent information, provide that to the budget agent as well.
    The budgeting step may be skipped if the user chooses to.
    Finally, try to answer any additional questions about the trip the user may have.""",
    tools=[AgentTool(agent=budget_agent)]
)
