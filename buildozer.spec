[app]
title = الصندوق
package.name = hesabat
package.domain = org.omar
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,db
version = 1.0
requirements = python3,kivy==2.3.0,kivymd==1.1.1,arabic_reshaper,python-bidi==0.4.2,sqlite3,openpyxl,et_xmlfile,plyer,pyjnius
p4a.branch = 2024.1.21
orientation = portrait
fullscreen = 0
icon.filename = %(source.dir)s/icon.png

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = 1
android.accept_sdk_license = True
