from elasticsearch import Elasticsearch
import hashlib


es = Elasticsearch(hosts=[{'host': "127.0.0.1", 'port': 9200}])

res = es.search(index="ssh", body={
    "aggs": {
      "sources": {
        "terms": {
          "field": "sourceEntryIp",
          "size": 10000011
        }
      }
    }
  })

count = 0

data = {}



for hit in res['aggregations']['sources']['buckets']:

    if (count <= 11):
        print(str(hit["key"]) + " Counter: " + str(hit["doc_count"]))

    count = count + 1


print("Total number of unique IPs:" + str(count))

