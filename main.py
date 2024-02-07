from fastapi import FastAPI
import pandas as pd
app = FastAPI()

#Endpoint 1
@app.get("/developer/{developer}")
def developer( developer : str ):   
    df_endpoint1 = pd.read_csv("df_endpoint1.csv")
    developer_data = df_endpoint1[df_endpoint1["developer"] == developer]
    developer_data_dict = developer_data.to_dict(orient="records")

    return developer_data_dict

#Endpoint 2
@app.get("/userdata/{user}")
def userdata(user_id : str):   
    df_endpoint2 = pd.read_csv("df_endpoint2.csv")
    user_data = df_endpoint2[df_endpoint2["user_id"] == user_id]
    user_data_dict = user_data.to_dict(orient="records")

    return user_data_dict

#Endpoint 3
@app.get("/UserForGenre/{genre}")
def  UserForGenre( genre : str ):   
    df_endpoint3 = pd.read_csv("df_endpoint3.csv")
    genre_data = df_endpoint3[df_endpoint3["genre"] == genre]
    genre_data_dict = genre_data.to_dict(orient="records")

    return genre_data_dict

#Endpoint 4
@app.get("/best_developer_year/{year}")
def best_developer_year( año : int ):
    df_endpoint4 = pd.read_csv("df_endpoint4.csv")
    developer_data = df_endpoint4[df_endpoint4["año"] == año]
    developer_data_dict = developer_data.to_dict(orient="records")

    return developer_data_dict

#Enpoint 5
@app.get("/sentiment_analysis/{year}")
def sentiment_analysis(year : int):
    df_endpoint5 = pd.read_csv("df_endpoint5.csv")
    sentiment_data = df_endpoint5[df_endpoint5["Year"] == year]
    sentiment_data_dict = sentiment_data.to_dict(orient="records")

    return sentiment_data_dict


#Endpoint Recommendation system
@app.get("/recomendacion_juego/{Game}")
def recomendacion_juego(Game : str):   
    df_RS = pd.read_csv("sistema_recomendacion.csv")
    RS_data = df_RS[df_RS["Game"] == Game]
    RS_data_dict = RS_data.to_dict(orient="records")

    return RS_data_dict