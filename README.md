## README for Immo Scraper Le Bon Coin

Welcome to the **Immo Scraper Le Bon Coin** repository! This project is designed to scrape real estate listings from Le Bon Coin, a popular French classifieds website, and extract useful data such as price and square footage of properties. The script is written in Python and uses Selenium and BeautifulSoup for web scraping.

### Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Output](#output)
- [Contributing](#contributing)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your machine
- Mozilla Firefox browser installed

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/Immo-scraper-le-bon-coin.git
   cd Immo-scraper-le-bon-coin
   ```

2. **Install the required Python packages:**

   ```sh
   pip install selenium beautifulsoup4
   ```

## Usage

1. **Update the Firefox binary location:**

   Ensure that the `options.binary_location` in the script points to the correct path of your Firefox installation. For example:

   ```python
   options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
   ```

2. **Run the script:**

   Execute the Python script to start scraping:

   ```sh
   python immo.py
   ```

   The script will navigate to the specified Le Bon Coin URL, scrape the real estate listings, and save the data in JSON and text files.

## Output

- **immo.json:**

  This file contains the raw JSON data extracted from the Le Bon Coin website.

- **immo.txt:**

  This file contains a summary of the scraped data, including the number of properties, average price per square meter, and average property price.

  Example output in `immo.txt`:

  ```
  01/08/2024, 17:01
  Housings: 34
  Average price per square metre : 11263
  Average housing price : 586994
  ```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

---

Thank you for using **Immo Scraper Le Bon Coin**! If you have any questions or encounter any issues, please feel free to open an issue on GitHub. Happy scraping!
