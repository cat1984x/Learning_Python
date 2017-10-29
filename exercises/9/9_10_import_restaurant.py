from restaurant import Restaurant

res=Restaurant('huangmen chicken','Chinese food')
res.read_number_served()

res.set_number_served(25)
res.read_number_served()

res.increment_number_served(8)
res.read_number_served()
