from client import TypeCoercionEngine

v1 = TypeCoercionEngine.coerce_value("128", "integer")
v2 = TypeCoercionEngine.coerce_value("true", "boolean")
print("Coerced values:", v1, type(v1), v2, type(v2))
