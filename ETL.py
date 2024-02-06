import json
import ast
import pandas as pd
import gzip
import shutil

# Descomprimo los archivos

with gzip.open('user_reviews.json.gz', 'rb') as file_in:
    with open('user_reviews.json', 'wb') as file_out:
        shutil.copyfileobj(file_in, file_out)

with gzip.open('steam_games.json.gz', 'rb') as file_in:
    with open('steam_games.json', 'wb') as file_out:
        shutil.copyfileobj(file_in, file_out)

with gzip.open('users_items.json.gz', 'rb') as file_in:
    with open('users_items.json', 'wb') as file_out:
        shutil.copyfileobj(file_in, file_out)

# Limpio los json y los convierto en csv

fr=open("user_reviews.json", "r", encoding="utf-8")
fw=open("user_reviews2.json", "w")

for line in fr:
    json_dat = json.dumps(ast.literal_eval(line))
    dict_dat = json.loads(json_dat)
    json.dump(dict_dat, fw)
    fw.write("\n")

fw.close()
fr.close()
        
input_filename = "user_reviews2.json"
output_filename = "user_reviews_cleaned.json"

with open(input_filename, "r") as fr, open(output_filename, "w") as fw:
    fw.write("[\n")
    for line in fr:
        line = line.strip()
        if line.endswith(""):
            fw.write(line + ",\n")
        else:
            fw.write(line + "\n")
    fw.write("]\n")

df_reviews = pd.read_json('user_reviews_cleaned.json')
df_reviews.to_csv('user_reviews.csv')


fr=open("users_items.json", "r", encoding="utf-8")
fw=open("users_items2.json", "w")

for line in fr:
    json_dat = json.dumps(ast.literal_eval(line))
    dict_dat = json.loads(json_dat)
    json.dump(dict_dat, fw)
    fw.write("\n")

fw.close()
fr.close

input_filename = "users_items2.json"
output_filename = "users_items_cleaned.json"

with open(input_filename, "r") as fr, open(output_filename, "w") as fw:
    fw.write("[\n")
    for line in fr:
        line = line.strip()
        if line.endswith(","):
            fw.write(line + "\n")
        else:
            fw.write(line + ",\n")
    fw.write("]\n")

df_items = pd.read_json("users_items_cleaned.json")
df_items.to_csv("users_items.csv")


input_filename = "steam_games.json"
output_filename = "steam_games2.json"

with open(input_filename, "r", encoding="utf-8") as fr, open(output_filename, "w") as fw:
    for line in fr:
        line = line.strip()
        if line.endswith(","):
            fw.write(line + "\n")
        else:
            fw.write(line + ",\n")

input_file = "steam_games2.json"
output_file = "steam_games3.json"

with open(input_file, "r") as fr, open(output_file, "w") as fw:
    json_data = fr.read()
    cleaned_data = json_data.replace("NaN", "null")
    fw.write(cleaned_data)

fw.close()
fr.close()

df = pd.read_json("steam_games3.json")
df.to_csv("steam_games.csv")
