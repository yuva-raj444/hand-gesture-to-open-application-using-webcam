from threading import Thread
import subprocess

applications = {
    1: 'notepad.exe',
    2: 'calc.exe',
    4: 'cmd.exe',
    5: 'mspaint.exe',
    6: 'explorer.exe',
    7: 'vlc',
    8: 'spotify',
    9: 'snippingtool',
    10: 'taskmgr.exe'
}

# Launch application in a non-blocking thread
def launch_application(app):
    try:
        Thread(target=subprocess.Popen, args=([app],)).start()
        print(f"🚀 Launched: {app}")
    except Exception as e:
        print(f"❌ Failed to launch {app}: {e}")
