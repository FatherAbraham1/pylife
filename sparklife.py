# from collections import defaultdict

# from functools import partial

generations = 300

def neighbors(point):
  for x in range(point[0]-1, point[0]+2):
    for y in range(point[1]-1, point[1]+2):
      yield ((x,y), 0.5 if (x,y) == point else 1.0)


input = sc.textFile("glider_gun.txt")
cells = input.map(lambda l: l.split(',')).map(lambda l: (int(l[0]), int(l[1])))
for generations in range(0, generations):
  neighbs = cells.flatMap(neighbors)
  result = neighbs.reduceByKey(lambda a,b: a + b)
  cells = result.filter(lambda p:  2.5 <= p[1] <= 3.5 ).map(lambda a: a[0])

cells.saveAsTextFile('glider_out_300')