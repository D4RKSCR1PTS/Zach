import os, time, cloudscraper, pyautogui, random, subprocess
from win10toast import ToastNotifier
from termcolor import cprint
os.system(f'title AutoRain ^')
storage = []
scraper = cloudscraper.create_scraper()
auth = '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'
toast = ToastNotifier()
AutoJoinRains = True
cprint("[CREDITS:] AutoRain made by Thwartedbrute#8188","cyan")
time.sleep(4)
os.system('cls')
try:
  get = scraper.get("https://rest-bf.blox.land/user", headers = {"origin": "https://bloxflip.com", "x-auth-token": auth})
  info = get.json()['user']
  print(f"Logged in as {info['robloxUsername']}\nCurrent balance: {info['wallet']}\n")
except:
  input("Invalid Auth Token\nPress enter to exit.")
  quit()
cprint("AutoRain Enabled! Press Ctrl + C to exit.","magenta")
while True:
  try:
    r = scraper.get('https://rest-bf.blox.land/chat/history').json()
    check = r['rain']
    if check['active'] == True:
      if check['prize'] >= 500:
        store = scraper.get("https://rest-bf.blox.land/user", headers = {"x-auth-token": f"{auth}"}).json()['user']['wallet']
        storage.append(store)
        grabprize = str(check['prize'])[:-2]
        prize = (format(int(grabprize),","))
        host = check['host']
        getduration = check['duration']
        convert = (getduration/(1000*60))%60
        duration = (int(convert))
        waiting = (convert*60+10)
        sent = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(int(time.time())))
        time.sleep(1)
        while True:
          x = random.randint(1,500)
          y = random.randint(1,500)
          join = pyautogui.locateCenterOnScreen('assets/pro.png', confidence = 0.9)
          if join:
            time.sleep(1)
            pyautogui.moveTo(join)
            time.sleep(0.5)
            pyautogui.click()
            time.sleep(2)
            pyautogui.moveTo(x, y, 0.5)
          if not join:
            cprint("Could not locate join button, opening bloxlfip...", "red")
            subprocess.call("start https://bloxflip.com",shell=True)
            time.sleep(10)
            join = pyautogui.locateCenterOnScreen('assets/pro.png', confidence = 0.9)
            pyautogui.moveTo(join)
            time.sleep(0.5)
            pyautogui.click()
            time.sleep(2)
            pyautogui.moveTo(x, y, 0.5)
          else: cprint("failed to locate button even after site opened.", "red")
          break
        info = scraper.get("https://rest-bf.blox.land/user", headers = {"x-auth-token": f"{auth}"}).json()['user']
        checker = scraper.get("https://rest-bf.blox.land/chat/history").json()['rain']['players']
        cprint(f"Successfully joined rain!","green")
        cprint(f"Rain amount: {prize} R$", "cyan")
        cprint(f"Expiration: {duration} minutes","yellow")
        cprint(f"Host: {host}","yellow")
        cprint(f"Timestamp: {sent}","magenta")
        cprint(f"Current balance: {info['wallet']}","green")
        time.sleep(waiting)
    elif check['active'] == False:
      time.sleep(5)
  except Exception as e:
    print(e)
    time.sleep(5)