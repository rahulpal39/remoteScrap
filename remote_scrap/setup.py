# Automatically created by: scrapyd-deploy

from setuptools import setup, find_packages

setup(
    name='remote_scrap',
    version='1.0',
    packages=find_packages(),
    entry_points={'scrapy': ['settings = remote_scrap']},
)

# curl http://localhost:6800/addversion.json -F project=remote_scrap -F version=r23
# curl http: // localhost: 6800/listjobs.json?project = remote_scrap | python - m json.tool
