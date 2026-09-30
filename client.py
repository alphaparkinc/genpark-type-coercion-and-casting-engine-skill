"""Type Coercion and Casting Engine.
100% Python Standard Library.
"""

import json

class TypeCoercionEngine:
    """Safely coerces stringified primitives and mixed types into strict schema types."""
    @staticmethod
    def coerce_value(val, target_type: str):
        if val is None:
            return None
        try:
            if target_type == "integer":
                return int(float(val))
            elif target_type == "number":
                return float(val)
            elif target_type == "boolean":
                if isinstance(val, str):
                    return val.lower() in ("true", "1", "yes", "t")
                return bool(val)
            elif target_type == "string":
                return str(val)
            elif target_type == "array":
                if isinstance(val, str):
                    if val.strip().startswith("[") and val.strip().endswith("]"):
                        return json.loads(val)
                    return [item.strip() for item in val.split(",") if item.strip()]
                elif isinstance(val, list):
                    return val
                return [val]
            elif target_type == "object":
                if isinstance(val, str):
                    return json.loads(val)
                return dict(val)
        except Exception:
            return val
        return val
