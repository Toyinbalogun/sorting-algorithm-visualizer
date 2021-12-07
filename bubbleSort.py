import time

def bubble_sort(data, drawData, timeTick):
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, ["green" if x == j or x == j+1 else "red" for x in range(len(data))])
                time.sleep(timeTick)
    # return data
    drawData(data, ["green" for x in range(len(data))])

# TEST
# data=[1,4,5,6,3,0]
# print(bubble_sort(data))