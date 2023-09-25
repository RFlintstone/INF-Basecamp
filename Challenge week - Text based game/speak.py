import json


def dialog_trigger(who_is_talking, dialog_name, dialog_step):
    with open('dialog.json') as f:
        dialogs = json.load(f)

    # Find dialog by name
    for dialog in dialogs['dialogs']:
        if dialog['name'] == dialog_name:
            steps = dialog['steps']
            break

    # If we say player instead of user it will now work as well
    if who_is_talking == "player":
        who_is_talking = "user"

    # Print first step user utterance
    print(who_is_talking.capitalize() + ": " + steps[dialog_step][who_is_talking])


if __name__ == '__main__':
    dialog_trigger('user', 'greeting', 0)
    dialog_trigger('npc', 'greeting', 0)
    dialog_trigger('user', 'greeting', 1)
    dialog_trigger('npc', 'greeting', 1)
    dialog_trigger('user', 'greeting', 2)
    dialog_trigger('npc', 'greeting', 2)
