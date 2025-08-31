# AI Stock Analyzer

AI Stock Analyzer is a Streamlit-based web application that fetches, visualizes, and analyzes stock market data using AI-powered insights.

## Features
- Fetches daily stock data from Alpha Vantage API
- Visualizes stock performance with interactive charts
- Provides AI-generated insights on stock trends
- Supports BSE and NASDAQ markets

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/AI-Stock-Analyzer.git
cd AI-Stock-Analyzer
```

### 2. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install pandas matplotlib requests pytz google-generativeai streamlit dotenv
```

### 4. Set up API keys
Create a `.env` file in the project root with the following content:
```
ALPHAVANTAGE_API_KEY=your_alphavantage_api_key
GOOGLEAI_API_KEY=your_googleai_api_key
```

### 5. Run the app
```bash
streamlit run webapp.py
```

## File Structure
- `webapp.py` - Main Streamlit app
- `stock_fetch.py` - Stock data fetching and plotting logic
- `ai_insight.py` - AI-powered stock analysis
- `.env` - API keys 


## Notes
- Do not share your `.env` file or API keys publicly.
- The app creates chart images in the project directory.

