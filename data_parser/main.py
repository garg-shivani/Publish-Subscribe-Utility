import string
import sys
from pathlib import Path
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject, Property, Signal
import os
import json
import time
import threading 

class EventManager:
    def __init__(self):
        self.subscribers = []
    
    #subscribe fun is by the subscribers for subscribing to event
    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self.subscribers.remove(subscriber)

    def notify(self, event, data):
        for subscriber in self.subscribers:
            subscriber.update(event, data)
            
class JsonUpdater:
    def __init__(self, event_manager):
        self.event_manager = event_manager

    def update_json_data(self, file_path):
        #this fun is updating the json data and sending the nofification for the data update
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                json_data = json.load(file)

            json_data["age"] += 1
            json_data["Occupation"] = "Updated Occupation"

            with open(file_path, 'w') as file:
                json.dump(json_data, file, indent=2)

            # Notify subscribers about the update
            self.event_manager.notify('json_updated', json_data)
        else:
            print(f"File '{file_path}' not found.")
            
class JsonSubscriber(QObject):
    #update function which will get invoked the event gets published by the publish
    def __init__(self, parent=None):
        super().__init__(parent)
        self.data = None
    nameChanged = Signal()
    ageChanged = Signal()
    genderChanged = Signal()
    occupationChanged = Signal()
           
    # Declare properties for QML access
    @Property(str, notify=nameChanged)
    def name(self):
        return self.data["name"]

    @name.setter
    def name(self, value):
        if self.data["name"] != value:
            self.data["name"] = value
            self.nameChanged.emit()

    @Property(int, notify=ageChanged)
    def age(self):
        return self.data["age"]

    @age.setter
    def age(self, value):
        if self.data["age"] != value:
            self.data["age"] = value
            self.ageChanged.emit()
            
    @Property(str, notify=genderChanged)
    def gender(self):
        return self.data["gender"]

    @gender.setter
    def gender(self, value):
        if self.data["gender"] != value:
            self.data["gender"] = value
            self.genderChanged.emit()
            
    @Property(str, notify=genderChanged)
    def occupation(self):
        return self.data["occupation"]

    @occupation.setter
    def occupation(self, value):
        if self.data["occupation"] != value:
            self.data["occupation"] = value
            self.occupationChanged.emit()
            
    
    def update(self, event, data):
        print(f"Received event '{event}' with data: {data}")
        self.data = data
        self.nameChanged.emit()
        self.ageChanged.emit()
        self.genderChanged.emit()
        self.occupationChanged.emit()
        
 

class JsonParser:
    def __init__(self):
        pass

    def parse_json_from_file(self, file_path):
        #this function returning the json data by reading the data from the json file
        try:
            with open(file_path, 'r') as file:
                # Read JSON data from the file
                json_data = file.read()

            # Parse the JSON data
            parsed_data = json.loads(json_data)

            # Return the parsed data
            return parsed_data
        except (json.JSONDecodeError, FileNotFoundError) as e:
            # Handle JSON decoding errors or file not found
            print(f"Error loading/parsing JSON: {e}")
            return None
 
def infinite_loop_task():
    while True:
        json_updater.update_json_data(file_path)
        data = json_parser.parse_json_from_file(file_path)
        time.sleep(4)  # Adjust sleep time as needed

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    # Get the current directory of the main.py script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    qml_file = os.path.join(script_dir, "Main.qml")
    # Create the QML engine
    engine = QQmlApplicationEngine()
    event_manager = EventManager()
    json_updater = JsonUpdater(event_manager)

    # Subscribe a JsonSubscriber to the 'json_updated' event
    subscriber = JsonSubscriber()
    event_manager.subscribe(subscriber)
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, 'data.json')
    json_parser = JsonParser()
    def infinite_loop_task():
        while True:
            json_updater.update_json_data(file_path)
            data = json_parser.parse_json_from_file(file_path)
            time.sleep(4)  # Adjust sleep time as needed
    thread = threading.Thread(target=infinite_loop_task)
    thread.start()
        # Load the QML file
    engine.load(qml_file)
    # Expose the subscriber's data to the QML context
    root_context = engine.rootContext()
    root_context.setContextProperty("subscriber", subscriber)

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())

    

        


