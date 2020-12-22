# opening .exe
import subprocess
import os

# windows media keys, win32 might be useful... maybe
# import win32api
# from win32con import VK_MEDIA_PLAY_PAUSE, KEYEVENTF_EXTENDEDKEY
from pyautogui import press, typewrite, hotkey

# windows notifications
from win10toast import ToastNotifier


def next_song():
    press('nexttrack')
    return 'Skipping...'


def shutdown(value):
    time = str(value * 60)
    os.system("shutdown -s -t  " + time)
    response = 'System due to shutdown in ' + str(value) + ' minutes.'
    return response


def abort_shutdown():
    os.system("shutdown -a")
    return 'Shutdown aborted.'


def volume(value):
    vol = str(round(value * 655.35))    # 65535 is max
    print(vol)
    os.system("V:\\Programs\\NirCMD\\nircmd.exe setsysvolume " + vol)
    response = 'Volume set to ' + str(value)
    return response


def audio_mute():
    hotkey('ctrl', 'left')
    return 'Discordo!'


def audio_microphone():
    toaster = ToastNotifier()
    os.system("V:\\Programs\\NirCMD\\nircmd.exe setdefaultsounddevice \"Microphone\" 1")
    os.system("V:\\Programs\\NirCMD\\nircmd.exe setdefaultsounddevice \"Microphone\" 2")
    toaster.show_toast("SiriFlask", "Using Microphone.")
    return 'Listening through the built-in mic.'


def audio_midi():
    toaster = ToastNotifier()
    os.system("V:\\Programs\\NirCMD\\nircmd.exe setdefaultsounddevice \"MIDI\" 1")
    os.system("V:\\Programs\\NirCMD\\nircmd.exe setdefaultsounddevice \"MIDI\" 2")
    toaster.show_toast("SiriFlask", "Using Virtual Desktop.")
    return 'Listening through the Oculus mic.'


def audio_headphones():
    toaster = ToastNotifier()
    os.system("V:\\Programs\\NirCMD\\nircmd.exe setdefaultsounddevice \"Headphones\" 1")
    os.system("V:\\Programs\\NirCMD\\nircmd.exe setdefaultsounddevice \"Headphones\" 2")
    toaster.show_toast("SiriFlask", "Using Headphones.")
    return 'Now playing audio through the headphones.'


def audio_speakers():
    toaster = ToastNotifier()
    os.system("V:\\Programs\\NirCMD\\nircmd.exe setdefaultsounddevice \"Speakers\" 1")
    os.system("V:\\Programs\\NirCMD\\nircmd.exe setdefaultsounddevice \"Speakers\" 2")
    toaster.show_toast("SiriFlask", "Using Speakers.")
    return 'Now playing audio through the speakers.'


def iTunes_open():
    subprocess.call(["C:\\Program Files\\iTunes\\iTunes.exe"])
    return 'iTunes coming right up!'


def play_pause():
    # win32api.keybd_event(VK_MEDIA_PLAY_PAUSE, 0, KEYEVENTF_EXTENDEDKEY, 0)
    press("playpause")
    return 'I did it!'


def err_opt():
    return 'Sorry, I don\'t know that command.'
