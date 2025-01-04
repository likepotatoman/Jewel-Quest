#you can take all the code in this repo and put it into Pyxel Studio or simply go to this link www.pyxelstudio.net/m63hb4g5
import pyxel
pyxel.init(128,128, title="Nuit du code")
pyxel.load("4.pyxres")
blocs = []
blocs_cassables = []
for i in range(-772,828,8):
    for j in range(-772,828,8):
        nombre = pyxel.rndi(0,4)
        if nombre == 0 or nombre == 1 or nombre == 2:
            if [i,j] != [60,60]:
                blocs_cassables.append([i,j])
blocs.append(blocs_cassables)
diamands = []
for i in range(640):
    x_diamand = (pyxel.rndi(-100,100)*8 +4)
    y_diamand = (pyxel.rndi(-100,100)*8 +4)
    if [x_diamand,y_diamand] in blocs[0]:
        blocs[0].remove([x_diamand,y_diamand])
        
    if [x_diamand,y_diamand] in diamands:
        diamands.append([x_diamand+8, y_diamand])
    else:
        if [x_diamand,y_diamand] != [60,60]:
            diamands.append([x_diamand,y_diamand])
        else:
            diamands.append([x_diamand+8,y_diamand])
blocs.append(diamands)
murs = []
for i in range(-772,828,8):
    murs.append([i,-772])
    murs.append([i,828])
    murs.append([-772,i])
    murs.append([828,i])
blocs.append(murs)
personnage1 = 0
personnage2 = 16
ang = "sud"
animation_start_frame = -8
animation_end_frame = -8
action = "mouvement"
PA_x = 0
PA_y = 0
PA_u = 0
PA_v = 0
PA_w = 0
PA_h = 0
score = 0
shovel_use = 0
S_x = 0
S_y = 0
S_u = 0
S_v = 0
S_w = 0
S_h = 0
ecran_phase = 0
ecran_phase_timer = 0
part = 1
timer_debut_part_3 = 0
nombre_de_pas = 0
blocs_cassees = 0
diamands_total = 0
liste_mini_diamands = []
def mouvement():
    global blocs, personnage1, personnage2, fini, ang, animation_start_frame, action, animation_end_frame,PA_x,PA_y,PA_u,PA_v,PA_w,PA_h, score, shovel_use,S_x,S_y,S_u,S_v,S_w,S_h, ecran_phase, ecran_phase_timer, part, timer_debut_part_3, nombre_de_pas,blocs_cassees,diamands_total, liste_mini_diamands
    if animation_start_frame + 2 == pyxel.frame_count or animation_start_frame + 1 == pyxel.frame_count or animation_start_frame + 5 == pyxel.frame_count or animation_start_frame + 6 == pyxel.frame_count:
        pixel = 1
    else :
        pixel = 2
    if ang == "north":
        for j in range(len(blocs)):
            for i in range(len(blocs[j])):
                blocs[j][i][1] += pixel
        if [60,60] in blocs[1]:
            blocs[1].remove([60,60])
            if ecran_phase == 2:
                score += 3
                diamands_total += 3
            else:
                score += 1
                diamands_total += 1
    elif ang == "west":
        for j in range(len(blocs)):
            for i in range(len(blocs[j])):
                blocs[j][i][0] += pixel
        if [60,60] in blocs[1]:
            blocs[1].remove([60,60])
            if ecran_phase == 2:
                score += 3
                diamands_total += 3
            else:
                score += 1
                diamands_total += 1
    elif ang == "east":
        for j in range(len(blocs)):
            for i in range(len(blocs[j])):
                blocs[j][i][0] -= pixel
        if [60,60] in blocs[1]:
            blocs[1].remove([60,60])
            if ecran_phase == 2:
                score += 3
                diamands_total += 3
            else:
                score += 1
                diamands_total += 1
    elif ang == "south":
        for j in range(len(blocs)):
            for i in range(len(blocs[j])):
                blocs[j][i][1] -= pixel
        if [60,60] in blocs[1]:
            blocs[1].remove([60,60])
            if ecran_phase == 2:
                score += 3
                diamands_total += 3
            else:
                score += 1
                diamands_total += 1
def input_tracker():
    global blocs, personnage1, personnage2, fini, ang, animation_start_frame,action, animation_end_frame,PA_x,PA_y,PA_u,PA_v,PA_w,PA_h, score, shovel_use,S_x,S_y,S_u,S_v,S_w,S_h, ecran_phase, ecran_phase_timer, part, timer_debut_part_3, nombre_de_pas,blocs_cassees,diamands_total, liste_mini_diamands
    if pyxel.btn(pyxel.KEY_SPACE):
        action = "attaque"
        animation_start_frame = pyxel.frame_count
        animation_end_frame = animation_start_frame + 14
    elif pyxel.btn(pyxel.KEY_S):
        if shovel_use > 0:
            shovel_use -= 1
            action = "shovel"
            animation_start_frame = pyxel.frame_count
            animation_end_frame = animation_start_frame + 9
    elif pyxel.btnr(pyxel.KEY_R):
        if score > 2:
            score -= 3
            shovel_use += 5
    elif pyxel.btnr(pyxel.KEY_T):
        if score > 4:
            if ecran_phase != 1:
                ecran_phase = 1
                score -= 5
                ecran_phase_timer = 900
    elif pyxel.btnr(pyxel.KEY_H):
        if score > 4:
            if ecran_phase != 2:
                ecran_phase = 2
                score -= 5
            ecran_phase_timer = 900
    elif pyxel.btnr(pyxel.KEY_B):
        if score > 9:
            score -= 10
            action = "bomb"
            animation_start_frame = pyxel.frame_count
            animation_end_frame = animation_start_frame + 30
    elif pyxel.btn(pyxel.KEY_UP):
        personnage1 = 88
        personnage2 = 16
        ang ="north"
        if [60,52] not in blocs[0] and [60,52] not in blocs[2]:
            nombre_de_pas += 1
            action = "mouvement"
            animation_start_frame = pyxel.frame_count
            animation_end_frame = animation_start_frame + 6
    elif pyxel.btn(pyxel.KEY_LEFT):
        personnage1 = 0 
        personnage2 = 24
        ang = "west"
        if [52,60] not in blocs[0] and [52,60] not in blocs[2]:
            nombre_de_pas += 1
            action = "mouvement"
            animation_start_frame = pyxel.frame_count
            animation_end_frame = animation_start_frame + 6
    elif pyxel.btn(pyxel.KEY_RIGHT):
        personnage1 = 0
        personnage2 = 16
        ang = "east"
        if [68,60] not in blocs[0] and [68,60] not in blocs[2]:
            nombre_de_pas += 1
            action = "mouvement"
            animation_start_frame = pyxel.frame_count
            animation_end_frame = animation_start_frame + 6
    elif pyxel.btn(pyxel.KEY_DOWN):
        personnage1 = 0
        personnage2 = 16
        ang = "south"
        if [60,68] not in blocs[0] and [60,68] not in blocs[2]:
            nombre_de_pas += 1
            action = "mouvement"
            animation_start_frame = pyxel.frame_count
            animation_end_frame = animation_start_frame + 6
def bomb():
    global blocs, personnage1, personnage2, fini, ang, animation_start_frame, animation_end_frame, action,PA_x,PA_y,PA_u,PA_v,PA_w,PA_h, score, shovel_use,S_x,S_y,S_u,S_v,S_w,S_h, ecran_phase, ecran_phase_timer, part, timer_debut_part_3, nombre_de_pas,blocs_cassees,diamands_total, liste_mini_diamands
    if animation_start_frame + 1 == pyxel.frame_count:
        for i in range(36,84,8):
            for j in range(36,84,8):
                if [i,j] in blocs[0]:
                    blocs[0].remove([i,j])
                    blocs_cassees += 1
    if animation_start_frame + 11 == pyxel.frame_count:
        for i in range(20,92,8):
            for j in range(20,92,8):
                if [i,j] in blocs[0]:
                    blocs[0].remove([i,j])   
                    blocs_cassees += 1
    if animation_start_frame + 16 == pyxel.frame_count:
        for i in range(-4,124,8):
            for j in range(-4,124,8):
                if [i,j] in blocs[0]:
                    blocs[0].remove([i,j])
                    blocs_cassees += 1
def attaque():
    global blocs, personnage1, personnage2, fini, ang, animation_start_frame, animation_end_frame, action,PA_x,PA_y,PA_u,PA_v,PA_w,PA_h, score, shovel_use,S_x,S_y,S_u,S_v,S_w,S_h, ecran_phase, ecran_phase_timer, part, timer_debut_part_3, nombre_de_pas,blocs_cassees,diamands_total, liste_mini_diamands
    if ang == "east":
        if animation_start_frame + 4 == pyxel.frame_count:
            if [60,52] in blocs[0]:
                blocs[0].remove([60,52])
                blocs_cassees += 1
        elif animation_start_frame + 8 == pyxel.frame_count:
            if [68,52] in blocs[0]:
                blocs[0].remove([68,52])
                blocs_cassees += 1
        elif animation_start_frame + 10 == pyxel.frame_count:
            if [68,60] in blocs[0]:
                blocs[0].remove([68,60])          
                blocs_cassees += 1
        elif animation_start_frame + 12 == pyxel.frame_count:
            if [68,68] in blocs[0]:
                blocs[0].remove([68,68])                
                blocs_cassees += 1
        elif animation_start_frame + 14 == pyxel.frame_count:
            if [60,68] in blocs[0]: 
                blocs[0].remove([60,68])
                blocs_cassees += 1
    elif ang == "west":
        if animation_start_frame + 4 == pyxel.frame_count:
            if [60,68] in blocs[0]:
                blocs[0].remove([60,68])
                blocs_cassees += 1
        elif animation_start_frame + 8 == pyxel.frame_count:
            if [52,68] in blocs[0]:
                blocs[0].remove([52,68]) 
                blocs_cassees += 1
        elif animation_start_frame + 10 == pyxel.frame_count:
            if [52,60] in blocs[0]:
                blocs[0].remove([52,60])               
                blocs_cassees += 1
        elif animation_start_frame + 12 == pyxel.frame_count:
            if [52,52] in blocs[0]:
                blocs[0].remove([52,52])                
                blocs_cassees += 1
        elif animation_start_frame + 14 == pyxel.frame_count:
            if [60,52] in blocs[0]: 
                blocs[0].remove([60,52]) 
                blocs_cassees += 1
    elif ang == "north":
        if animation_start_frame + 4 == pyxel.frame_count:
            if [52,60] in blocs[0]:
                blocs[0].remove([52,60])
                blocs_cassees += 1
        elif animation_start_frame + 8 == pyxel.frame_count:
            if [52,52] in blocs[0]:
                blocs[0].remove([52,52]) 
                blocs_cassees += 1
        elif animation_start_frame + 10 == pyxel.frame_count:
            if [60,52] in blocs[0]:
                blocs[0].remove([60,52])               
                blocs_cassees += 1
        elif animation_start_frame + 12 == pyxel.frame_count:
            if [68,52] in blocs[0]:
                blocs[0].remove([68,52])                
                blocs_cassees += 1
        elif animation_start_frame + 14 == pyxel.frame_count:
            if [68,60] in blocs[0]: 
                blocs[0].remove([68,60]) 
                blocs_cassees += 1
    elif ang == "south":
        if animation_start_frame + 4 == pyxel.frame_count:
            if [68,60] in blocs[0]:
                blocs[0].remove([68,60])
                blocs_cassees += 1
        elif animation_start_frame + 8 == pyxel.frame_count:
            if [68,68] in blocs[0]:
                blocs[0].remove([68,68]) 
                blocs_cassees += 1
        elif animation_start_frame + 10 == pyxel.frame_count:
            if [60,68] in blocs[0]:
                blocs[0].remove([60,68])               
                blocs_cassees += 1
        elif animation_start_frame + 12 == pyxel.frame_count:
            if [52,68] in blocs[0]:
                blocs[0].remove([52,68])                
                blocs_cassees += 1
        elif animation_start_frame + 14 == pyxel.frame_count:
            if [52,60] in blocs[0]: 
                blocs[0].remove([52,60]) 
                blocs_cassees += 1
def shovel():
    global blocs, personnage1, personnage2, fini, ang, animation_start_frame, action, animation_end_frame,PA_x,PA_y,PA_u,PA_v,PA_w,PA_h, score, shovel_use,S_x,S_y,S_u,S_v,S_w,S_h, ecran_phase, ecran_phase_timer, part, timer_debut_part_3, nombre_de_pas,blocs_cassees,diamands_total, liste_mini_diamands
    if ang == "east":
        if animation_start_frame + 1 == pyxel.frame_count:
            if [68,60] in blocs[0]:
                blocs[0].remove([68,60])
                blocs_cassees += 1
        elif animation_start_frame + 2 == pyxel.frame_count:
            if [76,60] in blocs[0]:
                blocs[0].remove([76,60]) 
                blocs_cassees += 1
        elif animation_start_frame + 3 == pyxel.frame_count:
            if [84,60] in blocs[0]:
                blocs[0].remove([84,60])               
                blocs_cassees += 1
        elif animation_start_frame + 4 == pyxel.frame_count:
            if [92,60] in blocs[0]:
                blocs[0].remove([92,60])                
                blocs_cassees += 1
        elif animation_start_frame + 5 == pyxel.frame_count:
            if [100,60] in blocs[0]: 
                blocs[0].remove([100,60])
                blocs_cassees += 1
    elif ang == "west":
        if animation_start_frame + 1 == pyxel.frame_count:
            if [52,60] in blocs[0]:
                blocs[0].remove([52,60])
                blocs_cassees += 1
        elif animation_start_frame + 2 == pyxel.frame_count:
            if [44,60] in blocs[0]:
                blocs[0].remove([44,60]) 
                blocs_cassees += 1
        elif animation_start_frame + 3 == pyxel.frame_count:
            if [36,60] in blocs[0]:
                blocs[0].remove([36,60])               
                blocs_cassees += 1
        elif animation_start_frame + 4 == pyxel.frame_count:
            if [28,60] in blocs[0]:
                blocs[0].remove([28,60])                
                blocs_cassees += 1
        elif animation_start_frame + 5 == pyxel.frame_count:
            if [20,60] in blocs[0]: 
                blocs[0].remove([20,60]) 
                blocs_cassees += 1
    elif ang == "north":
        if animation_start_frame + 1 == pyxel.frame_count:
            if [60,52] in blocs[0]:
                blocs[0].remove([60,52])
                blocs_cassees += 1
        elif animation_start_frame + 2 == pyxel.frame_count:
            if [60,44] in blocs[0]:
                blocs[0].remove([60,44]) 
                blocs_cassees += 1
        elif animation_start_frame + 3 == pyxel.frame_count:
            if [60,36] in blocs[0]:
                blocs[0].remove([60,36])               
                blocs_cassees += 1
        elif animation_start_frame + 4 == pyxel.frame_count:
            if [60,28] in blocs[0]:
                blocs[0].remove([60,28])                
                blocs_cassees += 1
        elif animation_start_frame + 5 == pyxel.frame_count:
            if [60,20] in blocs[0]: 
                blocs[0].remove([60,20]) 
                blocs_cassees += 1
    elif ang == "south":
        if animation_start_frame + 1 == pyxel.frame_count:
            if [60,68] in blocs[0]:
                blocs[0].remove([60,68])
                blocs_cassees += 1
        elif animation_start_frame + 2 == pyxel.frame_count:
            if [60,76] in blocs[0]:
                blocs[0].remove([60,76]) 
                blocs_cassees += 1
        elif animation_start_frame + 3 == pyxel.frame_count:
            if [60,84] in blocs[0]:
                blocs[0].remove([60,84])               
                blocs_cassees += 1
        elif animation_start_frame + 4 == pyxel.frame_count:
            if [60,92] in blocs[0]:
                blocs[0].remove([60,92])                
                blocs_cassees += 1
        elif animation_start_frame + 5 == pyxel.frame_count:
            if [60,100] in blocs[0]: 
                blocs[0].remove([60,100])     
                blocs_cassees += 1
def animation_state_mouvement():
    global blocs, personnage1, personnage2, fini, ang, animation_start_frame, action, animation_end_frame,PA_x,PA_y,PA_u,PA_v,PA_w,PA_h, score, shovel_use,S_x,S_y,S_u,s_w,S_w,S_h, ecran_phase, ecran_phase_timer, part, timer_debut_part_3, nombre_de_pas,blocs_cassees,diamands_total, liste_mini_diamands
    if ang == "east":
        if animation_start_frame + 2 == pyxel.frame_count or animation_start_frame + 4 == pyxel.frame_count:
            personnage1 = 32
            personnage2 = 16
        elif animation_start_frame + 3 == pyxel.frame_count:
            personnage1 = 24
            dierction2 = 16
        elif animation_start_frame + 1 == pyxel.frame_count:
            personnage1 = 8
            personnage2 = 16
        elif animation_start_frame + 6 == pyxel.frame_count:
            personnage1 = 40
            personnage2 = 16
        elif animation_start_frame + 5 == pyxel.frame_count:
            personnage1 = 48
            personnage2 = 16
    elif ang == "west":
        if animation_start_frame + 2 == pyxel.frame_count or animation_start_frame + 4 == pyxel.frame_count:
            personnage1 = 32
            personnage2 = 24
        elif animation_start_frame + 3 == pyxel.frame_count:
            personnage1 = 24
            dierction2 = 24
        elif animation_start_frame + 1 == pyxel.frame_count:
            personnage1 = 8
            personnage2 = 24
        elif animation_start_frame + 6 == pyxel.frame_count:
            personnage1 = 0
            personnage2 = 24
        elif animation_start_frame + 5 == pyxel.frame_count:
            personnage1 = 48
            personnage2 = 24
    elif ang == "north":
        if animation_start_frame + 6 == pyxel.frame_count :
            personnage1 = 88
            personnage2 = 16
        elif animation_start_frame + 2 == pyxel.frame_count:
            personnage1 = 80
            personnage2 = 24                
        elif animation_start_frame + 4 == pyxel.frame_count:
            personnage1 = 80
            personnage2 = 24
        elif animation_start_frame + 3 == pyxel.frame_count:
            personnage1 = 80
            personnage2 = 16
        elif animation_start_frame + 1 == pyxel.frame_count:
            personnage1 = 80
            personnage2 = 16
        elif animation_start_frame + 5 == pyxel.frame_count:
            personnage1 = 80
            personnage2 = 16
    elif ang == "south":
        if animation_start_frame + 2 == pyxel.frame_count or animation_start_frame + 4 == pyxel.frame_count:
            personnage1 = 56
            personnage2 = 16
        elif animation_start_frame + 3 == pyxel.frame_count or animation_start_frame + 1 == pyxel.frame_count or animation_start_frame + 5 == pyxel.frame_count:
            personnage1 = 56
            personnage2 = 24
        elif animation_start_frame + 6 == pyxel.frame_count:
            personnage1 = 40
            personnage2 = 16
def animation_state_attaque():
    global blocs, personnage1, personnage2, fini, ang, animation_start_frame, action, animation_end_frame,PA_x,PA_y,PA_u,PA_v,PA_w,PA_h, score, shovel_use,S_x,S_y,S_u,S_v,S_w,S_h, ecran_phase, ecran_phase_timer, part, timer_debut_part_3, nombre_de_pas,blocs_cassees,diamands_total, liste_mini_diamands
    if ang == "east":
        if animation_start_frame + 2 == pyxel.frame_count:
            PA_w = 8
            PA_h = 8
            PA_x = 60
            PA_y = 52
            if [60,52] in blocs[0]:
                PA_u = 96
                PA_v = 40
            else:
                PA_u = 88
                PA_v = 40  
        elif animation_start_frame + 4 == pyxel.frame_count:
            PA_w = 16
            PA_h = 8
            PA_x = 60
            PA_y = 52
            if [68,52] in blocs[0]:
                PA_u = 88
                PA_v = 64
            else:
                PA_u = 88
                PA_v = 56
        elif animation_start_frame + 6 == pyxel.frame_count:
            PA_w = 8
            PA_h = 8
            PA_x = 68
            PA_y = 52
            if [68,52] in blocs[0]:
                PA_u = 96
                PA_v = 48
            else:
                PA_u = 88
                PA_v = 48
        elif animation_start_frame + 8 == pyxel.frame_count:
            PA_w = 8
            PA_h = 8
            PA_x = 68
            PA_y = 60
            if [68,60] in blocs[0]:
                PA_u = 128
                PA_v = 64
            else:
                PA_u = 128
                PA_v = 48
        elif animation_start_frame + 10 == pyxel.frame_count:
            PA_w = 8
            PA_h = 8
            PA_x = 68
            PA_y = 68
            if [68,68] in blocs[0]:
                PA_u = 104
                PA_v = 58
            else:
                PA_u = 112
                PA_v = 48
        elif animation_start_frame + 12 == pyxel.frame_count:
            PA_w 
            PA_h = 8
            PA_x = 60
            PA_y = 68
            if [60,68] in blocs[0]:
                PA_u = 104
                PA_v = 64
            else:
                PA_u = 104
                PA_v = 56
        elif animation_start_frame + 14 == pyxel.frame_count:
            PA_w = 8
            PA_h = 8
            PA_x = 60
            PA_y = 68
            if [60,68] in blocs[0]:
                PA_u = 104
                PA_v = 40
            else:
                PA_u = 112
                PA_v = 40
    elif ang == "west":
        if animation_start_frame + 2 == pyxel.frame_count:
            PA_w = 8
            PA_h = 8
            PA_x = 60
            PA_y = 68
            if [60,68] in blocs[0]:
                PA_u = 104
                PA_v = 48
            else:
                PA_u = 112
                PA_v = 48
        elif animation_start_frame + 4 == pyxel.frame_count:
            PA_w = 16
            PA_h = 8
            PA_x = 52
            PA_y = 68
            if [52,68] in blocs[0]:
                PA_u = 104
                PA_v = 64
            else:
                PA_u = 104
                PA_v = 56
        elif animation_start_frame + 6 == pyxel.frame_count:
            PA_w = 8
            PA_h = 8
            PA_x = 52
            PA_y = 68
            if [52,68] in blocs[0]:
                PA_u = 104
                PA_v = 40
            else:
                PA_u = 112
                PA_v = 40
        elif animation_start_frame + 8 == pyxel.frame_count:
            PA_w = 8
            PA_h = 8
            PA_x = 52
            PA_y = 60
            if [52,60] in blocs[0]:
                PA_u = 128
                PA_v = 56
            else:
                PA_u = 128
                PA_v = 40
        elif animation_start_frame + 10 == pyxel.frame_count:
            PA_w = 8
            PA_h = 8
            PA_x = 52
            PA_y = 52
            if [52,52] in blocs[0]:
                PA_u = 96
                PA_v = 40
            else:
                PA_u = 88
                PA_v = 40
        elif animation_start_frame + 12 == pyxel.frame_count:
            PA_w = 16
            PA_h = 8
            PA_x = 52
            PA_y = 52
            if [60,52] in blocs[0]:
                PA_u = 88
                PA_v = 64
            else:
                PA_u = 88
                PA_v = 56
        elif animation_start_frame + 14 == pyxel.frame_count:
            PA_w = 8
            PA_h = 8
            PA_x = 60
            PA_y = 52
            if [60,52] in blocs[0]:
                PA_u = 96
                PA_v = 48
            else:
                PA_u = 88
                PA_v = 48          
    if ang == "south":
        if animation_start_frame + 2 == pyxel.frame_count:
            PA_w = 8
            PA_h = 8
            PA_x = 68
            PA_y = 60
            if [68,60] in blocs[0]:
                PA_u = 96
                PA_v = 48
            else:
                PA_u = 88
                PA_v = 48
        elif animation_start_frame + 4 == pyxel.frame_count:
            PA_w = 8
            PA_h = 16
            PA_x = 68
            PA_y = 60
            if [68,68] in blocs[0]:
                PA_u = 96
                PA_v = 72
            else:
                PA_u = 88
                PA_v = 72
        elif animation_start_frame + 6 == pyxel.frame_count:
            PA_w = 8
            PA_h = 8
            PA_x = 68
            PA_y = 68
            if [68,68] in blocs[0]:
                PA_u = 104
                PA_v = 48
            else:
                PA_u = 112
                PA_v = 48
        elif animation_start_frame + 8 == pyxel.frame_count:
            PA_w = 8
            PA_h = 8
            PA_x = 60
            PA_y = 68
            if [60,68] in blocs[0]:
                PA_u = 128
                PA_v = 64
            else:
                PA_u = 128
                PA_v = 48
        elif animation_start_frame + 10 == pyxel.frame_count:
            PA_w = 8
            PA_h = 8
            PA_x = 52
            PA_y = 68
            if [52,68] in blocs[0]:
                PA_u = 104
                PA_v = 40
            else:
                PA_u = 112
                PA_v = 40
        elif animation_start_frame + 12 == pyxel.frame_count:
            PA_w = 8
            PA_h = 16
            PA_x = 52
            PA_y = 60
            if [52,60] in blocs[0]:
                PA_u = 112
                PA_v = 72
            else:
                PA_u = 104 
                PA_v = 72
        elif animation_start_frame + 14 == pyxel.frame_count:
            PA_w = 8
            PA_h = 8
            PA_x = 52
            PA_y = 60
            if [52,60] in blocs[0]:
                PA_u = 96
                PA_v = 40
            else:
                PA_u = 88
                PA_v = 40  
    if ang == "north":
        if animation_start_frame + 2 == pyxel.frame_count:
            PA_w = 8
            PA_h = 8
            PA_x = 52
            PA_y = 60
            if [52,60] in blocs[0]:
                PA_u = 104
                PA_v = 40
            else:
                PA_u = 112
                PA_v = 40
        elif animation_start_frame + 4 == pyxel.frame_count:
            PA_w = 8
            PA_h = 16
            PA_x = 52
            PA_y = 52
            if [52,52] in blocs[0]:
                PA_u = 112
                PA_v = 72
            else:
                PA_u = 104
                PA_v = 72
        elif animation_start_frame + 6 == pyxel.frame_count:
            PA_w = 8
            PA_h = 8
            PA_x = 52
            PA_y = 52
            if [52,52] in blocs[0]:
                PA_u = 96
                PA_v = 40
            else:
                PA_u = 88
                PA_v = 40
        elif animation_start_frame + 8 == pyxel.frame_count:
            PA_w = 8
            PA_h = 8
            PA_x = 60
            PA_y = 52
            if [60,52] in blocs[0]:
                PA_u = 120
                PA_v = 56
            else:
                PA_u = 120
                PA_v = 40
        elif animation_start_frame + 10 == pyxel.frame_count:
            PA_w = 8
            PA_h = 8
            PA_x = 68
            PA_y = 52
            if [68,52] in blocs[0]:
                PA_u = 96
                PA_v = 48
            else:
                PA_u = 88
                PA_v = 48
        elif animation_start_frame + 12 == pyxel.frame_count:
            PA_w = 8
            PA_h = 16
            PA_x = 68
            PA_y = 52
            if [68,60] in blocs[0]:
                PA_u = 96
                PA_v = 72
            else:
                PA_u = 88
                PA_v = 72
        elif animation_start_frame + 14 == pyxel.frame_count:
            PA_w = 8
            PA_h = 8
            PA_x = 68
            PA_y = 60
            if [68,50] in blocs[0]:
                PA_u = 104
                PA_v = 48
            else:
                PA_u = 112
                PA_v = 48 
def animation_state_shovel(): 
    global blocs, personnage1, personnage2, fini, ang, animation_start_frame, action, animation_end_frame,PA_x,PA_y,PA_u,PA_v,PA_w,PA_h, score, shovel_use,S_x,S_y,S_u,S_v,S_w,S_h, ecran_phase, ecran_phase_timer, part, timer_debut_part_3, nombre_de_pas,blocs_cassees,diamands_total, liste_mini_diamands
    if ang == "north":
        if animation_start_frame + 1 == pyxel.frame_count or animation_start_frame + 9 == pyxel.frame_count:
            S_w = 8
            S_h = 8
            S_x = 60
            S_y = 52
            S_u = 128
            S_v = 96
        elif animation_start_frame + 2 == pyxel.frame_count or animation_start_frame + 8 == pyxel.frame_count:
            S_w = 8
            S_h = 16
            S_x = 60
            S_y = 44
            S_u = 128
            S_v = 96
        elif animation_start_frame + 3 == pyxel.frame_count or animation_start_frame + 7 == pyxel.frame_count:
            S_w = 8
            S_h = 24
            S_x = 60
            S_y = 36
            S_u = 128
            S_v = 96
        elif animation_start_frame + 4 == pyxel.frame_count or animation_start_frame + 6 == pyxel.frame_count:
            S_w = 8
            S_h = 32
            S_x = 60
            S_y = 28
            S_u = 128
            S_v = 96
        elif animation_start_frame + 5 == pyxel.frame_count:
            S_w = 8
            S_h = 40
            S_x = 60
            S_y = 20
            S_u = 128
            S_v = 96
    elif ang == "south":
        if animation_start_frame + 1 == pyxel.frame_count or animation_start_frame + 9 == pyxel.frame_count:
            S_w = 8
            S_h = 8
            S_x = 60
            S_y = 68
            S_u = 136
            S_v = 128
        elif animation_start_frame + 2 == pyxel.frame_count or animation_start_frame + 8 == pyxel.frame_count:
            S_w = 8
            S_h = 16
            S_x = 60
            S_y = 68
            S_u = 136
            S_v = 120
        elif animation_start_frame + 3 == pyxel.frame_count or animation_start_frame + 7 == pyxel.frame_count:
            S_w = 8
            S_h = 24
            S_x = 60
            S_y = 68
            S_u = 136
            S_v = 112
        elif animation_start_frame + 4 == pyxel.frame_count or animation_start_frame + 6 == pyxel.frame_count:
            S_w = 8
            S_h = 32
            S_x = 60
            S_y = 68
            S_u = 136
            S_v = 104
        elif animation_start_frame + 5 == pyxel.frame_count:
            S_w = 8
            S_h = 40
            S_x = 60
            S_y = 68
            S_u = 136
            S_v = 96
    elif ang == "east":
        if animation_start_frame + 1 == pyxel.frame_count or animation_start_frame + 9 == pyxel.frame_count:
            S_w = 8
            S_h = 8
            S_x = 68
            S_y = 60
            S_u = 120
            S_v = 96
        elif animation_start_frame + 2 == pyxel.frame_count or animation_start_frame + 8 == pyxel.frame_count:
            S_w = 16
            S_h = 8
            S_x = 68
            S_y = 60
            S_u = 112
            S_v = 96
        elif animation_start_frame + 3 == pyxel.frame_count or animation_start_frame + 7 == pyxel.frame_count:
            S_w = 24
            S_h = 8
            S_x = 68
            S_y = 60
            S_u = 104
            S_v = 96
        elif animation_start_frame + 4 == pyxel.frame_count or animation_start_frame + 6 == pyxel.frame_count:
            S_w = 32
            S_h = 8
            S_x = 68
            S_y = 60
            S_u = 96
            S_v = 96
        elif animation_start_frame + 5 == pyxel.frame_count:
            S_w = 40
            S_h = 8
            S_x = 68
            S_y = 60
            S_u = 88
            S_v = 96
    elif ang == "west":
        if animation_start_frame + 1 == pyxel.frame_count or animation_start_frame + 9 == pyxel.frame_count:
            S_w = 8
            S_h = 8
            S_x = 52
            S_y = 60
            S_u = 88
            S_v = 104
        elif animation_start_frame + 2 == pyxel.frame_count or animation_start_frame + 8 == pyxel.frame_count:
            S_w = 16
            S_h = 8
            S_x = 44
            S_y = 60
            S_u = 88
            S_v = 104
        elif animation_start_frame + 3 == pyxel.frame_count or animation_start_frame + 7 == pyxel.frame_count:
            S_w = 24
            S_h = 8
            S_x = 36
            S_y = 60
            S_u = 88
            S_v = 104
        elif animation_start_frame + 4 == pyxel.frame_count or animation_start_frame + 6 == pyxel.frame_count:
            S_w = 32
            S_h = 8
            S_x = 28
            S_y = 60
            S_u = 88
            S_v = 104
        elif animation_start_frame + 5 == pyxel.frame_count:
            S_w = 40
            S_h = 8
            S_x = 20
            S_y = 60
            S_u = 88
            S_v = 104
def number_to_location(number_str):
    global blocs, personnage1, personnage2, fini, ang, animation_start_frame, action, animation_end_frame,PA_x,PA_y,PA_u,PA_v,PA_w,PA_h, score, shovel_use,S_x,S_y,S_u,S_v,S_w,S_h, ecran_phase, ecran_phase_timer, part, timer_debut_part_3, nombre_de_pas,blocs_cassees,diamands_total, liste_mini_diamands
    if number_str == "0":
        return [176,8]
    elif number_str == "1":
        return [200,8]
    elif number_str == "2":
        return [224,8]
    elif number_str == "3":
        return [200,40]
    elif number_str == "4":
        return [224,40]
    elif number_str == "5":
        return [224,72]
    elif number_str == "6":
        return [224,104]
    elif number_str == "7":
        return [216,136]
    elif number_str == "8":
        return [208,168]
    elif number_str == "9":
        return [232,168]
def update():
    global blocs, personnage1, personnage2, fini, ang, animation_start_frame, action, animation_end_frame,PA_x,PA_y,PA_u,PA_v,PA_w,PA_h, score, shovel_use,S_x,S_y,S_u,S_v,S_w,S_h, ecran_phase, ecran_phase_timer, part, timer_debut_part_3, nombre_de_pas,blocs_cassees,diamands_total, liste_mini_diamands
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
    if part == 1:
        if pyxel.btnr(pyxel.KEY_SPACE):
            part += 1
    elif part == 2:
        if pyxel.btnr(pyxel.KEY_SPACE):
            part += 1
    elif part == 3:
        timer_debut_part_3 += 1
        if timer_debut_part_3 >= 3600:
            part += 1
        ecran_phase_timer -= 1
        if ecran_phase_timer < 0:
            ecran_phase = 0
        if animation_end_frame < pyxel.frame_count:
            input_tracker()
        else:
            if action == "mouvement":
                animation_state_mouvement()
                mouvement()
            elif action == "attaque":
                animation_state_attaque()
                attaque()
            elif action == "shovel":
                animation_state_shovel()
                shovel()
            elif action == "bomb":
                bomb()
    elif part == 4:
        if pyxel.frame_count % 12 ==0:
            liste_mini_diamands = []
            for i in range(0,128,4):
                for j in range(32,96,4):
                    if pyxel.rndi(1,20) == 20:
                        liste_mini_diamands.append([i,j])
def draw():
    global blocs, personnage1, personnage2, fini, ang, animation_start_frame, action, animation_end_frame,PA_x,PA_y,PA_u,PA_v,PA_w,PA_h, score, shovel_use,S_x,S_y,S_u,S_v,S_w,S_h, ecran_phase, ecran_phase_timer, part, timer_debut_part_3, nombre_de_pas,blocs_cassees,diamands_total, liste_mini_diamands
    if part == 1:
        pyxel.cls(0)
        pyxel.bltm(0,0,0,128,128,128,128)
        pyxel.bltm(0,0,0,0,128,128,128,5)
    elif part == 2:
        pyxel.cls(0)
        pyxel.bltm(0,0,0,128,128,128,128)
        pyxel.bltm(0,0,0,384,128,128,128,5)
    elif part == 3:
        pyxel.cls(0)
        pyxel.bltm(0,0,0,0,0,128,128)
        pyxel.blt(60,60,0,personnage1,personnage2,8,8,5)
        for i in range(len(blocs[0])):
            pyxel.blt(blocs[0][i][0], blocs[0][i][1],0,40,168,8,8)
        for i in range(len(blocs[1])):
            pyxel.blt(blocs[1][i][0], blocs[1][i][1],0, 56, 192,8,8,5)
        for i in range(len(blocs[2])):
            pyxel.blt(blocs[2][i][0], blocs[2][i][1],0, 56, 184,8,8)
        if action == "attaque" and pyxel.frame_count <= animation_end_frame and pyxel.frame_count > animation_start_frame + 2:
            pyxel.blt(PA_x,PA_y,0,PA_u,PA_v,PA_w,PA_h)
        elif action == "shovel" and pyxel.frame_count <= animation_end_frame and pyxel.frame_count > animation_start_frame+1:
            pyxel.blt(S_x,S_y,0,S_u,S_v,S_w,S_h)
        if ecran_phase == 0:
            pyxel.bltm(0,0,0,128,0,128,128,5)
        elif ecran_phase == 1:
            pyxel.bltm(0,0,0,256,0,128,128,5)
        elif ecran_phase == 2:
            pyxel.bltm(0,0,0,384,0,128,128,5)
        pyxel.bltm(0,0,0,256,128,128,128,5)
        pyxel.text(18,4, str(round(120-timer_debut_part_3/30)),7)
        if ecran_phase_timer > 0:
            if ecran_phase == 1:
                if round(ecran_phase_timer//30) >= 10:
                    pyxel.bltm(32,112,0,128,128,16,16)
                    pyxel.text(36,118,str(round(ecran_phase_timer//30)),7)
                else :
                    pyxel.bltm(32,112,0,128,128,16,16)
                    pyxel.text(38,118,str(round(ecran_phase_timer//30)),7)  
            if ecran_phase == 2:
                if round(ecran_phase_timer//30) >= 10:
                    pyxel.bltm(80,112,0,128,128,16,16)
                    pyxel.text(84,118,str(round(ecran_phase_timer//30)),7)  
                else :
                    pyxel.bltm(80,112,0,128,128,16,16)
                    pyxel.text(86,118,str(round(ecran_phase_timer//30)),7)  
        if shovel_use > 0:
            pyxel.text(10,122,str(shovel_use),8)
        if len(str(score)) < 10:
            pyxel.text(102,4,str(score),7)
        elif score < 100:
            pyxel.text(94,4,str(score),7)
        else:
            pyxel.text(86,4,str(score),7)
        if action == "bomb":
            if animation_start_frame + 1 < pyxel.frame_count < animation_start_frame + 6 or animation_start_frame + 11 < pyxel.frame_count < animation_start_frame + 16 or animation_start_frame + 21 < pyxel.frame_count < animation_start_frame + 26:
                pyxel.bltm(0,0,0,0,256,128,128)
    elif part == 4:
        pyxel.cls(0)
        pyxel.bltm(0,0,0,128,128,128,128)
        for i in range(len(liste_mini_diamands)):
            pyxel.blt(liste_mini_diamands[i][0],liste_mini_diamands[i][1],0,64,192,4,4)
        if len(str(score)) == 1:
            holder = number_to_location(str(score))
            pyxel.bltm(0,0,0,128,256,128,128,5)
            pyxel.blt(52,40,0,holder[0],holder[1],24,32,5)
        elif len(str(score)) == 2:
            pyxel.bltm(0,0,0,256,256,128,128,5)            
            holder = number_to_location(str(score)[0])
            pyxel.blt(32,40,0,holder[0],holder[1],24,32,5)
            holder = number_to_location(str(score)[1])
            pyxel.blt(72,40,0,holder[0],holder[1],24,32,5)
        elif len(str(score)) == 3:
            pyxel.bltm(0,0,0,384,256,128,128,5)            
            holder = number_to_location(str(score)[0])
            pyxel.blt(36,40,0,holder[0],holder[1],24,32,5)
            holder = number_to_location(str(score)[1])
            pyxel.blt(60,40,0,holder[0],holder[1],24,32,5)
            holder = number_to_location(str(score)[2])
            pyxel.blt(84,40,0,holder[0],holder[1],24,32,5)
        pyxel.text(20,116,str(blocs_cassees),7)
        pyxel.text(100,116,str(diamands_total),7)
pyxel.run(update, draw)
