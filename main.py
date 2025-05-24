import re
import requests
import sys

def extract_emails_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.text
        # Simple regex for emails
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        emails = re.findall(email_pattern, html_content)
        unique_emails = set(emails)
        return unique_emails
    except requests.RequestException as e:
        print(f"Erreur lors de la récupération de la page : {e}")
        return set()

def main():
    url = input("Paste your URL : ")
    emails = extract_emails_from_url(url)
    if emails:
        print(f"Adresses email trouvées sur {url}:")
        for email in emails:
            print(email)
    else:
        print(f"Aucune adresse email trouvée sur {url}.")

if __name__ == "__main__":
    main()
