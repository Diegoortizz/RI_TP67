
s = "\n , faster about 20% to 30% faster at running applications than my Vista ,  seriously\n  Yes, it'll make your computer run a bit slower but\n ,  Fast startup and performance\n  Also, in my non, benchmarked experience, Windows 7 has been at least as fast as XP if not faster "

# print(s.strip("\n"))
print(" ".join(s.strip("\n").split()).replace(",", "").split())

# print(s.strip("\n").split(","))