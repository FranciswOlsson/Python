#Strings
quote = "\"Backslash includes quote"

multi_line_quote = '''this is a multi
line quote"'''

print("%s %s %s" %('quote like this', quote, multi_line_quote))

print('\n'*3)

print("I don't like ", end="")
print("newlines")