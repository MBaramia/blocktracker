// Fetch data from CoinGecko API
fetch('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd')
  .then(response => response.json())
  .then(data => {
    const tableBody = document.querySelector('#coin-table tbody');

    // Iterate over each coin in the data
    data.forEach(coin => {
      const { name, current_price, total_volume, price_change_percentage_24h } = coin;

      // Create table row for each coin
      const row = document.createElement('tr');

      // Create table data cell for coin name
      const coinCell = document.createElement('td');
      coinCell.textContent = name;

      // Create table data cell for price (USD)
      const priceCell = document.createElement('td');
      priceCell.textContent = current_price;

      // Create table data cell for liquidity
      const liquidityCell = document.createElement('td');
      liquidityCell.textContent = total_volume.toLocaleString();

      // Create table data cell for daily percentage change
      const percentageCell = document.createElement('td');
      percentageCell.textContent = `${price_change_percentage_24h}%`;

      // Append cells to the row
      row.appendChild(coinCell);
      row.appendChild(priceCell);
      row.appendChild(liquidityCell);
      row.appendChild(percentageCell);

      // Append row to the table body
      tableBody.appendChild(row);
    });
  })
  .catch(error => console.error(error));
// Function to open the popup
function openPopup() {
  document.getElementById('popup').style.display = 'block';
}

function closePopup() {
  document.getElementById('popup').style.display = 'none';
}

async function searchCoins() {
  const searchInput = document.getElementById('coin-search').value;
  const coinOptionsContainer = document.getElementById('coin-options');

  // Clear previous options
  coinOptionsContainer.innerHTML = '';

  try {
    // Fetch coin options from CoinGecko API
    const response = await fetch(`https://api.coingecko.com/api/v3/coins/list?include_platform=false`);
    const coinOptions = await response.json();

    // Filter coin options based on the search input
    const filteredOptions = coinOptions.filter(coin => coin.name.toLowerCase().includes(searchInput.toLowerCase()));

    // Create option elements
    filteredOptions.forEach(coin => {
      const optionElement = document.createElement('div');
      optionElement.classList.add('coin-option');
      optionElement.textContent = coin.name;

      // Add an event listener to handle the click on a coin option
      optionElement.addEventListener('click', () => {
        addCoinToWatchlist(coin);
        closePopup();
      });

      coinOptionsContainer.appendChild(optionElement);
    });
  } catch (error) {
    console.error(error);
  }
}


function addCoinToWatchlist(coin) {
  fetch('/add_coin', {
    method: 'POST',
    body: JSON.stringify({ coin }),
    headers: {
      'Content-Type': 'application/json'
    }
  })
    .then(response => response.json())
    .then(data => {
      // Handle the response from the server
      if (data.message === 'Coin added to watchlist') {
        // Update the watchlist array in the frontend
        const watchlist = data.watchlist;
        console.log('Updated watchlist:', watchlist);
      } else {
        console.log('Failed to add coin:', data.message);
      }
    })
    .catch(error => console.error(error));
}


