Steps for running:
1-Build Django Application docker image
cd django
docker build -t ghozal/django-app:latest .
docker push ghozal/django-app:latest

1-Build Angular Application docker image

cd angular
docker build -t ghozal/angular-app:latest .
docker push ghozal/angular-app:latest


3-Install Helm Chart
cd smartseedschart
helm install smartseeds ./


Note : Update docker username "ghozal" in values.yaml , and docker build commands .'

References:
1-Angular Application https://github.com/anuragiiits/IOT-Smart-Agriculture
2-Django Server https://github.com/garvitkataria/IOT_Smart_Agriculture
