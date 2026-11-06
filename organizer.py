#!/usr/bin/env python3

import shutil
from pathlib import Path

EXTENSION_MAP = {
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".bmp": "Images",
    ".mp4": "Videos",
    ".avi": "Videos",
    ".mov": "Videos",
    ".mkv": "Videos",
    ".zip": "Archives",
    ".rar": "Archives",
    ".tar": "Archives",
    ".gz": "Archives",
    ".py": "Code",
    ".js": "Code",
    ".ts": "Code",
    ".java": "Code",
    ".cpp": "Code",
    ".cs": "Code",
    ".html": "Code",
    ".css": "Code",
    ".json": "Code",
}


def get_category_for_file(file_path):
    suffix = file_path.suffix.lower()
    return EXTENSION_MAP.get(suffix, "Other")


def ensure_category_folder(target_dir, category_name):
    folder = target_dir / category_name
    folder.mkdir(exist_ok=True)
    return folder


def safe_move_file(source_file, destination_dir):
    destination_path = destination_dir / source_file.name
    if destination_path.exists():
        stem = source_file.stem
        suffix = source_file.suffix
        counter = 1
        while True:
            candidate = destination_dir / f"{stem}_{counter}{suffix}"
            if not candidate.exists():
                destination_path = candidate
                break
            counter += 1

    shutil.move(str(source_file), str(destination_path))
    return destination_path


def organize_directory(target_dir):
    target_dir = Path(target_dir)
    moved_count = 0
    skipped = []

    for item in target_dir.iterdir():
        if item.is_dir():
            continue

        category = get_category_for_file(item)
        if category == "Other":
            continue

        try:
            category_dir = ensure_category_folder(target_dir, category)
            safe_move_file(item, category_dir)
            moved_count += 1
        except PermissionError as exc:
            skipped.append((item.name, f"PermissionError: {exc}"))
        except FileExistsError as exc:
            skipped.append((item.name, f"FileExistsError: {exc}"))
        except OSError as exc:
            skipped.append((item.name, f"OS error: {exc}"))

    print(f"\nOrganization complete.")
    print(f"Files relocated: {moved_count}")
    if skipped:
        print("Skipped files:")
        for name, reason in skipped:
            print(f" - {name}: {reason}")
    else:
        print("No files were skipped.")

    return moved_count


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = input("Enter directory to organize: ").strip() or "."

    organize_directory(directory)
