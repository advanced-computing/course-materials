## Setup

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Viewing slides

```sh
jupyter nbconvert --to slides \
   --SlidesExporter.reveal_scroll=True \
   --post serve lectures/lecture_NN.ipynb
```
