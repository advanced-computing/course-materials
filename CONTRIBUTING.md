## Setup

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Viewing slides

They are built in [Remark](https://github.com/gnab/remark).

1. From this directory, start the server.

   ```sh
   python3 -m http.server
   ```

1. Open http://localhost:8000/slides.html?lecture=01, replacing the slide number.
