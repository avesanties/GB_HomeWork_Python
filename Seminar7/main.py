from Adapter_CSV import *
from AppDataStore import AppDataStore
from UserInterface import UserInterface

adapter = Adapter_CSV(DataProvider_CSV())
data = adapter.read()
data_store = AppDataStore(data)

UserInterface(data_store)

adapter.write(data_store.select())