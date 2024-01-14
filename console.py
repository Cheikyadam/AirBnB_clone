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
    all_inst = []
    all_cls = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

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
            if arg == "BaseModel":
                inst = BaseModel()
            elif arg == "User":
                inst = User()
            elif arg == "State":
                inst = State()
            elif arg == "City":
                inst = City()
            elif arg == "Amenity":
                inst = Amenity()
            elif arg == "Place":
                inst = Place()
            else:
                inst = Review()
            inst.save()
            self.all_inst.append(inst.__str__())
            print(inst.id)

    def do_show(self, arg):
        """To show instances infos"""
        if my_helper(arg):
            args = arg.split(" ")
            if len(args) == 1:
                print("** instance id missing **")
            else:
                ins_id = args[1]
                found = False
                for inst in self.all_inst:
                    if ins_id in inst:
                        print(inst)
                        found = True
                        break
                if found is False:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """To destroy an instance id"""
        if my_helper(arg):
            args = arg.split(" ")
            if len(args) == 1:
                print("** instance id missing **")
            else:
                ins_id = args[1]
                found = False
                for inst in self.all_inst:
                    if ins_id in inst:
                        all_inst.remove(inst)
                        found = True
                        break
                if found is False:
                    print("** no instance found **")

    def do_all(self, arg):
        """To print all instances of a class or all instaneces"""
        if len(arg) == 0:
            print(self.all_inst)
        else:
            if arg != "BaseModel":
                print("** class doesn't exist **")
            else:
                print(self.all_inst)

    def do_update(self, arg):
        """Updating an instance"""
        if my_helper:
            args = arg.split(" ")
            if len(args) == 1:
                print("** instance id missing **")
            else:
                ins_id = args[1]
                found = False
                for inst in self.all_inst:
                    if ins_id in inst:
                        found = True
                        break
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
