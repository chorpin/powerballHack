from dataFeed_Plain.polygon_client import PolygonClient


client = PolygonClient().create_client().get_aggs("LCID",
                                                  1,
                                                  "day",
                                                  "2020-04-04",
                                                  "2023-01-04",)

print(len(client))
print(client)
