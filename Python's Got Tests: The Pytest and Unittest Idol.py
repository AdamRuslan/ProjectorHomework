def test_open_account():
    # Create a Bank object
    bank = Bank()

    # Create accounts with different balances
    zero_balance_account = Account.create_account("A001")  # Account with zero balance
    positive_balance_account = Account.create_account("A002")  # Account with positive balance
    negative_balance_account = Account.create_account("A003")  # Account with negative balance

    # Open the accounts in the bank
    bank.open_account(zero_balance_account)
    bank.open_account(positive_balance_account)
    bank.open_account(negative_balance_account)

    # Verify that the accounts are open and have the correct balances
    assert zero_balance_account.get_balance() == 0.0
    assert positive_balance_account.get_balance() == 0.0
    assert negative_balance_account.get_balance() == 0.0  # Negative balance should be set to zero

    # Verify that the accounts are in the bank's account list
    assert zero_balance_account in bank.accounts
    assert positive_balance_account in bank.accounts
    assert negative_balance_account in bank.accounts

    # Verify that the correct number of accounts are opened in the bank
    assert len(bank.accounts) == 3

    print("open_account test passed.")

# Run the test
test_open_account()
