# 1: The data details:
-   In the link provided, we can download a archived file. If we unzip it, we will see a mbdump folder with a file named by its entity type and without a extension. This is the dump in JSON lines format. Each line represents one record in the dump. 
-   The entity_type is the subject in the database. If this database is filled with 'recordings', then its entity_type is 'recording'.
-   In every line, there should be an object named "id". This is the key attribute of each record. When converting into CSV, we rename the id to "{entity_type}_id" to be more precise of which entity type we are working with.
-   During the conversion process, for all ids of different entity type (genre_id, artist_id, area_id, etc.), we add the MusicBrainz reference to the id in the format: "https://musicbrainz.org/{entity_type}/{id}". It automatically converts the id to a URI reference.
-   For all records, if it is reconciled with Wikidata link by MusicBrainz bots, then it should have an object in "relations" > "resources" > "url", with the Wikidata link as the value. It is exists, then it is extracted to the CSV file.

# 2: The experiment data sets:
-   For experiment purposes, I only used a small portion of each data dump. 
-   I used the command (example): 
        head -n 3000 "area">"test_area"
    to get the first 3000 lines from the area data dumps.
-   All other data dumps perform the same procedure.

# 3: The procedure:
-   Since all ids and Wikidata links are already reconciled in the conversion process, there's no need to go to OpenRefine.
-   Steps:
1.  Get the latest JSON files from https://data.metabrainz.org/pub/musicbrainz/data/json-dumps
    *  Examples in data folder.
2.  Run convert_to_csv.py, specify the JSON file in the first argument and the entity type in the second argument.
    *  Example command line: 
            cd musicbrainz/csv
            python3 convert_to_csv.py data/test_area area
3.  A CSV file named by its entity type will be generated. It can be used for further operations.