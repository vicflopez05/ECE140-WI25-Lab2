# ECE140-WI25-Lab2

Run the command below to build the docker image:

```
docker build -t fastapi-app .

```

Then, run the command below to start the server:

```
docker run -p 8000:8000 fastapi-app
```

You should then get some terminal output showing that the server is running, just like what we've seen in Lab Session 1.

You can then navigate to `http://localhost:8000/docs` to see the API documentation and test the API.

Also, if you open up Docker Desktop, you'll be able to see the running container.