from setuptools import setup, find_packages

setup(
    name='rishplot',
    version='0.1.0',
    description='Python library for creating complex, customized subplots in Matplotlib',
    author='ishiyeahman',
    author_email="ishiyeahman@gmail.com",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
