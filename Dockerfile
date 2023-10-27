# Use your private image as the base image
FROM ctfmail343/ctf:latest

# Install Apache and Uvicorn
RUN apt-get update
WORKDIR /var/www/html/ZIP

# Expose the necessary port for your application (e.g., 80)
EXPOSE 8000

# Start Apache and Uvicorn when the container runs
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "&&", "service", "apache2", "start"]
