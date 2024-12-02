print("Le Hoa Hiep")
print("235752021610073")
def calculate_balance (transactions):
    balance = 0
    for transaction in transactions:
      action, amount = transaction.split()
      amount = int(amount)
      if action == 'D':
          balance += amount
      elif action == 'W':
          balance -= amount
    return balance
input_transactions = []
print("nhập nhật kí giao dịch (nhap 'x' để kết thúc):")
while True:
    transaction = input()
    if transaction.lower() == 'x':
        break
    input_transactions.append(transaction)
final_balance = calculate_balance (input_transactions)
print("số tiền thực tài khoản là :", final_balance)
