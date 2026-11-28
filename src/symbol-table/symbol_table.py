
"""
ZARA PROGRAMMING LANGUAGE
MEMBER DENIS MUTHURI - SYMBOL TABLE

Features:
1. Integer, Float and String variables
2. Typed Arrays and Stacks
3. Add, search, update and retrieve
4. Variable scope management
5. Stack operations: push, pop and peek
6. Error handling
"""

from dataclasses import dataclass
from typing import Any


# =========================
# CUSTOM EXCEPTIONS
# =========================

class SymbolTableError(Exception):
    pass


class DuplicateDeclarationError(SymbolTableError):
    pass


class UndeclaredVariableError(SymbolTableError):
    pass


class TypeMismatchError(SymbolTableError):
    pass


class InvalidDataTypeError(SymbolTableError):
    pass


class EmptyStackError(SymbolTableError):
    pass


# =========================
# SYMBOL CLASS
# =========================

@dataclass
class Symbol:
    name: str
    data_type: str
    value: Any
    scope: str
    element_type: str = None


# =========================
# SYMBOL TABLE CLASS
# =========================

class SymbolTable:

    SUPPORTED_TYPES = {
        "Integer",
        "Float",
        "String",
        "Array",
        "Stack"
    }

    ELEMENT_TYPES = {
        "Integer",
        "Float",
        "String"
    }

    def __init__(self):
        self.scopes = [{}]
        self.scope_names = ["global"]

    # =========================
    # SCOPE MANAGEMENT
    # =========================

    def current_scope(self):
        return self.scope_names[-1]

    def enter_scope(self, name="local"):
        self.scopes.append({})
        self.scope_names.append(name)

        print(f"Entered scope: {name}")

    def exit_scope(self):

        if len(self.scopes) == 1:
            raise SymbolTableError(
                "Cannot exit global scope."
            )

        removed = self.scope_names.pop()
        self.scopes.pop()

        print(f"Exited scope: {removed}")

    # =========================
    # TYPE VALIDATION
    # =========================

    def validate_value(self, data_type, value):

        if data_type not in self.SUPPORTED_TYPES:
            raise InvalidDataTypeError(
                f"Unsupported data type: {data_type}"
            )

        if data_type == "Integer":
            valid = type(value) is int

        elif data_type == "Float":
            valid = type(value) is float

        elif data_type == "String":
            valid = isinstance(value, str)

        else:
            raise TypeMismatchError(
                f"{data_type} requires a collection "
                "element type."
            )

        if not valid:
            raise TypeMismatchError(
                f"Expected {data_type}, got "
                f"{type(value).__name__}"
            )

    def validate_collection(
        self, collection, element_type
    ):

        if element_type not in self.ELEMENT_TYPES:
            raise InvalidDataTypeError(
                f"Invalid collection element type: "
                f"{element_type}"
            )

        if not isinstance(collection, list):
            raise TypeMismatchError(
                "Collection value must be a list."
            )

        for item in collection:
            self.validate_value(element_type, item)

    # =========================
    # ADD VARIABLE
    # =========================

    def add(
        self,
        name,
        data_type,
        value,
        element_type=None
    ):

        current = self.scopes[-1]

        if name in current:
            raise DuplicateDeclarationError(
                f"Variable '{name}' already exists "
                f"in scope '{self.current_scope()}'."
            )

        if data_type in ("Array", "Stack"):

            if element_type is None:
                raise InvalidDataTypeError(
                    "Array and Stack require an "
                    "element_type."
                )

            self.validate_collection(
                value, element_type
            )

        else:

            if element_type is not None:
                raise InvalidDataTypeError(
                    "element_type is only for "
                    "Array and Stack."
                )

            self.validate_value(data_type, value)

        symbol = Symbol(
            name=name,
            data_type=data_type,
            value=value,
            scope=self.current_scope(),
            element_type=element_type
        )

        current[name] = symbol

        print(f"Variable '{name}' added successfully.")

    # =========================
    # SEARCH VARIABLE
    # =========================

    def search(self, name):

        for scope in reversed(self.scopes):

            if name in scope:
                return scope[name]

        raise UndeclaredVariableError(
            f"Variable '{name}' is not declared."
        )

    # =========================
    # UPDATE VARIABLE
    # =========================

    def update(self, name, new_value):

        symbol = self.search(name)

        if symbol.data_type in ("Array", "Stack"):

            self.validate_collection(
                new_value,
                symbol.element_type
            )

        else:

            self.validate_value(
                symbol.data_type,
                new_value
            )

        symbol.value = new_value

        print(f"Variable '{name}' updated successfully.")

    # =========================
    # RETRIEVE VARIABLE
    # =========================

    def retrieve(self, name):

        symbol = self.search(name)

        return {
            "name": symbol.name,
            "data_type": symbol.data_type,
            "value": symbol.value,
            "scope": symbol.scope,
            "element_type": symbol.element_type
        }

    # =========================
    # STACK OPERATIONS
    # =========================

    def push(self, name, value):

        symbol = self.search(name)

        if symbol.data_type != "Stack":
            raise TypeMismatchError(
                f"'{name}' is not a Stack."
            )

        self.validate_value(
            symbol.element_type, value
        )

        symbol.value.append(value)

        print(f"{value} pushed onto stack '{name}'.")

    def pop(self, name):

        symbol = self.search(name)

        if symbol.data_type != "Stack":
            raise TypeMismatchError(
                f"'{name}' is not a Stack."
            )

        if not symbol.value:
            raise EmptyStackError(
                f"Stack '{name}' is empty."
            )

        value = symbol.value.pop()

        print(f"{value} removed from stack '{name}'.")

        return value

    def peek(self, name):

        symbol = self.search(name)

        if symbol.data_type != "Stack":
            raise TypeMismatchError(
                f"'{name}' is not a Stack."
            )

        if not symbol.value:
            raise EmptyStackError(
                f"Stack '{name}' is empty."
            )

        return symbol.value[-1]

    # =========================
    # DISPLAY SYMBOL TABLE
    # =========================

    def display(self):

        print("\n========== SYMBOL TABLE ==========")

        for scope_name, scope in zip(
            self.scope_names, self.scopes
        ):

            print(f"\nScope: {scope_name}")

            if not scope:
                print("No variables declared.")
                continue

            for symbol in scope.values():

                print(
                    f"Name: {symbol.name}, "
                    f"Type: {symbol.data_type}, "
                    f"Value: {symbol.value}, "
                    f"Element Type: {symbol.element_type}"
                )

        print("==================================")
