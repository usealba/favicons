# Alba Favicon Service
This service provides Alba with favicons for websites in search results.

Privacy and Terms of Service available at [alba.quest/legal](https://alba.quest/legal).

### Availability
This service has two endpoints:
- Origin: [favicons.alba.quest](https://favicons.alba.quest)
- CDN: [favicons-cdn.alba.quest](https://favicons-cdn.alba.quest)

The CDN endpoint has additional CDN and browser caching configurations to reduce load on the origin server. If you require the latest favicon verison, use the origin endpoint. If you do not require the latest favicon version, please use the CDN endpoint. It might take up to 12 hours for new favicons to be available on the CDN endpoint.

### Development
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the server: `python main.py`

> **Note**: This service requires Python 3.6.x or higher. It was developed using Python 3.9.x.