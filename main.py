import sys
sys.dont_write_bytecode = True

from dotenv import load_dotenv
import uvicorn

from src.app.server import InitializeServer
from src.config.config import PORT, ENVIRONMENT

load_dotenv()

app = InitializeServer()

reload = ENVIRONMENT != "PROD"

# Run the app with Uvicorn if this file is executed directly
if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=PORT,
        reload=reload
    )