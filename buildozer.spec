[app]
title = Bangla Scientific Calculator
package.name = banglascientificcalculator
package.domain = org.example
source.dir = .
source.include_exts = py,ttf,png,jpg,kv
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1

[buildozer:android]
android.api = 35
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a
