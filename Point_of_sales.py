#! /usr/bin/python3

import enquiries
import os
import datetime
import shutil
import sys

from tkinter import *
from my_sqlite3 import *
from keyboard import *
from functools import partial

##########################
#### Global variables ####
##########################
db_name = 'meals.db'
db_path = db_name #will be different if "db" is not in the same directory

###################
#### Functions ####
###################

def purchase(employeeid_option, menu_idOption, confirmOption='n'):
  purchase_id = get_purchase_id()
  current_date = datetime.datetime.now()
  formated_date = current_date.strftime("%d-%m-%Y %H:%M:%S")

  employee_id = get_employee_id(employeeid_option)
  print(employee_id)
  employee_name = get_employee_name(employee_id)
  ticket_data = [purchase_id,formated_date,employee_name]

  db_link = connect_to_db(db_path)
  db_cursor = create_cursor(db_link)
  sql_query = "INSERT INTO purchase(date,employee_id) VALUES (?,?)"
  sql_values = (formated_date,employee_id)
  write_to_cursor(db_cursor,sql_query,sql_values)

  menu_id_list = get_id_list('menu')

  while True:
    menu_id = menu_idOption

    if not menu_id: #TODO if menu_id in menu_id_list:
      break

    os.system('clear')
    menu_id = int(menu_id)
    if menu_id in menu_id_list:
        menu_price = get_menu_price(menu_id) #TODO get_purchase_detail plutôt que get_menu_price?
        sql_query = "INSERT INTO purchase_detail(purchase_id,menu_id,menu_price) VALUES (?,?,?)"
        sql_values = (purchase_id,menu_id,menu_price)
        write_to_cursor(db_cursor,sql_query,sql_values)
        ticket_data.append(sql_values)
    tatat = display_ticket(ticket_data)
    gui_description.config(text='Purchase number :' + str(tatat[0])+'\nDate : '+ str(tatat[1])+ '\nEmployee : ' + str(tatat[2]))
    
    break
  
  confirm = confirmOption
  if ((confirm == 'y') and (len(ticket_data) >= 4)):
    commit_to_db(db_link)
    disconnect_from_db(db_link)
    save_database(db_path)
 
def get_purchase_id():
  db_link = connect_to_db(db_path)
  db_cursor = create_cursor(db_link)
  sql_query = "SELECT MAX(id) FROM purchase"
  query_result = read_from_cursor(db_cursor,sql_query)
  disconnect_from_db(db_link)
  if query_result[0][0] != None:
    last_purchase_id = query_result[0][0]
  else:
    last_purchase_id = 0
  purchase_id = last_purchase_id + 1
  return purchase_id

def get_employee_id(idemployee_option): #TODO idem que get_menu_id()?
  employee_id_list = get_id_list('employee')
  #print(employee_id_list) #[1, 2, 3, 4]
  employee_id = 0
  while employee_id not in employee_id_list:
    os.system('clear')
    employee_id = idemployee_option
    if not employee_id:
      employee_id = 0
    else:
      employee_id = int(employee_id)
  return employee_id

def get_id_list(table_name):
  db_link = connect_to_db(db_path)
  db_cursor = create_cursor(db_link)
  if (table_name == 'employee'): #TODO simlify with ?
    sql_query = "SELECT id FROM employee"
  elif (table_name == 'menu'):
    sql_query = "SELECT id FROM menu"
  query_result = read_from_cursor(db_cursor,sql_query)
  id_list = []
  for id in query_result:
    id_list.append(id[0])
  disconnect_from_db(db_link)
  return id_list

def get_employee_name(employee_id):
  db_link = connect_to_db(db_path)
  db_cursor = create_cursor(db_link)
  sql_query = "SELECT first_name,family_name FROM employee WHERE id=?"
  sql_values = (employee_id,)
  query_result = read_from_cursor(db_cursor,sql_query,sql_values)
  employee_name = query_result[0][0] + ' ' + query_result[0][1]
  disconnect_from_db(db_link)
  return employee_name

def get_menu_price(menu_id):
  db_link = connect_to_db(db_path)
  db_cursor = create_cursor(db_link)
  sql_query = "SELECT price FROM menu WHERE id=?"
  sql_values = (menu_id,)
  query_result = read_from_cursor(db_cursor,sql_query,sql_values)
  menu_price = query_result[0][0]
  disconnect_from_db(db_link)
  return menu_price

def display_ticket(ticket_data):
  purchase_line = 'Purchase number : ' + str(ticket_data[0])
  date_line = 'Date : ' + ticket_data[1]
  employee_line = 'Employee : ' + ticket_data[2] + '\n'

  print(purchase_line)
  print(date_line)
  print(employee_line)

  amount = 0.0
  for index in range(3,len(ticket_data)): #[purchase_id,date,employee,(p_id,menu_id,price)]
    menu_id = ticket_data[index][1]
    description = get_menu_description(menu_id)
    price = ticket_data[index][2]
    detail_string = "Menu: {:<18} {:>6} €"
    detail_line = detail_string.format(description,price)
    print(detail_line)
    amount = amount + price #TODO pourquoi 3.3 * 3 donne 9.89999999?
  amount_line = '\nAmount : ' + str(amount) + ' €'
  print(amount_line)
  print(ticket_data)
  print(type(ticket_data))
  return ticket_data

def get_menu_description(menu_id):
  db_link = connect_to_db(db_path)
  db_cursor = create_cursor(db_link)
  sql_query = "SELECT description FROM menu WHERE id=?"
  sql_values = (menu_id,)
  query_result = read_from_cursor(db_cursor,sql_query,sql_values)
  description = query_result[0][0]
  disconnect_from_db(db_link)
  return description

def save_database(db_name):
  backup_dir = 'backup'
  if not os.path.isdir(backup_dir):
    os.makedirs(backup_dir)
  date = datetime.datetime.now()
  hour = date.strftime("%H")
  source = db_name
  backup = backup_dir + '/' + db_name + '_' + hour
  shutil.copyfile(source, backup)

def add_employee(first_name, family_name, email_address) :

  db_link = connect_to_db(db_path)
  db_cursor = create_cursor(db_link)
  sql_query = "INSERT INTO employee(first_name,family_name,email_address) VALUES (?,?,?)"
  sql_values = (first_name,family_name, email_address)
  write_to_cursor(db_cursor,sql_query,sql_values)
  commit_to_db(db_link)
  disconnect_from_db(db_link)

def modify_employee(employee_id ,new_first_name, new_family_name, new_email_address):
  db_link = connect_to_db(db_path)
  db_cursor = create_cursor(db_link)
  sql_query = "SELECT first_name,family_name,email_address FROM employee WHERE id=?"
  sql_values = (employee_id,)
  query_result = read_from_cursor(db_cursor,sql_query,sql_values) # [('Jack', 'DAVIS', None)]
  first_name = query_result[0][0]
  family_name = query_result[0][1]
  email_address = query_result[0][2]
  db_cursor.close()

  db_cursor = create_cursor(db_link)

  if new_first_name:
    sql_query = "UPDATE employee SET first_name = ? WHERE id=?"
    sql_values = (new_first_name,employee_id)
    write_to_cursor(db_cursor,sql_query,sql_values)

  if new_family_name:
    sql_query = "UPDATE employee SET family_name = ? WHERE id=?"
    sql_values = (new_family_name,employee_id)
    write_to_cursor(db_cursor,sql_query,sql_values)

  if new_email_address:
    sql_query = "UPDATE employee SET email_address = ? WHERE id=?"
    sql_values = (new_email_address,employee_id)
    write_to_cursor(db_cursor,sql_query,sql_values)
    commit_to_db(db_link)
    disconnect_from_db(db_link)

def add_menu(description,price):
  db_link = connect_to_db(db_path)
  db_cursor = create_cursor(db_link)
  sql_query = "INSERT INTO menu(description,price) VALUES (?,?)"
  sql_values = (description,price)
  write_to_cursor(db_cursor,sql_query,sql_values)
  commit_to_db(db_link)
  disconnect_from_db(db_link)


def modify_menu(menu_id, new_description, new_price):

  db_link = connect_to_db(db_path)
  db_cursor = create_cursor(db_link)
  sql_query = "SELECT description,price FROM menu WHERE id=?"
  sql_values = (menu_id,)
  query_result = read_from_cursor(db_cursor,sql_query,sql_values)
  description = query_result[0][0]
  price = query_result[0][1]
  db_cursor.close()

  db_cursor = create_cursor(db_link)

  if new_description:
    sql_query = "UPDATE menu SET description = ? WHERE id=?"
    sql_values = (new_description,menu_id)
    write_to_cursor(db_cursor,sql_query,sql_values)

  if new_price:
    sql_query = "UPDATE menu SET price = ? WHERE id=?"
    sql_values = (new_price,menu_id)
    write_to_cursor(db_cursor,sql_query,sql_values)
    commit_to_db(db_link)
    disconnect_from_db(db_link)

def exit_program():
  sys.exit()

###################
#### Main code ####
###################

# Construction de la fenêtre :

def newWindowAddEmpl():
    newWindowAddEmpl = Toplevel(mainFen)
    newWindowAddEmpl.title('Add User')
    newWindowAddEmpl.geometry('512x200')
    newWindowAddEmpl.resizable(0, 0)

    def ev_bouton_valider_click() :
        confirm = Toplevel(newWindowAddEmpl)
        confirm.title('Confirm ?')
        confirm.geometry('250x150')
        confirm.resizable(0, 0)

        bo = Button(confirm, text = "YES", bg = "#6e6b95",
                         width = 10, height = 2, command = add_employee and closeWindow)
        bo.grid()
        bo.place(x = 100, y = 50)

        bouton_no = Button(confirm, text = "NO", bg = "#b00923",
                            command = closeWindow , width = 10, height = 2)
        bouton_no.grid()
        bouton_no.place(x = 10, y = 50)

        add_employee(firstName.get(), Lastname.get(), eMail.get())

    def closeWindow():
        newWindowAddEmpl.destroy()

    etName = Label(newWindowAddEmpl, text='Enter New User Name : ')
    etName.grid(row = 2, column = 0)
    etName.place (x = 10, y = 10)
    firstName = Entry(newWindowAddEmpl, width=35)
    firstName.grid(row = 2, column = 1)
    firstName.place(x = 200, y = 10)
    firstName.focus_force()

    Lastname = Label(newWindowAddEmpl, text='Enter New User Lastname : ')
    Lastname.grid(row = 3, column = 0)
    Lastname.place (x = 10, y = 50)
    Lastname = Entry(newWindowAddEmpl, width=35)
    Lastname.grid(row = 3, column = 1)
    Lastname.place (x = 200, y = 50)

    etMail = Label(newWindowAddEmpl, text='Enter New User Mail : ')
    etMail.grid(row = 4, column = 0)
    etMail.place (x = 10, y = 90)
    eMail = Entry(newWindowAddEmpl, width=35)
    eMail.grid(row = 4, column = 1)
    eMail.place (x = 200, y = 90)

    bouton_validé = Button(newWindowAddEmpl, text = "Confirm", bg = "#6e6b95",
                            width = 10, height = 2, command = ev_bouton_validé_click)
    bouton_validé.grid()
    bouton_validé.place(x = 390, y = 150)

    bouton_cancel = Button(newWindowAddEmpl, text = "Cancel", bg = "#b00923",
                        command = closeWindow , width = 10, height = 2)
    bouton_cancel.grid()
    bouton_cancel.place(x = 10, y = 150)

    bouton_clavier = Button(newWindowAddEmpl, text = 'keyboard', command = clavier_numerique, bg = "#70f050",
              fg = "black", height = 2, width = 24)
    bouton_clavier.grid()
    bouton_clavier.place(x = 150, y = 150)

def newWindowModEmpl():
    newWindowModEmpl = Toplevel(mainFen)
    newWindowModEmpl.title('Modify User')
    newWindowModEmpl.geometry('512x250')
    newWindowModEmpl.resizable(0, 0)

    def ev_bouton_valider_click() :
        confirm = Toplevel(newWindowModEmpl)
        confirm.title('Confirm ?')
        confirm.geometry('250x150')
        confirm.resizable(0, 0)

        bo = Button(confirm, text = "YES", bg = "#6e6b95",
                         width = 10, height = 2, command = modify_employee and closeWindow)
        bo.grid()
        bo.place(x = 100, y = 50)

        bouton_no = Button(confirm, text = "NO", bg = "#b00923",
                            command = closeWindow , width = 10, height = 2)
        bouton_no.grid()
        bouton_no.place(x = 10, y = 50)

        modify_employee(EmplID.get(), firstName.get(), Lastname.get(), eMail.get())

    def closeWindow():
        newWindowModEmpl.destroy()

    etEmployeeID = Label(newWindowModEmpl, text='Enter Employee ID : ')
    etEmployeeID.grid(row = 2, column = 0)
    etEmployeeID.place (x = 10, y = 10)
    EmployeeID = Entry(newWindowModEmpl, width=35)
    EmployeeID.grid(row = 2, column = 1)
    EmployeeID.place(x = 200, y = 10)
    EmployeeID.focus_force()

    etName = Label(newWindowModEmpl, text='Enter New User Name : ')
    etName.grid(row = 2, column = 0)
    etName.place (x = 10, y = 50)
    firstName = Entry(newWindowModEmpl, width=35)
    firstName.grid(row = 2, column = 1)
    firstName.place(x = 200, y = 50)

    Lastname = Label(newWindowModEmpl, text='Enter New User Lastname : ')
    Lastname.grid(row = 3, column = 0)
    Lastname.place (x = 10, y = 90)
    Lastname = Entry(newWindowModEmpl, width=35)
    Lastname.grid(row = 3, column = 1)
    Lastname.place (x = 200, y = 90)

    etMail = Label(newWindowModEmpl, text='Enter New User Mail : ')
    etMail.grid(row = 4, column = 0)
    etMail.place (x = 10, y = 130)
    eMail = Entry(newWindowModEmpl, width=35)
    eMail.grid(row = 4, column = 1)
    eMail.place (x = 200, y = 130)

    bouton_valider = Button(newWindowModEmpl, text = "Confirm", bg = "#6e6b95",
                            width = 10, height = 2, command = ev_bouton_valider_click)
    bouton_valider.grid()
    bouton_valider.place(x = 390, y = 200)

    bouton_cancel = Button(newWindowModEmpl, text = "Cancel", bg = "#b00923",
                        command = closeWindow , width = 10, height = 2)
    bouton_cancel.grid()
    bouton_cancel.place(x = 10, y = 200)

    bouton_clavier = Button(newWindowModEmpl, text = 'keyboard', command = clavier_numerique, bg = "#70f050",
              fg = "black", height = 2, width = 24)
    bouton_clavier.grid()
    bouton_clavier.place(x = 150, y = 200)


def newWindowAddMenu():
    newWindowAddMenu = Toplevel(mainFen)
    newWindowAddMenu.title('Add Menu')
    newWindowAddMenu.geometry('512x200')
    newWindowAddMenu.resizable(0, 0)

    def ev_bouton_valider_click() :
        confirm = Toplevel(newWindowAddMenu)
        confirm.title('Confirm ?')
        confirm.geometry('250x150')
        confirm.resizable(0, 0)

        bouton_OUI = Button(confirm, text = "YES", bg = "#6e6b95",
                         width = 10, height = 2, command = add_menu and closeWindow)
        bouton_OUI.grid()
        bouton_OUI.place(x = 100, y = 50)

        bouton_NON = Button(confirm, text = "NO", bg = "#b00923",
                            command = closeWindow , width = 10, height = 2)
        bouton_NON.grid()
        bouton_NON.place(x = 10, y = 50)

        add_menu(description.get(), price.get())

    def closeWindow():
        newWindowAddMenu.destroy()

    etDescr = Label(newWindowAddMenu, text='Enter Description : ')
    etDescr.grid(row = 2, column = 0)
    etDescr.place (x = 10, y = 10)
    description = Entry(newWindowAddMenu, width=35)
    description.grid(row = 2, column = 1)
    description.place(x = 200, y = 10)
    description.focus_force()

    etPrice = Label(newWindowAddMenu, text='Enter price : ')
    etPrice.grid(row = 3, column = 0)
    etPrice.place (x = 10, y = 50)
    price = Entry(newWindowAddMenu, width=35)
    price.grid(row = 3, column = 1)
    price.place (x = 200, y = 50)

    bouton_valider = Button(newWindowAddMenu, text = "Confirm", bg = "#6e6b95",
                            width = 10, height = 2, command = ev_bouton_valider_click)
    bouton_valider.grid()
    bouton_valider.place(x = 390, y = 150)

    bouton_cancel = Button(newWindowAddMenu, text = "Cancel", bg = "#b00923",
                        command = closeWindow , width = 10, height = 2)
    bouton_cancel.grid()
    bouton_cancel.place(x = 10, y = 150)

    bouton_clavier = Button(newWindowAddMenu, text = 'keyboard', command = clavier_numerique, bg = "#70f050",
              fg = "black", height = 2, width = 24)
    bouton_clavier.grid()
    bouton_clavier.place(x = 150, y = 150)

def newWindowModMenu():
    newWindowModMenu = Toplevel(mainFen)
    newWindowModMenu.title('Modify Menu')
    newWindowModMenu.geometry('512x200')
    newWindowModMenu.resizable(0, 0)

    def ev_bouton_valider_click() :
        confirm = Toplevel(newWindowModMenu)
        confirm.title('Confirm ?')
        confirm.geometry('250x150')
        confirm.resizable(0, 0)

        bouton_OUI = Button(confirm, text = "YES", bg = "#6e6b95",
                         width = 10, height = 2, command = modify_menu and closeWindow)
        bouton_OUI.grid()
        bouton_OUI.place(x = 100, y = 50)

        bouton_NON = Button(confirm, text = "NO", bg = "#b00923",
                            command = closeWindow , width = 10, height = 2)
        bouton_NON.grid()
        bouton_NON.place(x = 10, y = 50)

        modify_menu(MenuID.get(), description.get(), price.get())

    def closeWindow():
        newWindowModMenu.destroy()

    etMenuID = Label(newWindowModMenu, text='Enter Menu ID : ')
    etMenuID.grid(row = 2, column = 0)
    etMenuID.place (x = 10, y = 10)
    MenuID = Entry(newWindowModMenu, width=35)
    MenuID.grid(row = 2, column = 1)
    MenuID.place(x = 200, y = 10)
    MenuID.focus_force()

    etDescr = Label(newWindowModMenu, text='Enter Description : ')
    etDescr.grid(row = 2, column = 0)
    etDescr.place (x = 10, y = 50)
    description = Entry(newWindowModMenu, width=35)
    description.grid(row = 2, column = 1)
    description.place(x = 200, y = 50)
    description.focus_force()

    etPrice = Label(newWindowModMenu, text='Enter price : ')
    etPrice.grid(row = 3, column = 0)
    etPrice.place (x = 10, y = 90)
    price = Entry(newWindowModMenu, width=35)
    price.grid(row = 3, column = 1)
    price.place (x = 200, y = 90)

    bouton_valider = Button(newWindowModMenu, text = "Confirm", bg = "#6e6b95",
                            width = 10, height = 2, command = ev_bouton_valider_click)
    bouton_valider.grid()
    bouton_valider.place(x = 390, y = 150)

    bouton_cancel = Button(newWindowModMenu, text = "Cancel", bg = "#b00923",
                        command = closeWindow , width = 10, height = 2)
    bouton_cancel.grid()
    bouton_cancel.place(x = 10, y = 150)

    bouton_clavier = Button(newWindowModMenu, text = 'keyboard', command = clavier_numerique, bg = "#70f050",
              fg = "black", height = 2, width = 24)
    bouton_clavier.grid()
    bouton_clavier.place(x = 150, y = 150)

mytext = 'ratatatatata' 

mainFen = Tk()
mainFen.title('Point of sale')
mainFen.geometry('1024x768')
mainFen.resizable(0, 0)

mainCan = Canvas(mainFen, bg ="#8a203d", width = 1024, height = 768)


gui_description = Label(mainFen, text = "", width = 83, height = 37, bg ="#8a203d", anchor = "nw", )
gui_description.grid()
gui_description.place(x= 10, y= 120)

testpurchase = partial(purchase, 1,2)

bouton_test = Button(mainFen, text = "test", command = testpurchase , bg = "#70f050",
          fg = "black", height = 3, width = 35)
bouton_test.grid()
bouton_test.place(x = 700, y = 575)

bouton_add_employee = Button(mainCan, text='Add User', command = newWindowAddEmpl, bg = "#6e6b95",
          height = 5, width = 27)
bouton_add_employee.grid(row = 2, column = 2)

bouton_modif_employee = Button(mainCan, text='Modify User', command = newWindowModEmpl, bg = "#6e6b95",
          height = 5, width = 27)
bouton_modif_employee.grid(row = 2, column = 4)

bouton_add_menu = Button(mainCan, text='Add Menu', command = newWindowAddMenu, bg = "#6e6b95",
          height = 5, width = 27)
bouton_add_menu.grid(row = 2, column = 6)

bouton_modif_menu = Button(mainCan, text='Modify Menu', command = newWindowModMenu, bg = "#6e6b95",
          height = 5, width = 27)
bouton_modif_menu.grid(row = 2, column = 8)

bouton_cancel = Button(mainFen, text = 'CANCEL', command = None, bg = "#b00923",
          height = 5, width = 15)
bouton_cancel.grid()
bouton_cancel.place(x = 700, y = 655)



bouton_enter = Button(mainFen, text = 'ENTER', command = "<Enter>", bg = "#6e6b95",
          height = 5, width = 15)
bouton_enter.grid()
bouton_enter.place(x = 864, y = 655)

bouton_1 = Button(mainFen, text = '1', command = "<1>", bg = "#aca296", fg = "#b00923",
          height = 5, width = 8)
bouton_1.grid()
bouton_1.place(x = 700, y = 140)

bouton2 = Button(mainFen, text = '2', command = "<2>", bg = "#aca296", fg = "#b00923",
          height = 5, width = 8)
bouton2.grid()
bouton2.place(x = 800, y = 140)

bouton3 = Button(mainFen, text = '3', command = "<3>", bg = "#aca296", fg = "#b00923",
          height = 5, width = 8)
bouton3.grid()
bouton3.place(x = 900, y = 140)

bouton4 = Button(mainFen, text = '4', command = "<4>", bg = "#aca296", fg = "#b00923",
          height = 5, width = 8)
bouton4.grid()
bouton4.place(x =700 , y = 250)

bouton5 = Button(mainFen, text = '5', command = "<5>", bg = "#aca296", fg = "#b00923",
          height = 5, width = 8)
bouton5.grid()
bouton5.place(x = 800, y = 250)

bouton6 = Button(mainFen, text = '6', command = "<6>", bg = "#aca296", fg = "#b00923",
          height = 5, width = 8)
bouton6.grid()
bouton6.place(x = 900, y = 250)

bouton7 = Button(mainFen, text = '7', command = "<7>", bg = "#aca296", fg = "#b00923",
          height = 5, width = 8)
bouton7.grid()
bouton7.place(x = 700, y = 360 )

bouton8 = Button(mainFen, text = '8', command = "<8>", bg = "#aca296", fg = "#b00923",
          height = 5, width = 8)
bouton8.grid()
bouton8.place(x = 800, y = 360)

bouton9 = Button(mainFen, text = '9', command = "<9>", bg = "#aca296", fg = "#b00923",
          height = 5, width = 8)
bouton9.grid()
bouton9.place(x = 900, y = 360)

bouton0 = Button(mainFen, text = '0', command = "<0>", bg = "#aca296", fg = "#b00923",
          height = 5, width = 20)
bouton0.grid()
bouton0.place(x = 700, y = 470)

bouton_point = Button(mainFen, text = '.', command = "<.>", bg = "#aca296", fg = "#b00923",
          height = 5, width = 8)
bouton_point.grid()
bouton_point.place(x = 900, y = 470)



mainCan.grid(row =1, column =3, padx =10, pady =10)


mainFen.mainloop()
