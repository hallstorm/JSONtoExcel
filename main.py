import os
import pandas as pd
import json
import datetime

# Directorio de la carpeta "json"
json_folder = "json"

# Nombres de los dataframes
df_customer = pd.DataFrame()
df_sales = pd.DataFrame()
df_stock = pd.DataFrame()

# Recorrer los archivos JSON en la carpeta
for filename in os.listdir(json_folder):
    if filename.endswith(".json"):
        json_path = os.path.join(json_folder, filename)

        # Leer el archivo JSON
        with open(json_path, "r", encoding='utf-8') as file:
            json_data = json.load(file)

        # Leer la parte "customer" del JSON
        if "customer" in json_data:
            customer_data = json_data["customer"]

            # Convertir a DataFrame y agregar al DataFrame "df_customer"
            df_customer = df_customer.append(pd.DataFrame(customer_data), ignore_index=True)

        # Leer la parte "sales" del JSON
        if "sales" in json_data:
            sales_data = json_data["sales"]

            # Convertir a DataFrame y agregar al DataFrame "df_sales"
            df_sales = df_sales.append(pd.DataFrame(sales_data), ignore_index=True)

        # Leer la parte "stock" del JSON
        if "stock" in json_data:
            stock_data = json_data["stock"]

            # Convertir a DataFrame y agregar al DataFrame "df_stock"
            df_stock = df_stock.append(pd.DataFrame(stock_data), ignore_index=True)

# Crear el archivo de Excel con las hojas correspondientes
tiempo_actual = datetime.datetime.now().strftime("%Y-%m-%d--%H-%M-%S-%f")
excel_path = f"data-{tiempo_actual}.xlsx"
with pd.ExcelWriter(excel_path) as writer:
    df_customer.to_excel(writer, sheet_name="df_customer", index=False)
    df_sales.to_excel(writer, sheet_name="df_sales", index=False)
    df_stock.to_excel(writer, sheet_name="df_stock", index=False)
