import numpy as np

#Funciones necesarias para la realización óptima de los algoritmos
def create_processes(n, max=10):
    return np.random.randint(0, max, size=(n,2))

class process():
    def __init__(self, id, burst, arrival, left=False):
        self.id = id
        self.burst = burst
        self.arrival = arrival
        self.wait_time = 0
        self.turnaround_time = 0
        if left:
            self.left = burst

    def __repr__(self):
        return 'id: {}, burst:{}, arrival: {}, wait time: {}, turnaround :{}'.format(self.id, self.burst, self.arrival, self.wait_time, self.turnaround_time)

    def to_numpy(self):
        return np.array([self.id, self.burst, self.arrival, self.wait_time, self.turnaround_time, self.left])