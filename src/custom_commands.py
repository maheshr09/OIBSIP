import json
import webbrowser
import os
from src.responses import speak

def load_config(filepath="config/commands.json"):
    """Safely loads and parses the custom commands JSON file."""
    if not os.path.exists(filepath):
        print(f"Warning: Configuration file {filepath} not found.")
        return []

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get("commands", [])
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON syntax in {filepath}: {e}")
        return []
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return []

def handle_custom_command(command_text: str, custom_commands: list) -> bool:
    """
    Checks if the spoken text matches any custom triggers.
    If so, executes the safe action and returns True.
    Returns False if no match is found.
    """
    if not command_text or not custom_commands:
        return False
        
    command_lower = command_text.lower()
    
    for cmd in custom_commands:
        trigger = cmd.get("trigger", "").lower()
        if not trigger:
            continue
            
        # Match if the trigger is anywhere in the command
        if trigger in command_lower:
            action_type = cmd.get("action_type")
            action_value = cmd.get("action_value")
            
            # Strict secure routing - NO EVAL()
            if action_type == "open_url":
                speak(f"Opening {trigger}")
                webbrowser.open(action_value)
                return True
            elif action_type == "speak":
                speak(action_value)
                return True
            else:
                print(f"Unknown action_type '{action_type}' for trigger '{trigger}'")
                
    return False
