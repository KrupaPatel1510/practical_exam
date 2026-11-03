import time
import uuid
from datetime import datetime, timezone


names =['Neha', 'Imran', 'Dev', 'Sana']
ids = {
	name: uuid.uuid5(uuid.NAMESPACE_DNS, name.lower() + ".example")
	for name in names
}

for name, identifier in ids.items():
	print(name, str(identifier)[:8])
print("All UUIDs are different:", len(set(ids.values())) == len(ids))

uuid3 = uuid.uuid3(uuid.NAMESPACE_DNS, "example.com")
uuid5 = uuid.uuid5(uuid.NAMESPACE_DNS, "example.com")
print(uuid3 != uuid5, uuid3.version, uuid5.version)

ts = 1000000000
print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(ts)))
print(time.asctime(time.gmtime(ts)))
print(datetime.fromtimestamp(ts, timezone.utc).strftime("%d %b %Y"))

start = time.perf_counter()
total = sum(range(1_000_000))
elapsed = time.perf_counter() - start
print(total, type(elapsed).__name__, elapsed >= 0)