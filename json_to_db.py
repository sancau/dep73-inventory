# coding=utf-8

# exec this script from the django shell
import datetime
import json
from inventory import models

with open('inventory.json', encoding='utf-8') as json_file:
	content = json_file.readlines()
i = 0
for str in content:
	obj = json.loads(str)

	if obj['item_type'] == 'MiscItem':
		model = models.MiscItem()

		model.name = obj['name']
		model.code = obj['code']
		model.inventory_number = obj['inventory_number']
		model.unit = obj['unit']
		model.price = obj['price']
		model.quantity = obj['quantity']
		model.total_price = obj['total_price']
		model.actual_placement = obj['actual_placement']

		model.save()
		i += 1

		print(i,'MiscItem added') 

	if obj['item_type'] == 'Tool':

		model = models.Tool()

		model.name = obj['name']
		model.last_test_date = datetime.datetime.fromtimestamp(int(obj['last_test'][6:-5])).date()
		model.next_test_date = datetime.datetime.fromtimestamp(int(obj['next_test'][6:-5])).date()
		model.manufacturer = obj['manufacturer']
		model.year_of_production = obj['year_of_production']
		model.specification = obj['specification']
		model.code = obj['code']
		model.inventory_number = obj['inventory_number']
		model.unit = obj['unit']
		model.price = obj['price']
		model.quantity = obj['quantity']
		model.total_price = obj['total_price']
		model.actual_placement = obj['actual_placement']

		model.save()
		i += 1

		print(i,'Tool added')

	if obj['item_type'] == 'TestSystem':

		model = models.TestSystem()

		model.name = obj['name']
		model.purpose = obj['purpose'][:1]
		model.last_test_date = datetime.datetime.fromtimestamp(int(obj['last_test'][6:-5])).date()
		model.next_test_date = datetime.datetime.fromtimestamp(int(obj['next_test'][6:-5])).date()
		model.manufacturer = obj['manufacturer']
		model.year_of_production = obj['year_of_production']
		model.specification = obj['specification']
		model.code = obj['code']
		model.inventory_number = obj['inventory_number']
		model.unit = obj['unit']
		model.price = obj['price']
		model.quantity = obj['quantity']
		model.total_price = obj['total_price']
		model.actual_placement = obj['actual_placement']

		model.save()
		i += 1

		print(i,'TestSystem added')
