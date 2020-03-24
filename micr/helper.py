from pip._vendor.colorama import init, Fore

init(autoreset=False)

def display(info, is_warning = False):
  if is_warning:
    print(Fore.RED + 'this is a warning')
  else:
    print(Fore.BLUE + info)