# import hw_0 to run experiment
from hw_0 import *

# List of experiment will run in this file
"""
    python hw_0.py --exp 1 --hidden 2 --epochs 10
    python hw_0.py --exp 2 --hidden 3 --epochs 100
    python hw_0.py --exp 3 --hidden 4 --epochs 600
    python hw_0.py --exp 4 --hidden 4 --epochs 1000
    python hw_0.py --exp 5 --hidden 5 --epochs 4000
    python hw_0.py --exp 6 --hidden 10 --epochs 7000
    python hw_0.py --exp 7 --hidden 10 --epochs 7000
    python hw_0.py --exp 8 --hidden 12 --epochs 8000
    python hw_0.py --exp 9 --hidden 15 --epochs 9000
    python hw_0.py --exp 10 --hidden 20 --epochs 10000
"""
display_learning_curve_set('results','hw0_results')
display_histogram_absolute_error('results', 'hw0_results')
