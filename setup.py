from setuptools import setup

setup(name='tenma',
      version='0.1',
      description='The funniest joke in the world',
      url='https://github.com/danielcrowley/OpenTestRig-PowerSupply-Tenma',
      author='Daniel Crowley',
      author_email='crowley.daniel@gmail.com',
      license='MIT',
      packages=['tenma'],
      install_requires=[
        'pyserial'
    ])
