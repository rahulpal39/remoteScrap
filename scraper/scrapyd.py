from scrapyd_api import ScrapydAPI
scrapyd = ScrapydAPI('http://localhost:6800')
# $ curl http: // localhost: 6800/addversion.json - F project = scraper - F version = r23 - F egg = @project.egg

# print()