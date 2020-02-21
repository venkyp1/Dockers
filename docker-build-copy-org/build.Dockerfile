FROM gcc
ADD src /app
WORKDIR /app
RUN make 
