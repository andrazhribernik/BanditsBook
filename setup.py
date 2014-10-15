from distutils.core import setup

setup(
    name = 'bandits_book',
    version = '0.0.1',
    packages = [
    	'python',
	    'python/algorithms',
	    'python/algorithms/ucb', 
	    'python/algorithms/epsilon_greedy', 
	    'python/algorithms/exp3'
    ]
)