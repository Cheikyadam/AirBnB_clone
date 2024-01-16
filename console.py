#!/usr/bin/python3
"""My Cmd with python"""
import cmd
from models.base_model import BaseModel
import json
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Defintion of the class"""
    prompt = "(hbnb) "
    all_inst = {}
    all_cls = [
        "BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

    def do_quit(self, arg):
        """Quit Command to exit the program"""
        return True

    def emptyline(self):
        """Do Nothing on empty line"""
        pass

    def do_EOF(self, line):
        """EOF Command to exit the program"""
        print()
        return True

    def do_create(self, arg):
        """To create a new instance"""
        if my_helper(arg, self.all_cls):
            inst = creating(arg, {})
            inst.save()
            print(inst.id)

    def do_show(self, arg):
        """To show instances infos"""
        if my_helper(arg, self.all_cls):
            args = arg.split(" ")
            if len(args) == 1:
                print("** instance id missing **")
            else:
                ins_id = args[1]
                self.all_inst = storage.all()
                found = False
                for class_name, inst in self.all_inst.items():
                    if arg[0] in class_name and ins_id in class_name:
                        print(inst)
                        found = True
                        break
                if found is False:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """To destroy an instance id"""
        if my_helper(arg, self.all_cls):
            args = arg.split(" ")
            if len(args) == 1:
                print("** instance id missing **")
            else:
                ins_id = args[1]
                self.all_inst = storage.all()
                found = False
                for class_name, inst in self.all_inst.items():
                    if arg[0] in class_name and ins_id in class_name:
                        del self.all_inst[class_name]
                        storage.save()
                        found = True
                        break
                if found is False:
                    print("** no instance found **")

    def do_all(self, arg):
        """To print all instances of a class or all instaneces"""
        if len(arg) == 0:
            self.all_inst = storage.all()
            all_list = list()
            for class_name, inst in self.all_inst.items():
                all_list.append(str(inst))
            print(all_list)
        else:
            if arg not in self.all_cls:
                print("** class doesn't exist **")
            else:
                self.all_inst = storage.all()
                all_list = []
                for cls_id, inst in self.all_inst.items():
                    if arg in cls_id:
                        all_list.append(str(inst))
                print(all_list)

    def do_update(self, arg):
        """Updating an instance"""
        if my_helper:
            args = arg.split(" ")
            if len(args) == 1:
                print("** instance id missing **")
            else:
                ins_id = args[1]
                self.all_inst = storage.all()
                found = False
                for class_id, inst in self.all_inst.items():
                    if arg[0] in class_id and args[1] in class_id:
                        found = True
                        if len(args) == 2:
                            print("** attribute name missing **")
                        elif len(args) == 3:
                            print("** value missing **")
                        else:
                            updating(class_id, inst, args)
                        break
                if found is False:
                    print("** no instance found **")

    def default(self, line):
        """Default actions or commands"""
        if line.endswith(".all()"):
            arg = line[:-6]
            self.do_all(arg)
        elif line.endswith(".count()"):
            arg = line[:-8]
            if arg in self.all_cls:
                self.all_inst = storage.all()
                list_key = list(self.all_inst.keys())
                count = 0
                for elmt in list_key:
                    if arg in elmt:
                        count += 1
                print(count)
            else:
                print("** class doesn't exist **")
        else:
            for i in range(0, len(line)):
                if line[i] == '(':
                    break
            arg = line[i:]
            com = line[:i]
            arg = arg.replace('(', '')
            arg = arg.replace(')', '')
            if com.endswith(".show"):
                com = com[:-5]
                arg = arg.replace('"', '')
                if len(arg) != 0:
                    com = com + " " + arg
                self.do_show(com)
            elif com.endswith(".destroy"):
                com = com[:-8]
                arg = arg.replace('"', '')
                if len(arg) != 0:
                    com = com + " " + arg
                self.do_destroy(com)
            elif com.endswith(".update"):
                com = com[:-7]
                if "{" not in arg or "}" not in arg:
                    arg = arg.replace('"', '')
                    arg = arg.split(" ")
                    for elmt in arg:
                        com += " " + elmt
                    com = com.replace(',', '')
                    self.do_update(com)
                else:
                    arg = arg.split("{")
                    com = com + " " + arg[0].replace('"', '').replace(',', '')
                    dico = "{" + arg[1]
                    dico = dico.replace('\'', '"')
                    dico = json.loads(str(dico))
                    for key, value in dico.items():
                        run = com + str(key) + " " + str(value)
                        print(run)
                        self.do_update(run)
            else:
                print(f"*** Unknown syntax: {line}")


def updating(class_id, inst, args):
    attribute = str(args[2])
    value = args[3]
    change = False
    if "BaseModel" in class_id:
        setattr(inst, attribute, value)
        change = True
    elif "User" in class_id:
        if attribute in vars(User).keys():
            setattr(inst, attribute, value)
            change = True
    elif "State" in class_id:
        if attribute == "name":
            setattr(inst, attribute, value)
            change = True
    elif "City" in class_id:
        if attribute == "name":
            setattr(inst, attribute, value)
            change = True
    elif "Amenity" in class_id:
        if attribute == "name":
            setattr(inst, attribute, value)
            change = True
    elif "Review" in class_id:
        if attribute == "text":
            setattr(inst, attribute, value)
            change = True
    elif "Place" in class_id:
        list_int = ["number_rooms", "number_bathrooms", "max_guest",
                    "price_by_night"]
        if attribute in ["name", "description"]:
            setattr(inst, attribute, value)
            change = True
        elif attribute in ["latitue", "longitude"]:
            try:
                setattr(inst, attribute, float(value))
                change = True
            except ValueError:
                pass
        elif attribute in list_int:
            try:
                setattr(inst, attribute, int(value))
                change = True
            except ValueError:
                pass
    if change is True:
        inst.save()


def my_helper(arg, all_class):
    """Function to check if there is an error"""
    args = arg.split(" ")
    if len(arg) == 0:
        print("** class name missing **")
        return False
    elif args[0] not in all_class:
        print("** class doesn't exist **")
        return False
    return True


def creating(arg, kwargs):
    """To create instances"""
    if "BaseModel" in arg:
        inst = BaseModel(**kwargs)
    elif "User" in arg:
        inst = User(**kwargs)
    elif "State" in arg:
        inst = State(**kwargs)
    elif "City" in arg:
        inst = City(**kwargs)
    elif "Amenity" in arg:
        inst = Amenity(**kwargs)
    elif "Place" in arg:
        inst = Place(**kwargs)
    else:
        inst = Review(**kwargs)
    return inst


if __name__ == '__main__':
    HBNBCommand().cmdloop()
