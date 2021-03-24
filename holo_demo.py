from halo import Halo
from time import sleep

tasks=['breakfest','launch','dinner']

for task in tasks:
  spinner = Halo(text=f'Eating {task}', spinner='dots')
  spinner.start()
  sleep(3)
  spinner.succeed(text=f'Eated {task}')