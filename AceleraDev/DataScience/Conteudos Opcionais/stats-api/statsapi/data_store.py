from uuid import uuid4, UUID

in_memory_storage = dict()

def save(data):
    data_uuid = uuid4()
    in_memory_storage[data_uuid] = data
    return data_uuid

def get(uuid):
    return in_memory_storage[(UUID(uuid))]