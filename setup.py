# -*- encoding : utf-8 -*-

from setuptools import setup, find_packages

version = '0.1.0'
readme = open('README.rst').read()

setup(name='matcher_crowd',
      version=version,
      description='A crowd of matchers for Should-DSL expectations',
      long_description=readme,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.4',
          'Programming Language :: Python :: 2.5',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Topic :: Software Development :: Documentation',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Testing',
      ],
      install_requires=['should-dsl'],
      keywords='matcher should dsl assertion bdd python expectation',
      author='Rodrigo Manhães',
      author_email='rmanhaes@gmail.com',
      url='github.com/rodrigomanhaes/matcher_crowd',
      license='MIT License',
      packages=find_packages(),
      test_suite='run_all_examples.test_suite',
      )

