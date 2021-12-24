# Part 2


with open("input17") as f:
    input = f.readline().strip().split(": x=")[1]
    x, y = input.split(", y=")
    minX, maxX = list(map(int, x.split("..")))
    minY, maxY = list(map(int, y.split("..")))


initialY = abs(minY)-1
print((initialY*(initialY+1))//2)



# Part 1:
# target area: x=20..30, y=-10..-5
#
# with open("input17") as f:
#     input = f.readline().strip().split(": x=")[1]
#     x, y = input.split(", y=")
#     minX, maxX = list(map(int, x.split("..")))
#     minY, maxY = list(map(int, y.split("..")))
#
#
# initialY = abs(minY)-1
# print((initialY*(initialY+1))//2)
