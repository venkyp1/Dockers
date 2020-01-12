# Using multi-stage approach to create a Docker app image.

## Approach:
 ```
 This is to demo multi-stage approach in deploying apps
 The application build and deploy uses only one Dockerfile. 
 The magic keywords used in the Dockerfile are: AS and --from

  ```
  
  ## Run:
  
  ```
$$ mk-image.sh
Build the production image
Sending build context to Docker daemon  8.704kB
Step 1/9 : FROM alpine AS builder
 ---> cc0abc535e36
Step 2/9 : RUN apk add bash bash-doc bash-completion && apk add build-base gcc abuild binutils binutils-doc gcc-doc
 ---> Running in cdf4e1249992
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
Removing intermediate container cdf4e1249992
 ---> 54581479f80c
Step 3/9 : ADD src /app
 ---> 0aa61f7dd34c
Step 4/9 : WORKDIR /app
 ---> Running in 684245f48943
Removing intermediate container 684245f48943
 ---> 292ec2c6d5fb
Step 5/9 : RUN make
 ---> Running in f28830ca6c24
mkdir bin
gcc -o bin/hello hello.c
Removing intermediate container f28830ca6c24
 ---> 127eb8cb84e0
Step 6/9 : FROM alpine
 ---> cc0abc535e36
Step 7/9 : COPY --from=builder /app/bin /app
 ---> 5a9ba85e9fe3
Step 8/9 : RUN apk add bash bash-completion
 ---> Running in bdb78a5582c1
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
Removing intermediate container bdb78a5582c1
 ---> 03f2203951b6
Step 9/9 : ENTRYPOINT ["/app/hello"]
 ---> Running in c60abe1c1415
Removing intermediate container c60abe1c1415
 ---> efbe0c778194
Successfully built efbe0c778194
Successfully tagged production:latest
```
## Verify the images

### Note: The size of the production image

```
$$ docker images | grep production
production                                  latest                  efbe0c778194        7 minutes ago       12.3MB 
$$

```

## Run the production image

```
$$ 
docker run -it production:latest

Hello! Venky

$$
```


