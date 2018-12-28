from elasticsearch import Elasticsearch
import hashlib


es = Elasticsearch(hosts=[{'host': "127.0.0.1", 'port': 9200}])

res = es.search(index="ssh", body={
    "aggs": {
      "usernames": {
        "terms": {
          "field": "username",
          "size": 10000011
        }
      }
    }
  })

count = 0

for hit in res['aggregations']['usernames']['buckets']:
    print(hit["key"])
    count = count + 1

print("Total usernamea: " + str(count))

