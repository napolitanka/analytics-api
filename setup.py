from setuptools import setup

setup(
    name='analytics-cli',
    version='0.1',
    py_modules=['ancli'],
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        ancli=ancli.cli:cli
    ''',
)