import requests
import sqlite3
import time
import hashlib
from bs4 import BeautifulSoup


try:
    conn = sqlite3.connect("hash.db")

except Exception as err:
    print("I could not connect to the database!!", str(err))
    exit()

else:
    cur  = conn.cursor()
    cur.execute("CREATE TABLE if not exists Hash (TimeStamp TEXT, Hash TEXT)")

    url  = input("Enter a domain desired: ")

    count = 0 

    while True:

        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        print(soup.prettify())
        codeHtml = soup.prettify()


        Hash_Code_Html = hashlib.sha256(codeHtml.encode())


        tm = time.time()
        current_time = time.ctime(tm)
        

        cur.execute("INSERT OR REPLACE INTO Hash (TimeStamp, Hash) VALUES (\"%s\", \"%s\");" 
                    % (current_time, Hash_Code_Html.hexdigest()))
        conn.commit()

        count += 1
        print("ROUND {}".center(150,"*").format(count))

        time.sleep(20)


        



