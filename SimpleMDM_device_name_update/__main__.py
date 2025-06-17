import pathlib
import sys

from SimpleMDM_device_name_update.classes import Config

# Get the path of the file from which this module was loaded.
project_root  = str(pathlib.PurePath(__file__).parent)
# Make sure it is part of sys.path
if project_root not in sys.path:
    sys.path.append(project_root)

Config.get_instance().project_root = project_root

if __name__ == "__main__":
    from SimpleMDM_device_name_update.main import main
    main()