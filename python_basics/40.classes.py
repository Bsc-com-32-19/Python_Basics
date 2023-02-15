class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


# creating object


Point1 = Point()
Point1.x = 10
Point1.y = 20
print(Point1.x)
Point1.draw()

Point2 = Point()
Point2.x = 2
print(Point2.x)
Point2.move()
