from elasticsearch import Elasticsearch
import hashlib


es = Elasticsearch(hosts=[{'host': "127.0.0.1", 'port': 9200}])

res = es.search(index="ssh", body={
    "aggs": {
      "usernames": {
        "terms": {
          "field": "originalRequestString",
          "size": 10000011
        }
      }
    }
  })

count = 0



for hit in res['aggregations']['usernames']['buckets']:
    print(str(hit["key"]) + " Counter: " + str(hit["doc_count"]))
    count = count + 1

print("Total scripts: " + str(count))
