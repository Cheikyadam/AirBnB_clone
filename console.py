#!/usr/bin/python3
"""My Cmd with python"""
import cmd
from models.base_model import BaseModel
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
                all_it = dict(self.all_inst)
                for base, inst in all_it.items():
                    if arg[0] in str(base):
                        id_ins = inst['id']
                        if id_ins == ins_id:
                            new_inst = creating(args[0], inst)
                            print(new_inst)
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
                all_it = dict(self.all_inst)
                for base, inst in all_it.items():
                    if arg[0] in str(base):
                        id_ins = inst['id']
                        if id_ins == ins_id:
                            del self.all_inst[base]
                            storage.save()
                            found = True
                            break
                if found is False:
                    print("** no instance found **")

    def do_all(self, arg):
        """To print all instances of a class or all instaneces"""
        if len(arg) == 0:
            self.all_inst = storage.all()
            all_list = []
            all_it = dict(self.all_inst)
            for base, inst in all_it.items():
                new_inst = creating(base, inst)
                all_list.append(str(new_inst))
            print(all_list)
        else:
            if arg not in self.all_cls:
                print("** class doesn't exist **")
            else:
                self.all_inst = storage.all()
                all_list = []
                all_it = dict(self.all_inst)
                for base, inst in all_it.items():
                    if arg in base:
                        new_inst = creating(base, inst)
                        all_list.append(str(new_inst))
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
                all_it = dict(self.all_inst)
                for base, inst in all_it.items():
                    if arg[0] in str(base):
                        id_ins = inst['id']
                        if id_ins == ins_id:
                            found = True
                            if len(args) == 2:
                                print("** attribute name missing **")
                            elif len(args) == 3:
                                print("** value missing **")
                            else:
                                updat(base, inst)
                            break
                if found is False:
                    print("** no instance found **")
                if found is False:
                    print("** no instance found **")
                else:
                    if len(args) == 2:
                        print("** attribute name missing **")
                    else:
                        if len(args) == 3:
                            print("** value missing **")
                        else:
                            print("""UPDATING""")


def updat(base, inst):
    """To update instances"""
    pass


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
