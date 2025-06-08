# counttypes

Count types in a list - int, float, str, bool, list, set, dict, tuple

## Example

```python
from countertypes import CountTypes

data = [1, 2.2, 'hello', [1, 2], {'a': 1}]
counter = CountTypes(data)
print(counter.NonZeroTotal())
