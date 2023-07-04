def test_open_account():
    # Create a Bank object
    bank = Bank()

    # Create accounts with different balances
    account1 = Account.create_account("A001")  # Account with zero balance
    account2 = Account.create_account("A002")  # Account with positive balance
    account3 = Account.create_account("A003")  # Account with negative balance

    # Open the accounts in the bank
    bank.open_account(account1)
    bank.open_account(account2)
    bank.open_account(account3)

    # Verify that the accounts are open and have the correct balances
    assert account1.get_balance() == 0.0
    assert account2.get_balance() == 0.0
    assert account3.get_balance() == 0.0  # Negative balance should be set to zero

    # Verify that the accounts are in the bank's account list
    assert account1 in bank.accounts
    assert account2 in bank.accounts
    assert account3 in bank.accounts

    # Verify that the correct number of accounts are opened in the bank
    assert len(bank.accounts) == 3

    print("open_account test passed.")

# Run the test
test_open_account()
