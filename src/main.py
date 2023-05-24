from src.drivers.http_requester import HttpRequester
from src.stages.extract.extract_data import ExtractData

http_requester = HttpRequester()

# extract data
data = ExtractData(http_requester)

extract_data = data.extract()

