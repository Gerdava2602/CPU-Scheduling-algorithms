import numpy as np
from utils import create_processes

def fcfs(processes):
    n = len(processes)
    rows = []
    total_time = 0
    processes = processes[processes[:,1].argsort()]
    process = 0
    print(processes)
    for burst, arrival in processes:
        if process == 0:
            wait_time = 0
            total_time += burst + arrival
            process += 1
        else:
            wait_time = total_time - arrival
            total_time += burst    
        turnaround_time = wait_time + burst
        print('Process {}: wait time = {}, turnaround time = {}, total_time = {}'.format(process, wait_time, turnaround_time, total_time))
        rows.append([burst, arrival,wait_time, turnaround_time])
    rows = np.array(rows)
    return {
        'Gantt Chart': rows,
        'Average Wait Time': rows[:,2].mean(),
        'Average Turnaround Time': rows[:,3].mean(),
    }

process_1 = create_processes(int(input('Enter number of processes: ')))
print(fcfs(process_1))