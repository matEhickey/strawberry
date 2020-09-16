## Docker basic example

Example of a strawberry app in a docker container.


~~~sh
docker build . -t strawberry
docker run -it -p 8000:8000 -v `pwd`:/app strawberry
~~~

Graphiql is exposed into "localhost:8000"  

Arguments explanations:  
- "-p 8000:8000": expose the port 8000 of the container into the port 8000 of the computer
- "-v `pwd`:/app": replace the app folder of the container by the app source (to be able to modify them without re-building the image (you can uncomment the lines in app.js and reload to update))  
- "-it": get the terminal IO, to easily kill the container and see logs