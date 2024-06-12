import os
import shutil
import os.path

def print_error(skk): print("\033[91m {}\033[00m" .format(skk))
def print_success(skk): print("\033[92m {}\033[00m" .format(skk))
def print_warning(skk): print("\033[93m {}\033[00m" .format(skk))
def print_info(skk): print("\033[96m {}\033[00m" .format(skk))

def create_directories():
    os.mkdir("releases")
    os.chdir("releases") 
    os.mkdir("chromium") 
    os.mkdir("firefox") 
    os.chdir("chromium") 
    os.mkdir("html")   
    os.mkdir("scripts") 
    os.mkdir("static") 
    os.chdir("..")
    os.chdir("firefox")     
    os.mkdir("html") 
    os.mkdir("scripts")     
    os.mkdir("static")   
    os.chdir("../..")
    os.chdir("source/extension")
def build_chromium(): 
    try: 
        print_info("Copying files to chromium directory...")
        shutil.copytree("html", "../../releases/chromium/html", dirs_exist_ok=True)
        shutil.copytree("scripts", "../../releases/chromium/scripts", dirs_exist_ok=True)
        shutil.copytree("static", "../../releases/chromium/static", dirs_exist_ok=True)
        print_info("Copying manifest to chromium directory...")
        shutil.copy("manifests/chromium.json", "../../releases/chromium")
        os.chdir("../../releases/chromium")
        print_info("Renaming manifest file...")
        os.rename("chromium.json", "manifest.json")
        os.chdir("..")
        print_info("Creating archive...")
        shutil.make_archive("chromium_build", "zip", "chromium")
        print_info("Cleaning up...")
        shutil.rmtree("chromium") 
        print_success("SUCCESS: Chromium build created.")
    except FileNotFoundError:
        print_error("ERROR: File not found.")
def build_firefox():
    try:
        os.chdir("..")
        os.chdir("source/extension")
        print_info("Copying files to firefox directory...")
        shutil.copytree("html", "../../releases/firefox/html", dirs_exist_ok=True)
        shutil.copytree("scripts", "../../releases/firefox/scripts", dirs_exist_ok=True)
        shutil.copytree("static", "../../releases/firefox/static", dirs_exist_ok=True)
        print_info("Copying manifest to firefox directory...")
        shutil.copy("manifests/firefox.json", "../../releases/firefox")
        os.chdir("../../releases/firefox")
        print_info("Renaming manifest file...")
        os.rename("firefox.json", "manifest.json")
        os.chdir("..")
        print_info("Creating archive...")
        shutil.make_archive("firefox_build", "zip", "firefox")
        print_info("Cleaning up...")
        shutil.rmtree("firefox")
        print_success("SUCCESS: Firefox build created.")
    except FileNotFoundError:
        print_error("ERROR: File not found.")
if __name__ == "__main__":
    def main(): 
        if os.path.exists("releases"):
            print_warning("WARNING: Existing release directory found. Deleting...")
            shutil.rmtree("releases")
            create_directories() 
            build_chromium()  
            build_firefox()
        else:
            create_directories() 
            build_chromium()  
            build_firefox()    
    main()
else:
    exit()