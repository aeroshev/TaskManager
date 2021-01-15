# Task Manager
## ENV file
For launch required create `.env` file
```
cd backend && touch .env
```

In env file assign the value
```
DJANGO_SECRET_KEY=<some-key>

DJANGO_EMAIL_HOST_USER=<smtp-address>
DJANGO_EMAIL_HOST_PASSWORD=<smtp-password>

DATABASE_URL=postgres://user:password@address:5432/db
```
## Certificate for SSL connection
Either needs install certifications for ssl
Install `mkcert` for macOS
```
mkdir nginx/certificate

brew install mkcert

mkcert -install

mkcert -cert-file nginx/certificate/cert.pem \
-key-file nginx/certificate/key.pem \
0.0.0.0 localhost 127.0.0.1 ::1
```
## Run app
And finally run in root folder
```
docker-compose up --build
```

## Access to applications
`Frontend` available on `localhost:3000` <br>
`Backend` available on `localhost:8000/api/` <br>
 or on `https://localhost/api/` where is `localhost` temporary domain name <br>
this is access use nginx proxy
