# 🎂 Birthday Wishes Email Sender (Python)

A Python automation project that sends personalized birthday emails by reading data from a CSV file and using email templates.

---

## 🚀 Features

* 📅 Reads birthday data from a CSV file
* 🎉 Sends personalized birthday emails automatically
* 📝 Uses random email templates for variation
* 🔍 Uses pandas for data handling
* ⏱️ Can be scheduled to run daily using PythonAnywhere

---

## 🛠️ Tech Stack

* Python
* Pandas
* SMTP (Email)
* PythonAnywhere

---

## 📂 Project Structure

```text
birthday-email-sender/
│
├── main.py
├── birthdays_sample.csv
├── letter_templates/
│   ├── letter_1.txt
│   ├── letter_2.txt
│   └── letter_3.txt
```

---

## ⚙️ How to Run

1. Install required libraries:

```bash
pip install pandas
```

2. Open `main.py` and update:

```python
MY_EMAIL = "YOUR_EMAIL"
MY_PASSWORD = "YOUR_PASSWORD"
```

3. Run:

```bash
python main.py
```

---

## 💡 Notes

* Uses CSV file to store birthday data
* Automatically selects a random email template
* Sends email only if today's date matches a birthday
* Can be scheduled on PythonAnywhere to run daily

---

## ⭐ About this project

Built while learning Python and experimenting with automation, file handling, and email integration.

