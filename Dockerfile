FROM jfloff/alpine-python:recent-slim

# install flask on entry
RUN /entrypoint.sh \
    -p flask \
    && echo

# set up and run hook server
EXPOSE 5000
WORKDIR /app
COPY ./hook_server.py /app/hook_server.py
CMD python /app/hook_server.py
