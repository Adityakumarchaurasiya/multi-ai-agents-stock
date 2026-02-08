# 🚀 AI-Powered Stock Market Analyzer - Multi-Agent System

## 📊 Overview
A sophisticated multi-agent AI system for real-time stock market analysis and trading recommendations using CrewAI, Groq LLM, and Yahoo Finance data.

## ✨ Features
- **🤖 Multi-Agent Architecture**: Specialized AI agents for analysis and trading decisions
- **📈 Real-Time Data**: Live stock data via yfinance integration
- **🧠 Advanced AI**: Powered by Groq's Llama 3.3-70B model for intelligent analysis
- **🎯 Actionable Insights**: Clear Buy/Sell/Hold recommendations with reasoning
- **🔗 Seamless Integration**: Modular design with clear separation of concerns

## 🏗️ System Architecture
📦 Stock Analyzer
├── 🤖 Analyst Agent - Technical analysis & trend identification
├── 💼 Trader Agent - Decision making & risk assessment
├── 📊 Data Layer - Yahoo Finance API integration
├── 🧠 LLM Layer - Groq-powered reasoning engine
└── 🔧 Orchestrator - CrewAI multi-agent coordination


## 🛠️ Tech Stack
- **Python 3.13** - Core programming language
- **CrewAI** - Multi-agent orchestration framework
- **Groq API** - High-performance LLM inference
- **yfinance** - Real-time stock market data
- **Pydantic** - Data validation & settings management

## 📁 Project Structure 

stock-market-analyzer/
├── main.py # Application entry point
├── crew.py # Multi-agent crew configuration
├── .env # Environment variables
├── agents/
│ ├── analyst_agent.py # Analysis specialist agent
│ └── trader_agent.py # Trading decision agent
└── tasks/
├── analytics_tasks.py # Analysis tasks
└── trade_tasks.py # Trading decision tasks


## ⚡ Quick Start

### 1. Clone & Setup
```bash
git clone <your-repo-url>
cd stock-market-analyzer
pip install -r requirements.txt

🔍 Analyzing AAPL...
📈 Current Price: $182.63 (+1.2%)
📊 Volume: 45.2M shares
🤖 Analyst Agent: Strong bullish trend detected with RSI at 62
💼 Trader Agent: RECOMMENDATION: BUY
📋 Reasoning: Positive earnings outlook and technical breakout pattern

