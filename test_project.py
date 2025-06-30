from project import check_balance, deposit, withdraw


def test_check_balance(capsys):
    accounts = {'0000111122223333': {'pin': '111', 'balance': 300.0, 'transactions': []}}
    balance = check_balance('0000111122223333', accounts)
    captured = capsys.readouterr()
    assert balance == 300.0
    assert 'Your balance is 300.00€' in captured.out


def test_deposit():
    accounts = {'0000111122223333': {'pin': '111', 'balance': 0.0, 'transactions': []}}
    deposit('0000111122223333', accounts, deposit_amount=100.0)
    assert accounts['0000111122223333']['balance'] == 100.0
    assert '+100.00€' in accounts['0000111122223333']['transactions']


def test_withdraw():
    accounts = {'0000111122223333': {'pin': '111', 'balance': 100.0, 'transactions': []}}
    withdraw('0000111122223333', accounts, withdraw_amount=50.0)
    assert accounts['0000111122223333']['balance'] == 50.0
    assert '-50.00€' in accounts['0000111122223333']['transactions']

