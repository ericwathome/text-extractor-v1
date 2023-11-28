
# Text Extractor V1

A simple project that extracts text presumably sent from an ocr model and returns json object containing either an ID or a Logbook json


## API Reference

#### Get all items


| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `marvin.settings.openai.api_key` | `string` | **Required**. Your OpenAi API key |

#### Get ID Card json response

```http
  POST /identity_card_json
```

| Body | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `json` | **Required**. containing a single `text` field |

#### Get ID Card json response

```http
  POST /logbook_card_json
```

| Body | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `json` | **Required**. containing a single `text` field |


## Installation

Clone the project into your local machine. Ensure to have pydantic and marvin installed using pip

```bash
  cd /path/to/text-extractor-v1
  uvicorn main:app --reload
```
    