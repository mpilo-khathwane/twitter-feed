import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

REQUIREMENTS = []

DEV_REQUIREMENTS = [
    'black == 22.*',
    'build == 0.7.*',
    'coveralls == 3.*',
    'flake8 == 4.*',
    'isort == 5.*',
    'mypy == 0.942',
    'pytest == 7.*',
    'pytest-cov == 3.*',
    'twine == 4.*',
]

setuptools.setup(
    name='twitter-feed',
    version='0.1.0',
    description='This is a program to simulate a twitter-like feed.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/mpilo-khathwane/twitter-feed',
    author='mpilo-khathwane',
    license='MIT',
    packages=setuptools.find_packages(),
    package_data={'twitter-feed': ['py.typed']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=REQUIREMENTS,
    extras_require={
        'dev': DEV_REQUIREMENTS,
    },
    entry_points={
        'console_scripts': [
            'twitter-feed=twitter_feed.feed_module:main',
        ]
    },
    python_requires='>=3.7, <4',
)
