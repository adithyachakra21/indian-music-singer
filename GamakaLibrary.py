# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 14:45:39 2020

@author: mythkc
"""

# CONTENTS: This file contains functions that execute the 10 types of gamakas written in the SSP.
#           Beneath each file is a test of that gamakam working in Ragam Kalyani.


################################### REFERENCE: IMPORTANT SYMBOLS ##########################################

"""

Talam mid-cycle: |
Talam end-cycle: ∥

Mandara Stayi: d. is low pa
Tara Stayi: ˙S is high sa

Etra Jaaru: d/n
Irakka Jaaru: n\s    
Nokku: Swns is s n s with nokku on n
Orikai: pm⋎g⋎r is p m g r with orikai on g and r  
Odukkal: pd/×n is p d n with odukkal on n  
Ravai: p∧pm is p p m with ravai on second p  
Kandipu: p✓mG is p m g with kandipu on m  
Vali: s⌢N is s N with vali on N and small s  
Spuritham or Pratyaghatam: s∴s or s∵s
Kampitam: mp∼∼∼D is m p d with kampitam on d
   
"""
from FunWithScales import*

kalyani = [swara_dictionary["S1"], swara_dictionary["R2"], swara_dictionary["G3"],
           swara_dictionary["M2"], swara_dictionary["P"], swara_dictionary["D2"],
           swara_dictionary["N3"], swara_dictionary["S2"]]

######################################## SPURITHAM and PRATYAGHATAM #################################################

def spuritham (ragam, duration, note):
   
    lower_note = ragam [ragam.index(note)-1]
   
    output = np.concatenate(( hold_note(lower_note, 0.125/2),
                              hold_note(note, duration - (0.125/2))))
   
    return output


# testing spuritham of p p in kalyani, with spuritham on second pa
test = np.concatenate((hold_note (swara_dictionary["P"], 1), spuritham (kalyani, 2, swara_dictionary["P"])))
write('testspuritham.wav', sps, test)


######################################## KAMPITAM ######################################################


def kampita (duration, note):
   
    output = hold_note (note-7, 0.125/2)
   
    for i in range (0, int((2*duration/0.125)-1)):
       
        if i%2 == 0:
            output = np.concatenate ((output,
                                  jaaru(note-7, note+7,0.125/2,10)))
        else:
            output = np.concatenate ((output,
                                  jaaru(note+7, note-7,0.125/2,10)))
   
    return output

# testing kampita of p  
test2 = kampita (4, swara_dictionary["P"])
write('testkampita.wav', sps, test2)


######################################## ORIKAI ####################################################


def orikai (ragam, duration, note):
   
    higher_note = ragam [ragam.index(note)+1]
   
    output = np.concatenate(( hold_note(note, duration-0.125),
                              jaaru(note, higher_note, 0.125, 10)))
   
    return output

# testing orikai on ndpM-- with orikai on n d p
test3 = np.concatenate ((orikai (kalyani, 0.5, swara_dictionary["N3"]),
                        orikai (kalyani, 0.5, swara_dictionary["D2"]),
                        orikai (kalyani, 0.5, swara_dictionary["P"]),
                        hold_note(swara_dictionary["M2"], 1) ))
write('testorikai.wav', sps, test3)


######################################## NOKKU ####################################################


def nokku (ragam, duration, note):
    higher_note = ragam [ragam.index(note)+1]
   
    # a slow nokku with a jaaru going up, followed by a jaaru coming back down
    # sequence of events: hold note for 1/8 of remaining time, jaaru up (0.10s) and down (0.10s), hold note for 7/8 of remaining time
   
    if duration > 0.5:    
        output = hold_note(note, (duration - 0.2)/8)
        output = np.concatenate ((output, jaaru (note, higher_note, 0.10, 10),
                                  jaaru (higher_note, note, 0.10, 10)))
        output = np.concatenate ((output, hold_note(note, 7*(duration - 0.2)/8)))  
       
    # a medium nokku with a jaaru going up, followed by a jaaru coming back down
    # sequence of events: hold note for 1/4 of remaining time, jaaru up (0.10s) and down (0.10s), hold note for 3/4 of remaining time

    if duration == 0.5:    
        output = hold_note(note, (duration - 0.2)/4)
        output = np.concatenate ((output, jaaru (note, higher_note, 0.10, 10),
                                  jaaru (higher_note, note, 0.10, 10)))
        output = np.concatenate ((output, hold_note(note, 3*(duration - 0.2)/4)))    
   
    # a fast nokku with a jaaru coming straight down
    # sequence of events: jaaru down (half of duration), hold lower note (remaining half of duration)
   
    elif duration < 0.5:
        output = jaaru (higher_note, note, duration/2, 10)
        output = np.concatenate((output, hold_note(note, duration/2)))
       
    return output

# test SLOW nokku on kalyani srgmp with nokku on g
   
test4 = np.concatenate((hold_note (swara_dictionary["S1"], 1),
                        hold_note (swara_dictionary["R2"], 1),
                        nokku (kalyani, 1, swara_dictionary["G3"]),
                        hold_note (swara_dictionary["M2"], 1),
                        hold_note (swara_dictionary["P"], 2)                            
                             ))
write('testnokku_slow.wav', sps, test4)


# test MEDIUM nokku on kalyani srgmp with nokku on g

test5 = np.concatenate((hold_note (swara_dictionary["S1"], 0.5),
                        hold_note (swara_dictionary["R2"], 0.5),
                        nokku (kalyani, 0.5, swara_dictionary["G3"]),
                        hold_note (swara_dictionary["M2"], 0.5),
                        hold_note (swara_dictionary["P"], 0.5)                            
                             ))
write('testnokku_medium.wav', sps, test5)


# test FAST nokku on kalyani srgmp with nokku on g

test6 = np.concatenate((hold_note (swara_dictionary["S1"], 0.25),
                        hold_note (swara_dictionary["R2"], 0.25),
                        nokku (kalyani, 0.25, swara_dictionary["G3"]),
                        hold_note (swara_dictionary["M2"], 0.25),
                        hold_note (swara_dictionary["P"], 1)                            
                             ))
write('testnokku_fast.wav', sps, test6)
                                 

######################################## RAVAI and KANDIMPU ####################################################


def ravai (small_note, main_note, duration):
   
    # holding the small_note for 0.8(0.125s) because 0.125s was too long and 0.125/2 s was too short!
    output = np.concatenate(( hold_note(small_note, 0.8*0.125),
                              hold_note(main_note, duration - 0.8*0.125)))    
    return output


# testing ravai of N d P in kalyani, with ravai on d P:  d (small_note) and P (main_note)
test7 = np.concatenate((hold_note (swara_dictionary["N3"], 1),
                       ravai (swara_dictionary["D2"], swara_dictionary["P"], 1),
                       hold_note(swara_dictionary["P"], 1)))
write('testravai.wav', sps, test7)