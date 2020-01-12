FROM alpine AS builder
RUN apk add bash bash-doc bash-completion && apk add build-base gcc abuild binutils binutils-doc gcc-doc
ADD src /app
WORKDIR /app
RUN make 

FROM alpine
COPY --from=builder /app/bin /app
RUN apk add bash bash-completion
ENTRYPOINT ["/app/hello"]
