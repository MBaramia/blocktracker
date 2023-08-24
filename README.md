# Cryptocurrency Tracker

This is a web application that provides a service for monitoring cryptocurrency prices. It allows users to view a list of cryptocurrencies, their current prices, and a chart displaying the price change over the past 24 hours, using real time data from the CoinGecko API

## Features

### 1. Dashboard Page

The main feature of the application is the dashboard page, which displays a sliding carousel of cryptocurrency information. Each slide in the carousel represents a cryptocurrency from the user's watchlist and includes the following information:

- Name: The name of the cryptocurrency.
- Current Price: The current price of the cryptocurrency in USD.
- Chart: A line chart showing the price change of the cryptocurrency over the past 24 hours.

### 2. Watchlist Management

Users can manage their watchlist, which is a list of cryptocurrencies they want to track on the dashboard. The watchlist allows users to customize the cryptocurrencies displayed in the carousel. They can add or remove cryptocurrencies from the watchlist as desired.

### 3. Real-Time Data

The application fetches real-time cryptocurrency data from the CoinGecko API. It retrieves the latest market prices and price charts for the cryptocurrencies in the watchlist. The data is updated dynamically on the dashboard, providing users with the most up-to-date information.

## Technologies Used

The project is built using the following technologies:

- Python: Backend programming language for the Flask web framework.
- Flask: A micro web framework used for server-side development.
- HTML: Markup language for creating the structure of web pages.
- CSS: Styling language for enhancing the visual appearance of web pages.
- JavaScript: Programming language used for client-side interactivity.
- Splide: JavaScript library for creating the sliding carousel.
- Chart.js: JavaScript library for creating interactive charts.

## Getting Started

To run the project locally, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/cryptocurrency-dashboard.git`
2. Navigate to the project directory: `cd cryptocurrency-dashboard`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Set up your API credentials: Obtain an API key from CoinGecko and update the configuration file with your credentials.
5. Start the Flask development server: `python app.py`
6. Access the dashboard in your web browser at: `http://localhost:5000/dashboard`

Note: You may need to modify the Flask routes and API calls to fit your specific requirements or data sources.

## Future Enhancements

Here are some potential enhancements that can be made to the project:

- Additional data visualization: Expand the dashboard to include more detailed charts and analytics for each cryptocurrency.
- Portfolio tracking: Allow users to input their cryptocurrency holdings and track their portfolio performance over time.
- Alerts and notifications: Implement alerts and notifications for price changes, volume spikes, or other market events.

Feel free to contribute to the project by submitting bug reports, feature requests, or pull requests!

