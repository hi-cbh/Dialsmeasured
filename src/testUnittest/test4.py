

from src.base.baseFile import BaseFile
from src.base.baseAdb import BaseAdb


android_error_path = "/sdcard/Android/data/cn.cj.pe/log/"
pc_error_path = "/var/appiumRunLog/error_log/"
if BaseFile.adb_find_dir(android_error_path):
    BaseAdb.adb_pull(android_error_path,pc_error_path)