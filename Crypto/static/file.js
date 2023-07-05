fetch('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd')
  .then(response => response.json())
  .then(data => {
    const watchlistContainer = document.getElementById('crypto-slider');

    // Iterate over each coin in the watchlist
    watchlist.forEach(coin => {
      // Find the coin in the data
      const selectedCoin = data.find(item => item.name === coin);

      if (selectedCoin) {
        // Create a new slide
        const slide = document.createElement('li');
        slide.classList.add('splide__slide');

        // Set the title of the crypto
        const title = document.createElement('h2');
        title.textContent = selectedCoin.name;
        slide.appendChild(title);

        // Set the current price of the crypto
        const price = document.createElement('p');
        price.textContent = `Current Price: $${selectedCoin.current_price}`;
        slide.appendChild(price);

        // Create a chart element for the crypto
        const chart = document.createElement('div');
        chart.id = `chart-${selectedCoin.id}`;
        chart.classList.add('crypto-chart');
        slide.appendChild(chart);

        // Append the slide to the watchlist container
        watchlistContainer.appendChild(slide);

        // Render the chart for the crypto
        renderChart(selectedCoin.id);
      }
    });

    // Initialize the Splide slider
    const splide = new Splide('.splide', {
      type: 'loop',
      padding: '5rem',
    });

    splide.mount();
  })
  .catch(error => console.error(error));

// Function to render the chart for a specific crypto
function renderChart(coinId) {
  fetch(`https://api.coingecko.com/api/v3/coins/${coinId}/market_chart?vs_currency=usd&days=1`)
    .then(response => response.json())
    .then(data => {
      const prices = data.prices.map(price => price[1]);

      // Render the chart using the charting library of your choice
      // Example:
      const chartElement = document.getElementById(`chart-${coinId}`);
      const chart = new Chart(chartElement, {
        type: 'line',
        data: {
          labels: prices.map((_, index) => index),
          datasets: [
            {
              label: 'Price Change',
              data: prices,
              backgroundColor: 'rgba(0, 140, 255, 0.2)',
              borderColor: 'rgba(0, 140, 255, 1)',
              borderWidth: 1,
            },
          ],
        },
        options: {
          responsive: true,
        },
      });
    })
    .catch(error => console.error(error));
}
