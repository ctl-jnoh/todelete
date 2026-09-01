from ctl_data_client import DataClient

client = DataClient.from_config("./pophive.config.json")

info = client.dataset_info("crisistrends_monthly_aggregate")
print(f"Release: {info.release}")
print(f"Refreshed at: {info.refreshed_at}")

path = client.download(
    "crisistrends_monthly_aggregate",
    destination="./data",
)
print(f"Saved to {path}")

