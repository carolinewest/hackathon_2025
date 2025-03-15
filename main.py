import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Cyber Security Game")

# Fonts & Colors
font = pygame.font.Font(None, 32)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 200, 0)

# Game Messages (Phishing & Legitimate)
messages = [
    ("Your account has been locked! Click here to verify.", True),  # Phishing
    ("Don't forget the meeting at 3 PM today.", False),  # Legitimate
    ("You won a $1000 gift card! Claim now!", True),  # Phishing
    ("Can you send me the project file?", False),  # Legitimate
    ("Your password expired. Update it here!", True),  # Phishing
]

# Button Class
class Button:
    def __init__(self, text, x, y, width, height, color, action):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.action = action

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surf = font.render(self.text, True, BLACK)
        screen.blit(text_surf, (self.rect.x + 10, self.rect.y + 10))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# Game Class
class Game:
    def __init__(self):
        self.score = 0
        self.message, self.is_phishing = random.choice(messages)
        self.report_button = Button("Report", 200, 400, 100, 50, RED, self.report_phishing)
        self.ignore_button = Button("Ignore", 500, 400, 100, 50, GREEN, self.ignore_message)

    def update(self):
        pass  # No physics or movement needed

    def render(self):
        screen.fill(WHITE)
        text_surface = font.render(self.message, True, BLACK)
        screen.blit(text_surface, (100, 200))
        self.report_button.draw()
        self.ignore_button.draw()
        score_text = font.render(f"Score: {self.score}", True, BLACK)
        screen.blit(score_text, (10, 10))

    def handle_click(self, pos):
        if self.report_button.is_clicked(pos):
            self.report_button.action()
        elif self.ignore_button.is_clicked(pos):
            self.ignore_button.action()
        self.new_message()

    def report_phishing(self):
        if self.is_phishing:
            self.score += 1  # Correctly reported phishing
        else:
            self.score -= 1  # Mistakenly reported a legit message

    def ignore_message(self):
        if not self.is_phishing:
            self.score += 1  # Correctly ignored legit message
        else:
            self.score -= 1  # Missed a phishing attempt

    def new_message(self):
        self.message, self.is_phishing = random.choice(messages)

# Main Game Loop
game = Game()
running = True

while running:
    screen.fill(WHITE)
    game.render()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            game.handle_click(event.pos)
    
    pygame.display.update()

pygame.quit()
