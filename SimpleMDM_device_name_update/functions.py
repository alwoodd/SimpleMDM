API_KEY = "EBxI8BgAov9jY4gh60KJzPtU2fVCSanskjS9G4WYQ3219yupy7Yca8ZJENh2Z6x3",""
ROOT_URL = "https://a.simplemdm.com/api/v1/"
HTTP_SUCCESS = 200
MAX_NUMBER_OF_OBJECTS = 100 #100 is SimpleMDM's max.

from SimpleMDM_device_name_update.classes import *

def retrieve_devices() -> [dict]:
    """
    Use SimpleMDM API to retrieve all devices.
    The API can retrieve a maximum of 100 devices, so it is called repeatedly until has no more devices.
    Returns:
        [dict]
    """
    devices = []
    has_more = True
    starting_after = 0
    while has_more:
        response = requests.get(ROOT_URL + "devices", auth=API_KEY, params={
            "limit":  MAX_NUMBER_OF_OBJECTS,
            "starting_after": starting_after
        })
        if response.status_code == HTTP_SUCCESS:
            data_dict = response.json()
            logging.info(f"Retrieved {len(data_dict["data"])} devices ({data_dict["data"][0]["id"]}-{data_dict["data"][-1]["id"]})")
            devices += data_dict["data"]
            has_more = data_dict["has_more"]
            starting_after = data_dict["data"][-1]["id"]

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
