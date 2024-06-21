from config.database import zilliz_settings
from pymilvus import MilvusClient, DataType

class ZillizInitializerError(Exception):
    pass


class ZillizInitializaition:
    def __init__(self):
        # Initialize a MilvusClient instance
        CLUSTER_ENDPOINT = zilliz_settings.CLUSTER_ENDPOINT # Set your cluster endpoint
        TOKEN = zilliz_settings.TOKEN# Set your token

        try:
            self.client = MilvusClient(
                uri=CLUSTER_ENDPOINT,  # Cluster endpoint obtained from the console
                token=TOKEN  # API key or a colon-separated cluster username and password
            )
            print('Zilliz Connection Successful.')
        except Exception as e:
            raise ZillizInitializerError(f"Failed to initialize client: {str(e)}")


zilliz_client = ZillizInitializaition()
