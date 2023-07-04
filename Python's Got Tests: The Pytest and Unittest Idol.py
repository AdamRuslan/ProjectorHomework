# Test Bank Class
def test_bank_open_account():
    bank = Bank()

    # Test opening an account with a positive initial balance
    account1 = Account.create_account("A001")
    bank.open_account(account1)
    assert len(bank.accounts) == 1
    assert account1.get_balance() == 0.0

    account1.deposit(1000)
    assert account1.get_balance() == 1000.0

    # Test opening an account with a zero initial balance
    account2 = Account.create_account("A002")
    bank.open_account(account2)
    assert len(bank.accounts) == 2
    assert account2.get_balance() == 0.0

    # Test opening an account with a negative initial balance
    try:
        account3 = Account.create_account("A003")
        account3.withdraw(100)  # Attempt to withdraw from zero balance
        bank.open_account(account3)  # This line should raise a ValueError
        # If the line above doesn't raise an error, the test should fail
        assert False, "Opening an account with a negative balance should raise a ValueError"
    except ValueError:
        assert True

    # Test opening multiple accounts
    account4 = Account.create_account("A004")
    bank.open_account(account4)
    account5 = Account.create_account("A005")
    bank.open_account(account5)
    assert len(bank.accounts) == 4

    # Test opening duplicate accounts with the same account number
    account6 = Account.create_account("A004")
    bank.open_account(account6)
    account7 = Account.create_account("A005")
    bank.open_account(account7)
    assert len(bank.accounts) == 6

    # Test opening duplicate accounts with different account numbers
    account8 = Account.create_account("A006")
    bank.open_account(account8)
    account9 = Account.create_account("A007")
    bank.open_account(account9)
    assert len(bank.accounts) == 8

    print("Bank open_account method tests passed successfully!")


# Run the test
test_bank_open_account()
