# Automatically created by: scrapyd-deploy

from setuptools import setup, find_packages

setup(
    name='project',
    version='1.0',
    packages=find_packages(),
    entry_points={'scrapy': ['settings = scraper.settings']},
)

# curl http://localhost:6800/addversion.json -F project=scraper -F version=r23
