import pygame


class MainMenu(object):
    """MainMenu is an example of a menu using buttons."""
    
    def __init__(self, game):
        # Initialize the main menu bution group.
        self.button_group = ButtonGroup()
        self.button_group.set_keyboard(True)
        self.button_group.set_mouse(True)
        self.button_group.add_buttons(
            Button(game, "Start", [150, 50], [200, 100],
                lambda: None), # 'None' should be replace with a function to run
                              # when the button is clicked
            Button(game, "Load", [150, 175], [200, 100],
                lambda: None),
            Button(game, "Quit", [150, 300], [200, 100],
                lambda: None)
        )
        self.button_group.set_active(True)

    def update(self, dt):
        self.button_group.update(dt)

    def render(self):
        self.button_group.render()


class ButtonGroup(object):
    def __init__(self):
        self.buttons = []
        self.keyboard = False
        self.mouse = False
        self.active = False

    def set_active(self, active):
        self.active = active

        for button in self.buttons:
            button.set_active(active)

    def set_keyboard(self, keyboard):
        if keyboard:
            self.keyboard = True
            self.current = 0
            # Initialize key_wait to register key presses
            # when started without waiting 0.1 seconds first.
            self.key_wait = 100

        else:
            self.keyboard = False

    def set_mouse(self, mouse):
        self.mouse = mouse

    def update(self, dt):
        hovered_id = -1 # no button hovered

        # If button group is inactive, don't update the buttons.
        if not self.active:
            return

        if self.mouse:
            for button in self.buttons:
                button.mouse_update()

                if button.is_hovered():
                    hovered_id = button.get_id()

        if self.keyboard:
            keydown = pygame.key.get_pressed()

            # Wait 0.1 seconds between registering keypresses.
            self.key_wait += dt

            if hovered_id == -1 and self.key_wait >= 100:
                if keydown[pygame.K_DOWN]:
                    self.key_wait = 0
                    self.current += 1
                if keydown[pygame.K_UP]:
                    self.key_wait = 0
                    self.current -= 1

                if self.current < 0:
                    self.current = 0
                elif self.current >= len(self.buttons):
                    self.current = len(self.buttons) - 1

            else:
                self.current = hovered_id

            for button in self.buttons:
                if button.get_id() == self.current:
                    button.keyboard_update(True, keydown[pygame.K_SPACE])
                else:
                    button.keyboard_update(False, keydown[pygame.K_SPACE])

    def render(self):
        for button in self.buttons:
            button.render()

    def add_buttons(self, *buttons):
        ids = []

        for button in buttons:
            ids.append(self.add_button(button))

        return ids

    def add_button(self, button):
        self.buttons.append(button)

        id = len(self.buttons)-1 # the button's id
        self.buttons[-1].set_id(id)

        return id

    def get_button(self, id):
        return self.buttons[id]


class Button(object):
    def __init__(self, game, text="", pos=(0,0), size=(0,0), func=None,
                    text_size=50, text_color=(0,0,0), color=(127,127,127),
                    hovered_color=(190,190,190), inactive_color=(63,63,63),
                    image=""):
        self.game = game
        self.text = text
        self.pos = pos
        self.size = size
        self.function = func
        self.text_size = 50
        self.text_color = text_color
        self.color = color
        self.hovered_color = hovered_color
        self.inactive_color = inactive_color
        self.image_name = image

        if self.image_name == "":
            self.image = pygame.font.SysFont(None, text_size).render(
                text, True, text_color)
        else:
            self.image = pygame.image.load(self.image_name)

        self.active = False
        self.hovered = False
        self.id = -1

    def set_active(self, active):
        self.active = active

    def mouse_update(self):
        self.check_hovered()

        if self.hovered and pygame.mouse.get_pressed()[0]:
            self.activate()

    def keyboard_update(self, hovered, click):
        self.hovered = hovered

        if self.hovered and click:
            self.activate()

    def render(self):
        if not self.active:
            color = self.inactive_color
        elif self.hovered:
            color = self.hovered_color
        else:
            color = self.color

        # SCREEN should be replaced with whatever the screen variable is.
        pygame.draw.rect(SCREEN, color,
                [self.pos[0], self.pos[1], self.size[0], self.size[1]])

        # center_x is the x which is used to center the text in the rectangle.
        # It is the x position of the button, plus half the difference of the
        # width of the button minus the width of the text.
        center_x = self.pos[0] + (
                (self.size[0] - self.image.get_width()) / 2)
        # center_y is the same, except in the y-axis.
        center_y = self.pos[1] + (
                (self.size[1] - self.image.get_height()) / 2)

        # SCREEN should also be replaced here.
        SCREEN.blit(self.image, [center_x, center_y])

    def check_hovered(self):
        mouse_pos = pygame.mouse.get_pos()

        if ((self.pos[0] <= mouse_pos[0] <= self.pos[0]+self.size[0])
                and (self.pos[1] <= mouse_pos[1] <= self.pos[1]+self.size[1])):
            self.hovered = True
        else:
            self.hovered = False

    def is_hovered(self):
        return self.hovered

    def activate(self):
        if self.function is not None:
            self.function()

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id
