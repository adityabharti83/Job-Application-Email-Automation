# **Job Application Email Automation - README**

## **📌 Project Overview**
This Python application automates the process of sending job application emails to HR contacts listed in a provided PDF. The script will:
- Extract HR names, email addresses, and company names from the PDF.
- Compose a personalized cold email for each HR contact.
- Attach the applicant's resume.
- Send emails one by one using Gmail SMTP.
- Log all successfully sent emails for tracking purposes.

---

## **📁 Project Structure**
```
job_application/
│── main.py                   # Main script to send emails
│── config.py                  # Configuration file (email credentials)
│── hr_contacts.pdf           # Input file containing HR details
│── resume.pdf                 # Applicant's resume
│── logs/                      # Folder to store email logs
│── logs/sent_emails.log       # Log file tracking sent emails
│── requirements.txt           # Dependencies for the project
│── README.md                  # Project documentation
```

### **📂 File Descriptions:**
- **`main.py`**: Core Python script that extracts emails and sends job applications.
- **`config.py`**: Stores email credentials securely.
- **`hr_contacts.pdf`**: The provided PDF containing HR details.
- **`resume.pdf`**: Applicant's resume in PDF format.
- **`logs/sent_emails.log`**: Log file recording all successfully sent emails.
- **`requirements.txt`**: Contains dependencies required for the project.
- **`README.md`**: Project documentation with instructions.

---

## **🔧 Installation & Setup**
### **1️⃣ Install Python Dependencies**
Ensure you have Python installed (version 3.6 or higher). Install the required dependencies:
```sh
pip install -r requirements.txt
```

### **2️⃣ Configure Email Credentials**
Create a `config.py` file and add your Gmail credentials:
```python
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"
```
🔹 **Use an App Password** instead of your actual Gmail password (see next section for instructions).

---

## **🔑 Setting Up Google App Passwords**
Since Google blocks less secure apps, an **App Password** is required for authentication.

### **🔹 Steps to Generate an App Password**
1. **Enable 2-Step Verification**
   - Visit [Google Account Security](https://myaccount.google.com/security).
   - Enable **2-Step Verification** under "How you sign in to Google".
   
2. **Generate an App Password**
   - Go to [Google App Passwords](https://myaccount.google.com/apppasswords).
   - Select **"Mail"** as the app and **"Windows Computer"** as the device.
   - Click **"Generate"** and copy the **16-character App Password**.

3. **Use the App Password in `config.py`**
   ```python
   EMAIL_ADDRESS = "your_email@gmail.com"
   EMAIL_PASSWORD = "abcd efgh ijkl mnop"  # Use the generated app password
   ```

---

## **🚀 Running the Script**
Execute the script using the following command:
```sh
python main.py
```
### **🔹 What Happens Next?**
- The script extracts HR details from `hr_contacts.pdf`.
- It sends a personalized job application email with the attached resume.
- Successfully sent emails are logged in `logs/sent_emails.log`.

---

## **📌 Troubleshooting & Common Errors**
| Error | Solution |
|-------|----------|
| **Invalid email extraction** | Check the `extract_contacts()` function in `main.py`. |
| **SMTP authentication issues** | Ensure you are using an **App Password** instead of your actual Gmail password. |
| **Rate limiting by Gmail** | A delay of 2 seconds is added in the script, but if issues persist, increase the delay. |

---

## **📜 License**
This project is open-source and free to use for job application automation.

---

## **📞 Contact**
**Developer:** Aditya Bharti  
📧 Email: adityabharti6088@gmail.com  
🌐 GitHub: [adityabharti83](https://github.com/adityabharti83)  

---
### 🎯 **Happy Job Hunting! 🚀**

