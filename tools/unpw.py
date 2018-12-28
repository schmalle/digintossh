from elasticsearch import Elasticsearch
import hashlib


es = Elasticsearch(hosts=[{'host': "127.0.0.1", 'port': 9200}])


count = 0

res = es.search(index="ssh", body={
  "aggs": {
    "results": {
      "composite": {
        "size": 900000,
        "sources": [
          {
            "username": {
              "terms": {
                "field": "username"
              }
            }
          },
          {
            "password": {
              "terms": {
                "field": "password"
              }
            }
          }
        ]
      }
    }
  }
})

print(res)

count = 0

for hit in res['aggregations']['results']['buckets']:
    print(str(hit["key"]) + " " + str(hit["doc_count"]))

    count = count + 1

print("Total usernamea: " + str(count))

