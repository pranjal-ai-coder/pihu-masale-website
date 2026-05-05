import eel
import os
import sys

# Boss, path set kar rahe hain taaki 404 error kabhi na aaye
base_dir = os.path.dirname(os.path.abspath(__file__))
web_app_dir = os.path.join(base_dir, 'web')

eel.init(web_app_dir)

@eel.expose
def get_boss_name():
    return "Pranjal Boss"

print("--- PIHU MASALE PREMIUM AD ENGINE STARTING ---")
print(f"Directory: {web_app_dir}")

try:
    # High-quality desktop window
    eel.start('index.html', size=(450, 850), position=(500, 50))
except Exception as e:
    print(f"Error: {e}")

# site link  = https://pihu-masale.netlify.app/ 
#real work sites link -https://pihu-masale--pranjalgupta655.replit.app/