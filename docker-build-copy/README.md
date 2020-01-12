#Using docker to build images and create a production image
####This is for demo.

###Note:  The better approch is to use multi-stage builds.

## Approach:
```
  This approach uses 2 Dockerfiles. One is used for building the application which is a just a helloworld 'C' program.
  The build image will create the binary file using make. Once the binary is built, a container image is created to copy 
  the  binary to the local directory which is copied to the production image built using the prod.Dockerfile.
  
  A shell script is added to run all the described steps.
  
  Though this is an older approach, there is one important approach to learn.
  
  When we don't have a build setup for building a specific app, a docker image for that can be created to build.
  Then the built app, can be copied to the local dir to test.
  
  ```
  
  ## Run:
  
  ```
$$ mk-image.sh
Build the app docker image:
Sending build context to Docker daemon  19.46kB
Step 1/4 : FROM gcc
 ---> e2d82e0ef844
Step 2/4 : ADD src /app
 ---> 179ff0782868
Step 3/4 : WORKDIR /app
 ---> Running in ce4a0b80a508
Removing intermediate container ce4a0b80a508
 ---> c6e476b772ef
Step 4/4 : RUN make
 ---> Running in 40e1ae53110d
mkdir bin
gcc -o bin/hello hello.c
Removing intermediate container 40e1ae53110d
 ---> 64a60209e498
Successfully built 64a60209e498
Successfully tagged builder:latest
Create a container: appdata
cee8bf1a74825152d3bd6042b579b65e7c5775c0fe978c465bc91727c2dae487
appdata
Build the production image
Sending build context to Docker daemon  36.86kB
Step 1/3 : FROM gcc
 ---> e2d82e0ef844
Step 2/3 : ADD ./dist /app
 ---> e7a740e292b0
Step 3/3 : ENTRYPOINT ["/app/hello"]
 ---> Running in 626d2982c359
Removing intermediate container 626d2982c359
 ---> 84166b96d4b2
Successfully built 84166b96d4b2
Successfully tagged prodimage:latest
```
## Verify the images

```
$$ docker images| grep build
builder                                     latest                  64a60209e498        36 minutes ago      1.14GB
$$ docker images| grep prod
prodimage                                   latest                  84166b96d4b2        36 minutes ago      1.14GB
$$

```

## Run the production image

```
$$ docker run -it prodimage

Hello! Venky

$$
```


