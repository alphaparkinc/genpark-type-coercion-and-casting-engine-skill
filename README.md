# genpark-type-coercion-and-casting-engine-skill

Type casting and coercion engine normalizing stringified values into schema-compliant Python primitives and structures.

## Architecture

```mermaid
flowchart LR
    Raw["Stringified Values: 'true', '42', '[1, 2]'"] --> Coercer[TypeCoercionEngine]
    TargetType[Target Schema Type] --> Coercer
    Coercer --> TypedValues["Strict Types: True, 42, [1, 2]"]
```

## Features
- **Zero Dependencies**: 100% Python Standard Library.
- **Fail-Safe**: Returns original value if casting is impossible.
