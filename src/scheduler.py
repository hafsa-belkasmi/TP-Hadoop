import schedule
import time
from main import main

main()  # exécution immédiate au lancement

schedule.every(6).hours.do(main)

print("Automatisation lancée : première exécution faite, puis toutes les 6 heures.")

while True:
    schedule.run_pending()
    time.sleep(60)