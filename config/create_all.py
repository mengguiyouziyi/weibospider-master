import sys

# to work well inside config module or outsize config module
sys.path.append('..')
sys.path.append('.')

from db.tables import *
from db.basic import metadata
from utils.set_adsl import set_interface


def create_all_table():
    metadata.create_all()


if __name__ == "__main__":
    set_interface("10.146.252.112")
    create_all_table()
