# Automatically created by: scrapyd-deploy

from setuptools import setup, find_packages

setup(
    name='scraper',
    version='1.0',
    packages=find_packages(),
    entry_points={'scrapy': ['settings = scraper']},
)

# curl http://localhost:6800/addversion.json -F project=scraper -F version=r23
# curl http: // localhost: 6800/listjobs.json?project = remote_scrap | python - m json.tool
