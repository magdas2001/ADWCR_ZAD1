# Decision Rule API

Prosty serwis API w Flasku realizujący regułę decyzyjną na podstawie dwóch liczb.

## Opis działania

Endpoint:  
`GET /api/v1.0/predict`

Parametry zapytania (opcjonalne):
- `a` – liczba zmiennoprzecinkowa (domyślnie 0)
- `b` – liczba zmiennoprzecinkowa (domyślnie 0)

## Reguła decyzyjna

Jeśli `a + b > 5.8`, zwróć `prediction: 1`  
W przeciwnym razie zwróć `prediction: 0`

---

## Uruchamianie w Dockerze

1. Zbuduj obraz Dockera:

```bash
docker build -t decision-rule-api .
```

2. Uruchom aplikację:

```bash
docker run -p 5000:5000 decision-rule-api
```

---

## Przykład użycia (w przeglądarce)

Po uruchomieniu kontenera wejdź w przeglądarce pod adres:

```
http://localhost:5000/api/v1.0/predict?a=3.0&b=3.0
```

Odpowiedź (w przeglądarce w formacie JSON):

```json
{"features":{"a":3.0,"b":3.0},"prediction":1}
```

---

## Wymagania

- Python 3.10  
- Flask 2.2.5  
- Docker

