#!/usr/bin/env python

import envoy
import subprocess
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, LoggingEventHandler


try:
  WATCH = sys.argv[1]
except:
  WATCH = '001-initial.py'
LASTRUN = 0


class watcher(FileSystemEventHandler):
  def on_modified(self, event):
    global WATCH, LASTRUN
    what = 'directory' if event.is_directory else 'file'
    if what == 'file' and event.src_path.startswith('./%s' % WATCH[:3]) and time.time()-LASTRUN > 2.0:
      LASTRUN = time.time()
      logging.info("Modified %s: %s", what, event.src_path)

      # Record the active window
      r = envoy.run('xdotool getactivewindow')
      window_id = r.std_out.strip()

      envoy.run('pkill -x -f "python %s"' % WATCH)
      proc = subprocess.Popen(['python %s' % WATCH], shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)

      # Restore the active window
      time.sleep(1.0)
      envoy.run('xdotool windowactivate %s' % window_id)


if __name__ == "__main__":
  logging.basicConfig(level=logging.INFO,
                      format='%(asctime)s - %(message)s',
                      datefmt='%Y-%m-%d %H:%M:%S')
  # path = sys.argv[1] if len(sys.argv) > 1 else '.'
  path = '.'
  observer = Observer()
  observer.schedule(watcher(), path, recursive=True)
  observer.start()
  try:
    while True:
      time.sleep(1)
  except KeyboardInterrupt:
    observer.stop()
  observer.join()
