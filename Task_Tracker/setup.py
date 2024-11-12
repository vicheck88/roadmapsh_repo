from setuptools import setup

setup(
    name='task_cli',
    version='0.1',
    py_modules=['task_cli'],  # This tells setuptools that task-cli.py is the module
    entry_points={
        'console_scripts': [
            'task_cli=task_cli:main',  # This will call the 'main' function in task-cli.py
        ],
    },
)