import mt940
import pprint

transactions = mt940.parse('tests/jejik/abnamro.sta')

print 'Transactions:'
print transactions
pprint.pprint(transactions.data)

print
for transaction in transactions:
    print 'Transaction: ', transaction
    pprint.pprint(transaction.data)