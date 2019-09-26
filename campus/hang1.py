#!/usr/bin/env python3
# http://e-learn.cyber.org.il/python/rolling_assignment/resources/hangman_welcome_screen.txt

 
import random

r = random.randint(5,10)
 
print("""   
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/""");
 					 


print r;

 
#picture 1:
p1 = """
    x-------x"""; 


#picture 2:
p2 = """
    x-------x   
    |  
    |  
    |  
    |  
    |""";
		
p3 ="""
    x-------x
    |       |
    |       0
    |
    |
    |""";

p4 ="""
    x-------x
    |       |
    |       0
    |       | 
    |    
    |""";	
	
p5 ="""
    x-------x
    |       |
    |       0
    |      [|]
    |    
    |""";
p6 ="""
    x-------x
    |       |
    |       0
    |      [|]
    |     [     
    |""";	
	
p7 ="""
    x-------x
    |       |
    |       0
    |      [|]
    |     [   ]  
    |"""	;	
print p1;
print p2;
print p3;
print p4; 
print p5; 
print p6; 
print p7; 