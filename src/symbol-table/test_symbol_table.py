import sys
sys.path.insert(0, "src/symbol-table")

from symbol_table import SymbolTable

#create a  symbol table object
table = SymbolTable()

#add an integer variable
table.add("age", "Integer", 20)

#retrieve info about age
result = table.retrieve("age")

#print the retrieved info
print("\nRetrieved Variable Information:")
print(result)


#FLOAT INSERTION TEST
table.add("salary", "Float", 45000.50)

result = table.retrieve("salary")

print("\nSecond test: FLOAT")
print(result)



#STRING INSERTION TESTING
table.add("studentName", "String", "Denis Muthuri")

result =  table.retrieve("studentName")

print("\nTHIRD TEST: STRING")
print(result)


# TESTING INTERGER ARRAY
table.add(
     "marks",
     "Array",
     [70, 85, 90, 65],
     element_type="Integer"
)

result = table.retrieve("marks")

print("\nTEST 4: INTERGER ARRAY")
print(result)

