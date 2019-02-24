from pandasdmx import Request
from pprint import pprint
estat = Request('ESTAT')

table_code = 'teilm020'
flow_response = estat.dataflow(table_code)
structure_response = flow_response.dataflow[table_code].structure(request=True, target_only=False)
metadata = structure_response.write()

# List of of available keys
metadata.codelist.index.levels[0]

# List of names for potential key vaulues
metadata.codelist.loc['GEO']['name'].to_dict()



#resp = estat.data(table_code, key={'GEO': 'EL+ES+IE'}, params={'startPeriod': '2007'})
resp = estat.data(table_code)
data = resp.write()


## Accessing data by key

# Keys order
data.keys().names

# Available key values
[x.name +"= "+str([n for n in x]) for x in data.keys().levels]

## Accessing data by date

# List of available dates:
[str(x) for x in data.index]

# Data structure for a particular date
data[[str(x) for x in data.index][0]].keys()

    

