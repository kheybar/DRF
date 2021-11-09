"""

    json => dump, domps, load, loads

"""

import json

with open('what-is-json.js') as f:
    data = json.load(f)

# change
for i in data:
    del i['age']
    i['programer'] = True

with open('result-json.js', 'w') as d:
    json.dump(data, d, indent=2) # اول اطلاعات، دوم نام سند، سوم میزان فاصله گذاری

