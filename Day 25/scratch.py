import csv
import pandas

# with open("./Day 25/weather_data.csv") as file:
#     data = file.readlines()
# print(data)

# with open("./Day 25/weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for index, row in enumerate(data):
#         if not index:
#             pass
#         else:
#             temperatures.append(int(row[1]))


# data = pandas.read_csv("Day 25/weather_data.csv")
# # print(data["temp"])
# # data_dict = data.to_dict()
# # print(data_dict)
# # print(data["temp"].to_list())
# # temp = data["temp"]
# # print(sum(temp) / len(temp))
# # print(temp.mean())
# # print(data.temp.max())

# # print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_celsius = monday.temp[0]

# print((monday_celsius * 1.8) + 32)
