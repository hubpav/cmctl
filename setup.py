from setuptools import setup

setup(
    name='cmctl',
    version='1.0.0',
    description='Conductometer Control Tool',
    url='https://github.com/hubpav/cmctl',
    author='Pavel Hübner',
    author_email='pavel.hubner@hardwario.com',
    license='MIT',
    packages=['cmctl'],
    install_requires=[
        'click==6.7', 'pyserial==3.4'
    ],
    entry_points='''
        [console_scripts]
        cmctl=cmctl.cli:main
    ''',
)
