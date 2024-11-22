# Base image: Ubuntu
FROM ubuntu:20.04

# Install Python dependencies
RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

# Default entrypoint
CMD ["bash", "-c", "service postgresql start && tail -f /dev/null"]

