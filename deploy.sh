cd ui-flask_react/flask-api
nohup flask run &
cd ../ui-flask_react
nohup env PORT=3100 HOST=0.0.0.0 npm start &
