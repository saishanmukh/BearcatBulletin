### Front End:
* cd .\Frontend\
* npm i
* ng serve

### Backend:
* Make sure you are in backend folder if not use below cmd.
```
cd backend
```
<!-- * Active the Virtual Environment
```

``` -->
* Create Virtual Environment.
```
python -m venv bearcat_bulletin_env
```
* Now Active the Virtual Environment
```
.\bearcat_bulletin_env\Scripts\activate
```
* Install the packages by using pip installaer.
```
pip install -r .\requirements.txt
```
* Create .env from the sample.env change username, password, mysql host, port, db name.
* Create database in mysql.
* Now run the migration for that we need to create the migration
    ```
    flask db migrate 
    flask db upgrade
    ```
* Run the web app.
```
flask run
```




