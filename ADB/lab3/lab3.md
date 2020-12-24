# Ex 2
```
db.categories.find({},{CategoryID:1, Description:1, _id:0}, $sort: {CategoryID:-1})
```

# Ex 3

```
db.products.find({}).pretty()
```

# Ex 4
```
db.products.find({UnitPrice: {$gt: 18}}).pretty()
```

# Ex 5
```
db.products.aggregate([{$group: {_id: "$CategoryID",AverageUnitPrice: {$avg: "$UnitPrice"}}}])
```

# Ex 6
```
db.products.aggregate({$lookup: {from: "categories", localField: "CategoryID", foreignField: "CategoryID", as: "CatName"}}).pretty()
```

# Ex 7
```
 db.suppliers.insert({
...  "SupplierID" : 20,
...  "CompanyName" : "Leka Trading",
...  "ContactName" : "Chandra Leka",
...  "ContactTitle" : "Owner",
...  "Address" : "471 Serangoon Loop",
...  "City" : "Suite #402",
...  "Region" : "Singapore",
...  "PostalCode" : "NULL",
...  "Country" : 512,
...  "Phone" : "Singapore",
...  "Fax" : "555-8787",
...  "HomePage" : "NULL",
...  "field12" : "NULL"
... })
```

# Ex 8
```
db.suppliers.updateOne({SupplierID: 20}, {$set: {Phone: "+65 1234 5678"}})
```

# EX 9
```
db.suppliers.deleteOne({SupplierID: 20})
```

