FROM gcc
ADD ./dist /app
ENTRYPOINT ["/app/hello"]
