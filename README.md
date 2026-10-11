# task-queue

A bounded worker pool with backpressure, retries and graceful shutdown.

## Why

I kept rewriting the same thirty lines in every project, so I pulled them out.

## Install

```bash
pip install task-queue
```

## Usage

```python
from task_queue import taskQueue

result = taskQueue("example")
print(result)
```

## Notes

- No runtime dependencies outside the standard library.
- Tested on Python 3.9 and newer.

## License

MIT
