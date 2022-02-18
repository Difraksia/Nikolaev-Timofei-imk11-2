
import cpgames
from setuptools import setup, find_packages


'''readme'''
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()


'''package data'''
package_data = {

    'cpgames.modules.core.tankwar': ['resources/audios/*', 'resources/images/bullet/*', 'resources/images/enemyTank/*', 'resources/images/food/*', 'resources/images/home/*', 'resources/images/others/*', 'resources/images/playerTank/*', 'resources/images/scene/*'],
    'cpgames.modules.core.tankwar.modules': ['levels/*'],
}


setup(
    name=cpgames.__title__,
    version=cpgames.__version__,
    description=cpgames.__description__,
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent'
    ],
    author=cpgames.__author__,
    url=cpgames.__url__,
    author_email=cpgames.__email__,
    license=cpgames.__license__,
    include_package_data=True,
    package_data=package_data,
    install_requires=list(open('requirements.txt', 'r').readlines()),
    zip_safe=True,
    packages=find_packages(),
)

