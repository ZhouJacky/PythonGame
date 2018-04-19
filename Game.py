from gamelib import*
game = Game(800,600,"Wall Defense")

p = 470 #y value for fireball

#Graphics
bk = Image("bk.jpg",game)
bk.resizeTo(1269,713)
             
gbk = Image("Forest.jpg",game)
gbk.resizeTo(800,600)

layer1 = Image("Hills layer 01.png",game)
layer1.resizeTo(800,600)

layer2 = Image("Hills layer 02.png",game)
layer2.resizeTo(800,600)

layer3 = Image("Hills layer 03.png",game)
layer3.resizeTo(800,600)

layer4 = Image("Hills layer 04.png",game)
layer4.resizeTo(800,600)

layer5 = Image("Hills layer 05.png",game)
layer5.resizeTo(800,600)

layer6 = Image("Hills layer 06.png",game)
layer6.resizeTo(800,600)

title = Image("Logo.png",game)
title.y -= 200

play = Image("Play.png",game)
play.y = 450

hero = Animation("knight1.png",8,game,336/8,42,4)
hero.resizeBy(300)
hero.moveTo(100,510)
hero.health = 150

left = Animation("left.png",8,game,336/8,42,4)
left.resizeBy(300)
left.visible=False

attack = Animation("attack1.png",10,game,800/10,80)
attack.resizeBy(300)
attack.visible=False

attack2 = Animation("attack2.png",10,game,800/10,80)
attack2.resizeBy(300)
attack2.visible=False

block = Image("block.png",game)
block.resizeBy(300)
block.visible=False

block2 = Image("block2.png",game)
block2.resizeBy(300)
block2.visible=False

boss = Image("boss.png",game)
boss.resizeBy(190)

#Monsters
w = 512 #y value for the skeletons

skele1 = Animation("sidle1.png",11,game,264/11,32,4) #1
skele1.resizeBy(375)
skele1.moveTo(300,w)

skele2 = Animation("sattack1.png",18,game,774/18,37,4)
skele2.resizeBy(375)
skele2.moveTo(skele1.x - 15,skele1.y - 10)
skele2.visible = False

skele3 = Animation("sidle1.png",11,game,264/11,32,4) #2
skele3.resizeBy(375)
skele3.moveTo(500,w)

skele4 = Animation("sattack1.png",18,game,774/18,37,4)
skele4.resizeBy(375)
skele4.moveTo(skele3.x - 15,skele3.y - 10)
skele4.visible = False

skele5 = Animation("sidle1.png",11,game,264/11,32,4) #3
skele5.resizeBy(375)
skele5.moveTo(700,w)

skele6 = Animation("sattack1.png",18,game,774/18,37,4)
skele6.resizeBy(375)
skele6.moveTo(skele5.x - 15,skele5.y - 10)
skele6.visible = False

#Fireball Setup
fireball = Animation("fireball2.png",8,game,512/8,63)
fireball.resizeBy(100)
fireball.moveTo(800/2,p)

#Fireball 2 Setup
fireball2 = Animation("fireball2.png",8,game,512/8,63)
fireball2.resizeBy(100)
fireball2.moveTo(695,p)
fireball2.visible = False

gameover = Image("gameover.png",game)
gameover.resizeBy(100)

winner = Image("winner.png",game)
winner.resizeBy(100)

#Music
game.setMusic("bks.ogg") #https://www.youtube.com/watch?v=lUMSK6LmXCQ this helped
game.playMusic()

#Title Screen
while not game.over:
    game.processInput()

    bk.draw()
    title.draw()
    play.draw()

    if play.collidedWith(mouse) and mouse.LeftClick:
        game.over = True
 
    game.update(35)
game.over = False

#Beginning
Right = 0
Left = 0
while not game.over:
    game.processInput()

    layer1.draw()
    layer2.draw()
    layer3.draw()
    layer4.draw()
    layer5.draw()

    game.drawText("You are a wandering swordsman looking for adventure and excitement. You are currently walking",10,80)
    game.drawText("aimlessly through the grasslands. As you keep wallking you soon see the end of the desert",10,100)
    game.drawText("and start see a forest full of life. As you approach the forest you see a sign on the ground",10,120)
    game.drawText("and it has written on it DANGER with a skull and crossbones. You decide to keep",10,140)
    game.drawText("going to seek whatever the forest hides in the name of adventure and excitement.",10,160)

    #Character
    left.draw()
    left.stop()
    
    hero.draw()
    hero.stop()

    attack.draw()
    attack.stop()
    attack.moveTo(hero.x+60,hero.y-80)

    attack2.draw()
    attack2.stop()
    attack2.moveTo(left.x-60,left.y-80)

    block.draw()
    block.moveTo(hero.x,hero.y)
    
    block2.draw()
    block2.moveTo(left.x,left.y)

    #Character Movement
    if keys.Pressed[K_RIGHT]:
        hero.nextFrame()
        hero.x +=2
        left.visible = False
        hero.visible = True
        attack.visible=False
        attack2.visible=False
        block.visible=False
        block2.visible=False
        left.moveTo(hero.x,hero.y)
        Right += 1
        Left = 0
        
    if keys.Pressed[K_LEFT]:
        left.prevFrame()
        left.x -=2
        hero.visible = False
        left.visible = True
        attack.visible=False
        attack2.visible=False
        block.visible=False
        block2.visible=False
        hero.moveTo(left.x,left.y)
        Left += 1
        Right = 0

    if keys.Pressed[K_d]:
        block.visible=False
        block2.visible=False
        if Right > 0:
            attack.nextFrame()
            hero.visible = False
            attack.visible = True
        if Left > 0:
            attack2.prevFrame()
            left.visible = False
            attack2.visible = True
            
    if keys.Pressed[K_s]:
        attack.visible=False
        attack2.visible=False
        if Right > 0:
            hero.visible = False
            block.visible = True
        if Left > 0:
            left.visible = False
            block2.visible = True

    if hero.isOffScreen():
        game.over = True

    layer6.draw()

    game.update(35)
game.over = False

#Level 1
Right = 0
Left = 0
hero.moveTo(100,515)
while not game.over:
    game.processInput()
    gbk.draw()

#Character 2
    left.draw()
    left.stop()
    
    hero.draw()
    hero.stop()

    attack.draw()
    attack.stop()
    attack.moveTo(hero.x+50,hero.y-80)

    attack2.draw()
    attack2.stop()
    attack2.moveTo(left.x-50,left.y-80)

    block.draw()
    block.moveTo(hero.x,hero.y)
    
    block2.draw()
    block2.moveTo(left.x,left.y)

#Character Movement 2
    if keys.Pressed[K_RIGHT]:
        hero.nextFrame()
        hero.x +=2  #moves to right
        left.visible = False
        hero.visible = True
        attack.visible=False
        attack2.visible=False
        block.visible=False
        block2.visible=False
        left.moveTo(hero.x,hero.y)
        Right += 1
        Left = 0

    if keys.Pressed[K_LEFT]:
        left.prevFrame()
        left.x -=2  #moves to left
        hero.visible = False
        left.visible = True
        attack.visible=False
        attack2.visible=False
        block.visible=False
        block2.visible=False
        hero.moveTo(left.x,left.y)
        Left += 1
        Right = 0

    if keys.Pressed[K_d]:
        block.visible=False
        block2.visible=False
        if Right > 0:
            attack.nextFrame()
            hero.visible = False
            attack.visible = True
        if Left > 0:
            attack2.prevFrame()
            left.visible = False
            attack2.visible = True
            
    if keys.Pressed[K_s]:
        attack.visible=False
        attack2.visible=False
        if Right > 0:
            hero.visible = False
            block.visible = True
        if Left > 0:
            left.visible = False
            block2.visible = True

#Monster Attack
    X1 = 200 #1
    
    X2 = 400 #2
    
    X3 = 600 #3
       
    skele1.draw() #1
    skele2.draw()
    skele2.stop()

    if hero.x > X1:
        skele2.visible = True
        skele2.prevFrame()
        skele1.visible = False
    if hero.x < X1:
        skele2.visible = False
        skele1.visible = True

    if skele2.collidedWith(hero) or skele2.collidedWith(left):
        hero.moveTo(hero.x-10,hero.y)
        hero.health -=5
        left.health -=5

    if skele2.collidedWith(block) or skele2.collidedWith(block2):
        hero.moveTo(hero.x-10,hero.y)
        hero.health -=2
        left.health -=2

    if attack.collidedWith(skele2) or attack2.collidedWith(skele2):
        skele1.health -=5

    if skele1.health <=0:
        skele2.visible = False
        skele1.visible = False
        skele2.moveTo(1400,713)
        skele1.moveTo(1400,713)

    skele3.draw() #2
    skele4.draw()
    skele4.stop()

    if hero.x > X2:
        skele4.visible = True
        skele4.prevFrame()
        skele3.visible = False
    if hero.x < X2:
        skele4.visible = False
        skele3.visible = True

    if skele4.collidedWith(hero) or skele4.collidedWith(left):
        hero.moveTo(hero.x-10,hero.y)
        hero.health -=5
        left.health -=5

    if skele4.collidedWith(block) or skele4.collidedWith(block2):
        hero.moveTo(hero.x-10,hero.y)
        hero.health -=2
        left.health -=2

    if attack.collidedWith(skele4) or attack2.collidedWith(skele4):
        skele3.health -=5
    
    if hero.health <=0:
        game.over = True

    if skele3.health <=0:
        skele4.visible = False
        skele3.visible = False
        skele4.moveTo(1400,713)
        skele3.moveTo(1400,713)

    skele5.draw() #3
    skele6.draw()
    skele6.stop()

    if hero.x > X3:
        skele6.visible = True
        skele6.prevFrame()
        skele5.visible = False
    if hero.x < X3:
        skele6.visible = False
        skele5.visible = True

    if skele6.collidedWith(hero) or skele6.collidedWith(left):
        hero.moveTo(hero.x-10,hero.y)
        hero.health -=5
        left.health -=5

    if skele6.collidedWith(block) or skele6.collidedWith(block2):
        hero.moveTo(hero.x-10,hero.y)
        hero.health -=2
        left.health -=2

    if attack.collidedWith(skele6) or attack2.collidedWith(skele6):
        skele5.health -=5
    
    if hero.health <=0:
        game.over = True

    if skele5.health <=0:
        skele6.visible = False
        skele5.visible = False
        skele6.moveTo(1400,713)
        skele5.moveTo(1400,713)

    if hero.isOffScreen("right"):
        game.over = True

    game.drawText("Health: " + str(skele1.health),skele1.x,skele1.y - 100)#1
    game.drawText("Health: " + str(skele3.health),skele3.x,skele3.y - 100)#2
    game.drawText("Health: " + str(skele5.health),skele5.x,skele5.y - 100)#3
    game.drawText("Health: " + str(hero.health),hero.x,hero.y + 70)
    
    game.update(35)   
game.over = False
        
#Level 2
boss.health = 250
hero.moveTo(100,515)
Left = 0
Right = 0
boss.moveTo(800/2,460)
while not game.over:
    game.processInput()
    game.drawText("Level 2",200,200)
    gbk.draw()
    boss.draw()

#Character 3
    left.draw()
    left.stop()
    
    hero.draw()
    hero.stop()

    attack.draw()
    attack.stop()
    attack.moveTo(hero.x+50,hero.y-80)

    attack2.draw()
    attack2.stop()
    attack2.moveTo(left.x-50,left.y-80)

    block.draw()
    block.moveTo(hero.x,hero.y)
    
    block2.draw()
    block2.moveTo(left.x,left.y)

#Character Movement 3
    if keys.Pressed[K_RIGHT]:
        hero.nextFrame()
        hero.x +=2
        left.visible = False
        hero.visible = True
        attack.visible=False
        attack2.visible=False
        block.visible=False
        block2.visible=False
        left.moveTo(hero.x,hero.y)
        Right += 1
        Left = 0

    if keys.Pressed[K_LEFT]:
        left.prevFrame()
        left.x -=2
        hero.visible = False
        left.visible = True
        attack.visible=False
        attack2.visible=False
        block.visible=False
        block2.visible=False
        hero.moveTo(left.x,left.y)
        Left += 1
        Right = 0

    if keys.Pressed[K_d]:
        block.visible=False
        block2.visible=False
        if Right > 0:
            attack.nextFrame()
            hero.visible = False
            attack.visible = True
        if Left > 0:
            attack2.prevFrame()
            left.visible = False
            attack2.visible = True
            
    if keys.Pressed[K_s]:
        attack.visible=False
        attack2.visible=False
        if Right > 0:
            hero.visible = False
            block.visible = True
        if Left > 0:
            left.visible = False
            block2.visible = True

    #Fireball
    fireballpassed = 0
    fireball.setSpeed(5,90)
    fireball.move()



    #Fireball
    if fireball.collidedWith(hero) or fireball.collidedWith(left) or fireball.collidedWith(attack) or fireball2.collidedWith(attack2):
        hero.health -= 2
        fireball.visible = False
        fireball.moveTo(800/2,p)
        fireball.visible = True
        fireballpassed += 1
            
    if fireball.collidedWith(block) or fireball.collidedWith(block2):
        hero.health -= 1
        fireball.visible = False
        fireball.moveTo(800/2,p)
        fireball.visible = True
        fireballpassed += 1
        
    #Fireball 2
    if fireball2.collidedWith(hero) or fireball2.collidedWith(left) or fireball2.collidedWith(attack) or fireball2.collidedWith(attack2):
        hero.health -= 2
        fireball2.visible = False
        fireball2.moveTo(695,p)
        fireball2.visible = True
        fireballpassed += 1
            
    if fireball2.collidedWith(block) or fireball2.collidedWith(block2):
        hero.health -= 1
        fireball2.visible = False
        fireball2.moveTo(695,p)
        fireball2.visible = True
        fireballpassed += 1
        
    if fireball.isOffScreen():
        fireballpassed += 1

    if fireballpassed >= 1:
        fireball.moveTo(800/2,p)
        fireballpassed = 0

    if fireballpassed >= 1:
        fireball2.moveTo(695,p)
        fireballpassed = 0

    if attack.collidedWith(boss) or attack2.collidedWith(boss):
        boss.health -= 10

    if boss.health <= 125:
        boss.moveTo(695,460)
        fireball.visible = False
        fireball2.visible = True
        fireball2.draw()
        fireball2.setSpeed(5,90)
        fireball2.move()

    if hero.health <= 0:
        game.clearBackground()
        gameover.draw()
        
    if boss.health <= 0:
        game.clearBackground()
        winner.draw()

    game.drawText("Health: " + str(boss.health),boss.x + 50,boss.y + 145)
    game.drawText("Health: " + str(hero.health),hero.x,hero.y + 70)
    
    game.update(75)
game.quit()    
