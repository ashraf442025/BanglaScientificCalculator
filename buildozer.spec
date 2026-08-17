[app]

title = Bangla Scientific Calculator
package.name = banglascientificcalculator
package.domain = org.bangla
source.dir = .
source.include_exts = py,kv,ttf,png,jpg
version = 1.0

requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]

log_level = 2
warn_on_root = 1

[buildozer:android]

android.api = 35
android.minapi = 21
android.ndk = 28c
android.archs = arm64-v8a
android.accept_sdk_license = True
