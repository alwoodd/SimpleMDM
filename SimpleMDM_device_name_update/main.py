from my_utilities import init_log
from SimpleMDM_device_name_update.functions import *

LOG_FILE_NAME = "SimpleMDM_device_name_update.log"

def main():
    def local_update_and_log():
        """
        Call update_simple_mdm_name() and handle the logging cases.
        Returns:
        """
        log_message = "SimpleMDM name for serial number " + serial_number
        response = update_simple_mdm_name(device_id, device_name)
        if response.is_ok:
            logging.info(log_message + " updated to " + device_name)
        else:
            logging.error(log_message + " failed to update to " + device_name)
            for error in response.errors:
                logging.error("\t" + error)

    config = Config.get_instance()
    init_log(f"{config.project_root}/{LOG_FILE_NAME}", logging_level=logging.INFO)
    config.parse_cmd_line_args()

    existing_devices = retrieve_ipads()
    logging.info(str(len(existing_devices)) + " devices retrieved from SimpleMDM")
    logging.info("Device Updates:")

    for device in existing_devices:
        device_id = str(device["id"])
        attributes_dict = device["attributes"]
        device_name = attributes_dict["device_name"]
        simple_mdm_name = attributes_dict["name"]
        serial_number = attributes_dict["serial_number"]

        if device_name != simple_mdm_name:
            if device_name.startswith("iPad"):
                if config.all:
                    local_update_and_log()
            else:
                local_update_and_log()

    logging.info("Done")