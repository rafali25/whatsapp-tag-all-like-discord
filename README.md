# WhatsApp Group Tagger

This **WhatsApp Group Tagger** Python script enables you to tag all members in a WhatsApp group quickly by typing a specified pattern, `@allwp<number>`. It listens for this pattern as you type and automates tagging the specified number of group members using the `@` symbol.

## How It Works
When you type `@allwp<number>` (for example, `@allwp5`), the program will detect this pattern and automatically tag the specified number of group members. This is especially useful for group messages when you need to notify everyone quickly.

## Dependencies
This project relies on the following Python libraries:

- **`pynput`**: Monitors keyboard input to detect typing patterns in real time.
- **`pyautogui`**: Automates typing and navigation within the WhatsApp window to tag members.
- **`re`**: Built-in library for regular expression matching, used here to identify the `@allwp<number>` pattern.
- **`time`**: Built-in library for managing delays in automation to simulate realistic typing.

You can install the required dependencies using the command below:



## How to Use:-
just open the executable file and it will work.
Once running, the script will monitor your keyboard for the pattern @allwp<number>.
For example, typing @allwp5 will trigger the tagging process for 5 members.

## Typing the Pattern:
Type @allwp<number> in any input field in the WhatsApp group (e.g., @allwp10 for 10 members).
Press Shift (right shift) to activate the tagging feature.
The script will then automatically type @, navigate down to the next user, press Enter, and repeat until the specified number of tags has been entered.

## Stopping the Script:
Press the Escape (Esc) key to stop the script.

## Example Usage
Input: "@allwp5" (in WhatsApp chat)
Trigger: Press Right Shift
Result: Automatically tags 5 members in the chat.
