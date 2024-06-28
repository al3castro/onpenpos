
class Treeview():
    columns = ("ID", "COD", "Nombre", "Unidades", "Precio", "Total")
        self.tree = ttk.Treeview(self, columns=columns)

        for i in range(len(columns)):
            self.tree.heading(f'#{i}', text=f'{columns[i]}')
            self.tree.column(f'#{i}', minwidth=0, width=100, stretch=tk.NO)

        self.tree.place(x=width-250, y=height*0.1, height=700, width=600)