from setuptools import setup, find_packages
from konstable import __version__

setup(
    name='konstable',
    version=__version__,
    description='A Python project.',
    long_description=open('README.md', encoding='utf-8').read(),
    url='https://github.com/zafarali/konstable',
    author='Zafarali Ahmed',
    author_email='zafarali.ahmed@gmail.com',
    license='MIT',
    packages=find_packages(exclude=['tests*']),
    classifiers=[
        'Development Status :: 3 - Alpha'
    ],
    python_requires='>=3.4.3',
    entry_points={
        'console_scripts':[
            'konstable=konstable:main'
        ]
    }
)