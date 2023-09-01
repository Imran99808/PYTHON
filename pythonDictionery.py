d1={}
#print(type(d1))
d2={"harry":"Burger",
  "shkil":"ruyti",
  "Rana":{ "B":"maggi","L":"roti","D":"chicken"}
}
d2["shawon"]="junk food"
d2[420]="kabab"
del d2[420]
#print(d2["Rana"])
d3=d2.copy()
del d3 ["Rana"] 
#print(d3)
d2.update({"leena":"toffe"})
#print (d2.keys())
print(d2.items())