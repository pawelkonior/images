# Images App

## Usage:

1. Clone repository
2. Copy `./backend/env/.env-default` to `./backend/env/.env`
3. Add configuration data to `./backend/env/.env`
4. If you don`t know what kind of configuration data you should provide, then use example data:

```bash
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_DB=postgres
DATABASE_URL=postgres://postgres:password@db:5432/postgres

DEBUG=1
SECRET_KEY=django-insecure-ye9^i&m__*92n$veag$^jn3kkh9$3dh=ml_x9ab^-%#(p_vl2#
DJANGO_ALLOWED_HOSTS='backend localhost 127.0.0.1'

DJANGO_SU_NAME=testAdmin
DJANGO_SU_EMAIL=teastAdmin@aa.pl
DJANGO_SU_PASSWORD=testPass123 


```