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

### Basic Usage

```python
from selfie import selfie

@selfie
class Counter:
    def __init__(self):
        self.value = 0
        self.history = []

    def increment(self):
        self.value += 1
        self.history.append(self.value)

counter = Counter()
counter.increment()  # [Counter] value: 0 -> 1
counter.increment()  # [Counter] value: 1 -> 2
```

### Custom Logger

```python
import logging
from selfie import selfie

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
custom_logger = logging.getLogger(__name__)

@selfie(logger=custom_logger.info)
class DataProcessor:
    def __init__(self):
        self.status = "idle"
        self.processed_count = 0

processor = DataProcessor()
processor.status = "processing"  # [2024-01-01 12:00:00] [DataProcessor] status: 'idle' -> 'processing'
```

### Querying Change History

```python
@selfie
class Document:
    def __init__(self):
        self.title = "Untitled"
        self.content = ""
        self.tags = []

doc = Document()
doc.title = "My Document"
doc.content = "Hello world"
doc.tags.append("python")
doc.tags.append("documentation")

# Get flat change history
changes = doc.get_change_history()
# [
#   {'time': datetime, 'attr': 'title', 'from': 'Untitled', 'to': 'My Document'},
#   {'time': datetime, 'attr': 'content', 'from': '', 'to': 'Hello world'},
#   {'time': datetime, 'attr': 'tags', 'from': [], 'to': ['python']},
#   {'time': datetime, 'attr': 'tags', 'from': ['python'], 'to': ['python', 'documentation']}
# ]

# Get change history grouped by attribute
changes_by_attr = doc.get_change_history(format="attr")
print(changes_by_attr)
# {
#   'title': [{'time': datetime, 'from': 'Untitled', 'to': 'My Document'}],
#   'content': [{'time': datetime, 'from': '', 'to': 'Hello world'}],
#   'tags': [
#     {'time': datetime, 'from': [], 'to': ['python']},
#     {'time': datetime, 'from': ['python'], 'to': ['python', 'documentation']}
#   ]
# }

# Get history for specific attribute
tag_changes = doc.get_change_history("tags")
print(tag_changes)
# [
#   {'time': datetime, 'from': [], 'to': ['python']},
#   {'time': datetime, 'from': ['python'], 'to': ['python', 'documentation']}
# ]
```

## API Reference

### `@selfie(track_private=True, logger=None)`

Class decorator that enables attribute change tracking.

**Parameters:**

- `track_private` (bool): If `True` (default), track changes to private attributes (starting with `_`). If `False`, only track public attributes.
- `logger` (callable): Optional logger function. Defaults to `print`. Should accept a single string argument.

**Returns:**

Decorated class with change tracking enabled.

### `get_change_history(attribute=None, format="flat")`

Instance method available on decorated classes.

**Parameters:**

- `attribute` (str, optional): Specific attribute name to get history for. If `None`, returns history for all attributes.
- `format` (str): Either `"flat"` (list of all changes) or `"attr"` (dictionary grouped by attribute). Defaults to `"flat"`.

**Returns:**

- If `format="flat"`: List of dictionaries with keys `time`, `attr`, `from`, `to`
- If `format="attr"`: Dictionary mapping attribute names to lists of change records
- If `attribute` is specified: List of change records for that attribute

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
