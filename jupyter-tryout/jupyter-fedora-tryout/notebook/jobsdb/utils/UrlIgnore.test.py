from UrlIgnore import UrlIgnore

url_ignore_dict = UrlIgnore()

url_ignore_dict.add('https://hk.jobsdb.com/job/73509007?type=standout&ref=search-standalone#sol=ad24f6f9405c4b6dfc3e2e7f9def190ba6d7a37b')

print(url_ignore_dict.check('https://hk.jobsdb.com/job/73509007?type=standout&ref=search-standalone#sol=ad24f6f9405c4b6dfc3e2e7f9def190ba6d7a37b'))
