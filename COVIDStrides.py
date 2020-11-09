#!/usr/bin/env python
#  IMPORTS
import sys


from fasp.search  import DiscoverySearchClient
from setuptools import setup

setup(name='fasp',
      version='1.0',
      packages=['fasp',
                'fasp.search'],

      )


def main(argv):

	# Step 1 - Discovery
	# query for relevant DRS objects

	searchClient = DiscoverySearchClient('https://search-presto-public-covid19.prod.dnastack.com')

	# List tables
	#searchClient.listTables()
	# List table schema
	#searchClient.listTableInfo('coronavirus_dnastack_curated.covid_cloud_production.sequences')

	query = 'select accession, biosample, genus, species from coronavirus_dnastack_curated.covid_cloud_production.sequences limit 10'
	res = searchClient.runQuery(query)
	print(res)

if __name__ == "__main__":
	main(sys.argv[1:])


searchClient = DiscoverySearchClient('https://search-presto-public-covid19.prod.dnastack.com')

res = searchClient.runOneTableQuery(column_list=['accession', 'biosample', 'genus', 'species'], 
									table='coronavirus_dnastack_curated.covid_cloud_production.sequences',
						  			limit=15)
print(res)






