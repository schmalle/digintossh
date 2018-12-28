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
data = {}
smallest = 0

for hit in res['aggregations']['results']['buckets']:
    print(str(hit["key"]) + " " + str(hit["doc_count"]))

    current = int(hit["doc_count"])
    count = count + 1


    if (current in data):
        print("Counter " + str(current) + " already used")
        currentData = str(data[current])
        data[current] = currentData + ":" + str(hit["key"])


    else:
        data[current] = hit["key"]
        print("Counter " + str(current) + " not used")



print("Total unique username/password combinations: " + str(count))

breaker = 0

for x in range(count,1,-1):

    if (x in data):
        print(str(x) + ":" + " " + str(data[x]))
        breaker = breaker+1


    if (breaker == 21):
        break


