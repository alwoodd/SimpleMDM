import logging
import requests
from my_utilities.classes import SingletonBase

class Config(SingletonBase):
    """
    Exposes configurable items.
    Attributes:
        all (bool): If True, all iPad SimpleMDM names are updated.
    """
    def __init__(self):
        super().__init__()
        self.all = None
        self.dry_run = None
        self.project_root = None

    def parse_cmd_line_args(self):
        """
        Set up and use argparse to get expected config info.
        """
        import argparse
        update_mode = ("a", "all")
        dry_run = ("d", "dry-run")

        arg_parser = argparse.ArgumentParser(prog="SimpleMDM_device_name_update",
                                             description="Uses SimpleMDM API to update all iPad's SimpleMDM name to its device name. By default, iPads whose device name starts with 'iPad' are skipped.")
        arg_parser.add_argument("-" + update_mode[0], "--" + update_mode[1], action="store_true",
                                help="Update ALL iPad names, including those whose device names start with 'iPad'.")
        arg_parser.add_argument("-" + dry_run[0], "--" + dry_run[1], dest=dry_run[1], action="store_true",
                                help="Don't actually update SimpleMDM names.")

        args_namespace = arg_parser.parse_args()
        args_dict = vars(args_namespace) #Convert to dict

        self.all = args_dict[update_mode[1]]
        self.dry_run = args_dict[dry_run[1]]

        logging.info(f"{update_mode[1]}:{self.all}")
        logging.info(f"{dry_run[1]}:{self.dry_run}")


class ResponseValue:
    """
    Simplifies a requests.Response for easier use and consumption.
    """
    def __init__(self, response : requests.Response):
        self.is_ok = True
        self.errors = None
        # Handle response being passed None.
        if response is not None:
            self.is_ok = response.ok
            self.errors = ResponseValue._get_errors(response)

    @staticmethod
    def _get_errors(response : requests.Response):
        """
        Parse out any errors from the passed response.
        Args:
            response (requests.Response):

        Returns: [str]
        """
        errors = []

        response_dict = response.json()
        errors_list = response_dict.get("errors")
        if errors_list is not None:
            errors = [title_dict["title"] for title_dict in errors_list]

        return errors