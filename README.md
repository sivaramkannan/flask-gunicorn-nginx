# flask-gunicorn-nginx
Scaling flask with Gunicorn-wsgi

1. Clone the repo and run `docker-compose up`. 
2. The flask app simply wait for a random time between 10 to 100 seconds. 
3. The nginx is configured to wait for 300 seconds for the response. 
4. The app was tested with 100 parallel connections and it was giving 504 error before configuring the 300 seconds response time.


Use the below to test the parallel connection

```
for i in {1..100}
do
curl http://127.0.0.1:5000/api/wait&
done
```

The above test might still 504, but the queue at the gunicorn level would happen. The response timeout and the connection throttling can be experimented at the nginx level to give better user experience.
