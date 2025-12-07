import tkinter as tk
from tkinter import messagebox

class item:
        def __init__(self, name, category, quantity):
            self.name = name
            self.category = category
            self.quantity = quantity

def __str__(self):
        return f"{self.name} ({self.category}) - Qty: {self.quantity}"
    
class category:

    def __init__(self, name, description=""):
        self.name = name
        self.description = description

class inventory:
    def __init__(self):
          self.categories = {}
          self.items = []

def add_category(self, name, description=""):
      if name in self.categories:
            return
      self.categories[name] = categories(name, description)

def get_category_names(self):
      return list(self.categories.keys())

def add_item(self, name, category_name, quantity):
      if category_name not in self.categories:
            self.add_category(category_name)

      existing = self.find_item(name)
      if existing:
            existing.quantity += quantity
      else:
            self.items.append(item(name, category_name, quantity))

def find_item(self, name):
      for item in self.items:
            if item.name.lower() == name.lower():
                  return item
            return None

def update_quantity(self, name, new_quantity):
      item = self.find_item(name)
      if item is None:
            return False
      item.quantity = new_quantity
      return True

def delete_item(self, name):
      item = self.find_item(name)
      if item is None:
            return False
      self.items.remove(item)
      return True

def get_items(self):
      return self.items

def search_items(self, keyword):
      keyword = keyword.lower().strip()
      if not keyword:
            return self.items
      results = []
      for item in self.items:
            if keyword in item.name.lower() or keyword in item.category.lower():
                  result.append(item)
            return results

class inventoryGui:
      def __init__(self, root):
            self.root = root
            self.root.title("Inventory manager")

            self.system = InventorySystem()
            self.load_data()
            self.build_widgets()
            self.refresh_list(self.system.get_items())
