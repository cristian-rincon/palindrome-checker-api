# palindrome-checker-api

This api allows you to search the longest palindrome from a given text. You can find de Api docs at ´/´ (this will redirect you to ´/docs´).

The available endpoints are: 
´´´bash
/ - Redirects to /docs by default
/ping - Healthcheck endpoint
/palindrome - receives some text and returns the longest palindrome inside it.
´´´
## How to run this api

### Using Docker

´´´bash
docker pull crincon/api-palindrome:latest
docker run -p 8000:8000 crincon/api-palindrome
´´´

