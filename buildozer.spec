[app]

title = Bangla Scientific Calculator
package.name = banglascientificcalculator
package.domain = org.example

source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,ttf

version = 1.0

requirements = python3,kivy,charset_normalizer==3.3.2

orientation = portrait

fullscreen = 0


[buildozer]

log_level = 2
warn_on_root = 1


[buildozer:android]

android.api = 35
android.minapi = 24
android.ndk = 27.2.12479018
android.accept_sdk_license = True
