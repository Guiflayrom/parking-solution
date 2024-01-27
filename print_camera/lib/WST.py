import time
import pyautogui

class WST:
    def __init__(self,browser=None,mouse_con=None,keyboard_con=None):
        self.br = browser

    def elementary(self,xpath_list=list,key=None):
        b = 0
        for xpaths in xpath_list:
            if '#time' in xpaths:
                xpaths = xpaths.replace("#time","")
                tt = xpaths[-1]
                tt = float(tt)
                time.sleep(tt)
                tt = len(xpaths) - 1
                xpaths = xpaths[0:tt]
            if '#clickhere' in xpaths:
                newp = xpaths.replace("#clickhere", "")
                elen = self.br.find_element_by_xpath(newp).click()
            if '#stringme' in xpaths:
                newp = xpaths.replace("#stringme", "")
                elen = self.br.find_element_by_xpath(newp).string
                return elen     
            if '#textme' in xpaths:
                newp = xpaths.replace("#textme", "")
                elen = self.br.find_element_by_xpath(newp).text          
                return elen                
            if '#skeys' in xpaths:
                newp = xpaths.replace("#skeys", "")
                newp = newp.replace("#clear","")
                elen = self.br.find_element_by_xpath(newp).clear()
                elen = self.br.find_element_by_xpath(newp).send_keys(key[b])
                b += 1      

    def uniclick(self,xpath_list=str):
        self.br.find_element_by_xpath(xpath_list).click()

    def unitext(self,xpath_list=str):
        elen = self.br.find_element_by_xpath(xpath_list).text          
        return elen

    def unikey(self,xpath_list=str,key=str):
        self.br.find_element_by_xpath(xpath_list).send_keys(key)

    def remotary(self,command_list=list):
        pyautogui.FAILSAFE = False
        for command in command_list:
            if '#c' in command:
                time.sleep(10)
            if '#d' in command:
                time.sleep(5)       
            if '#i' in command:
                time.sleep(1)
            if '#time' in command:
                command = command.replace("#time","")
                tt = command[-1]
                tt = float(tt)
                time.sleep(tt)
                tt = len(command) - 1
                command = command[0:tt]
            if type(command) == tuple:
                if len(command) == 3:
                    pyautogui.click(command[:2],clicks=command[-1], duration=0.5)
                else:
                    pyautogui.click(command,duration=0.5)
            if '#key' in command:
                newp = command.replace('#key',"")
                pyautogui.typewrite(newp)
            if "#hkey" in command:
                newp = command.replace("#hkey","")
                newp = newp.split();newp = tuple(newp)
                if len(newp) == 1:
                    pyautogui.hotkey(newp[0])   
                if len(newp) == 2:
                    pyautogui.hotkey(newp[0],newp[1])
                if len(newp) == 3:
                    pyautogui.hotkey(newp[0],newp[1],newp[2])  
                if len(newp) == 4:
                    pyautogui.hotkey(newp[0],newp[1],newp[2],newp[3])                                      

    def unihotkey(self,newp=list):
        newp = tuple(newp)
        
        if len(newp) == 1:
            pyautogui.hotkey(newp[0]) 
        if len(newp) == 2:
            pyautogui.hotkey(newp[0],newp[1])
        if len(newp) == 3:
            pyautogui.hotkey(newp[0],newp[1],newp[2])  
        if len(newp) == 4:
            pyautogui.hotkey(newp[0],newp[1],newp[2],newp[3])         
        if len(newp) == 5:
            pyautogui.hotkey(newp[0],newp[1],newp[2],newp[3],newp[4])             