import sqlite3
def addDate(date):  # Adds date to dates database, and creates a database with a unique name (of the date)
	conn = sqlite3.connect('dates.db')
	c=conn.cursor()
	date=(date,)
	try:
		c.execute("CREATE TABLE dates (date TEXT)")
	except:
		pass
	conn2=sqlite3.connect(date[0]+".db")
	c2=conn2.cursor()
	c2.execute("CREATE TABLE data (videopath text)")
	conn2.commit()
	conn2.close()
	c.execute("INSERT INTO dates (date) VALUES (?)", date)
	conn.commit()
	conn.close()
