import pandas as pd

# Traemos los datos de la carperta indicada
path='./Assets/' 

# Leeemos el archivo Features
features = pd.read_csv(path+"features.csv",sep="|",low_memory=False)

# Leeemos el archivo historic_sales
historic_sales = pd.read_csv(path+"historic_sales.csv",sep="|",low_memory=False)
#Con el fin eliminar valores erroneos se eliminan filas que en la columna Weekly_Sales no sean numeros 
historic_sales.drop(historic_sales.loc[ historic_sales['Weekly_Sales'].str.extract(r'([abc])', expand=False).notnull()].index, inplace=True)
historic_sales['Weekly_Sales'] = historic_sales['Weekly_Sales'].str.replace(",", ".").astype(float)
#Para poder identificar ventas por trimeste se generan los datos mes año y se convierte la columna DATE en una fecha 
historic_sales['Date'] = pd.to_datetime(historic_sales['Date'], format="%Y-%m-%d")
historic_sales['Mes_ano']=historic_sales['Date'].dt.to_period('m')

# Leeemos el archivo store_info
store_info = pd.read_csv(path+"store_info.csv",sep=";",low_memory=False)


# Primer Punto Cual es la tienda con el mayor valor en ventas totales?
Ventas_store=historic_sales.loc[:,['Store',"Weekly_Sales"]].groupby('Store').sum().reset_index()
Ventas_store.sort_values(by=['Weekly_Sales'],ascending=False,inplace=True)

print('Las 3 tiendas con mayor numero de ventas son:')
print(Ventas_store.head(3))


# Segundo Punto Entre las 3 tiendas más grandes cuál es la que más ventas totales registra?

Tienda_grandes=store_info.sort_values(by=['Size'],ascending=False)
Tienda_grandes_max=Tienda_grandes.head(3)
Tienda_grandes_max_v=Tienda_grandes_max.Store.tolist()
Ventas_tiendas_g=Ventas_store[Ventas_store.Store.isin(Tienda_grandes_max_v)]

print('Las tres tiendas mas grandes son:')
print(Tienda_grandes_max_v)
print('De las mas grandes la que mas ventas tiene es la:')

print(Ventas_tiendas_g.loc[Ventas_tiendas_g['Weekly_Sales']==Ventas_tiendas_g['Weekly_Sales'].max()])

# Tercer punto Cual es la tienda con menor ventas ?
print('La tienda con menor ventas es la:')
print(Ventas_store.loc[Ventas_store['Weekly_Sales']==Ventas_store['Weekly_Sales'].min()])

# Cuarto punto Cual es la tienda que mas vendió en el 2 semestre del año 2012?
Semestre=2
ano=2012

if Semestre==1:
    fecha=str(ano)+'-'+'01'
elif Semestre==2:
    fecha=str(ano)+'-'+'07'
    
idx = pd.date_range(fecha,freq='m', periods=6).to_period('m')
Ventas_Semeste_store=historic_sales.loc[:,['Store','Mes_ano',"Weekly_Sales"]]
Ventas_Semeste_store_v=Ventas_Semeste_store[Ventas_Semeste_store.Mes_ano.isin(idx)]
Ventas_Semeste_store_v=Ventas_Semeste_store_v.groupby(['Store']).sum().reset_index()
Ventas_Semeste_store_v.sort_values(by=['Weekly_Sales'],ascending=False,inplace=True)

print('La tienda con mas ventas en el semeste '+str(Semestre)+' del año '+str(ano)+' es la:')
print(Ventas_Semeste_store_v.loc[Ventas_Semeste_store_v['Weekly_Sales']==Ventas_Semeste_store_v['Weekly_Sales'].max()])




