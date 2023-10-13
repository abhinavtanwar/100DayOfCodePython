import turtle
import pandas

states = ["jammu kashmir", "himachal", "punjab", "uttarakhand", "haryana", "rajasthan", "uttar pradesh", "bihar",
          "sikkim", "west bengal", "assam", "arunachal pradesh", "meghalaya", "nagaland", "manipur", "mizoram",
          "tripura", "gujarat", "madhya pradesh", "chhattisgarh", "jharkhand", "maharashtra", "odisha", "goa",
          "karnataka", "telangana", "andhra pradesh", "kerala", "tamil nadu"]

print(len(states))
x_cords = []
y_coords = []


def GetCoords(x, y):
    x_cords.append(x)
    y_coords.append(y)


screen = turtle.Screen()
screen.setup(width=700, height=700)
screen.addshape("IndiaMap.gif")
turtle.shape("IndiaMap.gif")
screen.onscreenclick(fun=GetCoords)
screen.mainloop()


data_dict = {
    "states": states,
    "x coords": x_cords,
    "y coords": y_coords
}
data = pandas.DataFrame(data_dict)
data.to_csv("State_Coordinate_Data.csv")
print(data)