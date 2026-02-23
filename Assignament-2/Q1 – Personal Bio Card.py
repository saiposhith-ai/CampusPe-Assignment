
name = "John Doe"
age = 20
course = "Python Programming"
college = "ABC University"
email = "john@example.com"

width = 50

print("┌" + "─" * (width - 2) + "┐")
print("│" + "STUDENT BIO CARD".center(width - 2) + "│")
print("├" + "─" * (width - 2) + "┤")

print(f"│ Name    : {name}".ljust(width - 1) + "│")
print(f"│ Age     : {age} years".ljust(width - 1) + "│")
print(f"│ Course  : {course}".ljust(width - 1) + "│")
print(f"│ College : {college}".ljust(width - 1) + "│")
print(f"│ Email   : {email}".ljust(width - 1) + "│")

print("└" + "─" * (width - 2) + "┘")