# Alba Favicon Service
This service provides Alba with favicons for websites in search results.

Privacy Policy and Terms of Service available at [alba.quest/legal](https://alba.quest/legal).

## Availability
This service has two endpoints:

- **Origin:** [favicons.alba.quest](https://favicons.alba.quest)

The CDN endpoint has additional CDN and browser caching configurations to reduce load on the origin server. If you require the latest favicon verison, use the origin endpoint. 

- 🚀 **CDN:** [favicons-cdn.alba.quest](https://favicons-cdn.alba.quest)

If you do not require the latest favicon version and prefer a fast response, please use the CDN endpoint. It might take up to 12 hours for new favicons to be available on the CDN endpoint.

## Usage
To request a favicon, use the following request pattern:
```http
GET  https://favicons-cdn.alba.quest/get?url=https://example.com
```
The favicon for the URL will be returned as a WEBP image with a file size of 16x16 pixels. If no favicon is available, a fallback favicon will be returned.

## Development
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the server: `python main.py`

> **Note**: This service requires Python 3.6.x or higher. It was developed using Python 3.9.x.

## License
This project is licensed under the [MIT License](LICENSE).

```text
MIT License

Copyright (c) 2023 Alba (alba.quest) by Paul Haedrich

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
```