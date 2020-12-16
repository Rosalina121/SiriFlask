# SiriFlask
Control your PC with a Flask server and Shortcuts through Siri
## What's that?
It's just an example of what can be done with a simple Flask app and some Siri Shortcuts. Ask to show a file buried somewhere deep on your hard drive? Copy iOS clipboard to a Windows machine? Got you covered.  

This code is meant to be changed, improved and adapted to one's needs. The examples contain the methods I use everyday for my workflow, but that's just me. If you want to add a Bitcoin miner or a smart home integration, nothing's stopping you but your skills. 
## How to use
This is just a Flask server that's supposed to be running on the machine you want to control. This version works on your local network, but it shouldn't be an issue to forward a port and use it through the internet (though some security would be advised).  
The workflow looks kind of like this:
- Flask server runs on your machine
- You run a Shortcut on your iOS device (Siri or however you want)
- Magic happens when you request a specified URL or provide data

## Requirements
- Python
    - I used 3.8.4, shouldn't be an issue to run on other versions.
- iOS Shortcuts
- Whatever libraries and utilities you want to use to make this magic happen.
    - If you want to try the example code, `requirements.txt` should have everything you need.
    - Also the example code is written for Windows, so [NirCMD](https://www.nirsoft.net/utils/nircmd.html) (which is great!) is used for some methods, as well as Explorer.exe and other Windows utilities.
    - The `open_file` method uses Voidtools [EverythingSDK](https://www.voidtools.com/support/everything/sdk/)

## Examples
This repo contains a code with some examples. They might not be the best written snippets from that one guy on StackOverflow who fixed your issue and rewrote half of the app, but they work and I think they are a good place to start off.  
Note: It's all written for Windows since as much as I'd love to I just can't stand Cortana. That means there is probably a better and safer way to do those things on Linux or macOS. Also hardly any input is validated as I stupidly trust myself and/or validation is already on the Shortcuts side.
Also almost every method returns a string, which is later spoken by Siri or a shortcut, so that's why they are like they are.  

You can try these from `make_a_wish`:
 -  `iTunes_open` to open iTunes or literally any other application. I got tired of Cortana asking me if I want to open *iTunesHelper.exe*.
 - `play_pause` to simulate pressing a media button. It's using `pyautogui` which is also used in other examples. You can see some commented code that used the `win32api` but was hardly an elegant solution (but still a working one).
 - `shutdown(val)` and `abort_shutdown` are just like their CMD counterparts. One will shut down your PC after specified time (in minutes) and the other will abort it. I'm using NirCMD here however, since I just wanted to try it (and by try it I mean shutting off the PC when testing since I forgot an argument).
 - `volume(val)` sets system volume to specified amount. It accepts values from 0 to 100 and converts that to NirCMD value range. Honestly it will accept anything and at worst throw an error since i don't check wether the value is within range.
 - `audio_mute` will send a hotkey. The one in example is the one I use to mute myself on Discord. 
 - `audio_microphone`, `audio_midi`, `audio_headphones`, `audio_speakers` will use NirCMD to change the deafult audio input and/or output device. The arguments 1 and 2 mean changing the default media and communications device respectively. Without it would just change one (I think only media) and leave the other one as a default for communications. I use this to switch between my headphones and speakers, as well as 2 microphones. Note: NirCMD takes the device's name as an argument. If some devices have the same name you can rename one in the Windows Sound settings, since NirCMD takes the first one.
 - `next_song` skips a song. Uses other `pyautogui` hotkey like `'nexttrack'`.
 
 And these, since they're seperate methods:  
 - `google` takes a POST request with `'query'` as a key and opens a new tab of your browser with the Google search.
 - `clipboard` is by far my favorite one. It will copy your iOS clipboard contents and add them to your Windows clipboard. Works kinda like continuity on Apple devices. If there is only text in clipboard it will just do that, if there is an image it's gonna save it to `UPLOAD_FOLDER`. This method also supports a share sheet shortcut. There you'd specify a filename and works for any file (as long as you provide a valid file extension). This uses a base64 encode since I'm to lazy right now to figure out other means of upload (SSH maybe?).
 - `open_file` does just that. It opens a file or directory on your PC. In shortcut you specify the filename/dirname and extension (optional). Then Everything SDK returns a list of candidates and after choosing one Explorer.exe will either open the folder containing the file, open the folder or run the .exe file.
 
 Obviously endpoints, method names and others are all subject to your wildest dreams.
 
## Shortcuts
Flask server is just a one side of the story. The rest are Shortcuts. All work basically by `Get contents of URL` and saying out loud the server response. Some ask for input like numbers and strings, other just do a simple GET request.  
I'd try to update the list with some example Shortcuts as fast as possible.
