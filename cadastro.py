from PySimpleGUI import PySimpleGUI as sg  # layout
sg.theme('BluePurple')
layout = [
    [sg.Text('Usuário'),sg.Input(key='usuario', size=(20,1))],
    [sg.Text('Senha'),sg.Input(key='senha',password_char='*')],
    [sg.Checkbox('Salvar o Login')],
    [sg.Button('Entrar')]


]
 #janela
janela = sg.Window('Tela de Login',layout)
print('aberto')
 #Ler enventos
while True:
      print('loop')
      eventos,valores = janela.read()
      if eventos == sg.WINDOW_CLOSED:
          print('fechado')
          break
      if eventos == 'Entrar':
           if valores ['usuario'] == 'fernando' and valores ['senha'] == 'add':
               print('Acesso Liberado!')














