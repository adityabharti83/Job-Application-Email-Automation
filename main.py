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
                        
                        name = parts[0].strip() if len(parts) > 0 else "Unknown"
                        company = parts[1].strip() if len(parts) > 1 else "Unknown"
                        
                        contacts.append((name, email, company))
    return contacts

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
    #Your Nmae
    📞 +91 #Mobile No
    📧 #Your Email
    """
    
    msg.set_content(body)
    
    with open(RESUME_FILE, "rb") as f:
        msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename="Aditya_Bharti_Resume.pdf")
    
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
    os.makedirs("logs", exist_ok=True)
    
    for name, email, company in contacts:
        send_email(name, email, company)

if __name__ == "__main__":
    main()
