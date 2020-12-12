from vk_api.keyboard import VkKeyboard, VkKeyboardColor

keyboard_out = VkKeyboard(one_time=False)
keyboard_in = VkKeyboard(inline=True)


def init():
    global keyboard_in, keyboard_out
    keyboard_out = VkKeyboard(one_time=True)
    keyboard_in = VkKeyboard(inline=True)


def reset_in():
    global keyboard_in
    keyboard_in = VkKeyboard(inline=True)


def reset_out():
    global keyboard_out
    keyboard_out = VkKeyboard(one_time=False)


def button_out(text, color='blue'):
    colors = {'blue': VkKeyboardColor.PRIMARY,
             'red': VkKeyboardColor.NEGATIVE,
             'green': VkKeyboardColor.POSITIVE,
             'white': VkKeyboardColor.SECONDARY}
    if color in colors.keys():
        global keyboard_out
        keyboard_out.add_button(text, color=colors[color])


def button_in(text, color='blue'):
    colors = {'blue': VkKeyboardColor.PRIMARY,
             'red': VkKeyboardColor.NEGATIVE,
             'green': VkKeyboardColor.POSITIVE,
             'white': VkKeyboardColor.SECONDARY}
    if color in colors.keys():
        global keyboard_in
        keyboard_in.add_button(text, color=colors[color])
