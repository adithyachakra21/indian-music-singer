# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 07:30:11 2020

@author: mythkc
"""


################################### REFERENCE: IMPORTANT SYMBOLS ##########################################

"""

Talam mid-cycle: |
Talam end-cycle: ∥

Mandara Stayi: d. is low pa
Tara Stayi: ˙S is high sa

Etra Jaaru: d/n
Irakka Jaaru: n\s    
Nokku: Swns is s n s with nokku on n
Orikai: pmg⋎r is p m g r with orikai on g and r  
Odukkal: pd/×n is p d n with odukkal on n  
Ravai: p∧pm is p p m with ravai on second p  
Kandipu: p✓mG is p m g with kandipu on m  
Vali: s⌢N is s N with vali on N and small s  
Spuritham or Pratyaghatam: s∴s or s∵s
Kampitam: mp∼∼∼D is m p d with kampitam on d
   
"""

from FunWithScales import*
from GamakaLibrary import*


def char_p (text, i, output, time, ragam):
    
    # by default, the note is madhyama sthayi, but if it passes through the tara sthayi or mandara stayi loops, the variable Madhyama_Sthayi is set to False
    madhyama_sthayi = True
    
    # mandara sthayi P, once the error condition is checked
    if i != (len(text)-1):
        if text[i+1] == ".":
            note = swara_dictionary["p"]
            output = np.concatenate ((output, hold_note(note, time)))
            madhyama_sthayi = False
    
    # tara sthayi P, once the error condition is checked
    if i != 0:
        if text[i-1] == "˙":
            note = swara_dictionary["pp"]
            output = np.concatenate ((output, hold_note(note, time)))
            madhyama_sthayi = False
            
    # madhyama sthayi P, if neither of the above two cases holds
    if madhyama_sthayi == True:
        note = swara_dictionary["P"]
        
        if i != 0:
            if i-3>=0:
                if str(text [i-3:i]) == "∼∼∼":
                    output = np.concatenate ((output, kampita (time, note)))
                
            
            if text [i-1] == "∵" or text [i-1] == "∴":
                output = np.concatenate ((output, spuritham (ragam, time, note)))         
                       
            elif text [i-1] == "w":
                output = np.concatenate ((output, nokku (ragam, time, note)))
                
            elif text [i-1] == "⋎":
                output = np.concatenate ((output, orikai (ragam, time, note)))
            
            elif text [i-1] == "✓":
                output = np.concatenate ((output, hold_note(note, 0.8*0.125)))
                            
            elif text [i-1] == "/" or text [i-1] == "\\": 
                output = output
                        
            else:
                output = np.concatenate ((output, hold_note(note, time)))
        
        else:
            output = np.concatenate ((output, hold_note(note, time)))
        
    return output


def char_d1 (text, i, output, time, ragam):
    
    # by default, the note is madhyama sthayi, but if it passes through the tara sthayi or mandara stayi loops, the variable Madhyama_Sthayi is set to False
    madhyama_sthayi = True
    
    # mandara sthayi D1, once the error condition is checked
    if i != (len(text)-1):
        if text[i+1] == ".":
            note = swara_dictionary["d1"]
             
            madhyama_sthayi = False
            
            if i != 0:
                if i-3>=0:
                    if str(text [i-3:i]) == "∼∼∼":
                        output = np.concatenate ((output, kampita (time, note)))
                        
                
                
                if text [i-1] == "∵" or text [i-1] == "∴":
                    output = np.concatenate ((output, spuritham (ragam, time, note)))         
                           
                elif text [i-1] == "w":
                    output = np.concatenate ((output, nokku (ragam, time, note)))
                    
                elif text [i-1] == "⋎":
                    output = np.concatenate ((output, orikai (ragam, time, note)))
                
                elif text [i-1] == "✓":
                    output = np.concatenate ((output, hold_note(note, 0.8*0.125)))
                                
                elif text [i-1] == "/" or text [i-1] == "\\": 
                    output = output
                            
                else:
                    output = np.concatenate ((output, hold_note(note, time)))
            
            else:
                output = np.concatenate ((output, hold_note(note, time)))
            
            
    # madhyama sthayi D1, if the above case doesn't hold
    if madhyama_sthayi == True:
        note = swara_dictionary["D1"]
        
        if i != 0:
            if i-3>=0:
                if str(text [i-3:i]) == "∼∼∼":
                    output = np.concatenate ((output, kampita (time, note)))
                    
            
            
            if text [i-1] == "∵" or text [i-1] == "∴":
                output = np.concatenate ((output, spuritham (ragam, time, note)))         
                       
            elif text [i-1] == "w":
                output = np.concatenate ((output, nokku (ragam, time, note)))
                
            elif text [i-1] == "⋎":
                output = np.concatenate ((output, orikai (ragam, time, note)))
            
            elif text [i-1] == "✓":
                output = np.concatenate ((output, hold_note(note, 0.8*0.125)))
                            
            elif text [i-1] == "/" or text [i-1] == "\\": 
                output = output
                        
            else:
                output = np.concatenate ((output, hold_note(note, time)))
        else:
            output = np.concatenate ((output, hold_note(note, time)))
    
    return output


def char_d2 (text, i, output, time, ragam):
    
    # by default, the note is madhyama sthayi, but if it passes through the tara sthayi or mandara stayi loops, the variable Madhyama_Sthayi is set to False
    madhyama_sthayi = True
    
    # mandara sthayi D2, once the error condition is checked
    if i != (len(text)-1):
        if text[i+1] == ".":
            note = swara_dictionary["d2"]
            madhyama_sthayi = False
            
            if i != 0:
                if i-3>=0:
                    if str(text [i-3:i]) == "∼∼∼":
                        output = np.concatenate ((output, kampita (time, note)))
                        
                
                         
                
                if text [i-1] == "∵" or text [i-1] == "∴":
                    output = np.concatenate ((output, spuritham (ragam, time, note)))         
                           
                elif text [i-1] == "w":
                    output = np.concatenate ((output, nokku (ragam, time, note)))
                    
                elif text [i-1] == "⋎":
                    output = np.concatenate ((output, orikai (ragam, time, note)))
                
                elif text [i-1] == "✓":
                    output = np.concatenate ((output, hold_note(note, 0.8*0.125)))
                                
                elif text [i-1] == "/" or text [i-1] == "\\": 
                    output = output
                            
                else:
                    output = np.concatenate ((output, hold_note(note, time)))
            
            else:
                output = np.concatenate ((output, hold_note(note, time)))
            
            
    # madhyama sthayi D2, if the above case doesn't hold
    if madhyama_sthayi == True:
        note = swara_dictionary["D2"]

        if i != 0:
                if i-3>=0:
                    if str(text [i-3:i]) == "∼∼∼":
                        output = np.concatenate ((output, kampita (time, note)))
                        
                
                
                if text [i-1] == "∵" or text [i-1] == "∴":
                    output = np.concatenate ((output, spuritham (ragam, time, note)))         
                           
                elif text [i-1] == "w":
                    output = np.concatenate ((output, nokku (ragam, time, note)))
                    
                elif text [i-1] == "⋎":
                    output = np.concatenate ((output, orikai (ragam, time, note)))
                
                elif text [i-1] == "✓":
                    output = np.concatenate ((output, hold_note(note, 0.8*0.125)))
                                
                elif text [i-1] == "/" or text [i-1] == "\\": 
                    output = output
                            
                else:
                    output = np.concatenate ((output, hold_note(note, time)))
                    
        else:
            output = np.concatenate ((output, hold_note(note, time)))
                    
    return output


def char_d3 (text, i, output, time, ragam):
    
    # by default, the note is madhyama sthayi, but if it passes through the tara sthayi or mandara stayi loops, the variable Madhyama_Sthayi is set to False
    madhyama_sthayi = True
    
    # mandara sthayi D3, once the error condition is checked
    if i != (len(text)-1):
        if text[i+1] == ".":
            note = swara_dictionary["d3"] 
            madhyama_sthayi = False
            
            
        if i != 0:
            if i-3>=0:
                if str(text [i-3:i]) == "∼∼∼":
                    output = np.concatenate ((output, kampita (time, note)))
                    
            
            
            if text [i-1] == "∵" or text [i-1] == "∴":
                output = np.concatenate ((output, spuritham (ragam, time, note)))         
                       
            elif text [i-1] == "w":
                output = np.concatenate ((output, nokku (ragam, time, note)))
                
            elif text [i-1] == "⋎":
                output = np.concatenate ((output, orikai (ragam, time, note)))
            
            elif text [i-1] == "✓":
                output = np.concatenate ((output, hold_note(note, 0.8*0.125)))
                            
            elif text [i-1] == "/" or text [i-1] == "\\": 
                output = output
                        
            else:
                output = np.concatenate ((output, hold_note(note, time)))
        
        else:
            output = np.concatenate ((output, hold_note(note, time)))
            
                
            
    # madhyama sthayi D3, if the above case doesn't hold
    if madhyama_sthayi == True:
        note=swara_dictionary["D3"]
        
        if i != 0:
            if i-3>=0:
                if str(text [i-3:i]) == "∼∼∼":
                    output = np.concatenate ((output, kampita (time, note)))
                
            
            if text [i-1] == "∵" or text [i-1] == "∴":
                output = np.concatenate ((output, spuritham (ragam, time, note)))         
                       
            elif text [i-1] == "w":
                output = np.concatenate ((output, nokku (ragam, time, note)))
                
            elif text [i-1] == "⋎":
                output = np.concatenate ((output, orikai (ragam, time, note)))
            
            elif text [i-1] == "✓":
                output = np.concatenate ((output, hold_note(note, 0.8*0.125)))
                            
            elif text [i-1] == "/" or text [i-1] == "\\": 
                output = output
                        
            else:
                output = np.concatenate ((output, hold_note(note, time)))
                
        else:
            output = np.concatenate ((output, hold_note(note, time)))
    
    return output


def char_n1 (text, i, output, time, ragam):
    
    # by default, the note is madhyama sthayi, but if it passes through the tara sthayi or mandara stayi loops, the variable Madhyama_Sthayi is set to False
    madhyama_sthayi = True
    
    # mandara sthayi N1, once the error condition is checked
    if i != (len(text)-1):
        if text[i+1] == ".":
            note=swara_dictionary["n1"]
            madhyama_sthayi = False
            
            if i != 0:
                if i-3>=0:
                    if str(text [i-3:i]) == "∼∼∼":
                        output = np.concatenate ((output, kampita (time, note)))
                        
               
                
                if text [i-1] == "∵" or text [i-1] == "∴":
                    output = np.concatenate ((output, spuritham (ragam, time, note)))         
                           
                elif text [i-1] == "w":
                    output = np.concatenate ((output, nokku (ragam, time, note)))
                    
                elif text [i-1] == "⋎":
                    output = np.concatenate ((output, orikai (ragam, time, note)))
                
                elif text [i-1] == "✓":
                    output = np.concatenate ((output, hold_note(note, 0.8*0.125)))
                                
                elif text [i-1] == "/" or text [i-1] == "\\": 
                    output = output
                            
                else:
                    output = np.concatenate ((output, hold_note(note, time)))
                    
            else:
                output = np.concatenate ((output, hold_note(note, time)))
                       
             
            
    # madhyama sthayi N1, if the above case doesn't hold
    if madhyama_sthayi == True:
        note =  swara_dictionary["N1"]
        
        if i != 0:
                if i-3>=0:
                    if str(text [i-3:i]) == "∼∼∼":
                        output = np.concatenate ((output, kampita (time, note)))
                        
               
                
                if text [i-1] == "∵" or text [i-1] == "∴":
                    output = np.concatenate ((output, spuritham (ragam, time, note)))         
                           
                elif text [i-1] == "w":
                    output = np.concatenate ((output, nokku (ragam, time, note)))
                    
                elif text [i-1] == "⋎":
                    output = np.concatenate ((output, orikai (ragam, time, note)))
                
                elif text [i-1] == "✓":
                    output = np.concatenate ((output, hold_note(note, 0.8*0.125)))
                                
                elif text [i-1] == "/" or text [i-1] == "\\": 
                    output = output
                            
                else:
                    output = np.concatenate ((output, hold_note(note, time)))
                    
        else:
            output = np.concatenate ((output, hold_note(note, time)))
                    
    return output


def char_n2 (text, i, output, time, ragam):
    
    # by default, the note is madhyama sthayi, but if it passes through the tara sthayi or mandara stayi loops, the variable Madhyama_Sthayi is set to False
    madhyama_sthayi = True
    
    # mandara sthayi N2, once the error condition is checked
    if i != (len(text)-1):
        if text[i+1] == ".":
            note = swara_dictionary["n2"]
            madhyama_sthayi = False
            
            if i != 0:
                if i-3>=0:
                    if str(text [i-3:i]) == "∼∼∼":
                        output = np.concatenate ((output, kampita (time, note)))
                        
            
                
                if text [i-1] == "∵" or text [i-1] == "∴":
                    output = np.concatenate ((output, spuritham (ragam, time, note)))         
                           
                elif text [i-1] == "w":
                    output = np.concatenate ((output, nokku (ragam, time, note)))
                    
                elif text [i-1] == "⋎":
                    output = np.concatenate ((output, orikai (ragam, time, note)))
                
                elif text [i-1] == "✓":
                    output = np.concatenate ((output, hold_note(note, 0.8*0.125)))
                                
                elif text [i-1] == "/" or text [i-1] == "\\": 
                    output = output
                            
                else:
                    output = np.concatenate ((output, hold_note(note, time)))
                    
            else:
                output = np.concatenate ((output, hold_note(note, time)))
            
    # madhyama sthayi N2, if the above case doesn't hold
    if madhyama_sthayi == True:
        note = swara_dictionary["N2"]
        
        if i != 0:
            if i-3>=0:
                if str(text [i-3:i]) == "∼∼∼":
                    output = np.concatenate ((output, kampita (time, note)))
                    
          
            
            if text [i-1] == "∵" or text [i-1] == "∴":
                output = np.concatenate ((output, spuritham (ragam, time, note)))         
                       
            elif text [i-1] == "w":
                output = np.concatenate ((output, nokku (ragam, time, note)))
                
            elif text [i-1] == "⋎":
                output = np.concatenate ((output, orikai (ragam, time, note)))
            
            elif text [i-1] == "✓":
                output = np.concatenate ((output, hold_note(note, 0.8*0.125)))
                            
            elif text [i-1] == "/" or text [i-1] == "\\": 
                output = output
                        
            else:
                output = np.concatenate ((output, hold_note(note, time)))
                
        else:
            output = np.concatenate ((output, hold_note(note, time)))
        
    return output


def char_n3 (text, i, output, time, ragam):
    
    # by default, the note is madhyama sthayi, but if it passes through the tara sthayi or mandara stayi loops, the variable Madhyama_Sthayi is set to False
    madhyama_sthayi = True
    
    # mandara sthayi N3, once the error condition is checked
    if i != (len(text)-1):
        if text[i+1] == ".":
            note = swara_dictionary["n3"]
            madhyama_sthayi = False
            
            if i != 0:
                if i-3>=0:
                    if str(text [i-3:i]) == "∼∼∼":
                        output = np.concatenate ((output, kampita (time, note)))
                        
             
                
                if text [i-1] == "∵" or text [i-1] == "∴":
                    output = np.concatenate ((output, spuritham (ragam, time, note)))         
                           
                elif text [i-1] == "w":
                    output = np.concatenate ((output, nokku (ragam, time, note)))
                    
                elif text [i-1] == "⋎":
                    output = np.concatenate ((output, orikai (ragam, time, note)))
                
                elif text [i-1] == "✓":
                    output = np.concatenate ((output, hold_note(note, 0.8*0.125)))
                                
                elif text [i-1] == "/" or text [i-1] == "\\": 
                    output = output
                            
                else:
                    output = np.concatenate ((output, hold_note(note, time)))
            
            else:
                output = np.concatenate ((output, hold_note(note, time)))
            
    # madhyama sthayi N3, if the above case doesn't hold
    if madhyama_sthayi == True:
        note = swara_dictionary["N3"]
        
        if i != 0:
                if i-3>=0:
                    if str(text [i-3:i]) == "∼∼∼":
                        output = np.concatenate ((output, kampita (time, note)))
                    
                
                if text [i-1] == "∵" or text [i-1] == "∴":
                    output = np.concatenate ((output, spuritham (ragam, time, note)))         
                           
                elif text [i-1] == "w":
                    output = np.concatenate ((output, nokku (ragam, time, note)))
                    
                elif text [i-1] == "⋎":
                    output = np.concatenate ((output, orikai (ragam, time, note)))
                
                elif text [i-1] == "✓":
                    output = np.concatenate ((output, hold_note(note, 0.8*0.125)))
                                
                elif text [i-1] == "/" or text [i-1] == "\\": 
                    output = output
                            
                else:
                    output = np.concatenate ((output, hold_note(note, time)))
            
        else:
            output = np.concatenate ((output, hold_note(note, time)))
                    
    return output


def char_m2 (text, i, output, time, ragam):
    
    # by default, the note is madhyama sthayi, but if it passes through the tara sthayi or mandara stayi loops, the variable Madhyama_Sthayi is set to False
    madhyama_sthayi = True
    
    # tara sthayi M2, once the error condition is checked
    if i != 0:
        if text[i-1] == "˙":
            note = swara_dictionary["mm2"] 
            madhyama_sthayi = False
            i = i-1
            if i != 0:
                if i-3>=0:
                    if str(text [i-3:i]) == "∼∼∼":
                        output = np.concatenate ((output, kampita (time, note)))
                        
          
                
                if text [i-1] == "∵" or text [i-1] == "∴":
                    output = np.concatenate ((output, spuritham (ragam, time, note)))         
                           
                elif text [i-1] == "w":
                    output = np.concatenate ((output, nokku (ragam, time, note)))
                    
                elif text [i-1] == "⋎":
                    output = np.concatenate ((output, orikai (ragam, time, note)))
                
                elif text [i-1] == "✓":
                    output = np.concatenate ((output, hold_note(note, 0.8*0.125)))
                                
                elif text [i-1] == "/" or text [i-1] == "\\": 
                    output = output
                            
                else:
                    output = np.concatenate ((output, hold_note(note, time)))
            
            else:
                output = np.concatenate ((output, hold_note(note, time)))
            
    # madhyama sthayi M2, if the above case doesn't hold
    if madhyama_sthayi == True:
        note = swara_dictionary["M2"]
        
        if i != 0:
                if i-3>=0:
                    if str(text [i-3:i]) == "∼∼∼":
                        output = np.concatenate ((output, kampita (time, note)))
                        
        
                
                if text [i-1] == "∵" or text [i-1] == "∴":
                    output = np.concatenate ((output, spuritham (ragam, time, note)))         
                           
                elif text [i-1] == "w":
                    output = np.concatenate ((output, nokku (ragam, time, note)))
                    
                elif text [i-1] == "⋎":
                    output = np.concatenate ((output, orikai (ragam, time, note)))
                
                elif text [i-1] == "✓":
                    output = np.concatenate ((output, hold_note(note, 0.8*0.125)))
                                
                elif text [i-1] == "/" or text [i-1] == "\\": 
                    output = output
                            
                else:
                    output = np.concatenate ((output, hold_note(note, time)))
                    
        else:
            output = np.concatenate ((output, hold_note(note, time)))
                    
    return output


def char_m1 (text, i, output, time, ragam):
    
    # by default, the note is madhyama sthayi, but if it passes through the tara sthayi or mandara stayi loops, the variable Madhyama_Sthayi is set to False
    madhyama_sthayi = True
    
    # tara sthayi M1, once the error condition is checked
    if i != 0:
        if text[i-1] == "˙":
            note = swara_dictionary["mm1"]
            madhyama_sthayi = False
            i = i-1
            if i != 0:
                if i-3>=0:
                    if str(text [i-3:i]) == "∼∼∼":
                        output = np.concatenate ((output, kampita (time, note)))
                        
         
                
                if text [i-1] == "∵" or text [i-1] == "∴":
                    output = np.concatenate ((output, spuritham (ragam, time, note)))         
                           
                elif text [i-1] == "w":
                    output = np.concatenate ((output, nokku (ragam, time, note)))
                    
                elif text [i-1] == "⋎":
                    output = np.concatenate ((output, orikai (ragam, time, note)))
                
                elif text [i-1] == "✓":
                    output = np.concatenate ((output, hold_note(note, 0.8*0.125)))
                                
                elif text [i-1] == "/" or text [i-1] == "\\": 
                    output = output
                            
                else:
                    output = np.concatenate ((output, hold_note(note, time)))
            
            else:
                output = np.concatenate ((output, hold_note(note, time)))
            
    # madhyama sthayi M1, if the above case doesn't hold
    if madhyama_sthayi == True:
        note = swara_dictionary["M1"]
        
        if i != 0:
                if i-3>=0:
                    if str(text [i-3:i]) == "∼∼∼":
                        output = np.concatenate ((output, kampita (time, note)))
                        
         
                
                if text [i-1] == "∵" or text [i-1] == "∴":
                    output = np.concatenate ((output, spuritham (ragam, time, note)))         
                           
                elif text [i-1] == "w":
                    output = np.concatenate ((output, nokku (ragam, time, note)))
                    
                elif text [i-1] == "⋎":
                    output = np.concatenate ((output, orikai (ragam, time, note)))
                
                elif text [i-1] == "✓":
                    output = np.concatenate ((output, hold_note(note, 0.8*0.125)))
                                
                elif text [i-1] == "/" or text [i-1] == "\\": 
                    output = output
                            
                else:
                    output = np.concatenate ((output, hold_note(note, time)))
                    
        else:
            output = np.concatenate ((output, hold_note(note, time)))
    
    return output


def char_g3 (text, i, output, time, ragam):
    
    # by default, the note is madhyama sthayi, but if it passes through the tara sthayi or mandara stayi loops, the variable Madhyama_Sthayi is set to False
    madhyama_sthayi = True
    
    # tara sthayi G3, once the error condition is checked
    if i != 0:
        if text[i-1] == "˙":
            note = swara_dictionary["gg3"]
            madhyama_sthayi = False
            
            i=i-1
            
            if i != 0:
                if i-3>=0:
                    if str(text [i-3:i]) == "∼∼∼":
                        output = np.concatenate ((output, kampita (time, note)))
                        
       
                
                if text [i-1] == "∵" or text [i-1] == "∴":
                    output = np.concatenate ((output, spuritham (ragam, time, note)))         
                           
                elif text [i-1] == "w":
                    output = np.concatenate ((output, nokku (ragam, time, note)))
                    
                elif text [i-1] == "⋎":
                    output = np.concatenate ((output, orikai (ragam, time, note)))
                
                elif text [i-1] == "✓":
                    output = np.concatenate ((output, hold_note(note, 0.8*0.125)))
                                
                elif text [i-1] == "/" or text [i-1] == "\\": 
                    output = output
                            
                else:
                    output = np.concatenate ((output, hold_note(note, time)))
                    
            else:
                output = np.concatenate ((output, hold_note(note, time)))
    
     
            
    # madhyama sthayi G3, if the above case doesn't hold
    if madhyama_sthayi == True:
        note = swara_dictionary["G3"] 
        
        if i != 0:
            if i-3>=0:
                if str(text [i-3:i]) == "∼∼∼":
                    output = np.concatenate ((output, kampita (time, note)))
                    
         
            
            if text [i-1] == "∵" or text [i-1] == "∴":
                output = np.concatenate ((output, spuritham (ragam, time, note)))         
                       
            elif text [i-1] == "w":
                output = np.concatenate ((output, nokku (ragam, time, note)))
                
            elif text [i-1] == "⋎":
                output = np.concatenate ((output, orikai (ragam, time, note)))
            
            elif text [i-1] == "✓":
                output = np.concatenate ((output, hold_note(note, 0.8*0.125)))
                            
            elif text [i-1] == "/" or text [i-1] == "\\": 
                output = output
                        
            else:
                output = np.concatenate ((output, hold_note(note, time)))
                
        else:
            output = np.concatenate ((output, hold_note(note, time)))
                    
    return output


def char_g2 (text, i, output, time, ragam):
    
    # by default, the note is madhyama sthayi, but if it passes through the tara sthayi or mandara stayi loops, the variable Madhyama_Sthayi is set to False
    madhyama_sthayi = True
    
    # tara sthayi G2, once the error condition is checked
    if i != 0:
        if text[i-1] == "˙":
            note = swara_dictionary["gg2"]            
            madhyama_sthayi = False
            i=i-1
            if i != 0:
                if i-3>=0:
                    if str(text [i-3:i]) == "∼∼∼":
                        output = np.concatenate ((output, kampita (time, note)))
                        
          
                
                if text [i-1] == "∵" or text [i-1] == "∴":
                    output = np.concatenate ((output, spuritham (ragam, time, note)))         
                           
                elif text [i-1] == "w":
                    output = np.concatenate ((output, nokku (ragam, time, note)))
                    
                elif text [i-1] == "⋎":
                    output = np.concatenate ((output, orikai (ragam, time, note)))
                
                elif text [i-1] == "✓":
                    output = np.concatenate ((output, hold_note(note, 0.8*0.125)))
                                
                elif text [i-1] == "/" or text [i-1] == "\\": 
                    output = output
                            
                else:
                    output = np.concatenate ((output, hold_note(note, time)))
            
            else:
                output = np.concatenate ((output, hold_note(note, time)))
            
    # madhyama sthayi G2, if the above case doesn't hold
    if madhyama_sthayi == True:
        note = swara_dictionary["G2"]
        
        if i != 0:
                if i-3>=0:
                    if str(text [i-3:i]) == "∼∼∼":
                        output = np.concatenate ((output, kampita (time, note)))
                        
           
                
                if text [i-1] == "∵" or text [i-1] == "∴":
                    output = np.concatenate ((output, spuritham (ragam, time, note)))         
                           
                elif text [i-1] == "w":
                    output = np.concatenate ((output, nokku (ragam, time, note)))
                    
                elif text [i-1] == "⋎":
                    output = np.concatenate ((output, orikai (ragam, time, note)))
                
                elif text [i-1] == "✓":
                    output = np.concatenate ((output, hold_note(note, 0.8*0.125)))
                                
                elif text [i-1] == "/" or text [i-1] == "\\": 
                    output = output
                            
                else:
                    output = np.concatenate ((output, hold_note(note, time)))
                    
        else:
            output = np.concatenate ((output, hold_note(note, time)))
            
    return output


def char_g1 (text, i, output, time, ragam):
    
    # by default, the note is madhyama sthayi, but if it passes through the tara sthayi or mandara stayi loops, the variable Madhyama_Sthayi is set to False
    madhyama_sthayi = True
    
    # tara sthayi G1, once the error condition is checked
    if i != 0:
        if text[i-1] == "˙":
            note = swara_dictionary["gg1"] 
            madhyama_sthayi = False
            i=i-1
            if i != 0:
                if i-3>=0:
                    if str(text [i-3:i]) == "∼∼∼":
                        output = np.concatenate ((output, kampita (time, note)))
                        
          
                
                if text [i-1] == "∵" or text [i-1] == "∴":
                    output = np.concatenate ((output, spuritham (ragam, time, note)))         
                           
                elif text [i-1] == "w":
                    output = np.concatenate ((output, nokku (ragam, time, note)))
                    
                elif text [i-1] == "⋎":
                    output = np.concatenate ((output, orikai (ragam, time, note)))
                
                elif text [i-1] == "✓":
                    output = np.concatenate ((output, hold_note(note, 0.8*0.125)))
                                
                elif text [i-1] == "/" or text [i-1] == "\\": 
                    output = output
                            
                else:
                    output = np.concatenate ((output, hold_note(note, time)))
            
            else:
                output = np.concatenate ((output, hold_note(note, time)))
                    
     
            
    # madhyama sthayi G1, if the above case doesn't hold
    if madhyama_sthayi == True:
        note = swara_dictionary["G1"]
        
        if i != 0:
                if i-3>=0:
                    if str(text [i-3:i]) == "∼∼∼":
                        output = np.concatenate ((output, kampita (time, note)))
                        
         
                if text [i-1] == "∵" or text [i-1] == "∴":
                    output = np.concatenate ((output, spuritham (ragam, time, note)))         
                           
                elif text [i-1] == "w":
                    output = np.concatenate ((output, nokku (ragam, time, note)))
                    
                elif text [i-1] == "⋎":
                    output = np.concatenate ((output, orikai (ragam, time, note)))
                
                elif text [i-1] == "✓":
                    output = np.concatenate ((output, hold_note(note, 0.8*0.125)))
                                
                elif text [i-1] == "/" or text [i-1] == "\\": 
                    output = output
                            
                else:
                    output = np.concatenate ((output, hold_note(note, time)))
                    
        else:
            output = np.concatenate ((output, hold_note(note, time)))
    
    return output


def char_r3 (text, i, output, time, ragam):
    
    # by default, the note is madhyama sthayi, but if it passes through the tara sthayi or mandara stayi loops, the variable Madhyama_Sthayi is set to False
    madhyama_sthayi = True
    
    # tara sthayi R3, once the error condition is checked
    if i != 0:
        if text[i-1] == "˙":
            note = swara_dictionary["rr3"]
            madhyama_sthayi = False
            i=i-1
            if i != 0:
                if i-3>=0:
                    if str(text [i-3:i]) == "∼∼∼":
                        output = np.concatenate ((output, kampita (time, note)))
                        
             
                
                if text [i-1] == "∵" or text [i-1] == "∴":
                    output = np.concatenate ((output, spuritham (ragam, time, note)))         
                           
                elif text [i-1] == "w":
                    output = np.concatenate ((output, nokku (ragam, time, note)))
                    
                elif text [i-1] == "⋎":
                    output = np.concatenate ((output, orikai (ragam, time, note)))
                
                elif text [i-1] == "✓":
                    output = np.concatenate ((output, hold_note(note, 0.8*0.125)))
                                
                elif text [i-1] == "/" or text [i-1] == "\\": 
                    output = output
                            
                else:
                    output = np.concatenate ((output, hold_note(note, time)))
                    
            else:
                output = np.concatenate ((output, hold_note(note, time)))
                    
     
            
    # madhyama sthayi R3, if the above case doesn't hold
    if madhyama_sthayi == True:
        note = swara_dictionary["R3"]
        if i != 0:
                if i-3>=0:
                    if str(text [i-3:i]) == "∼∼∼":
                        output = np.concatenate ((output, kampita (time, note)))
                        
           
                
                if text [i-1] == "∵" or text [i-1] == "∴":
                    output = np.concatenate ((output, spuritham (ragam, time, note)))         
                           
                elif text [i-1] == "w":
                    output = np.concatenate ((output, nokku (ragam, time, note)))
                    
                elif text [i-1] == "⋎":
                    output = np.concatenate ((output, orikai (ragam, time, note)))
                
                elif text [i-1] == "✓":
                    output = np.concatenate ((output, hold_note(note, 0.8*0.125)))
                                
                elif text [i-1] == "/" or text [i-1] == "\\": 
                    output = output
                            
                else:
                    output = np.concatenate ((output, hold_note(note, time)))
                    
        else:
            output = np.concatenate ((output, hold_note(note, time)))
    
    return output

def char_r2 (text, i, output, time, ragam):
    
    # by default, the note is madhyama sthayi, but if it passes through the tara sthayi or mandara stayi loops, the variable Madhyama_Sthayi is set to False
    madhyama_sthayi = True
    
    # tara sthayi R2, once the error condition is checked
    if i != 0:
        if text[i-1] == "˙":
            note = swara_dictionary["rr2"]
            madhyama_sthayi = False
            i=i-1
            
            if i != 0:
                if i-3>=0:
                    if str(text [i-3:i]) == "∼∼∼":
                        output = np.concatenate ((output, kampita (time, note)))
                        
            
                
                if text [i-1] == "∵" or text [i-1] == "∴":
                    output = np.concatenate ((output, spuritham (ragam, time, note)))         
                           
                elif text [i-1] == "w":
                    output = np.concatenate ((output, nokku (ragam, time, note)))
                    
                elif text [i-1] == "⋎":
                    output = np.concatenate ((output, orikai (ragam, time, note)))
                
                elif text [i-1] == "✓":
                    output = np.concatenate ((output, hold_note(note, 0.8*0.125)))
                                
                elif text [i-1] == "/" or text [i-1] == "\\": 
                    output = output
                            
                else:
                    output = np.concatenate ((output, hold_note(note, time)))
                
            else:
                output = np.concatenate ((output, hold_note(note, time)))
                    
             
            
    # madhyama sthayi R2, if the above case doesn't hold
    if madhyama_sthayi == True:
        note = swara_dictionary["R2"]
        
        if i != 0:
                if i-3>=0:
                    if str(text [i-3:i]) == "∼∼∼":
                        output = np.concatenate ((output, kampita (time, note)))
                        
           
                
                if text [i-1] == "∵" or text [i-1] == "∴":
                    output = np.concatenate ((output, spuritham (ragam, time, note)))         
                           
                elif text [i-1] == "w":
                    output = np.concatenate ((output, nokku (ragam, time, note)))
                    
                elif text [i-1] == "⋎":
                    output = np.concatenate ((output, orikai (ragam, time, note)))
                
                elif text [i-1] == "✓":
                    output = np.concatenate ((output, hold_note(note, 0.8*0.125)))
                                
                elif text [i-1] == "/" or text [i-1] == "\\": 
                    output = output
                            
                else:
                    output = np.concatenate ((output, hold_note(note, time)))
                    
        else:
            output = np.concatenate ((output, hold_note(note, time)))
    
    return output


def char_r1 (text, i, output, time, ragam):
    
    # by default, the note is madhyama sthayi, but if it passes through the tara sthayi or mandara stayi loops, the variable Madhyama_Sthayi is set to False
    madhyama_sthayi = True
    
    # tara sthayi R1, once the error condition is checked
    if i != 0:
        if text[i-1] == "˙":
            output = np.concatenate ((output, hold_note(swara_dictionary["rr1"],time)))
            madhyama_sthayi = False
            
            i = i-1
            
            if i != 0:
                if i-3>=0:
                    if str(text [i-3:i]) == "∼∼∼":
                        output = np.concatenate ((output, kampita (time, note)))
                        
             
                
                if text [i-1] == "∵" or text [i-1] == "∴":
                    output = np.concatenate ((output, spuritham (ragam, time, note)))         
                           
                elif text [i-1] == "w":
                    output = np.concatenate ((output, nokku (ragam, time, note)))
                    
                elif text [i-1] == "⋎":
                    output = np.concatenate ((output, orikai (ragam, time, note)))
                
                elif text [i-1] == "✓":
                    output = np.concatenate ((output, hold_note(note, 0.8*0.125)))
                                
                elif text [i-1] == "/" or text [i-1] == "\\": 
                    output = output
                            
                else:
                    output = np.concatenate ((output, hold_note(note, time)))
            
            else:
                output = np.concatenate ((output, hold_note(note, time)))
                    
             
            
    # madhyama sthayi R1, if the above case doesn't hold
    if madhyama_sthayi == True:
        note = swara_dictionary["R1"]
        
        if i != 0:
                if i-3>=0:
                    if str(text [i-3:i]) == "∼∼∼":
                        output = np.concatenate ((output, kampita (time, note)))
                        
            
                if text [i-1] == "∵" or text [i-1] == "∴":
                    output = np.concatenate ((output, spuritham (ragam, time, note)))         
                           
                elif text [i-1] == "w":
                    output = np.concatenate ((output, nokku (ragam, time, note)))
                    
                elif text [i-1] == "⋎":
                    output = np.concatenate ((output, orikai (ragam, time, note)))
                
                elif text [i-1] == "✓":
                    output = np.concatenate ((output, hold_note(note, 0.8*0.125)))
                                
                elif text [i-1] == "/" or text [i-1] == "\\": 
                    output = output
                            
                else:
                    output = np.concatenate ((output, hold_note(note, time)))
                    
        else:
            output = np.concatenate ((output, hold_note(note, time)))
    
    return output


def char_s (text, i, output, time, ragam):
    
    # by default, the note is madhyama sthayi, but if it passes through the tara sthayi or mandara stayi loops, the variable Madhyama_Sthayi is set to False
    madhyama_sthayi = True
    
    # tara sthayi S, once the error condition is checked
    if i != 0:
        if text[i-1] == "˙":
            note = swara_dictionary["S2"]
            madhyama_sthayi = False
            
            i=i-1
            
            if i != 0:
                if i-3>=0:
                    if str(text [i-3:i]) == "∼∼∼":
                        output = np.concatenate ((output, kampita (time, note)))
                        
           
                if text [i-1] == "∵" or text [i-1] == "∴":
                    output = np.concatenate ((output, spuritham (ragam, time, note)))         
                           
                elif text [i-1] == "w":
                    output = np.concatenate ((output, nokku (ragam, time, note)))
                    
                elif text [i-1] == "⋎":
                    output = np.concatenate ((output, orikai (ragam, time, note)))
                
                elif text [i-1] == "✓":
                    output = np.concatenate ((output, hold_note(note, 0.8*0.125)))
                                
                elif text [i-1] == "/" or text [i-1] == "\\": 
                    output = output
                            
                else:
                    output = np.concatenate ((output, hold_note(note, time)))
            else:
                output = np.concatenate ((output, hold_note(note, time)))
        
            
    # madhyama sthayi S, if the above case doesn't hold
    if madhyama_sthayi == True:
        note = swara_dictionary["S1"]
        
        if i != 0:
                if i-3>=0:
                    if str(text [i-3:i]) == "∼∼∼":
                        output = np.concatenate ((output, kampita (time, note)))
                        
               
                
                if text [i-1] == "∵" or text [i-1] == "∴":
                    output = np.concatenate ((output, spuritham (ragam, time, note)))         
                           
                elif text [i-1] == "w":
                    output = np.concatenate ((output, nokku (ragam, time, note)))
                    
                elif text [i-1] == "⋎":
                    output = np.concatenate ((output, orikai (ragam, time, note)))
                
                elif text [i-1] == "✓":
                    output = np.concatenate ((output, hold_note(note, 0.8*0.125)))
                                
                elif text [i-1] == "/" or text [i-1] == "\\": 
                    output = output
                            
                else:
                    output = np.concatenate ((output, hold_note(note, time)))
        else:
            output = np.concatenate ((output, hold_note(note, time)))
    
    return output

# input: a string like "p\D.n.⋎S$$#rGm⌢Pd∼∼∼N˙Ss˙s" with random symbols in the middle, and empty list: np.int16([])
# output: ignores all the symbols and plays the plain notes according to their time in KALYANI
    
def plain_notes (text, output, ragam):
    for i in range (0,len(text)):
        
        if text[i] == "s":
            output = char_s (text, i, output, 1, ragam)
        if text[i] == "S":
            output = char_s (text, i, output, 2, ragam)
        if text[i] == "r":
            
            if ragam[4] == swara_dictionary["R1"]:
                output = char_r1 (text, i, output, 1, ragam)
            if ragam[4] == swara_dictionary["R2"]:
                output = char_r2 (text, i, output, 1, ragam)
            if ragam[4] == swara_dictionary["R3"]:
                output = char_r3 (text, i, output, 1, ragam)
                
        if text[i] == "R":
            
            if ragam[4] == swara_dictionary["R1"]:
                output = char_r1 (text, i, output, 2, ragam)
            if ragam[4] == swara_dictionary["R2"]:
                output = char_r2 (text, i, output, 2, ragam)
            if ragam[4] == swara_dictionary["R3"]:
                output = char_r3 (text, i, output, 2, ragam)
                
        if text[i] == "g":
            
            if ragam[5] == swara_dictionary["G1"]:
                output = char_g1 (text, i, output, 1, ragam)
            if ragam[5] == swara_dictionary["G2"]:
                output = char_g2 (text, i, output, 1, ragam)
            if ragam[5] == swara_dictionary["G3"]:
                output = char_g3 (text, i, output, 1, ragam)
                
        if text[i] == "G":
            
            if ragam[5] == swara_dictionary["G1"]:
                output = char_g1 (text, i, output, 2, ragam)
            if ragam[5] == swara_dictionary["G2"]:
                output = char_g2 (text, i, output, 2, ragam)
            if ragam[5] == swara_dictionary["G3"]:
                output = char_g3 (text, i, output, 2, ragam)
                
        if text[i] == "m":
            
            if ragam[6] == swara_dictionary["M1"]:
                output = char_m1 (text, i, output, 1, ragam)
            if ragam[6] == swara_dictionary["M2"]:
                output = char_m2 (text, i, output, 1, ragam)
        
        if text[i] == "M":
            
            if ragam[6] == swara_dictionary["M1"]:
                output = char_m1 (text, i, output, 2, ragam)
            if ragam[6] == swara_dictionary["M2"]:
                output = char_m2 (text, i, output, 2, ragam)
            
        if text[i] == "p":
            output = char_p (text, i, output, 1, ragam)
        if text[i] == "P":
            output = char_p (text, i, output, 2, ragam)
            
        if text[i] == "d":
            
            if ragam[8] == swara_dictionary["D1"]:
                output = char_d1 (text, i, output, 1, ragam)
            if ragam[8] == swara_dictionary["D2"]:
                output = char_d2 (text, i, output, 1, ragam)
            if ragam[8] == swara_dictionary["D3"]:
                output = char_d3 (text, i, output, 1, ragam)
                
        if text[i] == "D":
            
            if ragam[8] == swara_dictionary["D1"]:
                output = char_d1 (text, i, output, 2, ragam)
            if ragam[8] == swara_dictionary["D2"]:
                output = char_d2 (text, i, output, 2, ragam)
            if ragam[8] == swara_dictionary["D3"]:
                output = char_d3 (text, i, output, 2, ragam)
                
        if text[i] == "n":
            
            if ragam[9] == swara_dictionary["N1"]:
                output = char_n1 (text, i, output, 1, ragam)
            if ragam[9] == swara_dictionary["N2"]:
                output = char_n2 (text, i, output, 1, ragam)
            if ragam[9] == swara_dictionary["N3"]:
                output = char_n3 (text, i, output, 1, ragam)
                
        if text[i] == "N":
            if ragam[9] == swara_dictionary["N1"]:
                output = char_n1 (text, i, output, 2, ragam)
            if ragam[9] == swara_dictionary["N2"]:
                output = char_n2 (text, i, output, 2, ragam)
            if ragam[9] == swara_dictionary["N3"]:
                output = char_n3 (text, i, output, 2, ragam)
            
    return output
            
output = plain_notes ("p\D.n.⋎S$$#rGm⌢Pd∼∼∼N˙Ss˙s", np.int16([]), kalyani)
    
write('plain_notesfunction3.wav', sps, output)




output = plain_notes ("w˙sw˙r⋎˙g⌢˙r˙r✓˙swdwp.wd.⋎n.", np.int16([]), kalyani)
  
write('test1.wav', sps, output)

























