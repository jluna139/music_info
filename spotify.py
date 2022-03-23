import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
import pprint

import spotipy.util as util
birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'

clint_id = "275629bde3154930918432f4f4446155"
client_secret = "a3868b2f03034ebda64237ec2ac7c0e5"
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=clint_id, client_secret=client_secret))


st.title("Spotipy")
st.write("This app lets you find the features of a specific song")
st.subheader("Your result")
st.subheader("")


song_selected = st.text_input(label="", value="hello")

str = spotify.search(song_selected)
song_dic0 = dict(str)["tracks"]["items"]



for i in range(len(song_dic0)):
    song_id = spotify.search(song_selected)
    song_dic0 = dict(song_id)["tracks"]["items"][i]

    song_dic0_id = song_dic0["id"]
    song_dic0_images = song_dic0["album"]["images"][0]["url"]
    song_dic0_artist = song_dic0["album"]["artists"][0]["name"]
    song_dic0_album = song_dic0["album"]["name"]
    song_dic0_name = song_dic0["name"]
    song_dic0_href = song_dic0["external_urls"]["spotify"]
    features = spotify.audio_features(song_dic0_id)[0]

    f1 = features.get("energy")
    f2 = features.get("tempo")
    f3 = features.get("liveness")
    f4 = features.get("instrumentalness")
    f5 = features.get("danceability")
    f6 = features.get("loudness")




    col1, col2 = st.beta_columns(2)
    col1.image(song_dic0_images)

    col2.subheader(song_dic0_name)
    col2.text(song_dic0_artist)
    col2.text(song_dic0_album)
    col2.text("Energy: % s " % f1)
    col2.text("Tempo: % s " % f2)
    col2.text("Liveness: % s " % f3)
    col2.text("Loudness: % s " % f4)

    col2.text("Danceability: % s " % f6)
    st.header(" ")

    # col2.write("Listen on: [Spotify](%s)" % song_dic0_href)



