"""Save a small streamed MIST sample without downloading the full dataset."""

import argparse
import json
from pathlib import Path


DATASET_ID = "jongwonryu/MIST-autonomous-driving-dataset"


def save_preview(dataset, output, limit):
    if limit < 1:
        raise ValueError("limit must be positive.")
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    records = []
    for index, sample in enumerate(dataset.take(limit)):
        image = sample["image"]
        image_name = f"sample_{index:03d}.png"
        image.save(output / image_name)
        records.append({
            "image": image_name, "text": sample["text"],
            "width": image.width, "height": image.height,
        })
    with (output / "samples.json").open("w", encoding="utf-8") as handle:
        json.dump(records, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    return records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--split", choices=("train", "test"), default="test")
    parser.add_argument("--limit", type=int, default=3)
    parser.add_argument("--output", type=Path, default=Path("outputs/preview"))
    args = parser.parse_args()
    if args.limit < 1:
        parser.error("--limit must be positive.")
    from datasets import load_dataset

    dataset = load_dataset(DATASET_ID, split=args.split, streaming=True)
    records = save_preview(dataset, args.output, args.limit)
    for record in records:
        print(f"{record['image']}: {record['text']} ({record['width']}x{record['height']})")
    print(f"Saved {len(records)} samples to {args.output}")


if __name__ == "__main__":
    main()
