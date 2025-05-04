# Django Project with Docker and CI/CD

This project is a Django application configured with Docker and Docker Compose for local development, testing, staging, and production environments. It includes a complete CI/CD pipeline using GitHub Actions.

## Features

- Django project with PostgreSQL database
- Multiple environment configurations (development, testing, staging, production)
- Docker and Docker Compose setup for each environment
- CI/CD with GitHub Actions for automated testing and deployment
- Nginx for serving static files and SSL termination
- Let's Encrypt SSL certificates with auto-renewal
- Sentry integration for error tracking
- Health check endpoint for monitoring

## Project Structure

```
myproject/
├── .github/workflows/       # GitHub Actions CI/CD workflows
├── app/                     # Django application code
├── docker/                  # Docker configurations for each environment
├── nginx/                   # Nginx configurations for staging and production
├── scripts/                 # Startup scripts for different environments
├── requirements/            # Python requirements for different environments
├── .dockerignore
├── .gitignore
└── README.md
```

## Development Setup

### Prerequisites

- Docker and Docker Compose
- Git

### Getting Started

1. Clone the repository:
   ```
   git clone https://github.com/your-username/myproject.git
   cd myproject
   ```

2. Start the development environment:
   ```
   cd docker/dev
   docker-compose up
   ```

3. Access the development server at http://localhost:8000

## Testing

Run tests locally:

```
cd docker/dev
docker-compose run web python app/manage.py test
```

Or use pytest:

```
cd docker/dev
docker-compose run web pytest app/
```

## Deployment

### Staging

Push your changes to the `staging` branch:

```
git checkout staging
git merge main
git push origin staging
```

GitHub Actions will automatically deploy to your staging server.

### Production

Push your changes to the `production` branch:

```
git checkout production
git merge staging
git push origin production
```

GitHub Actions will automatically deploy to your production server.

## GitHub Actions Secrets Configuration

For the CI/CD pipeline to work, you need to set up the following secrets in your GitHub repository:

### Staging Deployment
- `STAGING_SSH_PRIVATE_KEY`: SSH private key for accessing the staging server
- `STAGING_HOST`: Hostname or IP address of the staging server
- `STAGING_USER`: SSH username for the staging server
- `STAGING_SECRET_KEY`: Django secret key for staging
- `STAGING_DB_NAME`: Database name for staging
- `STAGING_DB_USER`: Database user for staging
- `STAGING_DB_PASSWORD`: Database password for staging
- `STAGING_ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- `STAGING_SENTRY_DSN`: Sentry DSN for error tracking in staging

### Production Deployment
- `PRODUCTION_SSH_PRIVATE_KEY`: SSH private key for accessing the production server
- `PRODUCTION_HOST`: Hostname or IP address of the production server
- `PRODUCTION_USER`: SSH username for the production server
- `PRODUCTION_SECRET_KEY`: Django secret key for production
- `PRODUCTION_DB_NAME`: Database name for production
- `PRODUCTION_DB_USER`: Database user for production
- `PRODUCTION_DB_PASSWORD`: Database password for production
- `PRODUCTION_ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- `PRODUCTION_SENTRY_DSN`: Sentry DSN for error tracking in production

## SSL Certificates

The project is configured to use Let's Encrypt SSL certificates. To set up SSL:

1. Update the domain names in the Nginx config files (`nginx/staging/default.conf` and `nginx/production/default.conf`)
2. On your first deployment, set up the certificates manually:
   ```
   docker-compose run --rm certbot certonly --webroot --webroot-path=/var/www/certbot -d example.com -d www.example.com
   ```

## License

[MIT](LICENSE)