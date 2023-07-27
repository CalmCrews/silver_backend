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
![image](https://github.com/CalmCrews/silver_backend/assets/90228925/b9fa6511-dff6-4181-8a53-2169b7e7b9f3)

