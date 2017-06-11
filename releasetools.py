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

def InstallSuperSU(info):
    root = info.input_zip.read("META/UPDATE-SuperSU.zip")
    common.ZipWriteStr(info.output_zip, "SuperSU/UPDATE-SuperSU.zip", root)

def FlashSUperSU(info):
    info.script.AppendExtra(('ui_print("Flashing SuperSU...");'))
    info.script.AppendExtra(('package_extract_dir("SuperSU", "/tmp/supersu");'))
    info.script.AppendExtra(('run_program("/sbin/busybox", "unzip", "/tmp/supersu/UPDATE-SuperSU.zip", "META-INF/com/google/android/*", "-d", "/tmp/supersu");'))
    info.script.AppendExtra(('run_program("/sbin/busybox", "sh", "/tmp/supersu/META-INF/com/google/android/update-binary", "dummy", "1", "/tmp/supersu/UPDATE-SuperSU.zip");'))
    info.script.AppendExtra(('ui_print("Finish!");'))

def FullOTA_InstallEnd(info):
    edify = info.script
    ModifyBegin(edify)
    InstallSuperSU(info)
    CopyConfig(info)
    CopyRecovery(info)
    FlashSUperSU(info)
