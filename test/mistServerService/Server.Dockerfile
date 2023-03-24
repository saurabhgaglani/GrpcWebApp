# Use an official Python runtime as a parent image 
FROM python:3
 
# Set the working directory to /app 
WORKDIR /app 
 
# Copy the current directory contents into the container at /app 
COPY . /app/ 

RUN pip install --upgrade pip 

# Install any needed packages specified in requirements.txt 
RUN pip3 install -r requirements.txt 
 
# Make port 50051 available to the world outside this container 
EXPOSE 50051
 
# Run app.py when the container launches 
CMD ["python3", "greeter_server.py"]