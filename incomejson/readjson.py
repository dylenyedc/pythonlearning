import json
with open('incomejson/income.json', 'r') as f:
    data = json.load(f)
years = data['years']
incomes = data['incomes']
print('年份:', years)
print('各城市收入:', incomes)