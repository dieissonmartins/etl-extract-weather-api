from typing import List, Dict


class TransformRawData:
    def transfrom(self, extract_data) -> List[Dict]:
        try:
            ret = self.__filter_and_transform_data(extract_data)
            return ret
        except Exception as e:
            raise TypeError(e)

    def __filter_and_transform_data(self, extract_data) -> List[Dict]:
        transformed_information = []

        data = extract_data['data']

        resolvedAddress = data['resolvedAddress']
        address = data['address']
        timezone = data['timezone']
        latitude = data['latitude']
        longitude = data['longitude']

        for row in data['days']:
            aux = {
                'resolvedAddress': resolvedAddress,
                'address': address,
                'timezone': timezone,
                'latitude': latitude,
                'longitude': longitude,
                'datetime': row['datetime'],
                'tempmin': row['tempmin'],
                'tempmax': row['tempmax'],
                'temp': row['temp'],
                'description': row['description']
            }

            transformed_information.append(aux)

        return transformed_information
