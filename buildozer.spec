!rm -f buildozer.spec
!buildozer init
# إضافة المكتبات الضرورية (sdl2) وتصاريح اليد والبلوتوث
!sed -i 's/requirements = .*/requirements = python3,kivy,sdl2,sdl2_image,sdl2_mixer,sdl2_ttf/' buildozer.spec
!sed -i 's/# android.permissions = .*/android.permissions = INTERNET,BLUETOOTH,BLUETOOTH_ADMIN,USB_PERMISSION/' buildozer.spec
!sed -i 's/# android.accept_sdk_license = False/android.accept_sdk_license = True/' buildozer.spec
!sed -i 's/# android.fullscreen = 0/android.fullscreen = 1/' buildozer.spec
