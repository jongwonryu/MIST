# MIST

**Multi-Domain Synthetic Dataset for Rural Driving**

[![Paper](https://img.shields.io/badge/Paper-IEEE_Access_2026-00629B)](https://doi.org/10.1109/ACCESS.2026.3725755)
[![Dataset](https://img.shields.io/badge/Dataset-Hugging_Face-FFD21E)](https://huggingface.co/datasets/jongwonryu/MIST-autonomous-driving-dataset)
[![Simulator](https://img.shields.io/badge/Simulator-Slowroads-426C4D)](https://slowroads.io)

**Jongwon Ryu, Jaehoon Go, Trung X. Pham, and Junyeong Kim**

<p align="center">
  <img src="https://cdn-uploads.huggingface.co/production/uploads/6510f03888cdfe73a89a4bd6/KVt3wsGvHbBMxWZd0rmFG.png" alt="MIST rural driving dataset overview" width="800">
</p>

MIST is a synthetic rural-driving dataset for studying environmental domain
variation. This repository accompanies [the paper](https://doi.org/10.1109/ACCESS.2026.3725755)
and provides documentation and dataset-access examples. The image data is hosted
on [Hugging Face](https://huggingface.co/datasets/jongwonryu/MIST-autonomous-driving-dataset),
not in GitHub.

This repository was previously named **SMS** and is now named **MIST** to match
the published paper and dataset.

## Overview

Unlike urban-centric driving data, MIST focuses on rural roads and variations in
background appearance. Scenes are generated with [Slowroads](https://slowroads.io)
and organized into **32 balanced domain configurations**:

| Factor | Values |
| --- | --- |
| Season | Spring, summer, autumn, winter |
| Time of day | Dawn, daytime, dusk, night |
| Weather | Clear, overcast |

The dataset supports research on multi-domain image-to-image translation,
vision-language analysis, and environmental domain shifts. Domain labels are
provided as text, such as `autumn dawn clear weather rural road`.

## Public Data

The current Hugging Face release provides image-text pairs in Parquet format:

| Split | Image-text pairs |
| --- | ---: |
| Train | 32,000 |
| Test | 3,200 |
| Total | 35,200 |

| Field | Content |
| --- | --- |
| `image` | Rural-driving image, decoded as a PIL image when loaded |
| `text` | Text description of the environmental domain |

The released files occupy approximately **73 GB** compressed. Streaming is
recommended for inspecting a few samples without downloading the full release.
These counts describe the current public subset, not the full dataset described
by the paper.

The dataset card lists segmentation annotations and remaining data as ongoing
release work. The current default configuration contains only `image` and `text`;
do not assume that segmentation masks are already included. Check the
[dataset card and files](https://huggingface.co/datasets/jongwonryu/MIST-autonomous-driving-dataset/tree/main)
for the latest availability.

## Quick Start

Use Python 3.10 or newer:

```bash
git clone https://github.com/jongwonryu/MIST.git
cd MIST
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Save three streamed test images and their domain descriptions.
python examples/preview_dataset.py --split test --limit 3 --output outputs/preview
```

The requirements pin the tested Datasets version to avoid a reported
[partial-Parquet-stream shutdown issue](https://github.com/huggingface/datasets/issues/7357)
in newer scanner releases.

Or use Hugging Face Datasets directly:

```python
from datasets import load_dataset

dataset = load_dataset(
    "jongwonryu/MIST-autonomous-driving-dataset",
    split="test",
    streaming=True,
)
sample = next(iter(dataset))
print(sample["text"])
print(sample["image"].size)
sample["image"].save("mist_sample.png")
```

Image dimensions should be read from the loaded sample rather than assumed from
the simulator's original rendering settings. Set `streaming=False` only when
you intend to download and cache the requested split locally.

## Repository Scope

This GitHub release contains dataset documentation, citation metadata, and a
small preview utility. It does not currently contain the simulator modifications,
dataset-generation pipeline, or training/evaluation code used in the paper.

## Citation

```bibtex
@article{ryu2026mist,
  title   = {{MIST}: Multi-Domain Synthetic Dataset for Rural Driving},
  author  = {Ryu, Jongwon and Go, Jaehoon and Pham, Trung X. and Kim, Junyeong},
  journal = {IEEE Access},
  volume  = {14},
  pages   = {132866--132877},
  year    = {2026},
  doi     = {10.1109/ACCESS.2026.3725755}
}
```

## License and Contact

The Hugging Face dataset card declares **Apache-2.0** for the dataset. No separate
software license has been specified for this GitHub repository. Refer to the
dataset card and applicable simulator terms when reusing those materials.

Jongwon Ryu: `fbwhddnjs511@cau.ac.kr`.
