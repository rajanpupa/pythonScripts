from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time

class OnMyWatch:
    def __init__(self, watchDirectory: str): 
        self.watchDirectory = watchDirectory
        self.observer = Observer() 
    def run(self): 
        event_handler = Handler() 
        self.observer.schedule(event_handler, self.watchDirectory, recursive = True) 
        self.observer.start() 
        try: 
            while True: 
                time.sleep(5) 
        except: 
            self.observer.stop() 
            print("Observer Stopped") 
        self.observer.join() 
class Handler(FileSystemEventHandler): 
    @staticmethod
    def on_any_event(event): 
        if event.is_directory: 
            return None
        elif event.event_type == 'created':
            print("Watchdog received created event - % s" % event.src_path) 
        elif event.event_type == 'deleted':
            print("Watchdog received deleted event - % s" % event.src_path) 
        elif event.event_type == 'modified': 
            print("Watchdog received modified event - % s." % event.src_path) 

if __name__ == '__main__': 
    watch = OnMyWatch("c:\\Users\Raj\Downloads") 
    watch.run() 