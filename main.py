#MapPlot.py
#Name: Edip Uman
#Date: 4/19/26
#Assignment: Lab 10 

import csv
import matplotlib.pyplot as plt
 

trials = []
reaction_times = []
 
with open('reaction_time_data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  
    for row in reader:
        trial = int(row[0])
        time = float(row[1])
        trials.append(trial)
        reaction_times.append(time)
 

clean_trials = []
clean_times = []
 
for t, rt in zip(trials, reaction_times):
    if rt > 0:
        clean_trials.append(t)
        clean_times.append(rt)
 

plt.plot(clean_trials, clean_times, marker='o', linestyle='-')
plt.title('Reaction Time Over Trials')
plt.xlabel('Trial Number')
plt.ylabel('Reaction Time (ms)')
plt.grid(True)
plt.savefig('reaction_time_graph.png')
plt.show()

# As the number of trials increases the reaction time decreases steadily. The downward trend of the graph shows the consisent decrease in reaction time. 

    
  
