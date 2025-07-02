import database_manager

def add_item(thing: str, username: str) -> None:
	database = database_manager.load_database()
	print("[*] Adding item to user...")
	for data in database:
		if data["USERNAME"] == username:
			shopping_list = data["SHOPPING"]
			if thing in shopping_list.keys():
				shopping_list[thing] += 1 
			else:
				shopping_list[thing] = 1
			database_manager.update_users(users = database)
			return
	print("[-] Could not find ID")

def list_items() -> dict:
	in_stock = {
		"flowerbed": 9.99,
		"bed": 49.99,
		"sink": 2.99
	}
	return in_stock

if __name__ == '__main__':
	
	add_item("sink", ID=1)
