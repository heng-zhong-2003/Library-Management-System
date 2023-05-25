# Hitoha's Library
### A Simple Library Management System Based on Flask and Node

## Installation and Starting
First make sure that you have python 3.10 or later versions and nodejs 14.0 or later versions. `cd` to the project folder. Run the following instructions to configure the backend environment.
```shell
pip install flask
pip install sqlalchemy
pip install flask_cors
```
Then `cd` to the frontend folder and run the following instructions.
```shell
npm install
```
Finally, write in the file `_config.init` the configuration of you MySQL server. In the root folder of the project, run

```shell
python main.py
```
to start the backend. In the front folder, run 
```shell
npm run dev
```
to start the frontend.

## Notice
This project is just for finishing a term project of a database course and is **NOT** for any practical scene that requires even slight safety. The password is not encoded and tokens are not used here. However, it is well structured can be easily modified to meet these safety requirements.