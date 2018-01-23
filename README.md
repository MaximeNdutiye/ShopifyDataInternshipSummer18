Shopify data intership problem summer 2018 


### usage
``` BASH
    
    # inner|left|right are the join types
    # left_table is the first json file
    # right_table is the second json file
    # field1 is the field to join on first table
    # field2 is the field to join on second table
    
    ./joiner.py inner|left|right left_table right_table field1 field2 
```

### examples

```
    # perform inner join on customers.json and orders.json
    # with keys cid and customer_id
    # output is in file result.json
    
    ./joiner.py inner customers.json orders.json cid customer_id
    
```

created with 💚 by maxime