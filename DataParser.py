import requests
from bs4 import BeautifulSoup
import json
import os 
import datetime

cwd = os.getcwd()
base_url = input("Please Specify url: ")
timeInterval = input("Please chart time in mins: ")
fileWrite = input("Do you want to write to file (y/n): ")

r = requests.get(base_url)

soup = BeautifulSoup(r.text, 'html.parser')

var_all_scripts = soup.find_all('script', type="text/javascript")

#data = json.loads(all_scripts[6].get_text()[27:])

#2. Go through the aisol folder and collect all files that have modified dates after the target date and also have dll extension ... 

script_line_anchor = "initData.content"
def get_targetLine(all_scripts, line_anchor):
	for script_tag in all_scripts:
		for line in (script_tag.get_text()).splitlines():
			if line_anchor in line:
				return line
	return 0

var_target_line = get_targetLine(var_all_scripts, script_line_anchor)

prop_line_anchor_start = "TRADING_FEES"
prop_line_anchor_end = "Deluxe Tuner BE"
def get_target_props(target_line, line_anchor_start, line_anchor_end):

	target_start = target_line.find('{')
	target_end = target_line.rfind('}') + 1

	target_line = target_line[target_start:target_end]
	target_start = target_line.find(line_anchor_start)
	target_end = target_line.find(line_anchor_end) + 1

	target_start = target_start - (target_start - (target_line[:target_start]).rfind('{'))
	target_end = target_end + (target_line[target_end:]).find('}') + 1

	target_line = target_line[(target_start+1):(target_end-1)]

	jsonList=[]
	for line_entry in target_line.split('},{'):
		jsonList.append(json.loads( '{' + line_entry + '}' ))

	return jsonList

var_jsonList = get_target_props(var_target_line, prop_line_anchor_start, prop_line_anchor_end)
# the jsonList entry looks like this: {'defval': 0.25, 'id': 'in_0', 'isFake': True, 'max': 1000000000000, 'min': 0, 'name': 'TRADING_FEES', 'step': 0.05, 'type': 'float'}

prop_anchor_start = "in_0"
prop_anchor_end = "in_99"
def get_target_values(target_line, line_anchor_start, line_anchor_end):

	target_start = target_line.find('{')
	target_end = target_line.rfind('}') + 1

	target_line = target_line[target_start:target_end]
	target_start = target_line.find(line_anchor_start)
	#print(str(target_start))
	target_end = target_line.find(line_anchor_end) + 1
	#print(str(target_end))

	target_start = target_start - (target_start - (target_line[:target_start]).rfind('{'))
	#print(str(target_start))
	target_end = target_end + (target_line[target_end:]).find(',') + 1 # note, the end for target find is a comma , as opposed to a curly brace
	#print(str(target_end))

	target_line = target_line[(target_start+1):(target_end-1)]
	
	return json.loads( '{' + target_line + '}' )

var_json_prop_values = get_target_values(var_target_line, prop_anchor_start, prop_anchor_end)
# the json_prop_values look as such: {'in_0': 0.1, 'in_1': 'MACD', 'in_10': 14, 'in_100': 'AUTO', ...

# go through and print out the values
def prepare_final_draft(jsonList, json_prop_values):
	final_prop_list={}
	for entry in jsonList:
		final_prop_list[entry['name']] = json_prop_values[entry['id']]
	return final_prop_list

final_props = prepare_final_draft(var_jsonList, var_json_prop_values)
#print(str(final_props))

# get the market name
var_market_anchor_string = '"symbol":'

def extract_marketName(all_scripts, line_anchor, market_anchor_string):
	target_line = get_targetLine(all_scripts, line_anchor)
	target_start = target_line.find('{')
	target_end = target_line.rfind('}') + 1
	target_line = target_line[target_start:target_end]

	#get market name
	target_start = target_line.find(market_anchor_string)
	target_end = target_start + (target_line[target_start:]).find(',')
	market = target_line[target_start:target_end]
	return market

market = extract_marketName(var_all_scripts, script_line_anchor, var_market_anchor_string)

now = datetime.datetime.now()
time_now = now.strftime("%Y_%m_%d_%H_%M")
print(time_now)
print(market)
print("The period is: " + timeInterval + " mins")
print("---------------------------------------------")
for key, value in final_props.items():
	print("%-20s %-30s" % (key, str(value)))

if fileWrite == 'y':
	os.path.join(cwd, (time_now + '.txt'))
	file = open(os.path.join(cwd, (time_now + '.txt')), 'w+')
	file.write(time_now + '\n')
	file.write(market + '\n')
	file.write("The period is: " + timeInterval + " mins" + '\n')
	file.write("---------------------------------------------" + '\n')
	for key, value in final_props.items():
		file.write("%-20s %-30s" % (key, str(value)) + '\n')
	file.close

