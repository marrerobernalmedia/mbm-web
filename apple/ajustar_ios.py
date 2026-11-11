# Ajustes del proyecto Xcode que Capacitor no pone solo (se puede correr varias veces).
# Uso: python3 apple/ajustar_ios.py elhome|recta
import sys, os
app = sys.argv[1]; R = os.path.join(os.path.dirname(os.path.abspath(__file__)), app, "ios", "App")
p = f"{R}/App/Info.plist"; s = open(p).read()
s = s.replace("<key>CFBundleDevelopmentRegion</key>\n\t<string>en</string>", "<key>CFBundleDevelopmentRegion</key>\n\t<string>es</string>")
s = s.replace("<string>armv7</string>", "<string>arm64</string>")
if "UIBackgroundModes" not in s:
    s = s.replace("\t<key>UIViewControllerBasedStatusBarAppearance</key>", "\t<key>UIBackgroundModes</key>\n\t<array>\n\t\t<string>remote-notification</string>\n\t</array>\n\t<key>ITSAppUsesNonExemptEncryption</key>\n\t<false/>\n\t<key>UIViewControllerBasedStatusBarAppearance</key>")
open(p, "w").write(s)
p = f"{R}/App.xcodeproj/project.pbxproj"; s = open(p).read()
if "CODE_SIGN_ENTITLEMENTS" not in s:
    s = s.replace("CODE_SIGN_STYLE = Automatic;", "CODE_SIGN_ENTITLEMENTS = App/App.entitlements;\n\t\t\t\tCODE_SIGN_STYLE = Automatic;")
open(p, "w").write(s)
open(f"{R}/App/App.entitlements", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n<plist version="1.0">\n<dict>\n\t<key>aps-environment</key>\n\t<string>production</string>\n</dict>\n</plist>\n')
print(app, "ajustado")
