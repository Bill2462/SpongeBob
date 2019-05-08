from setuptools import setup
import sys

#get readme file
def readme():
    with open('README.md') as f:
        return f.read()

setup(name='spongeBob',
      version='0.1',
      author='Krzysztof Adamkiewicz',
      author_email='kadamkiewicz835@gmail.com',
      url='https://github.com/Bill2462/SpongeBob',
      description='Calculate material porosity based on image processing using openCV.',
      long_description=readme(),
      packages=['spongeBob'],
      classifiers=['Development Status :: 3 - Alpha',
                   'Intended Audience :: Education',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 3',
                  ],
     install_requires=[
          'opencv-python'
      ],
     )
