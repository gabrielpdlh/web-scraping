# Web Scraping and PDF Download Project

This project demonstrates how to scrape a website for PDF links, download the PDFs, and compress them into a single ZIP file. It uses Python libraries such as requests, BeautifulSoup, for web scraping and file downloads.

# Description
This project is designed to automate the process of downloading PDF files from a specific government website and compressing them into a ZIP file. It leverages web scraping to find all the PDF links and file compression to store them in one convenient file.

# Features
- Scrapes PDF links from a given URL.
- Downloads PDFs.
- Compresses all downloaded files into a ZIP file.

# Installation
To run this project, you'll need to have Python 3.6+ installed on your machine. Follow these steps to get started:

1 - Clone the repository:

`git clone https://github.com/yourusername/web-scraping-pdf-download.git`
`cd web-scraping-pdf-download`

2 - Install the required dependencies:

`pip install -r requirements.txt`

# Usage

To run the project, execute the following command:

`python main.py`

This will:
- Scrape the page at the specified URL for PDF links.
- Download each PDF file.
- Compress all PDFs into a ZIP file named attachments.zip in the downloads folder.

