import json

def update_users(users: dict) -> None:
	print("[*] Updating database")
	with open("database.json", "w") as file:
		for user in users:
			file.write(f"{json.dumps(user)}\n")
	print("[+] Database has been updated!")

def create_user(username: str, password: str) -> None:
	print("[*] Creating user....")
	user_id = count_users()
	users = load_database()
	users.append({"USERNAME":username, "PASSWORD":password, "SHOPPING":{}, "ID":user_id})	
	update_users(users = users)

def count_users() -> int:
	print("[*] Counting users")
	users = load_database()
	num = len(users)
	print(f"[+] USERS: {num}")
	return num


def load_database() -> list:
	users = []
	print("[*] Loading database")	
	try:
		with open("database.json", "r") as file:
			for line in file.readlines():
				users.append(json.loads(line))					
		print("[+] Users loaded")
		return users
	except FileNotFoundError as e:
		print(f"[-] Database not found! {e}")
		return users


if __name__ == '__main__':
	create_user(username = 'billy', password = '1234')
