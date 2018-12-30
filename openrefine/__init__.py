import os
import sys

def main():
    """
    Start the openrefine process
    """
    refine_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'extracted',
        'refine'
    )
    os.execv(refine_path, sys.argv)