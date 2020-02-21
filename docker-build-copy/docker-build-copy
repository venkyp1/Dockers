FROM alpine
RUN apk add bash bash-doc bash-completion && apk add build-base gcc abuild binutils binutils-doc gcc-doc
ADD src /app
WORKDIR /app
RUN make 
