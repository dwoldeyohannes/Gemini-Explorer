# Gemini-Explorer

# Demo

https://www.loom.com/share/2ad0c2ba4c59420682957c844127f2f0?sid=ebfee4f9-92f6-4713-a9b2-3f44fe9ce75f

## Overview:

Gemini/Don Explorer is a streamlit Chat Interface integrating Google's advanced language model, Gemini. This project aims to provide an accessible and interactive platform for exploring the capabilities of large language models. Users can seamlessly interact with advanced AI technology by leveraging Streamlit's intuitive interface and the powerful Gemini model.

## Key Features:

Interactive Chat Interface: A sleek and responsive chat interface built with Streamlit, designed for seamless user interactions.
Google Gemini Integration: Utilizes the advanced capabilities of Google's Gemini language model to provide accurate and context-aware responses.
Customizable and Extensible: The project is designed to be easily customized and extended, allowing users to tailor the interface to their specific needs.

The primary goal of this project is to demonstrate the practical applications of large language models in a user-friendly environment. Whether you're a developer looking to integrate language models into your applications or a curious user wanting to experiment with AI-driven interactions, this project serves as a valuable resource.

## Installation
0. Basic Setup
1. Enable Google Cloud
2. Initialize Google Cloud
3. Setup Google Gemini
4. Streamlit Integration
5. Enhance Personality

## 0. Basic Setup
### [Visual Studio Code](https://code.visualstudio.com/)
You may also choose other develop tools that you prefer.
### [Python](https://www.python.org/downloads/)
make sure that your version is above 3.11
### Google Cloud Code
install this extension to connect your Google Cloud project

## 1. Enable Google Cloud
[Start](https://console.cloud.google.com/)

follow the instructions [here](https://cloud.google.com/cloud-console?utm_source=google&utm_medium=cpc&utm_campaign=na-US-all-en-dr-bkws-all-all-trial-e-dr-1707554&utm_content=text-ad-none-any-DEV_c-CRE_665735422256-ADGP_Hybrid%20%7C%20BKWS%20-%20MIX%20%7C%20Txt-Management%20Tools-Cloud%20Console-KWID_43700077225654741-kwd-55675752867&utm_term=KW_google%20cloud%20console-ST_google%20cloud%20console&gad_source=1&gclid=Cj0KCQiArrCvBhCNARIsAOkAGcXO2_affz2IH9q_ps1LDwrdsOe43AmOiJps1j9UK_ri0mnBWRd9eA0aApkNEALw_wcB&gclsrc=aw.ds)

## 2. Initialize Google Cloud
* setup the API server

* install and initialize SDK by typing the following command into the terminal
```sh
gcloud init
```

* install required packages
```sh
pip install vertexai
```

* initialize vertexai project
```python
import vertexai
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel, Part, Content, ChatSession
project = "your-project-ID"
vertexai.init( project = project )
```
* create config and load model
```python
config = generative_models.GenerationConfig( # add attributes you need )
model = GenerativeModel ( "gemini-pro", generation_config = config )
chat = model.start_chat()
```
## 3. Setup Google Gemini
* installation
```sh
pip install streamlit
```
* import package
```python
import streamlit as st
```
* [Streamlit Guide](https://docs.streamlit.io/get-started)
  * We use `"Gemini-Pro"` by Google!
## 4. Streamlit Integration
* display and load chat history
* capture user input effortlessly

## 5. Add Initial Message
### Initial Prompt
* enhance personality: This is something you can **define** your chatbot. Including what you want it to be called, what its style of chatting is going to be. All those requirements can be included in a string. 

## Launch The App
```zsh
streamlit run gemini_explorer.py
```
