from tkinter import * 
import customtkinter as ctk



class VentanaProductos():

    frameColumns1Products: ctk.CTkFrame
    frameColumns2Products: ctk.CTkFrame
    frameColumns3Products: ctk.CTkFrame
    frameColumns4Products: ctk.CTkFrame
    frameColumns5Products: ctk.CTkFrame
    frameColumns6Products: ctk.CTkFrame    

    frameAddProdcuto: ctk.CTkFrame
    

    def CreatePage(self, root:Tk):

        self.frameProductos=ctk.CTkFrame(
            root, 
            width=1000, 
            height=500, 
            corner_radius=20,
            fg_color="white"
            )

        self.ventanaFeutures(self.frameProductos)
    

    def ventanaFeutures(self, frame: ctk.CTkFrame):        

        frame.pack(padx=10, pady=10)

        frame.pack_propagate(False)


        self.HeadPageInfoGenerica(frame)
        self.FrameMenu(frame)
        self.FrameTableProucts(frame)        




    def HeadPageInfoGenerica(self, frameProdcutos:ctk.CTkFrame):

        frameHeade=ctk.CTkFrame(frameProdcutos, 
                                width=1000,
                                height=70,
                                fg_color="white"                               
                                )
        
        frameHeade.pack(pady=15, padx=5)

        frameHeade.pack_propagate(False)

        self.BoxInfo(frameHeade)

    def BoxInfo(self, frameHeade: ctk.CTkFrame):

        #----------------------TotalProducto-----------------------------

        frameBoxInfoTotalProdcuto=ctk.CTkLabel(frameHeade, 
                                width=150, 
                                height=70,
                                border_color="red",
                                border_width=1,
                                fg_color="white",
                                text="Total Productos",
                                text_color="black",
                                corner_radius=10
                                )
        frameBoxInfoTotalProdcuto.grid(row=1, column=1, padx=5, pady=5)
        frameBoxInfoTotalProdcuto.pack_propagate(False)

        #----------------------Low Stock-----------------------------

        frameBoxInfoLowStock=ctk.CTkLabel(frameHeade, 
                                width=150, 
                                height=70,
                                border_color="red",
                                border_width=1,
                                text="Low Stock", 
                                text_color="black",
                                fg_color="white",
                                corner_radius=10
                                )
        frameBoxInfoLowStock.grid(row=1, column=2, padx=5, pady=5)
        frameBoxInfoLowStock.pack_propagate(False)

        #----------------------Out of Stock-----------------------------

        frameBoxInfoOutStock=ctk.CTkLabel(frameHeade, 
                                width=150, 
                                height=70,
                                border_color="red",
                                border_width=1, 
                                fg_color="white",
                                text="Out of stock", 
                                text_color="black",
                                corner_radius=10
                                )
        frameBoxInfoOutStock.grid(row=1, column=3, padx=5, pady=5)
        frameBoxInfoOutStock.pack_propagate(False)
    
        #----------------------Categories-----------------------------

        frameBoxInfoCategories=ctk.CTkLabel(frameHeade, 
                                width=150, 
                                height=70,
                                border_color="red",
                                border_width=1,                                
                                fg_color="white",
                                text="Categories", 
                                text_color="black",
                                corner_radius=10
                                )
        frameBoxInfoCategories.grid(row=1, column=4, padx=5, pady=5)
        frameBoxInfoCategories.pack_propagate(False)

    def FrameMenu(self, frameProdcutos):

        frameMenu=ctk.CTkFrame(frameProdcutos,
                                width=717,
                                height=30,                                
                                corner_radius=20,  
                                fg_color="white" 
                               )
        
        ButtonAddProduct=ctk.CTkButton(frameMenu,
                                 width=50,
                                 height=30, 
                                 border_color="gray",
                                 border_width=1,
                                 corner_radius=20,  
                                 fg_color="white", 
                                 text="+ Add product",
                                 command=lambda: self.FrameAddProdcuto(frameProdcutos)                                            
                                 )
                
        ButtonAddProduct.grid(row=1, column=1, padx=5)
        
        ButtonSearch=ctk.CTkButton(frameMenu,
                                 width=50,
                                 height=30, 
                                 border_color="gray",
                                 border_width=1,
                                 corner_radius=20,  
                                 fg_color="white", 
                                 text="Search"                                                           
                                 )
        
        
        ButtonSearch.grid(row=1, column=2, padx=5)

        frameMenu.grid_propagate(False)
        frameMenu.pack(pady=5)


    def FrameAddProdcuto(self, frameProdcutos: ctk.CTkFrame):

        if self.frameAddProdcuto is not None:

            self.frameAddProdcuto.destroy()
        

        self.frameAddProdcuto=ctk.CTkFrame(frameProdcutos,
                                width=717,
                                height=30,                                
                                corner_radius=20,  
                                fg_color="white" 
                               )

        label=ctk.CTkLabel(self.frameAddProdcuto,
                            width=50,
                            height=30, 
                            border_color="gray",
                            border_width=1,
                            corner_radius=20,  
                            fg_color="white", 
                            text="Search"
                           )
        label.pack()
        
        self.frameAddProdcuto.grid_propagate(False)
        self.frameAddProdcuto.pack(pady=5)



    def FrameTableProucts(self, frameProdcutos:ctk.CTkFrame):        
        
        frameTableProductos=ctk.CTkFrame(frameProdcutos,
                                         width=717,
                                         height=70,
                                         border_color="gray",
                                         border_width=1,
                                         corner_radius=20,  
                                         fg_color="white"                                                                                                                    
                                         )
                                         
        
        frameTableProductos.pack_propagate(False)
        frameTableProductos.pack(padx=5)        

        self.ColumnsProducts(frameTableProductos)
        self.HeadTableProducts()

        NumProducts=2

        for product in range(0,3):
            
            if(product<=NumProducts):
                self.rowsProducts(product+2)


    def ColumnsProducts(self, frameTableProductos:ctk.CTkFrame):

        #--------------Column 1

        self.frameColumns1Products=ctk.CTkFrame(frameTableProductos,                                                                                                                        
                                         height=70,                                         
                                         corner_radius=20,  
                                         fg_color="white"                                                                                                                       
                                         )
        

        
        self.frameColumns1Products.pack_propagate(False)
        self.frameColumns1Products.grid(padx=5, row=1, column=1)        

        #--------------Column 2

        self.frameColumns2Products=ctk.CTkFrame(frameTableProductos,                                                                                                                         
                                         height=70,                                         
                                         corner_radius=20,  
                                         fg_color="white"                                                                                                                       
                                         )
        

        
        self.frameColumns2Products.pack_propagate(False)
        self.frameColumns2Products.grid(padx=5, row=1, column=2) 

        #--------------Column 3

        self.frameColumns3Products=ctk.CTkFrame(frameTableProductos,                                                                                                                          
                                         height=70,                                         
                                         corner_radius=20,  
                                         fg_color="white"                                                                                                                       
                                         )
        

        
        self.frameColumns3Products.pack_propagate(False)
        self.frameColumns3Products.grid(padx=5, row=1, column=3)

        #--------------Column 4

        self.frameColumns4Products=ctk.CTkFrame(frameTableProductos,                                                                                                                         
                                         height=70,                                         
                                         corner_radius=20,  
                                         fg_color="white"                                                                                                                       
                                         )
        

        
        self.frameColumns4Products.pack_propagate(False)
        self.frameColumns4Products.grid(padx=5, row=1, column=4)

        #--------------Column 5

        self.frameColumns5Products=ctk.CTkFrame(frameTableProductos,                                                                                                                           
                                         height=70,                                         
                                         corner_radius=20,  
                                         fg_color="white"                                                                                                                       
                                         )
        

        
        self.frameColumns5Products.pack_propagate(False)
        self.frameColumns5Products.grid(padx=5, row=1, column=5) 

        #--------------Column 6

        self.frameColumns6Products=ctk.CTkFrame(frameTableProductos,                                                                                                                         
                                         height=70,                                        
                                         corner_radius=20,  
                                         fg_color="white"                                                                                                                       
                                         )
        

        
        self.frameColumns6Products.pack_propagate(False)
        self.frameColumns6Products.grid(padx=5, pady=5, row=1, column=6)

        


    def HeadTableProducts(self):

        #----------------------Prodcuts-----------------------------

        LabelPRODUCTO=ctk.CTkLabel(self.frameColumns1Products, 
                                   text="PRODUCT", 
                                   fg_color="white",
                                   border_width=1, 
                                   border_color="white",
                                   text_color="black", 
                                   corner_radius=10, 
                                   width=100
                                   )
        
        LabelPRODUCTO.grid(row=1, column=1, padx=5, pady=5)
        LabelPRODUCTO.pack_propagate(False)

        #----------------------SKU-----------------------------
        LabelSKU=ctk.CTkLabel(self.frameColumns2Products, 
                                   text="SKU", 
                                   fg_color="white",
                                   border_width=1, 
                                   border_color="white",
                                   text_color="black", 
                                   corner_radius=10, 
                                   width=100
                                   )
        
        LabelSKU.grid(row=1, column=2, padx=5, pady=5)
        LabelSKU.pack_propagate(False)

        #----------------------Category-----------------------------

        LabelCategory=ctk.CTkLabel(self.frameColumns3Products, 
                                   text="Category", 
                                   fg_color="white",
                                   border_width=1, 
                                   border_color="white",
                                   text_color="black", 
                                   corner_radius=10, 
                                   width=100
                                   )
        
        LabelCategory.grid(row=1, column=3, padx=5, pady=5)
        LabelCategory.pack_propagate(False)

        #----------------------Stock-----------------------------

        LabelStock=ctk.CTkLabel(self.frameColumns4Products, 
                                   text="Stock", 
                                   fg_color="white",
                                   border_width=1, 
                                   border_color="white",
                                   text_color="black", 
                                   corner_radius=10, 
                                   width=100
                                   )
        
        LabelStock.grid(row=1, column=4, padx=5, pady=5)
        LabelStock.pack_propagate(False)

        #----------------------Price-----------------------------

        LabelPrice=ctk.CTkLabel(self.frameColumns5Products, 
                                   text="Price", 
                                   fg_color="white",
                                   border_width=1, 
                                   border_color="white",
                                   text_color="black", 
                                   corner_radius=10, 
                                   width=100
                                   )
        
        LabelPrice.grid(row=1, column=5, padx=5, pady=5)
        LabelPrice.pack_propagate(False)
        
        #----------------------Status-----------------------------

        LabelStatus=ctk.CTkLabel(self.frameColumns6Products, 
                                   text="Status", 
                                   fg_color="white",
                                   border_width=1, 
                                   border_color="white",
                                   text_color="black", 
                                   corner_radius=10, 
                                   width=100
                                   )
        
        LabelStatus.grid(row=1, column=6, padx=5, pady=5)
        LabelStatus.pack_propagate(False)

    def rowsProducts(self, numRow:int):

        #----------------------Prodcuts-----------------------------

        LabelPRODUCTO=ctk.CTkLabel(self.frameColumns1Products, 
                                   text="Coffe late", 
                                   fg_color="white",
                                   border_width=1, 
                                   border_color="gray",
                                   text_color="black", 
                                   corner_radius=10, 
                                   width=100
                                   )
        
        LabelPRODUCTO.grid(row=numRow, column=1, padx=5, pady=5)
        LabelPRODUCTO.pack_propagate(False)

        #----------------------SKU-----------------------------
        LabelSKU=ctk.CTkLabel(self.frameColumns2Products, 
                                   text="DRK-001", 
                                   fg_color="white",
                                   border_width=1, 
                                   border_color="gray",
                                   text_color="black", 
                                   corner_radius=10, 
                                   width=100
                                   )
        
        LabelSKU.grid(row=numRow, column=2, padx=5, pady=5)
        LabelSKU.pack_propagate(False)

        #----------------------Category-----------------------------

        LabelCategory=ctk.CTkLabel(self.frameColumns3Products, 
                                   text="Drinks", 
                                   fg_color="white",
                                   border_width=1, 
                                   border_color="gray",
                                   text_color="black", 
                                   corner_radius=10, 
                                   width=100
                                   )
        
        LabelCategory.grid(row=numRow, column=3, padx=5, pady=5)
        LabelCategory.pack_propagate(False)

        #----------------------Stock-----------------------------

        LabelStock=ctk.CTkLabel(self.frameColumns4Products, 
                                   text="156", 
                                   fg_color="white",
                                   border_width=1, 
                                   border_color="gray",
                                   text_color="black", 
                                   corner_radius=10, 
                                   width=100
                                   )
        
        LabelStock.grid(row=numRow, column=4, padx=5, pady=5)
        LabelStock.pack_propagate(False)

        #----------------------Price-----------------------------

        LabelPrice=ctk.CTkLabel(self.frameColumns5Products, 
                                   text="5.50", 
                                   fg_color="white",
                                   border_width=1, 
                                   border_color="gray",
                                   text_color="black", 
                                   corner_radius=10, 
                                   width=100
                                   )
        
        LabelPrice.grid(row=numRow, column=5, padx=5, pady=5)
        LabelPrice.pack_propagate(False)
        
        #----------------------Status-----------------------------

        LabelStatus=ctk.CTkLabel(self.frameColumns6Products, 
                                   text="In Stock", 
                                   fg_color="white",
                                   border_width=1, 
                                   border_color="gray",
                                   text_color="black", 
                                   corner_radius=10, 
                                   width=100
                                   )
        
        LabelStatus.grid(row=numRow, column=6, padx=5, pady=5)
        LabelStatus.pack_propagate(False)


        


