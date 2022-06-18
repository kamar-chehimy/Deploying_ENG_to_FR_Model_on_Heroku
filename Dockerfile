FROM  python:3.9

# Create the working directory
RUN set -ex && mkdir /En_Fr_Translation
WORKDIR /En_Fr_Translation

# Install Python dependencies
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# Copy the relevant directories
COPY model/ ./model
COPY . ./

# Run the web server
EXPOSE 8000
ENV PYTHONPATH /En_Fr_Translation
CMD python3 /En_Fr_Translation/app.py