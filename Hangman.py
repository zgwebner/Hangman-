import pygame as pg
import random as rd
import sprite as sp
pg.init()
pg.font.init()
w = pg.display.set_mode([1200, 600])
wordfont = pg.font.Font(None, 32)
enterfont = pg.font.Font(None, 32)
c = pg.time.Clock()
textrect = pg.Rect(530, 550, 140, 32)
inactivecolor = (0, 0, 0)
activecolor = (102, 255, 102)
black = (0, 0, 0)
textcolor = (199, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255)
currentcolor = inactivecolor
timer = 0
typer = True
active = False
boxtext = ''
donetext = False
ske1 = False
ske2 = False
ske3 = False
ske4 = False
ske5 = False
ske6 = False
inputtext1 = 'Input the word you want the other'
inputtext2 = 'player to guess'
letters = []
donedone = False
endscene = True
while not donetext:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            donedone = True
        if event.type == pg.MOUSEBUTTONDOWN:
            if textrect.collidepoint(event.pos):
                active = not active
            else:
                active = False
            currentcolor = activecolor if active else inactivecolor
        if event.type == pg.KEYDOWN:
            if active:
                if event.key == pg.K_RETURN:
                    word = boxtext
                    boxtext = ''
                    donetext = True
                elif event.key == pg.K_BACKSPACE:
                    boxtext = boxtext[:-1]
                else:
                    boxtext += event.unicode
    mousex, mousey = pg.mouse.get_pos()
    if textrect.collidepoint(mousex, mousey):
        pg.mouse.set_visible(False)
        hovering = True
    else:
        pg.mouse.set_visible(True)
        hovering = False
    surfacetext = wordfont.render(boxtext, True, textcolor)
    infosurfacetext = wordfont.render(inputtext1, True, textcolor)
    infosurfacetext2 = wordfont.render(inputtext2, True, textcolor)    
    width = max(200, surfacetext.get_width() + 10)
    textrect.w = width
    w.fill(white)
    w.blit(surfacetext, (textrect.x + 5, textrect.y + 5))
    w.blit(infosurfacetext, (((w.get_width() / 2) - (infosurfacetext.get_width() / 2)), 20))
    w.blit(infosurfacetext2, (((w.get_width() / 2) - (infosurfacetext2.get_width() / 2)), 45))
    x, y = ((surfacetext.get_width() + (textrect.x + 5))), (textrect.y + 5)
    wi, h = ((surfacetext.get_width() + (textrect.x + 5)), ((textrect.y + textrect.h) - 5))
    if active:
        timer += c.get_time()
        if timer >= 550:
            timer = 0
            typer = not typer
        if typer:
          pg.draw.line(w, black, (x, y), (wi, h), 2)
    if hovering:
        pg.draw.line(w, (0, 0, 0), (mousex, (mousey + 7)), (mousex, (mousey - 7)))
        pg.draw.line(w, (0, 0, 0), ((mousex - 2), (mousey + 7)), ((mousex + 2), (mousey + 7)))
        pg.draw.line(w, (0, 0, 0), ((mousex - 2), (mousey - 7)), ((mousex + 2), (mousey - 7)))
    pg.draw.rect(w, currentcolor, textrect, 2)
    pg.display.flip()
    c.tick(30)
    if donedone:
        pg.quit()
pg.mouse.set_visible(True)
donetext = False
w.fill(white)
pg.display.flip()
timer = 0
active = False
for r in word:
  letters.append(r)
thetext1 = "Your word is: " + str(letters) + ". "
thetext2 = "Loading..."
theetext = enterfont.render(thetext1, True, textcolor)
theetext2 = enterfont.render(thetext2, True, textcolor)
w.blit(theetext, (((w.get_width() / 2) - (theetext.get_width() / 2)), 20))
w.blit(theetext2, (((w.get_width() / 2) - (theetext2.get_width() / 2)), 45))
pg.display.flip()
pg.time.wait(3000)
w.fill(white)
tracker2 = 0
seudoletters = []
guessedletters = []
wrongletters = []
for g in range(len(letters)):
  h = letters[tracker2]
  seudoletters.append(h)
  tracker2 += 1
for h in range(len(letters)):
  guessedletters.append('_')
lettertracker = 0
strikes = 0
guesses = 0
currentcolor = inactivecolor
while strikes < 6:
  lettertracker = 0
  guesses += 1
  anothersone = 0
  guesstext = ('What is your #' + str(guesses) + ' guess? ')
  wrongtext = ('You have incorrectly guessed: ' + str('[%s]' % ', '.join(map(str, wrongletters))) + '. ')
  goodtext = ('Currently, you have revealed: ' + str('[%s]' % ', '.join(map(str, guessedletters))) + '. ')
  while not donetext:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            donedone = True
        if event.type == pg.MOUSEBUTTONDOWN:
            if textrect.collidepoint(event.pos):
                active = not active
            else:
                active = False
            currentcolor = activecolor if active else inactivecolor
        if event.type == pg.KEYDOWN:
            if active:
                if event.key == pg.K_RETURN:
                    theguess = boxtext
                    boxtext = ''
                    donetext = True
                elif event.key == pg.K_BACKSPACE:
                    boxtext = boxtext[:-1]
                else:
                    boxtext += event.unicode
    mousex, mousey = pg.mouse.get_pos()
    if textrect.collidepoint(mousex, mousey):
        pg.mouse.set_visible(False)
        hovering = True
    else:
        pg.mouse.set_visible(True)
        hovering = False
    surfacetext = wordfont.render(boxtext, True, currentcolor)
    infosurfacetext = wordfont.render(guesstext, True, activecolor)
    goodsurfacetext = wordfont.render(goodtext, True, textcolor)
    badsurfacetext = wordfont.render(wrongtext, True, textcolor)
    width = max(200, surfacetext.get_width() + 10)
    textrect.w = width
    w.fill(white)
    pg.draw.line(w, (0, 0, 0), (50 , 525), (150, 525), 5)
    pg.draw.line(w, (0, 0, 0), (100, 525), (100, 100), 5)
    pg.draw.line(w, (0, 0, 0), (100, 100), (300, 100), 5)
    pg.draw.line(w, (0, 0, 0), (300, 100), (300, 125), 5)                        
    w.blit(infosurfacetext, (((w.get_width() / 2) - (infosurfacetext.get_width() / 2)), 20))
    w.blit(surfacetext, (textrect.x + 5, textrect.y + 5))
    w.blit(goodsurfacetext, (((w.get_width() / 2) - (goodsurfacetext.get_width() / 2)), 45))
    w.blit(badsurfacetext, (((w.get_width() / 2) - (badsurfacetext.get_width() / 2)), 70))
    x, y = ((surfacetext.get_width() + (textrect.x + 5))), (textrect.y + 5)
    wi, h = ((surfacetext.get_width() + (textrect.x + 5)), ((textrect.y + textrect.h) - 5))
    if active:
        timer += c.get_time()
        if timer >= 550:
            timer = 0
            typer = not typer
        if typer:
          pg.draw.line(w, black, (x, y), (wi, h), 2)
    if hovering:
        pg.draw.line(w, (0, 0, 0), (mousex, (mousey + 7)), (mousex, (mousey - 7)))
        pg.draw.line(w, (0, 0, 0), ((mousex - 2), (mousey + 7)), ((mousex + 2), (mousey + 7)))
        pg.draw.line(w, (0, 0, 0), ((mousex - 2), (mousey - 7)), ((mousex + 2), (mousey - 7)))
    pg.draw.rect(w, currentcolor, textrect, 2)
    if ske1:
      pg.draw.circle(w, (0, 0, 0), (300, 175), 50, 5)
    if ske2:
      pg.draw.line(w, (0, 0, 0), (300, 225), (300, 375), 5)
    if ske3:
      pg.draw.line(w, (0, 0, 0), (300, 315), (200, 300), 5)
    if ske4:
      pg.draw.line(w, (0, 0, 0), (300, 315), (400, 300), 5)
    if ske5:
      pg.draw.line(w, (0, 0, 0), (300, 375), (215, 400), 5)
    if ske6:
      pg.draw.line(w, (0, 0, 0), (300, 375), (385, 400), 5)
    pg.display.flip()
    c.tick(30)
    if donedone:
        pg.quit()
  timer = 0
  donetext = False
  if letters.count(theguess) == 0:
    strikes += 1
    wrongletters.append(theguess)
    if strikes == 1: 
      ske1 = True
    if strikes == 2:
      ske2 = True
    if strikes == 3:
      ske3 = True
    if strikes == 4:
      ske4 = True
    if strikes == 5:
      ske5 = True
    if strikes == 6:
      ske6 = True
  if ske1:
    pg.draw.circle(w, (0, 0, 0), (300, 175), 50, 5)
  if ske2:
    pg.draw.line(w, (0, 0, 0), (300, 225), (300, 375), 5)
  if ske3:
    pg.draw.line(w, (0, 0, 0), (300, 315), (200, 300), 5)
  if ske4:
    pg.draw.line(w, (0, 0, 0), (300, 315), (400, 300), 5)
  if ske5:
    pg.draw.line(w, (0, 0, 0), (300, 375), (215, 400), 5)
  if ske6:
    pg.draw.line(w, (0, 0, 0), (300, 375), (385, 400), 5)
    loser = True
  pg.display.flip()
  while letters.count(theguess) > 0:
    i = letters.index(theguess)
    letters[i] = 0
  for j in range(len(letters)):
    if letters[anothersone] == 0:
      i = seudoletters[anothersone]
      guessedletters[anothersone] = i
    anothersone += 1
  if letters.count(0) == len(letters):
    loser = False
    break
w.blit(infosurfacetext, (((w.get_width() / 2) - (infosurfacetext.get_width() / 2)), 20))
w.blit(goodsurfacetext, (((w.get_width() / 2) - (goodsurfacetext.get_width() / 2)), 45))
w.blit(badsurfacetext, (((w.get_width() / 2) - (badsurfacetext.get_width() / 2)), 70))
pg.draw.rect(w, currentcolor, textrect, 2)
if ske1 == True:
  pg.draw.circle(w, (0, 0, 0), (300, 175), 50, 5)
if ske2 == True:
  pg.draw.line(w, (0, 0, 0), (300, 225), (300, 375), 5)
if ske3 == True:
  pg.draw.line(w, (0, 0, 0), (300, 315), (200, 300), 5)
if ske4 == True:
  pg.draw.line(w, (0, 0, 0), (300, 315), (400, 300), 5)
if ske5 == True:
  pg.draw.line(w, (0, 0, 0), (300, 375), (215, 400), 5)
if ske6 == True:
  pg.draw.line(w, (0, 0, 0), (300, 375), (385, 400), 5)
w.fill(white)
pg.display.flip()
pg.mouse.set_visible(True)
if loser:
  losertext = "Loser Loser Chicken Dinner"
  wordwas = 'Your word was ' + str(seudoletters) + '. '
  surfaceloser = wordfont.render(losertext, True, red)
  surfacewordwas = wordfont.render(wordwas, True, red)
  w.blit(surfaceloser, (10, 300))
  w.blit(surfacewordwas, (10, 325))
  pg.display.flip()
else:
  winner = "Winner Winner Chicken Dinner!"
  wordwas = 'Your word was ' + str(seudoletters) + '. '
  surfacewinner = wordfont.render(winner, True, red)
  surfacewordwas = wordfont.render(wordwas, True, red)
  w.blit(surfacewinner, (10, 300))
  w.blit(surfacewordwas, (10, 325))
  pg.display.flip()
while endscene:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      pg.quit()
      endscene = False
