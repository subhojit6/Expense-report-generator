ledger = [
    {"amount": 30000, "source": "salary", "type": "income"},
    {"amount": 1500, "source": "freelance", "type": "income"},
    {"amount": 500, "category": "groceries", "type": "expense"},  # Uses 'category'
    {"amount": 1200, "category": "rent", "type": "expense"}       # Uses 'category'
]

for item in ledger:
    amount = item["amount"]
    type = item["type"]

    if type == "income":
        pass