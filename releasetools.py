import common
import edify_generator
import os

def ModifyBegin(edify):
  edify.script[0] = \
  '''ifelse(is_mounted("/system"), unmount("/system"));
ifelse(is_mounted("/data"), unmount("/data"));
ui_print("******************************************");
ui_print("* Flyme6 based on Android6.0");
ui_print("*");
ui_print("* Powered by GuaiYiHu");
ui_print("* Now loading Flyme...");
ui_print("******************************************");\n''' + edify.script[0]

def CopyConfig(info):
    config = info.input_zip.read("META/flash.config")
    common.ZipWriteStr(info.output_zip, "flash.config", config)

def CopyRecovery(info):
    recovery = info.input_zip.read("META/twrp_recovery.img")
    common.ZipWriteStr(info.output_zip, "twrp_recovery.img", recovery)

def FullOTA_InstallEnd(info):
    edify = info.script
    ModifyBegin(edify)
    CopyConfig(info)
    CopyRecovery(info)
