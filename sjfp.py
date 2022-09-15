import numpy as np
from utils import create_processes, process

#Función que realiza el algoritmo SRF de forma preemptive
def srtf(processes):
    #Helper functions
    def process_creation(processes):
        i = 0
        all_processes = []
        for burst, arrival in processes:
            all_processes.append(process(i, burst, arrival, left=True))
            i += 1
        return all_processes
    def add_all(processes, total_time, except_id=None):
        if except_id is None:
            return
        for process in processes:
            if process[0] != except_id and process[2] < total_time:
                process[3] += 1
        return processes

    def subs_actual(processes, id):
        for process in processes:
            if process[0] == id:
                process[-1] -= 1
        return processes

    def depurate(processes):
        actual = []
        final = []
        for process in processes:
            if process[-1] > 0:
                actual.append(process)
            else:
                process[-2] = process[1] + process[3]
                final.append(process)
        return np.array(actual), np.array(final)
    processes = process_creation(processes)
    processes = np.array([ex.to_numpy() for ex in processes])
    processes = processes[processes[:,2].argsort()]
    total_time = 0
    actual_id = processes[0][0]
    final = []
    while True:
        processes = subs_actual(processes, actual_id)
        processes = add_all(processes, total_time, except_id=actual_id)
        processes, new_final = depurate(processes)
        if len(new_final) > 0:
            final.extend(new_final)
        if len(processes) == 0:
            total_time+=1
            break
        processes = processes[np.lexsort((processes[:,2],processes[:,1], processes[:,-1]))]
        if processes[0][2] <= total_time:
            actual_id = processes[0][0]
        total_time+=1
    final = np.array(final)
    return {
        'Gantt Chart': final[:,:-1],
        'Average Wait Time': final[:,3].mean(),
        'Average Turnaround Time': final[:,4].mean(),
    }

process_1 = create_processes(int(input('Enter number of processes: ')), max=100)
print(srtf(process_1))