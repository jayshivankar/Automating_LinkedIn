# LinkedIn Job Application Automation with Selenium

## Overview
This Python script automates the process of logging into LinkedIn, navigating to a specific job listing, and interacting with the job post by saving and following the company. The script uses Selenium WebDriver for automation.

## Prerequisites
Before running the script, ensure you have the following installed:
- Python (>=3.7)
- Google Chrome (latest version)
- Chrome WebDriver (compatible with your Chrome version)
- Selenium Python package

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/linkedin-automation.git
   cd linkedin-automation
   ```

2. Install dependencies:
   ```bash
   pip install selenium
   ```

3. Download and set up Chrome WebDriver:
   - Download the appropriate version of ChromeDriver from [here](https://chromedriver.chromium.org/downloads).
   - Extract the driver and place it in the script directory or set its path in your system variables.

## Usage
1. Open the script (`linkedin_automation.py`) and update the following variables with your LinkedIn credentials:
   ```python
   ACCOUNT_EMAIL="your_email@example.com"
   ACCOUNT_PASSWORD="your_password"
   ```

2. Run the script:
   ```bash
   python linkedin_automation.py
   ```

## Functionality
- Navigates to LinkedIn job search for Android Developer jobs.
- Logs into LinkedIn using provided credentials.
- Clicks on a job listing.
- Saves the job listing.
- Follows the company associated with the job.

## Notes
- Using hardcoded credentials in scripts is **not recommended**. Consider using environment variables or a configuration file to store credentials securely.
- LinkedIn's website structure may change, requiring updates to the XPath locators in the script.
- Excessive automated actions on LinkedIn may result in temporary or permanent account restrictions.

## Disclaimer
This script is intended for educational and personal use only. Automating interactions with LinkedIn violates LinkedIn’s Terms of Service. Use this script responsibly and at your own risk.

