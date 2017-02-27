import os
from io import open
from setuptools import setup

DIST_NAME = 'DiscordMusicBot'
VERSION = 'v1.0.0'
AUTHOR = 'James Payne'
EMAL = 'jepayne1138@gmail.com'
GITHUB_USER = 'jepayne1138'
GITHUB_URL = 'https://github.com/{GITHUB_USER}/{DIST_NAME}'.format(**locals())

# Get the long description from the README file
setup_dir = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(setup_dir, 'README.md'), encoding='utf-8') as readme:
    long_description = readme.read()

setup(
    name=DIST_NAME,
    packages=['discordmusicbot'],
    version=VERSION,
    description='A modification of the discord.py playlist example.',
    author=AUTHOR,
    author_email=EMAL,
    url=GITHUB_URL,
    license='MIT',
    download_url='{GITHUB_URL}/tarball/{VERSION}'.format(**locals()),
    keywords='',
    install_requires=[
        'requests[security]==2.10.0',
        'six==1.10.0',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'console_scripts': [
            'musicbot = discordmusicbot.console:entry',
        ],
    }
)
