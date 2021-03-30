from halo import Halo
from time import sleep

tasks = ['breakfest', 'launch', 'dinner']

# for task in tasks:
#   spinner = Halo(text=f'Eating {task}', spinner='dots')
#   spinner.start()
#   sleep(3)
#   spinner.succeed(text=f'Eated {task}')

# for task in tasks:
#   with Halo(text=f'Eating {task}', spinner='dots') as spinner:
#     sleep(3)
#     spinner.succeed(text=f'Eated {task}')



from functools import wraps
from contextlib import contextmanager
class HaloExtend:
  def __init__(self, text, spinner='dots', **kwargs):
    self.text = text
    self.spinner = spinner
    self.kwargs = kwargs

  def __call__(self, func):
    @wraps(func)
    def wrapped(*args, **kwargs):
      halo = Halo(text=self.text.format(*args, **kwargs), spinner=self.spinner)
      halo.start()
      func(*args, **kwargs)
      halo.succeed()
    return wrapped


@HaloExtend(text='Loading {task}', spinner='line')
def run_task(task):
  '''pass text'''
  sleep(3)


for task in tasks:
  run_task(task=task)
