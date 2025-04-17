# Use the official Python base image
FROM python:3.10

# Set working directory inside the container
WORKDIR /app/src


# Copy all files from current dir into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for the API
EXPOSE 8000

# Command to run the FastAPI app
CMD ["python", "src/app.py"]

