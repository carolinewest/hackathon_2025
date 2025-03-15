import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1280, 720
TIME_LIMIT = 4000  # 5 seconds in milliseconds
BAR_WIDTH = 200
BAR_HEIGHT = 20
CHECKPOINT_DISPLAY_TIME = 2000  # 4 seconds

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Load images and define hidden object positions

images = [
    ("images/1_domain.jpeg", [(300, 200, 50, 50)]),  # Example image with hidden object
    ("images/2_asap.jpeg", [(500, 350, 40, 40)]),
    ("images/3_reply.jpeg", [(250, 400, 30, 30)]),
    ("images/4_immediate.jpeg", [(600, 150, 45, 45)]),
    ("images/5_logoNdomain.jpeg", [(200, 300, 35, 35), (550, 250, 40, 40)])  # One image with two objects
]

# Preload images
loaded_images = []
msg = ["DOMAIN: \nGenuine sender's usually don't use default 'gmail.com' to send official notifications", 
       "ASAP: \nPhishing emails like to sound urgent, to people won't have time to find out the trick", 
       "REPLY: \nSuspect first, if they want you to reply to different email address", 
       "IMMEDIATE: \nPhishing emails like to sound urgent",
       "LOGO: \nthe logo is distorted\n DOMAIN: \nthey have different email address from the company"]

img_count = 0
for img_path, _ in images:
    img = pygame.image.load(img_path)
    original_width, original_height = img.get_size()
    aspect_ratio = original_width / original_height
    
    if original_width > original_height:
        new_width = min(1100, original_width)
        new_height = int(new_width / aspect_ratio)
    else:
        new_height = min(600, original_height)
        new_width = int(new_height * aspect_ratio)

    img_resized = pygame.transform.scale(img, (new_width, new_height))

    x_pos = (WIDTH - new_width) // 2
    y_pos = (HEIGHT - new_height) // 2

    loaded_images.append((img_resized, x_pos, y_pos, msg[img_count]))
    print('img count: ', img_count, 'x_pos: ', x_pos, 'y_pos: ', y_pos)
    print('\n')
    img_count+=1

# Game variables
current_image = 0
found_objects = []
start_time = pygame.time.get_ticks()
score = 0
font = pygame.font.Font(None, 15)
running = True
show_answer = False

def show_checkpoint():
    screen.fill(GRAY)
    title = font.render("CHECKPOINTS", True, BLACK)
    message = font.render(current_msg, True, BLACK)
    screen.blit(title, (WIDTH // 2 - 80, HEIGHT // 2 - 40))
    screen.blit(message, (WIDTH // 2 - 120, HEIGHT // 2))
    pygame.display.flip()
    pygame.time.delay(CHECKPOINT_DISPLAY_TIME)

def show_game_over():
    screen.fill(WHITE)
    text = font.render(f"Game Over! Your Score: {score}/6", True, BLACK)
    screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2))
    pygame.display.flip()
    pygame.time.delay(3000)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FIND THE RED FLAGS")

while running:
    screen.fill(WHITE)
    img_resized, x_pos, y_pos, current_msg = loaded_images[current_image]
    screen.blit(img_resized, (x_pos, y_pos))
    
    # Timer logic
    elapsed_time = pygame.time.get_ticks() - start_time
    time_left = max(TIME_LIMIT - elapsed_time, 0)
    pygame.draw.rect(screen, RED, (WIDTH - BAR_WIDTH - 20, 20, BAR_WIDTH * (time_left / TIME_LIMIT), BAR_HEIGHT))

     # Display score on top left
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Show "Try Again!" message if clicked wrong
    if not show_answer and len(found_objects) < len(images[current_image][1]):
        try_again_text = font.render("Try Again!", True, RED)
        screen.blit(try_again_text, (WIDTH // 2 - 50, 10))

    # Draw found objects with red oval
    for obj in found_objects:
        pygame.draw.ellipse(screen, RED, obj["rect"].move(x_pos, y_pos), 5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            hit = False
            for obj in images[current_image][1]:
                if x >= x_pos + obj[0] and x <= x_pos + obj[0] + obj[2] and y >= y_pos + obj[1] and y <= y_pos + obj[1] + obj[3]:
                    found_objects.append(obj)
                    hit = True
            if not hit:
                text = font.render("Try Again!", True, RED)
                screen.blit(text, (WIDTH // 2 - 50, 10))
    
    # Draw found objects
    for obj in found_objects:
        pygame.draw.ellipse(screen, RED, (x_pos + obj[0], y_pos + obj[1], obj[2], obj[3]), 3)
    
    # Check if all objects are found
    if len(found_objects) == len(images[current_image][1]):
        score += len(images[current_image][1])
        pygame.time.delay(1000)
        show_checkpoint()
        current_image += 1
        if current_image >= len(images):
            show_game_over()
            running = False
        else:
            found_objects = []
            start_time = pygame.time.get_ticks()
    
    # Check time limit
    if time_left <= 0:
        show_checkpoint()
        current_image += 1
        if current_image >= len(images):
            show_game_over()
            running = False
        else:
            found_objects = []
            start_time = pygame.time.get_ticks()
    
    pygame.display.flip()

pygame.quit()
sys.exit()
