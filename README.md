# Cherry Syte
Sweet little exercise in bundling up Docker based apps.

## Building the App image
```
cd <repo_directory>
docker build -t cherry-syte .
```

## Running the App locally
```
docker run -p 5000:5000 cherry-syte
```

## App responses
To get the server IP and echoed string
```
curl http://localhost:5000?my_string=MY_STRING
```
To get `index.html` from `html` directory:
```
curl http://<SERVER_IP>:5000/html/index.html
```
NOTE: any file added to html directory can be accessed using the filename like so:
```
curl http://<SERVER_IP>:5000/html/my-file.html
```

## Deploy Kubernetes cluster

