FROM 3336661/todobackend-base:latest
# Copy application artifacts
COPY target /wheelhouse

# Install application
RUN . /appenv/bin/activate && \
    pip install --no-index -f /wheelhouse todobackend && \
rm -rf /wheelhouse