import numpy as np
from utils import create_processes

def sjf(processes):
    def order_inside(processes, time):
        new_processes = []
        last_processes = []
        for process in processes:
            process = process.tolist()
            if process[1] <= time:
                new_processes.append(process)
            else:
                last_processes.append(process)
        new_processes.sort()
        return np.array(new_processes + last_processes)
    n = len(processes)
    rows = []
    total_time = 0
    processes = processes[processes[:,1].argsort()]
    process = 0
    for i in range(len(processes)):
        if process == 0:
            (burst, arrival), processes = processes[0], processes[1:]
            wait_time = 0
            total_time += burst + arrival
            process += 1
        else:
            processes = order_inside(processes, total_time)
            (burst, arrival), processes = processes[0], processes[1:]
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

process_1 = create_processes(int(input('Enter number of processes: ')), max=100)
print(sjf(process_1))