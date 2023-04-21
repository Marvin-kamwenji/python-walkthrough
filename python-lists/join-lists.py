colors = ["blue", "red", "green", "brown"]
shapes = ["square", "rectangle", "oval", "circle"]

# CONCATENATION
colorsAndShapes = colors + shapes
print(colorsAndShapes)

# USING APPEND
for x in shapes:
    colors.append(x)

print(colors)

# USING EXTEND FUNCTION
shapes.extend(colors)
print(shapes)