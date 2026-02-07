from dotenv import load_dotenv
from crew import stock_market_crew;


load_dotenv();

def run(stock:str):
    result=stock_market_crew.kickoff(inputs={"stock":stock});
    print(result);



if __name__=="__main__":
    run("AAPL")