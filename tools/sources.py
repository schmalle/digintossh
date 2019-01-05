from elasticsearch import Elasticsearch
from geoip import open_database



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


with open_database('/var/lib/GeoIP/GeoLite2-Country.mmdb') as db:


    for hit in res['aggregations']['sources']['buckets']:

        if (count <= 11):
            match = db.lookup(str(hit["key"]))
            print(str(hit["key"]) + " Counter: " + str(hit["doc_count"]) + " Country: " + str(match.country))



        count = count + 1


print("Total number of unique IPs:" + str(count))

