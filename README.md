# Banking Problem

This Python program simulates a banking system with multiple features such as account creation, deposits, withdrawals, fund transfers, and credit card creation. Randomized balances and account numbers are used to enhance functionality and realism. 

---

## Features

1. **Open a New Account**  
   - Users can open a new account by providing personal details (name, age, and postal code).  
   - If the user is 16 or older, a random 6-digit account number is generated.  
   - Phone number validation ensures a valid 10-digit input.

2. **Deposit Money**  
   - Users can deposit money into their account by providing a valid 6-digit account number.  
   - The program calculates and displays the new balance after the deposit.

3. **Withdraw Money**  
   - Users can withdraw up to $1000 per transaction by providing a valid account number.  
   - The updated balance is shown after the withdrawal.  

4. **Transfer Funds**  
   - Users can transfer up to $1000 between two accounts.  
   - Both the sender's and receiver's account numbers must be valid 6-digit numbers.  
   - The remaining balance is displayed after the transfer.  

5. **Create a Credit Card**  
   - Users can create a credit card by entering their name, address, social security number (validated for 9 digits), and age.  
   - Credit cards are only available for users 16 years or older.  
   - A random 12-digit credit card number and a 3-digit CVC number are generated.  
   - The card's expiry date is displayed, and the card will be mailed to the user.  

6. **Quit the Program**  
   - Users can exit the system at any time, and a thank-you message is displayed.

---

## Prerequisites

Ensure you have Python 3.x installed to run this program.  
No additional libraries are required, except for the built-in `random` module.

---

## Usage

1. Run the program in your Python environment:
   ```bash
   python banking_problem.py
