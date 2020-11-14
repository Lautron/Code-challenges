def alphabet_position(text):
    # Make dict to represent values
    position = {chr(y):str(y-64) for y in range(65,91)}
    # Replace values
    replaced = [position.get(i.upper(), i) for i in text if i.isalpha()]
    # return
    return ' '.join(replaced)

print(alphabet_position("The narwhal bacons at midnight."))