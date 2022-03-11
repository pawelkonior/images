export POSTGRES_USER=postgres
export POSTGRES_PASSWORD=password
export POSTGRES_DB=postgres
export DATABASE_URL=postgres://postgres:password@localhost:5432/postgres

export DEBUG=1
export SECRET_KEY="django-insecure-ye9^i&m__*92n$veag$^jn3kkh9$3dh=ml_x9ab^-%#(p_vl2#"
export DJANGO_ALLOWED_HOSTS='backend localhost 127.0.0.1 0.0.0.0'

export DJANGO_SU_NAME=testAdmin
export DJANGO_SU_EMAIL=teastAdmin@aa.pl
export DJANGO_SU_PASSWORD=testPass123

export TEST_DIR='test'

python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000