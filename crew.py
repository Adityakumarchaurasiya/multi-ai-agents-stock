from crewai import Crew;

from agents.trader_agent import trader_agent_data;
from agents.analyst_agent import analyst_agent;
from tasks.analytics_tasks import get_stock_analysis;
from tasks.trade_tasks import trade_decision;


stock_market_crew=Crew(
    agents=[trader_agent_data,analyst_agent],
    tasks=[get_stock_analysis, trade_decision],
    verbose=True
)