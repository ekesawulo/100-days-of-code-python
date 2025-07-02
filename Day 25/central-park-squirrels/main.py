import pandas

data = pandas.read_csv(
    "Day 25/central-park-squirrels/Central Park Squirrel Census Data.csv"
)
squirrel_colours = data["Primary Fur Color"]
squirrel_dict = {
    "Fur Colour": ["Grey", "Cinnamon", "Black"],
    "Count": [0, 0, 0],
}
for colour in squirrel_colours:
    if colour == "Gray":
        squirrel_dict["Count"][0] += 1
    elif colour == "Cinnamon":
        squirrel_dict["Count"][1] += 1
    elif colour == "Black":
        squirrel_dict["Count"][2] += 1

df = pandas.DataFrame(squirrel_dict)
df.to_csv("Day 25/central-park-squirrels/squirrel_count.csv")
