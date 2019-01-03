from elasticsearch import Elasticsearch
import hashlib


es = Elasticsearch(hosts=[{'host': "127.0.0.1", 'port': 9200}])

res = es.search(index="ssh", body={
    "aggs": {
      "scripts": {
        "terms": {
          "field": "originalRequestString",
          "size": 10000011
        }
      }
    }
  })

count = 0

data = {}

for hit in res['aggregations']['scripts']['buckets']:
    #print(str(hit["key"]) + " Counter: " + str(hit["doc_count"]))
    count = count + 1

    current = int(hit["doc_count"])
    count = count + 1


    if (current in data):
        #print("Counter " + str(current) + " already used")
        currentData = str(data[current])
        data[current] = currentData + ":" + str(hit["key"])


    else:
        data[current] = hit["key"]
        #print("Counter " + str(current) + " not used")

breaker = 0

print("Often used scripts are: ")

for x in range(count,1,-1):

    if (x in data):
        print(str(x) + ":" + " " + str(data[x]))
        breaker = breaker+1


    if (breaker == 11):
        break




print("Total scripts: " + str(count))
