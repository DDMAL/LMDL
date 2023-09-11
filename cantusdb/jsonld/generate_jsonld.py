import pandas as pd
import json

df = pd.read_csv('../cantus_reconciled.csv')
json_data = df.to_json(orient='records')
parsed_json = json.loads(json_data)
# pretty_json = json.dumps(parsed_json, indent=4)
# with open('gen_json.json', 'w') as json_file:
#     json_file.write(pretty_json)

'''
@context:{
"chant"{id}
"cantusdb"
"cantus_source":{"@id": "https://cantusdatabase.org/source/", "@type":"@id"},
"volpiano": "https://web.mit.edu/music21/doc/moduleReference/moduleVolpiano.html"
}'''


for work in parsed_json:
    work["@context"] = "https://raw.githubusercontent.com/malajvan/linkedmusic-datalake/main/simssadb/jsonld/context.jsonld"
    work["@id"] = f"chant:{work.pop('chant_id')}"
    work["@type"] = "wd:Q37097256" #chant
   
    work['database'] = 'cantusdb:'
   
   
    work["P86"] = "wdt:Q4233718" #composer anonymous
    work["P1922"] = work.pop("incipit")
    work["P136"] = f'wd:{work.pop("genre")}'
    work["Q731978"] = f'wd:{work.pop("mode_name")}'
    work["Q4484726"] = work.pop("finalis")

    work["source"] = f'cantus_source:{work.pop("src_link").replace("cantusdatabase.org/source/","")}'
    del work["mode"]
    del work["absolute_url"]
    del work["composer"]
    
# Print the nested list of dictionaries
pretty_json = json.dumps(parsed_json, indent=4)
with open('compact.jsonld', 'w') as json_file:
    json_file.write(pretty_json)






