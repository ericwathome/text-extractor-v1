# Text Extractor V1

A simple project that extracts text presumably sent from an ocr model and returns a json object containing either an ID or Logbook data depending on the api request

## API Reference

#### Get all items

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `api_key` | `string` | **Required**. Your OpenAi API key |

#### Get ID Card json response

```http
  POST /identity_card_json
```

| Body   | Type   | Description                                    |
| :----- | :----- | :--------------------------------------------- |
| `text` | `json` | **Required**. containing a single `text` field |

#### Get LogBook json response

```http
  POST /logbook_card_json
```

| Body   | Type   | Description                                    |
| :----- | :----- | :--------------------------------------------- |
| `text` | `json` | **Required**. containing a single `text` field |

## Installation

Clone the project into your local machine. Ensure to have pydantic and marvin installed using pip

```bash
  cd /path/to/text-extractor-v1
  uvicorn main:app --reload
```
