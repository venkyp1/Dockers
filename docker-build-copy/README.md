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
Sending build context to Docker daemon  9.728kB
Step 1/5 : FROM alpine
latest: Pulling from library/alpine
Digest: sha256:2171658620155679240babee0a7714f6509fae66898db422ad803b951257db78
Status: Downloaded newer image for alpine:latest
 ---> cc0abc535e36
Step 2/5 : RUN apk add bash bash-doc bash-completion && apk add build-base gcc abuild binutils binutils-doc gcc-doc
 ---> Running in 3eefdf5ea252
fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/main/x86_64/APKINDEX.tar.gz
fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/community/x86_64/APKINDEX.tar.gz
(1/8) Installing ncurses-terminfo-base (6.1_p20191130-r0)
(2/8) Installing ncurses-terminfo (6.1_p20191130-r0)
(3/8) Installing ncurses-libs (6.1_p20191130-r0)
(4/8) Installing readline (8.0.1-r0)
(5/8) Installing bash (5.0.11-r1)
Executing bash-5.0.11-r1.post-install
(6/8) Installing pkgconf (1.6.3-r0)
(7/8) Installing bash-completion (2.9-r0)
(8/8) Installing bash-doc (5.0.11-r1)
Executing busybox-1.31.1-r8.trigger
OK: 19 MiB in 22 packages
(1/36) Installing fakeroot (1.24-r0)
(2/36) Installing sudo (1.8.29-r0)
(3/36) Installing libcap (2.27-r0)
(4/36) Installing pax-utils (1.2.4-r0)
(5/36) Installing openssl (1.1.1d-r3)
(6/36) Installing libattr (2.4.48-r0)
(7/36) Installing attr (2.4.48-r0)
(8/36) Installing libacl (2.2.53-r0)
(9/36) Installing tar (1.32-r1)
(10/36) Installing patch (2.7.6-r6)
(11/36) Installing libgcc (9.2.0-r3)
(12/36) Installing libstdc++ (9.2.0-r3)
(13/36) Installing lzip (1.21-r0)
(14/36) Installing ca-certificates (20191127-r0)
(15/36) Installing nghttp2-libs (1.40.0-r0)
(16/36) Installing libcurl (7.67.0-r0)
(17/36) Installing curl (7.67.0-r0)
(18/36) Installing abuild (3.5.0-r0)
Executing abuild-3.5.0-r0.pre-install
(19/36) Installing binutils (2.33.1-r0)
(20/36) Installing binutils-doc (2.33.1-r0)
(21/36) Installing libmagic (5.37-r1)
(22/36) Installing file (5.37-r1)
(23/36) Installing gmp (6.1.2-r1)
(24/36) Installing isl (0.18-r0)
(25/36) Installing libgomp (9.2.0-r3)
(26/36) Installing libatomic (9.2.0-r3)
(27/36) Installing mpfr4 (4.0.2-r1)
(28/36) Installing mpc1 (1.1.0-r1)
(29/36) Installing gcc (9.2.0-r3)
(30/36) Installing musl-dev (1.1.24-r0)
(31/36) Installing libc-dev (0.7.2-r0)
(32/36) Installing g++ (9.2.0-r3)
(33/36) Installing make (4.2.1-r2)
(34/36) Installing fortify-headers (1.1-r0)
(35/36) Installing build-base (0.5-r1)
(36/36) Installing gcc-doc (9.2.0-r3)
Executing busybox-1.31.1-r8.trigger
Executing ca-certificates-20191127-r0.trigger
OK: 208 MiB in 58 packages
Removing intermediate container 3eefdf5ea252
 ---> 8c993afad4bb
Step 3/5 : ADD src /app
 ---> 7dc1dc5adbfb
Step 4/5 : WORKDIR /app
 ---> Running in c3ebe72ba4fc
Removing intermediate container c3ebe72ba4fc
 ---> 13d43d156c0e
Step 5/5 : RUN make
 ---> Running in 63369af467a6
mkdir bin
gcc -o bin/hello hello.c
Removing intermediate container 63369af467a6
 ---> 90eddf54dc81
Successfully built 90eddf54dc81
Successfully tagged builder:latest
bb2c74bdf78d3baaf86795915f327a31f2b883698c81de26a72c8ef5461da146
appdata
Build the production image
Sending build context to Docker daemon  30.72kB
Step 1/4 : FROM alpine
 ---> cc0abc535e36
Step 2/4 : RUN apk add bash bash-completion
 ---> Running in 6d80e9cf4822
fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/main/x86_64/APKINDEX.tar.gz
fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/community/x86_64/APKINDEX.tar.gz
(1/7) Installing ncurses-terminfo-base (6.1_p20191130-r0)
(2/7) Installing ncurses-terminfo (6.1_p20191130-r0)
(3/7) Installing ncurses-libs (6.1_p20191130-r0)
(4/7) Installing readline (8.0.1-r0)
(5/7) Installing bash (5.0.11-r1)
Executing bash-5.0.11-r1.post-install
(6/7) Installing pkgconf (1.6.3-r0)
(7/7) Installing bash-completion (2.9-r0)
Executing busybox-1.31.1-r8.trigger
OK: 17 MiB in 21 packages
Removing intermediate container 6d80e9cf4822
 ---> 97621df68a97
Step 3/4 : ADD ./dist /app
 ---> c950d18988ca
Step 4/4 : ENTRYPOINT ["/app/hello"]
 ---> Running in 0e61bb854e51
Removing intermediate container 0e61bb854e51
 ---> 7dd6ae7f4dc4
Successfully built 7dd6ae7f4dc4
Successfully tagged prodimage:latest
```
## Verify the images
### Note: The build image size was bigger because of the build environment but the runtime production image is much smaller.

```
$$ docker images| grep build
builder                                     latest                  90eddf54dc81        About a minute ago   207MB
$$ docker images| grep prod
prodimage                                   latest                  7dd6ae7f4dc4        About a minute ago   12.3MB
$$
```

## Run the production image

```
$$ docker run -it prodimage

Hello! Venky

$$
```


