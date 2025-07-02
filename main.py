import database_manager
import shop
from flask import Flask, render_template, request, redirect, url_for, session


app = Flask(__name__)
app.secret_key = "123"


@app.route("/signup", methods=["POST", "GET"])
def signup() -> render_template:
	error = None
	if request.method == "POST":
		database = database_manager.load_database()
		print([data["USERNAME"] for data in database])
		username = request.form.get("username")
		password = request.form.get("password")
		repeat = request.form.get("verify")
		print(password)
		print(repeat)
		if password == repeat and username not in [data["USERNAME"] for data in database]:
			database_manager.create_user(	
							username = username, 
							password = password
			)	
			return redirect(url_for('home_page'))	
		else:
			print("[-] Error: Password does not match or username is in database")
			error = "Passwords do not match try again!"
		
	return render_template("signup.html")


@app.route("/login", methods=["POST", "GET"])
def login() -> render_template:
	if request.method == "POST":
		users = database_manager.load_database()
		username = request.form.get("username")
		password = request.form.get("password")
		for user in users:
			if user["USERNAME"] == username and user["PASSWORD"] == password:
				session["username"] = username
				print("[+] Logged in")
				return redirect(url_for("logged_in"))
			
	return render_template("login.html")
@app.route("/", methods=["POST", "GET"])
def home_page() -> render_template:
	if request.method == "POST":	
		if 'login' in request.form:
			return redirect(url_for('login'))
		elif 'signup' in request.form:
			return redirect(url_for('signup'))	
	return render_template("home_page.html")

@app.route("/logout", methods=["POST", "GET"])
def logout() -> render_template:
	session.pop("username", None)
	return redirect(url_for("home_page"))

@app.route("/profile/in_bag/")
def currently_saved() -> render_template:
	database = database_manager.load_database()
	in_stock = [data["SHOPPING"] for data in database if data["USERNAME"] == session["username"]][0]
	
	print(in_stock)
	return render_template("checkout.html", in_stock=in_stock)
		
@app.route("/profile", methods=["POST", "GET"])
def logged_in() -> render_template:
	if "username" in session:
		username = session["username"]
		in_stock = shop.list_items() 
		if request.method == "POST":
			user_item = request.form.get("item")
			shop.add_item(user_item, username = username)
				
		return render_template("profile.html", username = username, in_stock = in_stock)
	else:
		return redirect(url_for("home_page"))

app.run(debug=True)
