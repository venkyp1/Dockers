FROM alpine
RUN apk add bash bash-completion
ADD ./dist /app
ENTRYPOINT ["/app/hello"]
