import mt940
import pprint

mt940.tags.BalanceBase.scope = mt940.models.Transaction

# The currency has to be set manually when setting the BalanceBase scope to Transaction.
transactions = mt940.models.Transactions(processors=dict(
    pre_statement=[
        mt940.processors.add_currency_pre_processor('EUR'),
    ],
))

with open('tests/jejik/abnamro.sta') as f:
    data = f.read()

transactions.parse(data)

for transaction in transactions:
    print 'Transaction: ', transaction
    pprint.pprint(transaction.data)

