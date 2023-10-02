# SimssaDB flattening and json-ld structures

> Summary:  
>   1. Upload SQL dump to local postgreSQL database
>   2. With output run `flattening/SQL_query.py`
>   3. With output run `flattening/restructure.py`
>   4. Reconcile `final_flattened.csv` with OpenRefine
>   5. With output run `jsonld/generate_jsonld.py `(which also takes `jsonld/context.jsonld` as the initial context)

## 1. Extracting columns and feature flattening
After uploading the database dump to the local PostgreSQL database the flattening process happens at 2 stages:
1. Selection and initial file feature flattening with `psycopg` in `SQL_query.py` 
2. Further restructuring and flattening of nested structures (files) in `restructure.py`, extracting only relevant information
Note that we divided the flattening step to 2 since one could want to bypass the PostgreSQL part and start at the `restructure.py` script (Happens often in development, also mainly because simssadb doesn't have much updates yet).



## 2. Reconciliation with OpenRefine
I performed OpenRefine reconciliation. You can see the reconciled file `reconciled_wikiID.csv`. You can use `openrefine/history.json` to facilitate reconciliation and `openrefine/export_template.json` to export to the desired csv format.
The following is a list of reconciled columns:
- genre_style
- genre_type
- file_format
- composer
  

## 3. Reconcile column names and generating json-ld
Currently the json-ld is generated as follow:  

In [`generate_jsonld.py`](https://github.com/malajvan/linkedmusic-datalake/blob/main/simssadb/jsonld/generate_jsonld.py):
- convert csv to json documents 
- Loop through each json document and edit each entry, creating the compact jsonld. Each json document is a musical work, and the files are listed as nested json documents in a list.
- Generate the jsonld file at [`compact.jsonld`](https://github.com/malajvan/linkedmusic-datalake/blob/main/simssadb/jsonld/compact.jsonld)
- The contexts used in the compact.jsonld file is imported from [`context.jsonld`](https://github.com/malajvan/linkedmusic-datalake/blob/main/simssadb/jsonld/context.jsonld)
- Test jsonld and its contexts with PyLD. We use the file `test_expansion/test.py` to use PyLD's expand function to generate `expanded.json`.

