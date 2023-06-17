import psutil

def get_storage_info():
    total_storage = psutil.disk_usage('/').total / (1024 ** 3)  
    used_storage = psutil.disk_usage('/').used / (1024 ** 3)  
    remaining_storage = total_storage - used_storage

    storage_info = {
        'total_storage': round(total_storage, 2),
        'used_storage': round(used_storage, 2),
        'remaining_storage': round(remaining_storage, 2)
    }

    return storage_info
