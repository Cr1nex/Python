import subprocess
import optparse
import re

def change_mac(interface,new_mac):

    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
    subprocess.call(["ifconfig",interface,"up"])
    
def get_arguments():

    parser = optparse.OptionParser()
    parser.add_option("-i","--interface", dest="interface", help="Interface to change its MAC address")
            
    parser.add_option("-m","--mac", dest="new_mac", help="New mac address")

    (options, arguments) =  parser.parse_args()             
    if not options.interface:
        #handle error for interface
        parser.error("[-]Please specify an interface, use --help for more info")
    elif not options.new_mac:
        #handle error for new mac
        parser.error("[-]Please specify a new mac address, use --help for more info")
    return options

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read the mac address")







options = get_arguments()
if options != None:



    print("#Your mac address#")
    print("###########")
    print("##########")
    print("#########")
    print("########")
    print("#######")
    print("######")

    subprocess.call(["ifconfig"])
            
            
    print("######")
    print("#######")
    print("########")
    print("#########")
    print("##########")
    print("###########")
    


current_mac = get_current_mac(options.interface)
if current_mac != None:
    change_mac(options.interface,options.new_mac)
if str(current_mac) == options.new_mac:
    print("[+] Current mac address =" + str(current_mac))
else:
    print("[-] Mac address change is unsuccesful")
