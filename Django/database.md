# Database

# Enter in the shell

```
python manage.py shell
```

### Step 1: 
    import the models from the app

    from main.models import Items, ToDoList
### Step 2:

* Create a ToDo List
```
    list1 = ToDoList(name = "Aravind K V") 
```

* Save the list in the database
```
    list1.save()
```

* Prints 1, each list is given an id automatically
```
print(list1.id)
```

* Prints all of the ToDoLists in the database

```
print(ToDoList.objects.get(name="Aravind K V")
```

### Item Set

* To get all the item_set

```
list1.item_set.all()
```

* To create a item set

```
list1.create(text="Play Valorant")

## Tutorial example
list1.item_set.create(text="Play valorant", complete=False)
```
* To change the name of the list
```
list1.name= "New Name"
```

* Save changes

```
list1.save()
```

* Delete the list()

```
list1.delete()
```