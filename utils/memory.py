from pymem import Pymem
from pymem.process import module_from_name

def update_client(process, value):
    try:
        mem = Pymem("dota2.exe")
        game_module = module_from_name(mem.process_handle, "client.dll").lpBaseOfDll
        mem.write_float(game_module + int(process, 16), float(value))
        return "Successful"
    except Exception as e:
        return f"Error: {e}"

def read_client(process):
    try:
        mem = Pymem("dota2.exe")
        game_module = module_from_name(mem.process_handle, "client.dll").lpBaseOfDll
        return mem.read_float(game_module + int(process, 16))
    except:
        return None
