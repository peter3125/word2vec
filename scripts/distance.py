#!/usr/bin/python3.5
import math

vecs = []
with open('../data/test-vector.txt') as reader:
  for line in reader:
    line = line.strip()
    parts = line.split(' ')
    if len(parts) > 2:
      word = parts[0]
      vector = [float(v) for v in parts[1:]]
      vecs.append((word, vector))

print("loaded " + str(len(vecs)) + " vectors")

def dist(v1, v2):
  total = 0.0
  for i in range(len(v1)):
    delta = v1[i] - v2[i]
    total += delta * delta
  return math.sqrt(total)

for i in range(len(vecs)):
  w1 = vecs[i][0]
  wv1 = vecs[i][1]
  for j in range(i + 1, len(vecs)):
    w2 = vecs[j][0]
    wv2 = vecs[j][1]
    print("%s,%s=%s" % (w1, w2, dist(wv1,wv2))

