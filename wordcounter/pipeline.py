class Task:
    def __init__(self, func):
        self.func = func
        self.next_task = None

    def __add__(self, other):
        self.next_task = other
        return other
    
    def __call__(self):
        self.func()
        if self.next_task:
            self.next_task()

@Task
def start():
    print('Starting pipeline...')

@Task
def extract():
    print('Extracting data from source...')

@Task
def transform():
    print('Performing transformations on data...')

def load():
    print('Loading transformed data into database...')

load = Task(load)

start + extract + transform + load

start()
