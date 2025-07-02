# Python Bank Web App - Built with Streamlit

This is a simple web application that simulates basic banking functionalities using Python and Streamlit. It allows users to interact with Current and Savings accounts, performing deposits and withdrawals.

## Project Structure

```
.
├── account.py                # Base class for bank accounts.
├── current_account.py        # Defines the CurrentAccount class, inheriting from Account.
├── savings_account.py        # Defines the SavingsAccount class, inheriting from Account.
├── home.py                   # The main entry point for the Streamlit application (the home page).
├── pages/                    # Directory containing Streamlit pages for different account types.
│   ├── current_account_page.py # Streamlit page for Current Account operations.
│   └── savings_account_page.py # Streamlit page for Savings Account operations.
├── README.md                 # This file.
└── __pycache__/              # Directory for Python bytecode cache (auto-generated).
```

## How the App Works

The application is built around a few core Python classes that define account behaviors:

*   **`Account` (`account.py`):** This is the base class for all account types. It defines common methods like `deposit()` and `withdraw()` and stores the account `balance`.
*   **`CurrentAccount` (`current_account.py`):** This class inherits from `Account` and represents a current (checking) account. It has its own implementation of `withdraw()` and `deposit()` with specific rules (e.g., preventing negative withdrawal amounts, checking for sufficient funds).
*   **`SavingsAccount` (`savings_account.py`):** This class also inherits from `Account` and represents a savings account. It includes a `withdrawal_limit` and specific logic for deposits and withdrawals, ensuring the withdrawal limit and available balance are respected.

The user interface is created using **Streamlit**:

*   **`home.py`:** This script serves as the landing page of the application. It provides links to navigate to the Current Account and Savings Account pages.
*   **`pages/current_account_page.py`:** This script handles all interactions for the Current Account. It allows users to:
    *   View their current balance.
    *   Deposit funds.
    *   Withdraw funds.
    It uses Streamlit's session state to maintain the account balance and display success or error messages.
*   **`pages/savings_account_page.py`:** This script manages the Savings Account interactions. Users can:
    *   Enter their name (which initializes or retrieves their savings account).
    *   View their account balance.
    *   Deposit funds.
    *   Withdraw funds, subject to a withdrawal limit and available balance.
    Similar to the current account page, it uses session state for account data and messaging.

## Getting Started

To run this application, you need to have Python and Streamlit installed.

1.  **Clone the repository (if you haven't already):**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Install Streamlit (if you don't have it):**
    ```bash
    pip install streamlit
    ```

3.  **Run the application:**
    Open your terminal in the project's root directory and run:
    ```bash
    streamlit run home.py
    ```
    This will start the Streamlit development server, and the application should open in your web browser.

## Account Functionalities

### Current Account
*   **Deposit:** Add funds to the account.
*   **Withdraw:** Remove funds from the account. Withdrawals are checked against the available balance.

### Savings Account
*   **Deposit:** Add funds to the account. Only positive amounts can be deposited.
*   **Withdraw:** Remove funds from the account. Withdrawals are subject to:
    *   A maximum withdrawal limit per transaction.
    *   The available account balance.

## Credits

*   **King David:** Worked on current account withdrawal function.
*   **Israel:** Worked on current account deposit function.
*   **Miracle:** Created savings account page (including withdrawal and deposit functions).
*   **Benedict:** Created error and success messages for account actions.
*   **Michael:** Created home page.
