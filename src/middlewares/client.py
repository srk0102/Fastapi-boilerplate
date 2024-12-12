import requests
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from user_agents import parse

from src.config.config import IP_INFO_API_KEY

class ClientInfoMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Collect client information from request headers
        client_info = {
            "client_ip": request.headers.get("X-Forwarded-For", request.client.host),  # Client's IP address
            "user_agent": request.headers.get("User-Agent", ""),  # User agent string
            "accept_language": request.headers.get("Accept-Language", ""),  # Accepted languages
            "accept_encoding": request.headers.get("Accept-Encoding", ""),  # Accepted encoding
            "referrer": request.headers.get("Referer", ""),  # Referrer URL
            "method": request.method,  # HTTP method (GET, POST, etc.)
            "path": request.url.path,  # Requested URL path
            "host": request.headers.get("Host", ""),  # Host of the request
            "origin": request.headers.get("Origin", ""),  # Origin of the request
        }

        # Parse the User-Agent string for browser and device details
        user_agent_string = request.headers.get("User-Agent", "")
        if user_agent_string:
            user_agent = parse(user_agent_string)
            client_info["browser"] = {
                "name": user_agent.browser.family,  # Browser name (e.g., Chrome, Firefox)
                "version": user_agent.browser.version_string,  # Browser version
            }
            client_info["os"] = {
                "name": user_agent.os.family,  # Operating system (e.g., Windows, macOS)
                "version": user_agent.os.version_string,  # OS version
            }
            client_info["device"] = {
                "family": user_agent.device.family,  # Device type (e.g., Desktop, Mobile)
                "brand": user_agent.device.brand,  # Device brand (e.g., Apple, Samsung)
                "model": user_agent.device.model,  # Device model (e.g., iPhone 12)
            }
            try:
                geoData = await self.GeoLocationOfClient(request.headers.get("X-Forwarded-For", request.client.host))
                client_info["geo_location"] = geoData
            except Exception as e:
                print(e)

        # Store client information in request.state for access in route handlers
        request.state.client_info = client_info

        # Process the request and return the response
        response = await call_next(request)
        return response

    async def GeoLocationOfClient(self, ip: str):
        url = "https://ipinfo.io/{}/json?token=31453a8a845c35".format(ip)  # Simplified URL construction
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad HTTP status
            data = response.json()
            return data
        except requests.RequestException as e:
            print(e)
            return {}