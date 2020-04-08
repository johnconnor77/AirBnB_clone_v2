# 0x02. AirBnB clone - MySQL
---
<img align="center" src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/263/HBTN-hbnb-Final.png"  width="100%"/>

## Holberton School Airbnb Clone - MySQL applications

The Command Interpreter is used to manage the whole application's functionality from the command line, such as:
+ Crete a new object.
+ Retrieve an object from a file, database, etc.
+ Update object's attributes.
+ Destroy an object.

### Supported classes:
* BaseModel
* User
* State
* City
* Amenity
* Place
* Review

### Features

To launch console application at interactive mode simply run:

```console.py ```

or at non-interactive mode run:

```echo "your-command-goes-here" | ./console.py ```


### Commands:

Commands | Description | Usage
-------- | ----------- |-------- |
**help** or **?**| Displays the documented commands. | **help**
**quit**     | Exits the program. | **quit**
**EOF**      | Ends the program. Used when files are passed into the program. | N/A
**create**  | Creates a new instance of the \<class_name\>. Creates a Json file with the object representation. and prints the id of created object. | **create** \<class_name\>
**show**    | Prints the string representation of an instance based on the class name and id. | **show** \<class_name class_id\>
**destroy** | Deletes and instance base on the class name and id. | **destroy** \<class_name class_id\>
**all** | Prints all string representation of all instances based or not on the class name | **all** or **all** \<class_name class_id\>
**update** | Updates an instance based on the class name and id by adding or updating attribute | **update** \<class_name class_id key value\>

#### Create
`create <class name>`
Ex:
`create BaseModel`

#### Show
`show <class name> <object id>`
Ex:
`show User my_id`

#### Destroy
`destroy <class name> <object id>`
Ex:
`destroy Place my_place_id`

#### All
`all` or `all <class name>`
Ex:
`all` or `all State`

#### Quit
`quit` or `EOF`

#### Help
`help` or `help <command>`
Ex:
`help` or `help quit`

Additionally, the console supports `<class name>.<command>(<parameters>)` syntax.
Ex:
`City.show(my_city_id)`

## Tests

To run at the test for this application all of the tests are located
on **test/** folder and it will be checked by running from root folder:

```python3 -m unittest discover tests ```


