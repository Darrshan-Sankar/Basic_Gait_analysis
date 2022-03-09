import pandas as pd
import matplotlib.pyplot as plt
import os

fout=open("out1.csv","a")
# first file:
for line in open("base1.csv"):
    fout.write(line)
# now the rest:
count = 0
for file in os.listdir():
    if file.startswith("base"):
        count += 1    
for num in range(count-1):
    f = open("base"+str(num+2)+".csv")
    for line in f:
         fout.write(line)
    f.close() # not really needed
fout.close()

labels = ['x', 'y', 'z', 'visibility']
df = pd.read_csv('out1.csv', names = labels)
print(df)

plt.plot(df['x'],df['y'],df['z'], color='green', linestyle='dashed', linewidth=0.05)
x=[]
for i in range(0, 6600):
    if i%100 == 0:
        x.append(i)
plt.xticks(x)
plt.title("Base Graph")
plt.savefig('Base.png')
plt.show()
