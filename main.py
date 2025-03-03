import smtplib
import pdfplumber
import re
import os
import time
from email.message import EmailMessage
from config import EMAIL_ADDRESS, EMAIL_PASSWORD

# File paths
PDF_FILE = "hr_contacts.pdf"
RESUME_FILE = "resume.pdf"
LOG_FILE = "logs/sent_emails.log"

def extract_contacts(pdf_path):
    contacts = []
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"  # Regex for valid emails
    
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                lines = text.split("\n")
                for line in lines:
                    email_match = re.search(email_pattern, line)
                    if email_match:
                        email = email_match.group()
                        parts = line.split(email)
                        
                        # Extract HR name (removing numbers and trimming spaces)
                        raw_name = parts[0].strip() if len(parts) > 0 else "Unknown"
                        name = re.sub(r'^\d+\s+', '', raw_name)  # Remove leading numbers
                        
                        # Extract company name (removing job title if present)
                        raw_company = parts[1].strip() if len(parts) > 1 else "Unknown"
                        company = re.sub(r'^[^A-Za-z]*', '', raw_company.split()[-1])  # Keep only the company name
                        
                        contacts.append((name, email, company))
    return contacts

def get_sent_emails():
    """Reads the log file and returns a set of already sent email addresses."""
    if not os.path.exists(LOG_FILE):
        return set()
    
    with open(LOG_FILE, "r") as log:
        return set(line.strip().split(": ")[-1] for line in log if line.strip())

def send_email(to_name, to_email, company):
    msg = EmailMessage()
    msg['Subject'] = f'Data Analyst Role Inquiry – {company}'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email
    
    body = f"""
    Dear {to_name},

    I hope you are doing well. I am writing to express my interest in potential Data Analyst opportunities at {company}. 
    As a Computer Science Engineering student with expertise in Python, SQL, Power BI, and Data Analytics, 
    I am eager to contribute my skills to your esteemed organization.

    I have attached my resume for your reference. Please let me know if there are any opportunities suitable for my profile.

    Looking forward to your response.

    Best regards,
    Aditya Bharti
    📞 +91 8379084993
    📧 adityabharti6088@gmail.com
    """
    
    msg.set_content(body)
    
    with open(RESUME_FILE, "rb") as f:
        msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename=os.path.basename(RESUME_FILE))
    
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        
        with open(LOG_FILE, "a") as log:
            log.write(f"Sent to: {to_email}\n")
        print(f"Email sent to {to_name} at {to_email}")
        time.sleep(2)  # Delay to prevent spamming
    except Exception as e:
        print(f"Failed to send email to {to_name} ({to_email}): {e}")

def main():
    contacts = extract_contacts(PDF_FILE)
    sent_emails = get_sent_emails()
    os.makedirs("logs", exist_ok=True)
    
    for name, email, company in contacts:
        if email in sent_emails:
            print(f"Skipping already sent email to {name} ({email})")
            continue
        send_email(name, email, company)

if __name__ == "__main__":
    main()
