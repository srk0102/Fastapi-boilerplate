from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from src.config.config import DATABASE_URL, DATABASE_NAME, ENVIRONMENT

client_kwargs = {}

if ENVIRONMENT == 'PROD':
    client_kwargs['tls'] = True
    client_kwargs['tlsAllowInvalidCertificates'] = False


class Database:
    _client: AsyncIOMotorClient | None = None
    _db: AsyncIOMotorDatabase | None = None

    @staticmethod
    async def connect() -> None:
        Database._client = AsyncIOMotorClient(
            DATABASE_URL, **client_kwargs)
        Database._db = Database._client[DATABASE_NAME]
        print(f"✅ Connected to DataBase!")

    @staticmethod
    async def close() -> None:
        if Database._client is not None:
            Database._client.close()
            print("🚦 MongoDB connection closed.")
        else:
            print("⚠️ No MongoDB client to close.")

    @staticmethod
    def get_db() -> AsyncIOMotorDatabase:
        if Database._db is not None:
            return Database._db
        else:
            raise ConnectionError("Database not connected")
