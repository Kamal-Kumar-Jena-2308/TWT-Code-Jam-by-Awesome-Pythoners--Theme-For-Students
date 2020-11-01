import pygame
import wikipedia
import random
import os
from tkinter import *
import tkinter as tk
from PIL import Image
from PIL import ImageTk
import requests
import json
import tkinter.messagebox as tsmg

pygame.init()
pygame.mixer.init()
try:
    def ok():
        print("Ok")


    def Game():

        ScreenW = 500
        ScreenH = 500
        FPS = 60
        gameIcon = pygame.image.load('Logo.ico')
        pygame.display.set_icon(gameIcon)
        window = pygame.display.set_mode((ScreenW, ScreenH))
        pygame.display.set_caption("Snakes - Made By :- Kamal Kumar Jena")
        pygame.display.update()
        font = pygame.font.SysFont("comicsans", 28)
        font1 = pygame.font.SysFont("Showcard Gothic", 69)
        font2 = pygame.font.SysFont("comicsans", 48)
        white = (255, 255, 255)
        black = (0, 0, 0)
        kuch_bhi = (255, 0, 0)
        pink = (255, 192, 203)
        # lime = (0, 0, 255)
        # purple = (148, 0, 211)
        # green = (0, 128, 0)
        darkgreen = (0, 0, 255)
        aese1 = (0, 125, 0)
        aese2 = (255, 125, 0)
        aese3 = (255, 125, 160)
        img = pygame.image.load("pictures\\1.jpg")
        img = pygame.transform.scale(img, (ScreenW, ScreenH)).convert_alpha()
        img1 = pygame.image.load("pictures\\gameover.jpg")
        img1 = pygame.transform.scale(img1, (ScreenW, ScreenH)).convert_alpha()
        # mainS = pygame.image.load("pictures\\saap.jpg")
        # mainS = pygame.transform.scale(mainS, (200,300)).convert_alpha()
        maina = pygame.image.load("pictures\\start.png")
        maina = pygame.transform.scale(maina, (500, 500)).convert_alpha()

        # mainst = pygame.image.load("pictures\\play.png")
        # mainst = pygame.transform.scale(mainst, (100, 100)).convert_alpha()

        def draw_snake(window1, color, snakelist, snakeW, snakeL):
            for x, y in snakelist:
                pygame.draw.rect(window1, color, [x, y, snakeW, snakeL])

        # def draw_aankh(window, color, x, y, snakeS):
        # for x, y in snakelist:
        # pygame.draw.rect(window, color, [x, y, snakeS, snakeS])

        def score_shower(text, color, x, y):
            screenText = font.render(text, True, color)
            window.blit(screenText, [x, y])

        def score_shower1(text, color, x, y):
            screenText = font1.render(text, True, color)
            window.blit(screenText, [x, y])

        def score_shower2(text, color, x, y):
            screenText = font2.render(text, True, color)
            window.blit(screenText, [x, y])

        clock = pygame.time.Clock()

        def gameloop():
            snakeX = 55
            snakeY = 45
            SCORE = 0
            foodX = random.randint(20, ScreenW / 2)
            foodY = random.randint(20, ScreenH / 2)
            snakeW = 10
            snakeL = 10
            snakeS = 10
            initV = 2
            SNAKE_V_X = 0
            SNAKE_V_Y = 0
            snkLen = 1
            snkList = []
            exitGame = False
            Gameover = False
            if not os.path.exists("hiscore.txt"):
                with open("hiscore.txt", "w") as f:
                    f.write("0")
            with open("hiscore.txt", "r") as f:
                highScr = f.read()
            while not exitGame:
                if Gameover:
                    with open("hiscore.txt", "w") as k:
                        k.write(str(highScr))
                    window.fill(white)
                    score_shower(f"Score: {SCORE}   Highscore: {highScr}", black, 6, 55)
                    window.blit(img1, (0, 0))
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            exitGame = True
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                welcome()
                else:
                    for event in pygame.event.get():
                        if snakeX + 8 > ScreenW or snakeX - 5 < 0 or snakeY + 8 > ScreenH or snakeY - 2 < 0:
                            pygame.mixer.music.load('sounds\\hit.wav')
                            pygame.mixer.music.play()
                            Gameover = True
                        if event.type == pygame.QUIT:
                            exitGame = True
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_q:
                                SCORE += 10
                            if event.key == pygame.K_RIGHT:
                                if SCORE < 200:
                                    SNAKE_V_X = initV
                                    SNAKE_V_Y = 0
                                if 200 < SCORE < 400:
                                    SNAKE_V_X = initV + 2
                                    SNAKE_V_Y = 0
                                if SCORE >= 400 and SCORE >= 800:
                                    SNAKE_V_X = initV + 4
                                    SNAKE_V_Y = 0
                                if SCORE >= 1000:
                                    SNAKE_V_X = initV + 7
                                    SNAKE_V_Y = 0
                            if event.key == pygame.K_DOWN:
                                if SCORE < 200:
                                    SNAKE_V_Y = initV
                                    SNAKE_V_X = 0
                                if 200 < SCORE < 400:
                                    SNAKE_V_Y = initV + 2
                                    SNAKE_V_X = 0
                                if SCORE >= 400 and SCORE >= 800:
                                    SNAKE_V_Y = initV + 4
                                    SNAKE_V_X = 0
                                if SCORE >= 1000:
                                    SNAKE_V_Y = initV + 7
                                    SNAKE_V_X = 0
                            if event.key == pygame.K_LEFT:
                                if SCORE < 200:
                                    SNAKE_V_Y = 0
                                    SNAKE_V_X = -initV
                                if 200 < SCORE < 400:
                                    SNAKE_V_Y = 0
                                    SNAKE_V_X = -initV - 2
                                if SCORE >= 400 and SCORE >= 800:
                                    SNAKE_V_Y = 0
                                    SNAKE_V_X = -initV - 4
                                if SCORE >= 1000:
                                    SNAKE_V_Y = 0
                                    SNAKE_V_X = -initV - 7
                            if event.key == pygame.K_UP:
                                if SCORE < 200:
                                    SNAKE_V_Y = -initV
                                    SNAKE_V_X = 0
                                if 200 < SCORE < 400:
                                    SNAKE_V_Y = -initV - 2
                                    SNAKE_V_X = 0
                                if SCORE >= 400 and SCORE >= 800:
                                    SNAKE_V_Y = -initV - 4
                                    SNAKE_V_X = 0
                                if SCORE >= 1000:
                                    SNAKE_V_Y = -initV - 4
                                    SNAKE_V_X = 0
                    snakeX = snakeX + SNAKE_V_X
                    snakeY = snakeY + SNAKE_V_Y
                    # aankX = snakeX+SNAKE_V_X
                    # aankY = snakeY+SNAKE_V_Y
                    if abs(snakeX - foodX) < 7 and abs(snakeY - foodY) < 7:
                        SCORE += 5
                        foodX = random.randint(20, ScreenW / 2)
                        foodY = random.randint(20, ScreenH / 2)
                        snkLen += 3
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound('sounds\\eat.wav'))
                        if SCORE > int(highScr):
                            highScr = SCORE
                    window.fill(white)
                    window.blit(img, (0, 0))
                    highScr = int(highScr)
                    head = [snakeX, snakeY]
                    snkList.append(head)

                    score_shower(f"Score: {SCORE}   Highscore: {highScr}", black, 10, 55)
                    draw_snake(window, black, snkList, snakeW, snakeL)
                    # draw_aankh(window, white, aankX, aankY, 2)
                    pygame.draw.rect(window, kuch_bhi, [foodX, foodY, snakeS, snakeS])
                    if len(snkList) > snkLen:
                        del (snkList[0])
                    if head in snkList[:-1]:
                        pygame.mixer.music.load('sounds\\hit.wav')
                        pygame.mixer.music.play()
                        Gameover = True
                clock.tick(FPS)
                pygame.display.update()

            pygame.quit()
            return main()

        def welcome():
            exitGame = False
            # window.fill(pink)
            # window.blit(mainS, (0,0))
            window.blit(maina, (0, 0))
            # window.blit(mainS, (100, 50))
            # window.blit(mainst, (100,250))
            pygame.mixer.music.load('sounds\\title.wav')
            pygame.mixer.music.play(-1)
            while not exitGame:
                score_shower1("SNAKES", kuch_bhi, 220, 200)
                score_shower2("Press Spacebar", black, 120, 350)
                pygame.draw.rect(window, darkgreen, [120, 340, 250, 6])
                pygame.draw.rect(window, aese2, [120, 400, 250, 6])
                pygame.draw.rect(window, darkgreen, [230, 270, 229, 2])
                pygame.draw.rect(window, pink, [235, 275, 229, 2])
                pygame.draw.rect(window, kuch_bhi, [240, 280, 229, 2])
                pygame.draw.rect(window, aese1, [245, 285, 229, 2])
                pygame.draw.rect(window, aese2, [250, 290, 229, 2])
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exitGame = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            pygame.mixer.music.load('sounds\\back.wav')
                            pygame.mixer.music.play(-1)
                            gameloop()
                clock.tick(FPS)
                pygame.display.update()
            pygame.quit()
            return main()

        welcome()
        gameloop()


    photoimage_list = []


    def wiki():
        window = tk.Toplevel()
        window.wm_iconbitmap("Logo.ico")
        img1 = Image.open("pictures//Wimg.jpg")
        img = img1.resize((600, 500), Image.ANTIALIAS)
        img.load()
        photoimg = ImageTk.PhotoImage(img)
        photoimage_list.append(photoimg)
        tk.Label(window, image=photoimg).pack()
        word = StringVar()
        window.geometry("700x700")
        window.minsize("600", "500")
        window.maxsize("600", "500")
        wrd = Entry(window, font="lucida 19 bold", bg="#C0C0C0", borderwidth=3, textvariable=word)
        wrd.place(x=280, y=138, width=250, height=45)

        def getWikis():
            b1 = Button(window, text="🢂", command=getWikis, font="black 16 bold", bg="yellow", width=2, borderwidth=5)
            b1.place(x=525, y=138)
            wiki1 = Text(window, bg="#C0C0C0", borderwidth=3, font="lucida 12")
            wiki1.place(x=50, y=227, width=500, height=250)
            # examples = Text(window, bg="#B9D9EB", borderwidth=3, font="lucida 12")
            # examples.place(x=245, y=303, width=300, height=60)
            # global word
            word1 = word.get()
            output = wikipedia.summary(f"{word1}", sentences=3)
            output1 = output.capitalize()
            wiki1.insert(1.0, output1)

        b1 = Button(window, text="🢂", command=getWikis, font="black 16 bold", bg="yellow", width=2, borderwidth=5)
        b1.place(x=525, y=138)
        wiki1 = Text(window, bg="#C0C0C0", borderwidth=3, font="lucida 12")
        wiki1.place(x=50, y=227, width=500, height=250)


    def Dicitionary():
        window = tk.Toplevel()
        window.wm_iconbitmap("Logo.ico")
        img = Image.open("pictures//Dictimg.jpg")
        img.load()
        photoimg = ImageTk.PhotoImage(img)
        photoimage_list.append(photoimg)
        tk.Label(window, image=photoimg).pack()
        word = StringVar()
        mean = StringVar()
        examSent = StringVar()
        window.geometry("600x400")
        window.minsize("600", "400")
        window.maxsize("600", "400")

        def getMeaning():
            tk.Label(window, image=photoimg).place(x=0, y=0)
            wrd1 = Entry(window, font="lucida 19 bold", bg="#B9D9EB", borderwidth=3, textvariable=word)
            wrd1.place(x=180, y=118, width=300, height=60)
            meaningss1 = Text(window, bg="#B9D9EB", borderwidth=3, font="lucida 12")
            meaningss1.place(x=240, y=203, width=300, height=60)
            examples = Text(window, bg="#B9D9EB", borderwidth=3, font="lucida 12")
            examples.place(x=245, y=303, width=300, height=60)
            b1 = Button(window, text="🢂", command=getMeaning, font="black 21 bold", bg="yellow", width=3,
                        borderwidth=5)
            b1.place(x=421, y=118)
            b2 = Button(window, text=" ⚠️issues ⚠️", command=issues, font="black 11 bold", bg="red", width=10,
                        borderwidth=5)
            b2.place(x=40, y=42)
            wrd1 = word.get()
            url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{wrd1}"
            a = requests.get(url)
            text = a.text
            jtext = json.loads(text)
            raw1 = jtext[0].get('meanings')
            if raw1 != []:
                raw2 = raw1[0].get('definitions')
                raw3 = raw2[0].get('definition')
                # raw4 = raw2[0].get('definition')
                raw5 = raw2[0].get('example')
                # raw6 = raw2[0].get('synonyms')
                if raw3 and raw5:
                    meaningss1.insert(1.0, f"{raw3.capitalize()}")
                    examples.insert(1.0, f"{raw5.capitalize()}.")
                window.update()
            else:
                return main()

        def issues():
            tsmg.showinfo("Sorry ,if you didn't found the word",
                          "Word was not found because of following reasons:-\n     -Check your internet connection\n     -Make sure that the spelling of word is correct\n     -Try again if everything is ok")

        wrd = Entry(window, font="lucida 19 bold", bg="#B9D9EB", borderwidth=3, textvariable=word)
        wrd.place(x=170, y=118, width=300, height=60)
        b1 = Button(window, text="🢂", command=getMeaning, font="black 21 bold", bg="yellow", width=3, borderwidth=5)
        b1.place(x=421, y=118)
        meaningss1 = Text(window, bg="#B9D9EB", borderwidth=3, font="lucida 12")
        meaningss1.place(x=240, y=203, width=300, height=60)
        examples = Text(window, bg="#B9D9EB", borderwidth=3, font="lucida 12")
        examples.place(x=245, y=303, width=300, height=60)
        b2 = Button(window, text=" ⚠️issues ⚠️", command=issues, font="black 11 bold", bg="red", width=10,
                    borderwidth=5)
        b2.place(x=40, y=42)


    root = Tk()


    def main():
        root.wm_iconbitmap("Logo.ico")
        image = Image.open("pictures//MainScr.jpg")
        image = image.resize((700, 500), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        label = Label(image=photo)
        label.pack()
        b1 = Button(text="🌸🌸 Get Meaning 🌸🌸", command=Dicitionary, bg="#c7ff20", height=5, width=17, relief=SUNKEN,
                    borderwidth=6)
        b1.place(
            x=150, y=210)
        b2 = Button(text="🌸🌸 Get Wiki 🌸🌸", command=wiki, bg="#c7ff20", height=5, width=17, relief=SUNKEN,
                    borderwidth=6)
        b2.place(
            x=449, y=210)
        b3 = Button(text="Play Game", command=Game, bg="coral", height=2, relief=SUNKEN, borderwidth=10)
        b3.place(x=315, y=400)
        root.minsize("700", "500")

        root.maxsize("700", "500")
        root.geometry("500x500")
        root.mainloop()
        exit()

    main()

except Exception as e:
    print(e)
