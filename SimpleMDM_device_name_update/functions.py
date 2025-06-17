API_KEY = "EBxI8BgAov9jY4gh60KJzPtU2fVCSanskjS9G4WYQ3219yupy7Yca8ZJENh2Z6x3",""
ROOT_URL = "https://a.simplemdm.com/api/v1/"
HTTP_SUCCESS = 200
MAX_NUMBER_OF_OBJECTS = 500

from SimpleMDM_device_name_update.classes import *

def retrieve_devices() -> [dict]:
    """
    Use SimpleMDM API to retrieve all (up to MAX_NUMBER_OF_OBJECTS) devices.
    Returns:
        [dict]
    """
    devices = []
    response = requests.get(ROOT_URL + "devices", params={"limit":  MAX_NUMBER_OF_OBJECTS}, auth=API_KEY)
    if response.status_code == HTTP_SUCCESS:
        data_dict = response.json()
        devices = data_dict["data"]

    return devices

def retrieve_ipads() -> [dict]:
    """
    retrieve_devices(), then filter out everything but iPads.
    Returns:
        [dict]
    """
    devices = retrieve_devices()
    #Filter out everything but iPads.
    devices = [device_dict for device_dict in devices if device_dict["attributes" ]["model_name"].startswith("iPad")]
    return devices

def update_simple_mdm_name(device_id, simple_mdm_name):
    """
    Use SimpleMDM API to update the simple_mdm_name for the passed device_id.
    Args:
        device_id (str): SimpleMDM's PK
        simple_mdm_name (str): Value to update SimpleMDM name to.

    Returns: ResponseValue
    """
    response = None
    
    if not Config.get_instance().dry_run:
        response = requests.patch(ROOT_URL + "devices/" + device_id, auth=API_KEY, data={"name": simple_mdm_name})

    return ResponseValue(response)
