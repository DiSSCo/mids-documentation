@echo off
REM Activate the virtual environment
call .stadocgen-venv\Scripts\activate

REM Set the FLASK_APP environment variable
set FLASK_APP=app.routes

REM Launch Flask
flask run