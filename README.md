# Selfie

A Python decorator for logging attribute changes in classes. Track every modification to your object's attributes with automatic logging and change history.

## Features

- **Automatic attribute change tracking**: Decorated classes automatically log all attribute changes
- **Container support**: Tracks changes to dictionaries, lists, sets, and tuples, including nested modifications
- **Flexible logging**: Use built-in `print` or any custom logger function
- **Change history**: Query complete change history for any attribute

## Installation

```bash
pip install selfie
```

Or using mighty `uv`:

```bash
uv add selfie
```

## Usage

```python
from selfie import selfie

@selfie
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

# Create counter and use it
counter = Counter()
counter.increment()
counter.decrement()

# Changes are automatically logged:
# [Counter] value: 0 -> 1
# [Counter] value: 1 -> 0

# Query change history
all_changes = counter.get_change_history()
# [
#   {'time': datetime, 'attr': 'value', 'from': None, 'to': 0},
#   {'time': datetime, 'attr': 'value', 'from': 0, 'to': 1},
#   {'time': datetime, 'attr': 'value', 'from': 1, 'to': 0}
# ]

# Get changes for specific attribute
value_changes = counter.get_change_history("value")
# [
#   {'time': datetime, 'from': None, 'to': 0},
#   {'time': datetime, 'from': 0, 'to': 1},
#   {'time': datetime, 'from': 1, 'to': 0}
# ]

# Get changes grouped by attribute
grouped = counter.get_change_history(format="attr")
# {
#   'value': [
#     {'time': datetime, 'from': None, 'to': 0},
#     {'time': datetime, 'from': 0, 'to': 1},
#     {'time': datetime, 'from': 1, 'to': 0}
#   ]
# }
```

### More Examples

See more examples in the [`examples/`](examples/) directory.

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
