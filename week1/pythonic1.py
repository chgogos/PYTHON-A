a, b = 7, 42

# μη πυθωνικός κώδικας
temp = a
a = b
b = temp
print(a, b)

# πυθωνικός κώδικας
a, b = b, a
print(a, b)
