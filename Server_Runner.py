import os
import sys
import platform
#The path of folder that has the minecraft server run shortcuts
path = "/run/media/mari/CC4C06354C061B3A/Users/Mari/Documents/Minecraft Servers/Server_Batchs/"
#"Windows" or "Linux"
#Change only if you know what your doing ;3
os_sys = sys.platform
def main():

    numbered_files = {}
    def get_server_files():

        files = []
        for i in os.listdir(path) :
            if os.path.isfile(path) :
                    named_file , extension = os.path.splitext(i)
            else :
                print("File/Directory Error -")
                print("Directory Empty? Check Path.. :3")
            if  extension == ".lnk" or extension == ".sh":
                files.append (named_file)

        for index, element in enumerate(files):
                numbered_files[index + 1] = element

    def main_menu() :

        while True :
            print ("1: Run_server")
            print ("2: Connect to running server")
            print ("3: Settings")
            print ("4: Exit")
            menu_input = input(("Please choose an option- "))


            if (menu_input) == "1" or (menu_input.lower()) == "run_server":
                run_server()
            elif (menu_input) == "2" or (menu_input.lower()) == "connection options":
                print("Connection options")
            elif (menu_input) == "3" or (menu_input.lower()) == "settings":
                print("Settings")
                settings_menu()
            elif (menu_input) == "4" or (menu_input.lower()) == "exit":
                print("Server Runner Made by Mari! <3")
                print("Hope it helped!")
                sys.exit()
            else :
                print ("Inccorect Option! Try again!")

    def run_server() :
        get_server_files()
        os.chdir (path)
        while True :
            print (numbered_files)
            server_number=input("Which pack do you want to start?: ")
            if server_number.lower() == "exit" :
                print ("Returning to menu~")
                break

            chosen_server = numbered_files.get(int(server_number))
            if chosen_server == None :
                print (f"Server number {server_number} was not found, Check Path or Files")
                run_server()
            print(f"Server {chosen_server} was selected")
            confrimation = input("Is this the server you wish to start?: Y/N ")
            if  confrimation.lower() == "yes" or confrimation.lower() == "y" :
                if os.popen(chosen_server) :
                    print ("Server Opened")
                    break

            else :
                print ("Confirmation denied")
                print ("Returning to menu~")

    def settings_menu():

        print(path)

        install_dir= os.path.abspath(__file__)
        print(install_dir)

    main_menu()
main()
