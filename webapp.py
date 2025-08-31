from stock_fetch import StockAPI, StockAnalyzer
from ai_insight import AIInsights

import streamlit as st

if 'page' not in st.session_state:
    st.session_state.page = 'home'
    st.session_state.ticker = 'RELIANCE' 
    st.session_state.market = 'BSE' 
    st.session_state.image_path = ''
    st.session_state.ai_insights = ''
    st.session_state.internal_results_available = False

def home():
    st.title("Stock AI Agent")

    col1, col2 = st.columns(2)
    with col1:
        st.session_state.ticker = st.text_input('Enter Stock Ticker', value=st.session_state.ticker, key='ticker_input')
    with col2:
        st.session_state.market = st.selectbox('Select Market', options=['BSE', 'NASDAQ'], index=['BSE', 'NASDAQ'].index(st.session_state.market), key='market_input')
    
    st.sidebar.header("About")
    st.sidebar.write("This is a Stock Analysis platform")

    st.markdown("---")

    if st.button("Submit"):
        st.session_state.page = 'analysis'
        st.session_state.internal_results_available = False
        st.rerun()

def analysis():
    st.title(f"Analysis for {st.session_state.ticker} ({st.session_state.market})")

    stock = st.session_state.ticker
    market = st.session_state.market
    if not st.session_state.internal_results_available:
        with st.spinner('Fetching and analyzing data...'):
            image_path = f"/Users/janyak/Desktop/Personal Projects/AI Stock Analyzer/{market}_{stock}.png"
            st.session_state.image_path = image_path
            stock_api = StockAPI()
            market_data = stock_api.get_stock_data(stock, market)
            stock_analyzer = StockAnalyzer()
            df = stock_analyzer.json_to_dataframe(market_data, stock, market)
            stock_analyzer.plot_stock_data(df, stock, market, image_path)
            ai_api = AIInsights()
            response = ai_api.generate_insights(image_path, stock, market)

            candidates = response.candidates
            for candidate in candidates:
                text_parts = candidate.content.parts
                for part in text_parts:
                    print(part.text)
                    st.session_state.ai_insights += part.text
            st.session_state.internal_results_available = True
        
    if st.session_state.internal_results_available:
        st.subheader("Chart Analysis")
        st.image(st.session_state.image_path, caption = f"{st.session_state.ticker} Chart",use_column_width=True)

        st.subheader("Analysis Results")
        st.write(st.session_state.ai_insights)

        if st.button("Home"):
            st.session_state.page = "home"
            st.session_state.internal_results_available = False
            st.rerun()

if st.session_state.page == "home":
    home()
elif st.session_state.page == "analysis":
    analysis()

