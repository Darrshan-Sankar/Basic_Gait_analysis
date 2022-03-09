import os
import pandas as pd
from threading import Thread
from functools import partial

print("[INFO] Starting Gait analysis!!.......")

files = os.listdir()
if len(files) > 10:
    print('[WARNING] Already an instance of the program has been executed!..... \n [INFO] Please clear the old Output and execute this program again for the required result ')

else:
    os.system('python gait_base.py')
    os.system('python combine_base.py')
    count = 0
    for file in os.listdir():
        if file.startswith("base"):
            count += 1 
    for i in range(count):
        os.remove('base'+str(i+1)+'.csv')
    os.system('python gait_result.py')
    os.system('python combine_result.py')
    count = 0
    for file in os.listdir():
        if file.startswith("result"):
            count += 1 
    for i in range(count):
        os.remove('result'+str(i+1)+'.csv')

    print('[INFO] Task Completed Succesfully!!...')
    print("[INFO] ASCERTAINING THE ANALYSIS...")
    df1 = pd.read_csv('out1.csv', names = ['x', 'y', 'z', 'visibility'])
    df2 = pd.read_csv('out2.csv', names = ['x', 'y', 'z', 'visibility'])
    df = (df2/df1)*100
    df = df.dropna()
    print(df)
    results_x = df['x'].to_list()
    results_y = df['y'].to_list()
    results_z = df['z'].to_list()
    
    x = 0
    y = 0
    z = 0

    for i in results_x:
        x += i
    for j in results_y:
        y += i
    for k in results_z:
        z += i
    x = x/len(results_x)
    y = y/len(results_y)
    z = z/len(results_z)

    os.system("output1.gif")
    os.system("output2.gif")

    if x > 70 and y>70 and z>70 and x<=100 and y<=100 and z<=100:
        print("The First sample and the second sample belongs to the same person")
    else:
        print("The samples provided does not match")