# import pygame, os

# class SOUND:
#         def __init__(self, path_to_sound, path_to_covers):
#             self.sound = pygame.mixer.Sound('Music\\' + path_to_sound)
#             self.cover = pygame.image.load('AssetsPlayer\\Covers\\' + path_to_covers)
#             self.is_playing = True
        
#         def placePhoto(self, screen):
#             self.cover = pygame.transform.scale(self.cover, (230, 200))
#             screen.blit(self.cover, (90, 100))

# def main():
    
#     width = 400
#     height = 500
    
#     screen = pygame.display.set_mode((width, height))
#     pygame.display.set_caption('MP3 Player')
#     clock = pygame.time.Clock()
#     run = True
    
#     path_to_sound = os.listdir('Music\\')
#     path_to_covers = os.listdir('AssetsPlayer\\Covers\\')
#     path_to_sound.sort()
#     path_to_covers.sort()
#     music = []
    
#     for i in zip(path_to_covers, path_to_sound):
#         sound = SOUND(path_to_covers = i[0], path_to_sound = i[1])
#         music.append(sound)
    
#     index = 0
#     back = pygame.image.load(os.path.join('AssetsPlayer', 'Back.png'))
#     screen.blit(back, (0, 0))
    
#     music[0].sound.play()
#     music[0].placePhoto(screen)
    
#     while run:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#             if pygame.mouse.get_pressed()[0]:
#                 if 223 <= pygame.mouse.get_pos()[0] <= 258 and 343 <= pygame.mouse.get_pos()[1] <= 366: 
#                     if music[index].is_playing:
#                         pygame.mixer.pause()
#                         music[index].is_playing = False
#                     else:
#                         pygame.mixer.unpause()
#                         music[index].is_playing = True
#                 elif 149 <= pygame.mouse.get_pos()[0] <= 184 and 378 <= pygame.mouse.get_pos()[1] <= 401:
#                     pygame.mixer.stop()
#                     index -= 1
#                     music[index+1].is_playing = True
#                     if index == -1:
#                         index = len(music) - 1
#                     music[index].sound.play()
#                     music[index].placePhoto(screen)
#                 elif 267 <= pygame.mouse.get_pos()[0] <= 302 and 343 <= pygame.mouse.get_pos()[1] <= 366:
#                     pygame.mixer.stop()
#                     index += 1
#                     music[index+1].is_playing = True
#                     if index == len(music):
#                         index = -1
#                     music[index].sound.play()
#                     music[index].placePhoto(screen)
                         
        
        
#         pygame.display.update()
#         clock.tick(60)
    
# if __name__ == '__main__':
#     pygame.init()
#     main()
#     pygame.quit()

import os
import pygame as pg

pg.init()

class SOUND:
    def __init__(self, path_to_sound, path_to_covers):
        self.sound = pg.mixer.Sound('Music\\' + path_to_sound)
        self.photo = pg.image.load('AssetsPlayer\\Covers\\' + path_to_covers)
        self.is_playing = True

    def placePhoto(self, screen):
        self.photo = pg.transform.scale(self.photo, (200, 200))
        screen.blit(self.photo, (111, 93))

path_to_sound = os.listdir('Music\\')
path_to_covers = os.listdir('AssetsPlayer\\Covers\\')
path_to_sound.sort()
path_to_covers.sort()

sounds = []

for index in zip(path_to_covers, path_to_sound):
    print(index)
    print(index[0])
    sound = SOUND(path_to_covers = index[0], path_to_sound = index[1])
    sounds.append(sound)

screen = pg.display.set_mode((400, 500))

BACKGROUND = pg.image.load('AssetsPlayer/Back.png').convert()
screen.blit(BACKGROUND, (0, 0))
sound_index = 0
sounds[0].sound.play()
sounds[0].placePhoto(screen)

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if pg.mouse.get_pressed()[0]:
            print(pg.mouse.get_pos())
            if 200 <= pg.mouse.get_pos()[0] <= 235 and 343 <= pg.mouse.get_pos()[1] <= 366:
                if sounds[sound_index].is_playing:
                    pg.mixer.pause()
                    sounds[sound_index].is_playing = False
                else:
                    pg.mixer.unpause()
                    sounds[sound_index].is_playing = True
            elif 147 <= pg.mouse.get_pos()[0] <= 182 and 343 <= pg.mouse.get_pos()[1] <= 366:
                pg.mixer.stop()
                sounds[sound_index].is_playing = True
                if(sound_index == 0):
                    sound_index = len(sounds)
                sound_index -= 1
                sounds[sound_index].sound.play()
                sounds[sound_index].placePhoto(screen)
            elif 243 <= pg.mouse.get_pos()[0] <= 278 and 343 <= pg.mouse.get_pos()[1] <= 366:
                pg.mixer.stop()
                sounds[sound_index].is_playing = True
                if(sound_index == len(sounds) - 1):
                    sound_index = -1
                sound_index += 1
                sounds[sound_index].sound.play()
                sounds[sound_index].placePhoto(screen)
    pg.display.flip()