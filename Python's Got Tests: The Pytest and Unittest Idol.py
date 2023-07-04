def test_bank_update():
    # Create test accounts
    savings_account = SavingsAccount(2000, "SA001", 3)
    current_account = CurrentAccount(-500, "CA001", 1000)

    # Create a Bank object and open the accounts
    bank = Bank()
    bank.open_account(savings_account)
    bank.open_account(current_account)

    # Perform the update
    bank.update()

    # Check if the balances are updated correctly for SavingsAccount
    expected_savings_balance = 2000 + (2000 * 3 / 100)  # Initial balance + interest
    assert savings_account.get_balance() == expected_savings_balance

    # Check if the overdraft notification is displayed for CurrentAccount
    expected_current_balance = -500
    assert current_account.get_balance() == expected_current_balance

    # Perform additional transactions to trigger overdraft notification
    current_account.withdraw(100)
    bank.update()

    # Check if the overdraft notification is displayed again after the update
    expected_current_balance -= 100
    assert current_account.get_balance() == expected_current_balance

    print("Bank update method tests passed successfully!")

# Run the test
test_bank_update()
