# APT_ThreatIntel
A web crawler designed to detect APTs and zero-day threats
# APT Zero-Day Web Crawler

A web crawler designed to search for **Advanced Persistent Threats (APTs)** and **zero-day vulnerabilities** across the internet. This project is intended for **threat intelligence** and **cybersecurity** professionals who want to gather information on emerging threats from various public sources.

The crawler scrapes web pages from well-known cybersecurity, vulnerability, and threat intelligence sites to look for keywords related to APTs, zero-day exploits, vulnerabilities, and cyberattacks.

### Created by: **Amarjeet**

## Features

- Scrapes a range of well-known cybersecurity and vulnerability websites.
- Detects mentions of **APT** groups, **zero-day vulnerabilities**, **exploit** information, and other threat-related keywords.
- Follows pagination links to crawl additional pages and continuously scrape relevant content.
- Outputs the relevant articles, including titles, links, and summaries.

## How It Works

The crawler begins scraping the following websites:
- **CISA News** (https://www.cisa.gov/news)
- **FireEye Blog** (https://www.fireeye.com/blog.html)
- **Bleeping Computer** (https://www.bleepingcomputer.com/)
- **SecurityFocus** (https://www.securityfocus.com/)
- **Exploit-DB** (https://www.exploit-db.com/)
- **MITRE ATT&CK** (https://www.mitre.org/)
- **Cybersecurity News** (https://www.cybersecurity-news.com/)
- **DarkReading** (https://www.darkreading.com/)

It looks for articles that mention key terms such as "APT," "zero-day," "exploit," "vulnerability," "CVE," "cyberattack," and more. When these terms are found, the crawler extracts the title, link, and summary of the article for further analysis.

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/cruvel-cyber/APT_ThreatIntel.git
   

