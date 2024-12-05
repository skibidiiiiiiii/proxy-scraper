# Proxy Scraper

A Python-based proxy scraper that collects free proxies from popular websites and saves them into a text file.

## Description
This tool fetches proxies from multiple sources, processes them, and stores the results in a `proxies.txt` file. It's useful for tasks requiring proxy lists, such as web scraping or anonymity purposes.

## Features
- Scrapes proxies from well-known sources such as:
  - [Free Proxy List](https://free-proxy-list.net/)
  - [US Proxy](https://www.us-proxy.org/)
  - [ProxyScrape](https://www.proxyscrape.com/)
- Saves scraped proxies to a `proxies.txt` file.
- Handles errors gracefully to continue scraping from available sources.

## Prerequisites
- Python 3.8 or newer
- Required libraries:
  - `requests`
  - `beautifulsoup4`

Install dependencies with:
```bash
pip install requests beautifulsoup4
