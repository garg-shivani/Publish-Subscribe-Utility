import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    visible: true
    width: 400
    height: 300
    title: "Pub Sub Model"
   
    Item {
        anchors.fill: parent
        ColumnLayout {
            anchors.centerIn: parent
            spacing: 10
    
            // Name field
            ColumnLayout {
                spacing: 2
                Label {
                    text: "Name:"
                    Layout.fillWidth: true
                }
                TextField {
                    id: nameField
                    placeholderText: "Enter your name"
                    Layout.fillWidth: true
                    text: subscriber.name
                }
            }
    
            // Age field
            ColumnLayout {
                spacing: 2
                Label {
                    text: "Age:"
                    Layout.fillWidth: true
                }
                TextField {
                    id: ageField
                    placeholderText: "Enter your age"
                    Layout.fillWidth: true
                    text: subscriber.age
                }
            }
        
    

            
            // Gender field
            ColumnLayout {
                spacing: 2
                Label {
                    text: "Gender:"
                    Layout.fillWidth: true
                }
                TextField {
                    id: genderField
                    placeholderText: "Enter your gender"
                    Layout.fillWidth: true
                    text: subscriber.gender
                }
            }
            
            // Occupation field
            ColumnLayout {
                spacing: 2
                Label {
                    text: "Occupation:"
                    Layout.fillWidth: true
                }
                TextField {
                    id: occupationField
                    placeholderText: "Enter your occupation"
                    Layout.fillWidth: true
                    text: subscriber.occupation
                }
            }
            //// Update button
            //Button {
            //    text: "Receive Data"
            //    Layout.fillWidth: true
            //    onClicked: {
            //        // Handle the update action
            //      
            //
            //    }
            //}
        }
    }
}
