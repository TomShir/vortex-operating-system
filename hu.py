from colorama import Fore 
import time 
import os 
import sys 
import logging 
import tqdm 
from readchar import readkey,key
import random
colors=[Fore.LIGHTBLUE_EX,Fore.RED,Fore.GREEN,Fore.RESET,Fore.BLUE,Fore.CYAN,Fore.MAGENTA,Fore.YELLOW,Fore.LIGHTRED_EX]
extension_of_files=['cpp','py','txt','mp3','log','java','rust','lua','kotlin','json','cs','c','css','html']
bar=tqdm.tqdm(range(100),ncols=100,colour='Green')
commands=['sudo.hack','sudo.create_file','sudo.exit','sudo.tic_tac_toe','sudo.counter','sudo.read_file']
my_logger=logging.getLogger('operating_system_logger')
my_logger.setLevel(logging.ERROR)
file_handler=logging.FileHandler('user.log')
format=logging.Formatter('%(asctime)s-%(name)s-%(message)s')
file_handler.setFormatter(format)
my_logger.addHandler(file_handler)
def loop_over(text_color,iterable_container,delay_time):
  for text in iterable_container:
    sys.stdout.flush()
    time.sleep(delay_time)
    sys.stdout.write(f'{text_color}{text}')
  else:
    pass
def error_msg(error_text):
  loop_over(text_color=colors[1],iterable_container=error_text,delay_time=0.1)
  my_logger.error(f'{error_text}')
os_title='''
          ___ __              ___ __   ______________  _______________   ___________ ___    ____________  _______          ________
          \  \  \            /  /  /  /          /  / / /        / / /  |___________|___| / \___________\ \  \    \       /    /  /
           \  \  \          /  /  /  /          /  / / /        / / /      |    |  |     /  /  /________/  \  \    \     /    /  /
            \  \  \        /  /  /  /          /  / / /________/ / /       |    |  |    /  /  /_________    \  \    \   /    /  /
             \  \  \______/  /  /  /          /  / / /_________\ \ \       |    |  |   /  /  /_________/     \  \    \ /    /  /
              \__\_______/__/__/  /          /  / / / _________ \ \ \      |    |  |  /  /  /_________        \  \___/_\__/\  \\
               \_\_______/__/_/  /_________ /__/ /_/_/           \ \_\     |____|__| /__/__/_________/        /__/___/  \__ \__\\
              _____________________________________________________________________________________________________________________\n\t
              '''
for num in bar:
  time.sleep(0.01)
  pass 
else:
  time.sleep(1)
  print('\tOperating system loaded...')
  time.sleep(1)
  print('Welcome to....\n\t')
  loop_over(text_color=colors[0],iterable_container=os_title,delay_time=0.0001)
  os.system("cls")
  print(f'{colors[2]}')
  username=input('username:')
  time.sleep(1)
  os.system("cls")
  print(f'{colors[5]}Date:{colors[-3]}{time.asctime()}\n{colors[1]}Current Python version:{colors[-2]}{sys.version[0:6]}')
  time.sleep(1)
  loop_over(text_color=colors[2],iterable_container='Type in help to see all commands\n',delay_time=0.001)
  time.sleep(1)
  while True:
    try:
     print(f'{colors[3]}')
     time.sleep(0.1)
     command=input(f'{colors[2]}vortex/{colors[5]}{username}/{colors[3]}runner{colors[-2]}>')
     if 'vortex//runner>'==command:
      error_msg(error_text='usernameError:No username specified') 
     elif command=='help':
      time.sleep(1)
      print(colors[3]+'commands:\n\t')
      for command in commands:
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write(f'{colors[2]}{command}\n')
      else:
        pass
     elif command==commands[0]:
      enter_button=key.ENTER 
      open_text_file=open('hack.txt','r')
      readlines=open_text_file.readlines()
      loop_over(text_color=colors[2],iterable_container=readlines,delay_time=0.00001)
     elif command==commands[1]:
      file_name=input('filename:')
      dot='.'
      #Checking the extension of the file
      if dot in file_name:
        file_extension=file_name[file_name.index(dot)+1:]
        if file_extension in extension_of_files:
          filename=f'{file_name[0:file_name.index(dot)+1]+file_name[file_name.index(dot)+1:]}'
          with open(filename,'w') as a:
            pass
     elif command==commands[2]:
      print('\n')
      loop_over(text_color=colors[1],iterable_container='Exitting Vortex operating system...',delay_time=0.1)
      time.sleep(0.1)
      os.system("cls")
      sys.exit(f'{colors[3]}')
     elif command==commands[3]:
        title='tic tac toe'
        x='x'.upper()
        o='o'.upper()
        for text in title:
         sys.stdout.flush()
         time.sleep(0.1)
         sys.stdout.write(f'\t{random.choice(colors)}{text.upper()}')
        else:
         print(f'{colors[3]}')
         time.sleep(0.2)
         print('Creating the board....\n')
         time.sleep(0.2)
         def create_board():
            global game_board
            global join_game_board
            game_board=['-','-','-','\n-','-','-','\n-','-','-']
            join_game_board=" ".join(game_board)
            print(f'{join_game_board}')
        
         create_board()
                
        def win_condition(player_1_symbol,player_2_symbol):
          player_1_won_msg='PLayer 1 won!'
          player_2_won_msg='Player 2 won!'
          tie_msg='Its a tie, nobody wins' 
          if game_board[0]==player_1_symbol and game_board[1]==player_1_symbol and game_board[2]==player_1_symbol:
            sys.exit(f'{player_1_won_msg}')
          elif game_board[0]==player_2_symbol and game_board[1]==player_2_symbol and game_board[2]==player_2_symbol:
            sys.exit(f'{player_2_won_msg}')
          elif game_board[3]==f'\n{player_1_symbol}' and game_board[4]==player_1_symbol and game_board[5]==player_1_symbol:
            sys.exit(f'{player_1_won_msg}')
          elif game_board[3]==f'\n{player_2_symbol}' and game_board[4]==player_2_symbol and game_board[5]==player_2_symbol:
            sys.exit(f'{player_2_won_msg}')
          elif game_board[6]==f'\n{player_1_symbol}' and game_board[7]==player_1_symbol and game_board[8]==player_1_symbol:
            sys.exit(f'{player_1_won_msg}')
          elif game_board[6]==f'\n{player_2_symbol}' and game_board[7]==player_2_symbol and game_board[8]==player_2_symbol:
            sys.exit(f'{player_2_won_msg}')
          elif game_board[0]==player_1_symbol and game_board[3]==f'\n{player_1_symbol}' and game_board[6]==f'\n{player_1_symbol}':
            sys.exit(f'{player_1_won_msg}')
          elif game_board[0]==player_2_symbol and game_board[3]==f'\n{player_2_symbol}' and game_board[6]==f'\n{player_2_symbol}':
            sys.exit(f'{player_2_won_msg}')
          elif game_board[1]==player_1_symbol and game_board[4]==player_1_symbol and game_board[7]==player_1_symbol:
            sys.exit(f'{player_1_won_msg}')
          elif game_board[1]==player_2_symbol and game_board[4]==player_2_symbol and game_board[7]==player_2_symbol:
            sys.exit(f'{player_2_won_msg}')
          elif game_board[2]==player_1_symbol and game_board[5]==player_1_symbol and game_board[8]==player_1_symbol:
            sys.exit(f'{player_1_won_msg}')
          elif game_board[2]==player_2_symbol and game_board[5]==player_2_symbol and game_board[8]==player_2_symbol:
            sys.exit(f'{player_2_won_msg}')
          elif game_board[0]==player_1_symbol and game_board[4]==player_1_symbol and game_board[8]==player_1_symbol:
            sys.exit(f'{player_1_won_msg}')
          elif game_board[0]==player_2_symbol and game_board[4]==player_2_symbol and game_board[8]==player_2_symbol:
            sys.exit(f'{player_2_won_msg}') 
          elif game_board[2]==player_1_symbol and game_board[4]==player_1_symbol and game_board[6]==f'\n{player_1_symbol}':
            sys.exit(f'{player_1_won_msg}')
          elif game_board[2]==player_2_symbol and game_board[4]==player_2_symbol and game_board[6]==f'\n{player_2_symbol}':
            sys.exit(f'{player_2_won_msg}')
          else:
            print(f'{tie_msg}')
        player_1_name=input('Player 1 name:')
        time.sleep(1)
        player_2_name=input('Player 2 name:')
        time.sleep(1)
        symbol=input(f'What symbol do you want to be, {player_1_name}, {o} or {x}:')
        if symbol==x or symbol==x.lower() or symbol==o or symbol==o.lower():
            time.sleep(1)
            print(f'{player_1_name} chose {symbol}')
            if symbol==x or symbol==x.lower():
                time.sleep(1)
                print(f'Since {player_1_name} chose {symbol}, {player_2_name} will be {o}')
                opponent_symbol=o
            elif symbol==o or symbol==o.lower():
                time.sleep(1)
                print(f'Since {player_1_name} chose {symbol}, {player_2_name} will be {x} ')
                opponent_symbol=x
            def choose_position(player_1,player_2):
                if player_1:
                    player_1_turn=f'It is now {player_1_name}"s turn'
                    print(f'{player_1_turn}')
                    time.sleep(1)
                    position=int(input('Enter a number between 0 and 8: '))
                    if position>8 or position<0:
                        error_msg('Error, invalid index, pls restart the game')
                    elif position==3 or position==6:
                        del game_board[position] 
                        game_board.insert(position,f'\n{symbol}')
                        print(f'{" ".join(game_board)}')
                    else:
                        del game_board[position]
                        game_board.insert(position,symbol)
                        print(f'{" ".join(game_board)}')
                elif player_2:
                    print(f'It"s now {player_2_name}"s turn')
                    time.sleep(1)
                    position=int(input('Enter a number between 0 and 8:'))
                    if position>8 or position<0:
                        error_msg('Error, invalid index, pls restart the game')
                    elif position==3 or position==6:
                        del game_board[position]
                        game_board.insert(position,f'\n{opponent_symbol}')
                        print(f'{" ".join(game_board)}')
                    else:
                        del game_board[position]
                        game_board.insert(position,f'{opponent_symbol}')
                        print(f'{" ".join(game_board)}')
                        
            choose_position(player_1=player_1_name,player_2=player_2_name)
            if opponent_symbol not in game_board[:]:
                choose_position(player_1=None,player_2=player_2_name)
                choose_position(player_1=player_1_name,player_2=None)
                choose_position(player_1=None,player_2=player_2_name)
                choose_position(player_1=player_1_name,player_2=None)
                win_condition(player_1_symbol=symbol,player_2_symbol=opponent_symbol)
                choose_position(player_1=None,player_2=player_2_name)
                win_condition(player_1_symbol=symbol,player_2_symbol=opponent_symbol)
                choose_position(player_1=player_1_name,player_2=None)
                choose_position(player_1=None,player_2=player_2_name)
        else:
            error_msg(txt='Error, invalid symbol, pls restart the game')
     elif command==commands[4]:
       count=0
       number=int(input('Enter the number you "d like to count up to:'))
       while count<number:
         count+=1 
         time.sleep(0.00001)
         print(f'{colors[5]}{count}',end='\r')
       else:
         pass
     elif command==commands[-1]:
       select_file_name=input('filename:')
       open_file=open(select_file_name,'r')
       all_content=open_file.readlines()
       print(f'All content being read from file {select_file_name}:\n\t')
       loop_over(text_color=colors[3],iterable_container=all_content,delay_time=0.01)
     elif command not in commands or command!='help':
       error_msg(error_text=f"CommandError:'{command}' is not recognized as an internal or external command,operable program or batch file.")
    except FileNotFoundError:
      error_msg(f'FileNotFoundError:File {select_file_name} does not exist')
    except ValueError:
      pass 
    except IndexError:
     pass