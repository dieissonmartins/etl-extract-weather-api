from src.drivers.http_requester import HttpRequester
from src.stages.extract.extract_data import ExtractData
from src.stages.load.load_data import LoadData
from src.stages.transform.transform_raw_data import TransformRawData

http_requester = HttpRequester()

# extract data
data = ExtractData(http_requester)
extract_data = data.extract()

# transform data
data = TransformRawData()
transformed_data = data.transfrom(extract_data)

# load data
data = LoadData()
data.load(transformed_data)
