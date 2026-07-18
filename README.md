<div align="center">
# 💰 Personal Finance Tracker
### *Track. Save. Grow.*
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
[![Standard Library](https://img.shields.io/badge/Dependencies-None%20(Std%20Lib%20Only)-success?style=for-the-badge)](requirements.txt)
[![PEP 8](https://img.shields.io/badge/Code%20Style-PEP%208-informational?style=for-the-badge)](https://peps.python.org/pep-0008/)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)]()
> A **clean, menu-driven command-line application** to track your daily income and expenses,  
> view summaries, and export financial reports — built entirely with Python's standard library.
![Finance Tracker Banner](assets/screenshot.png)
</div>
---
## 📌 Table of Contents
- [About the Project](#-about-the-project)
- [Features](#-features)
- [Technologies Used](#-technologies-used)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Example Output](#-example-output)
- [Screenshots](#-screenshots)
- [Future Improvements](#-future-improvements)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)
---
## 🧾 About the Project
**Personal Finance Tracker** is a beginner-friendly Python CLI application that helps you take control of your money. Whether you're tracking daily coffee expenses or monthly salary, this tool gives you a clear picture of where your money comes from and where it goes.
This project was built to demonstrate:
- Clean, modular Python code
- Real-world data handling with CSV
- Professional terminal UX with ANSI colors
- PEP 8 coding standards and best practices
> ✅ **No pip install needed** — uses only Python's built-in modules!
---
## ✨ Features
|
 Feature 
|
 Description 
|
|
---
|
---
|
|
 ➕ 
**
Add Income
**
|
 Log salary, freelance, investments, and more 
|
|
 ➖ 
**
Add Expense
**
|
 Track food, rent, transport, entertainment, etc. 
|
|
 📋 
**
View Transactions
**
|
 See all records in a clean formatted table 
|
|
 🔍 
**
Filter by Type
**
|
 View only income or only expense records 
|
|
 📅 
**
Filter by Month
**
|
 View transactions for any specific month 
|
|
 📊 
**
Financial Summary
**
|
 Total income, expenses, net balance + ASCII bar charts 
|
|
 🗑️ 
**
Delete Records
**
|
 Remove any transaction by its ID 
|
|
 📤 
**
Export Report
**
|
 Save a plain-text financial report to file 
|
|
 🎨 
**
Colored Output
**
|
 ANSI-colored terminal UI for better readability 
|
|
 ✅ 
**
Input Validation
**
|
 All inputs are validated with helpful error messages 
|
---
## 🛠 Technologies Used
|
 Technology 
|
 Purpose 
|
|
---
|
---
|
|
**
Python 3.10+
**
|
 Core programming language 
|
|
**
`csv`
 module
**
|
 Reading and writing transaction data 
|
|
**
`os`
 module
**
|
 File system and terminal operations 
|
|
**
`datetime`
 module
**
|
 Date formatting and validation 
|
|
**
`sys`
 module
**
|
 Graceful exit handling 
|
|
**
ANSI escape codes
**
|
 Terminal color styling 
|
> 🚫 **No third-party dependencies** — zero `pip install` required!
---
## 📁 Project Structure
```
personal-finance-tracker/
│
├── main.py                  # 🚀 Entry point — run this to start the app
│
├── src/
│   ├── __init__.py          # Package marker
│   ├── functions.py         # 🧠 Core business logic (CRUD, summary, export)
│   └── utils.py             # 🔧 Utility helpers (colors, formatting, validation)
│
├── data/
│   └── transactions.csv     # 💾 Auto-created — your transaction data
│
├── reports/                 # 📄 Auto-created — exported text reports
│
├── assets/
│   └── screenshot.png       # 🖼 Project banner
│
├── requirements.txt         # 📦 No dependencies (standard library only)
├── .gitignore               # 🚫 Ignored files
├── LICENSE                  # ⚖  MIT License
└── README.md                # 📖 You are here
```
---
## ⚙️ Installation
### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/personal-finance-tracker.git
cd personal-finance-tracker
```
### 2. Verify Python Version
This project requires **Python 3.10 or higher**.
```bash
python --version
# Expected: Python 3.10.x or higher
```
### 3. Run the Application
```bash
python main.py
```
> 📝 **No virtual environment needed!** The project uses only Python's built-in standard library.
---
## 🚀 Usage
Once you run `python main.py`, you'll see the welcome screen, followed by the main menu:
```
══════════════════════════════════════════════════════════
  💰  MAIN MENU
══════════════════════════════════════════════════════════
  [1] ➕  Add Income
  [2] ➖  Add Expense
  [3] 📋  View All Transactions
  [4] 🔍  View Income Transactions
  [5] 🔍  View Expense Transactions
  [6] 📅  View by Month
  [7] 📊  Financial Summary
  [8] 🗑   Delete a Transaction
  [9] 📤  Export Report
  [0] 🚪  Exit
```
### Adding a Transaction
1. Select `[1]` to add income or `[2]` to add expense
2. Choose a category from the numbered list
3. Enter a description, amount, and date (or press Enter for today)
4. Your record is saved automatically ✅
### Viewing the Summary
Select `[7]` to see:
- Total income and total expenses
- Net balance (in green if positive, red if negative)
- Category-by-category breakdown with ASCII bar charts
---
## 📟 Example Output
### Main Menu
```
  ╔══════════════════════════════════════════════════════╗
  ║                                                      ║
  ║     💰  PERSONAL FINANCE TRACKER  💰                ║
  ║         Track. Save. Grow.                           ║
  ║                                                      ║
  ╚══════════════════════════════════════════════════════╝
```
### Transaction Table
```
  ID   Date         Type      Category       Description            Amount
  ────────────────────────────────────────────────────────────
  1    2025-07-01   ▲ income  Salary         Monthly Salary      ₹50,000.00
  2    2025-07-05   ▼ expense Food           Grocery Shopping     ₹2,500.00
  3    2025-07-10   ▼ expense Transport      Metro Card Recharge    ₹500.00
  ────────────────────────────────────────────────────────────
  Total records: 3
```
### Financial Summary
```
  ── Overall Financial Summary ──
  Total Income                   ₹50,000.00
  Total Expenses                  ₹3,000.00
  ──────────────────────────────────────────
  ▲ Net Balance                  ₹47,000.00
  ── Expense Breakdown by Category ──
  Food            ₹2,500.00  ████████████████     83.3%
  Transport         ₹500.00  ████                 16.7%
```
---
## 📸 Screenshots
<div align="center">
![Banner](assets/screenshot.png)
</div>
---
## 🔮 Future Improvements
Here are features planned for future versions:
- [ ] 📈 **Monthly trend charts** using `matplotlib`
- [ ] 💱 **Multi-currency support** (USD, EUR, INR, etc.)
- [ ] 🏦 **Budget limits** — set spending limits per category with alerts
- [ ] 📊 **Export to Excel/CSV** for spreadsheet analysis
- [ ] 🔐 **Password protection** for sensitive financial data
- [ ] 🌐 **Web interface** using Flask or FastAPI
- [ ] 🤖 **AI spending insights** — detect patterns and suggest savings
- [ ] 📱 **Mobile-friendly** version using Kivy
- [ ] 🔔 **Recurring transactions** — auto-add monthly bills
- [ ] 📧 **Email reports** — schedule and email monthly summaries
---
## 🤝 Contributing
Contributions are welcome! Here's how to get started:
1. **Fork** the repository
2. **Clone** your fork:
   ```bash
   git clone https://github.com/yourusername/personal-finance-tracker.git
   ```
3. **Create a branch** for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Make your changes** and follow PEP 8 style
5. **Add comments** to all new functions and classes
6. **Test your changes** manually before committing
7. **Commit** with a descriptive message:
   ```bash
   git commit -m "feat: add monthly budget limit alerts"
   ```
8. **Push** and open a **Pull Request** with a clear description
> 💡 Please open an **Issue** first if you're planning a large change, so we can discuss it.
---
## ⚖️ License
Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for details.
---
## 👨‍💻 Author
<div align="center">
**Mallikarjun Arjun**
[![GitHub](https://img.shields.io/badge/GitHub-yourusername-181717?style=for-the-badge&logo=github)](https://github.com/yourusername)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/yourprofile)
*"Code is like money — manage it well and it grows." 💰*
</div>
---
<div align="center">
⭐ **If you found this project helpful, please give it a star!** ⭐
Made with ❤️ and Python 🐍
</div>
