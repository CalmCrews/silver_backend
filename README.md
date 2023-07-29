# 중앙 해커톤

### 팀원

> 기획 - 서의정
>
> 디자인 - 양정민
>
> 프론트엔드 - 김우림 / 이인
>
> 백엔드 - 안금장 / 임장혁

## Commands

### nginx reload

```
docker exec -it nginx-dev-container nginx -s reload
```

### Build for Dev

```
docker-compuse up -d --build
```

### Build for Production

```
docker-compose -f docker-compose.production.yml up -d --build
```

### Log

```
docker-compose logs -f

docker-compose logs -f webapp
```

### Superuser

```
docker-compose run --rm webapp python manage.py createsuperuser
```

### ERD
![moyeo (3)](https://github.com/CalmCrews/silver_backend/assets/90228925/9468ad07-8d21-4d1f-bdfb-5bb80ed7fab3)


