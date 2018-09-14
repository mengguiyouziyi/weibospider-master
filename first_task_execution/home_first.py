import sys

sys.path.append('.')
sys.path.append('..')

from tasks import execute_home_task
from utils.set_adsl import set_interface

if __name__ == '__main__':
	set_interface(sys.argv[1])
    execute_home_task()
