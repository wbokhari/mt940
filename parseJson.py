import json
import mt940


transactions = mt940.parse('tests/jejik/abnamro.sta')

print(json.dumps(transactions, indent=4, cls=mt940.JSONEncoder))