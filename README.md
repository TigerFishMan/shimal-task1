# How to run on docker

Install Docker


Install docker-compose


Run the following command


This will run app in development mode
```
docker-compose up
```

To run the app in production mode run
```
docker-compose -f docker-compose.prod.yml up -d
````

Go to [http://localhost:8008](http://localhost:8008) to see if app is working

Task 1 API is at [http://localhost:8008/users/](http://localhost:8008/users/)

To test the api you can run the the following curl command

Note: Date needs to be in ISO format

```
curl --request POST \
  --url http://localhost:8008/users/ \
  --header 'content-type: application/json' \
  --data '{
  "username": "Ahmed Shimal",
  "email": "email@email.com",
  "number": "7966921",
  "dob": "1982-10-14"
}'
```

This will output the following

```
{
  "username": "Ahmed Shimal",
  "email": "email@email.com",
  "number": "7966921",
  "dob": "1982-10-14",
  "age": 40
}
```

After running you can access the docs at 
[http://localhost:8008/docs](http://localhost:8008/docs)

# How to run on virtual environment

Run the following commands

```
python3 -m venv venv
source venv bin activate
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8008
```
