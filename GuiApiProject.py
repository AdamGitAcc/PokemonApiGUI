from variables import *
import requests
import SearchByName
import SearchByType
import SearchByAbilities


def main():
    root.title('My first gui')

    root.geometry(f'{window_width}x{window_height}+{center_width}+{center_height}')

    root.maxsize(window_max_width, window_max_height)

    paint()

    root.mainloop() # to start the gui 

def paint():
    title = tk.Label(root,font=('Times New Roman', 40),text = "PokemonSearchDatabase")
    title.pack(pady=20)
    
    # Frame to have the combobox and the label on the same line
    row_frame = tk.Frame(root)
    row_frame.pack(pady=20)

    #combobox at the left
    temp_label = tk.Label(row_frame, height='2', font=('Times New Roman', 30), text="What would you like to search")
    temp_label.pack(side='left',pady=20)

    options = ['Name','Type','Abilities']
    combo = ttk.Combobox(row_frame, values=options,font=('Times New Roman', 15),width=15,state='readonly')
    combo.set('Search by:')
    combo.pack(side='left', padx=30, pady=10)

    def my_value():
        global value_combobox
        value_combobox = combo.get()
        if value_combobox != 'Search by:':
            combo.destroy()
            temp_label.destroy()
            btn.destroy()
            title.destroy()
            what_next()
            row_frame.destroy()

    btn = tk.Button(root, text="Get Value",command=my_value)
    btn.pack() 

def what_next():
    if value_combobox == 'Name':
        question_label = tk.Label(root,text='Name of your desired pokemon',font=('Times New Roman', 15), height=2)
        question_label.pack(pady=20)
        input_label = tk.Text(root, height=1, width=40)
        input_label.pack(pady=20)
        
        def my_value(event = None):
            Pokemon_Name = input_label.get("1.0", "end-1c")
            question_label.destroy()
            input_label.destroy()
            btn.destroy()
            data = SearchByName.name_search(Pokemon_Name)
            write_result(data)

            
        input_label.bind('<Return>', my_value)

        btn = tk.Button(root, text="Search",command=my_value)
        btn.pack(pady=40)

        
    elif value_combobox == 'Type':
        question_label = tk.Label(root,text='Type you would like to search',font=('Times New Roman', 15), height=2)
        question_label.pack(pady=20)
        input_label = tk.Text(root, height=1, width=40)
        input_label.pack(pady=20)
        
        def my_value(event = None):
            Pokemon_Type = input_label.get("1.0", "end-1c")
            question_label.destroy()
            input_label.destroy()
            btn.destroy()
            data = SearchByType.type_search(Pokemon_Type)
            write_result(data)
            

            
        input_label.bind('<Return>', my_value)

        btn = tk.Button(root, text="Search",command=my_value)
        btn.pack(pady=40)

    else:
        question_label = tk.Label(root,text='Name of your desired ability',font=('Times New Roman', 15), height=2)
        question_label.pack(pady=20)
        input_label = tk.Text(root, height=1, width=40)
        input_label.pack(pady=20)
        
        def my_value(event = None):
            Pokemon_Ability = input_label.get("1.0", "end-1c")
            question_label.destroy()
            input_label.destroy()
            btn.destroy()
            data = SearchByAbilities.ability_search(Pokemon_Ability)
            write_result(data)

            
        input_label.bind('<Return>', my_value)

        btn = tk.Button(root, text="Search",command=my_value)
        btn.pack(pady=40)

def write_result(data):
    result = tk.Label(root, text='\n'.join(data),font=('Times New Roman', 30))
    result.pack(pady=100)
        

if __name__ == '__main__':
    main()