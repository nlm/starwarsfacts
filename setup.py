from setuptools import setup,find_packages

setup(
    name = "starwarsfacts",
    version = "0.1",
    packages = ['starwarsfacts'],
    author = "Nicolas Limage",
    author_email = 'github@xephon.org',
    description = "Star Wars fake facts and spoilers generator",
    license = "GPL",
    keywords = "starwars facts spoilers",
    url = "https://github.com/nlm/starwarsfacts",
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    install_requires = [
    ],
    entry_points = {
        'console_scripts': [
            'swfacts = starwarsfacts.__init__:main',
        ],
    },
)
