import xmlrpc.client

url = "http://localhost:8069"
username = "admin"
password = "admin"
db = 'odoo17' # or theodooguys

common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
user_uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')

#search function
property_ids = models.execute_kw(db, user_uid, password, 'estate.property', 'search', [[]])
print("search function ==>", property_ids)

#count function
count_property_ids = models.execute_kw(db, user_uid, password, 'estate.property', 'search_count', [[]])
print("count function ==>", count_property_ids)

#read function
read_property_ids = models.execute_kw(db, user_uid, password, 'estate.property', 'read', [property_ids], {'fields':['name']})
print("read function ==>", read_property_ids)

#search and read function
search_read_property_ids = models.execute_kw(db, user_uid, password, 'estate.property', 'search_read', [[]], {'fields':['name']})
print("search_read function ==>", search_read_property_ids)

#create function
# create_property_id = models.execute_kw(db, user_uid, password, 'estate.property', 'create', [{'name': 'Property from RPC', 'sales_id': 6}])
# print("create property ==> ", create_property_id)

#write function
# write_property_id = models.execute_kw(db, user_uid, password, 'estate.property', 'write', [[22],  {'name': 'Property from RPC updated'}])
# read_name_get = models.execute_kw(db, user_uid, password, 'estate.property', 'name_get', [22])
# print("update property ==> ", read_name_get)

# #unlink / delete
# unlink_property_id = models.execute_kw(db, user_uid, password, 'estate.property', 'unlink', [[22]])
# print("unlink property ==> ", unlink_property_id)

