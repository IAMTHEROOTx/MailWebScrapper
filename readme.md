# 📬 MailWebScrapper

**MailWebScrapper** is a simple Python script that extracts email addresses from web pages.  
I created this project as part of my work-study search, to help me quickly find recruiter contact information from company websites or professional platforms.

## 🔍 Purpose

The main goal of this tool is to automate the process of finding publicly visible email addresses on websites, which can be time-consuming to do manually.  
It can be especially useful for:

- Job seekers  
- People doing outreach  
- Developers learning basic web scraping  

## 🛠️ How It Works

The script performs the following steps:

1. Requests the URL from the user via an input prompt.
2. Sends an HTTP request to the specified URL.
3. Retrieves and parses the HTML content of the page.
4. Uses a regular expression to find all email addresses.
5. Prints the unique email addresses found.

## 🐍 Requirements

Make sure you have Python installed (preferably Python 3).

Install the required `requests` library if it's not already available:

```bash
pip install requests
```

## ▶️ Usage

To run the script, open your terminal or command prompt and use the following command:

```bash
python main.py
```

You will then be prompted to enter the URL of the website you want to scrape:

```
Paste your URL : http://example.com
```

The script will then fetch the emails from the page and print them.

### Example Output

```
Paste your URL : http://example.com

Email addresses found on http://example.com:
contact@company.com
recruiter@jobs.com
```

## ⚠️ Notes

- The script only finds emails that are directly visible in the raw HTML. It won’t detect emails hidden behind JavaScript or forms.
- It does not bypass captchas or login walls.

## 📄 License

This project is open-source and free to use. Feel free to modify it to suit your needs.
