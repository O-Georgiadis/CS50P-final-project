## ATM Simulator


Description:

The ATM simulator is a command-line Python application that emulates the core functionality of a real-world Automated Teller Machine (ATM). Users can securely log in using a 16-digit card number and 3-digit PIN, view their current balance, deposit funds, withdraw funds with overdraft protection, and review a chronological transaction history. All account data is persisted in a JSON file, ensuring that transactions remain intact between sessions.

Features

- User Authentication: Validates a 16-digit card number and a 3-digit PIN.
Locks out unregistered or invalid credentials.
- Balance Inquiry: Displays the user's current balance, formatted to two decimal places with the euro symbol.
- Deposits: Allows users to deposit a positive amount, updates the balance, and logs each deposit in the transaction history.
- Withdrawals: Enforces non-negative balance by preventing withdrawals that exceed the current balance. Logs successful withdrawals.
- Transaction History: Prints a numbered list of all past deposits and withdrawals for audit and review.

File Structure

- project.py: Contains all application logic and the main() entry point. Top-level functions include:
  - open_accounts() / save_accounts(): Load and save Json data.
  - check_info(): Handle login flow and input validation.
  - options(): Present menu and route user choices.
  - check_balance(), deposit(), withdraw(), transaction_history(): Implement the ATM operations.
- test_project.py: Implements unit tests using pytest for three core functions:
  - test_check_balance(): Verifies output formatting and return value.
  - test_deposit(): Confirms correct balance update and transaction logging.
  - test_withdraw(): Confirms correct balance deduction and transaction logging.
- accounts.json: Stores the persistent account database in JSON format. Each account entry includes pin, balance and transactions fields.
- requirements.txt: Lists external dependencies (pytest) for easy environment setup.

Design Choices

- JSON Persistence: Chosen for simplicity and human readability. JSON allows quick inspection of account data and straightforward serialization/deserialization.
- Procedural Structure: Functions are defined at the top level to satisfy courses requirements and to facilitate direct testing without class overhead. A main() function serves as the single entry point.
- Input Validation and Loops: Used while True loops instead of recursion for robust re-prompting on invalid inputs, avoiding potential stack overflows.
- Return Values for Testing: Modified check_balance to return the numeric balance alongside printing it, enabling assertions in unit tests without altering interactive behavior

Testing

Unit tests in test_project.py leverage pytest's build-in features:
- capsys fixture captures stdout for testing printed messages.
- Transactions and balance changes are asserted against expected values.
- Test run in an isolated context by constructing in-memory account dictionaries, preventing side effects on the real accounts.json

This README provides a comprehensive view of the ATM Simulator's functionality, structure and rationale. Feel free to explore the code, run the demo video, and review the unit tests for a deeper understanding of design and implementation decisions.
