from elasticsearch import Elasticsearch
from dotenv import load_dotenv
import os

load_dotenv()

user = os.getenv('ELASTIC_USER')
pw = os.getenv('ELASTIC_PW')

es = Elasticsearch(
    "https://localhost:9200",
    basic_auth=(user, pw),
    verify_certs=False  # nur für Entwicklung!
)

print(es.info())

'''
Ingestions
'''
'Single document '
doc = {
	"title": "Die Verwandlung",
	"author": "Franz Kafka",
	"year": 1912
}

es.index(index="books", document=doc)

'Bulk ingestion'

from elasticsearch.helpers import bulk

actions = [
    {"_index": "books", "_source": {"title": "Book A", "year": 2020}},
    {"_index": "books", "_source": {"title": "Book B", "year": 2021}},
]

bulk(es, actions)
