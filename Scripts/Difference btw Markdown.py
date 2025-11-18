#!/usr/bin/env python3
"""
Compare two English doc folders and extract diffs for Markdown files.

Usage:
  python scripts/diff_markdown.py docs/en/v0.54 docs/en/v0.55 diff_output

It will create:
  diff_output/
    summary.csv                     <- overview of added/removed/modified files
    added/<relpath>.md              <- new files to translate
    removed/<relpath>.md            <- files that disappeared
    diffs/<relpath>.diff            <- unified diff (for review)
    changes_new/<relpath>.md        <- only the NEW/changed lines (for translation)
    changes_old/<relpath>.md        <- the OLD lines that were replaced/removed (context)
"""

import filecmp
import difflib
from pathlib import Path
import shutil
import csv

# Paths
old_version = Path.home() / "Documents/Metabase/docs-0.54"
new_version = Path.home() / "Documents/Metabase/docs"
output_dir = Path.home() / "Documents/Metabase/diff_output1"

# Output subfolders
added_dir = output_dir / "added"
removed_dir = output_dir / "removed"
diffs_dir = output_dir / "diffs"
changes_new_dir = output_dir / "changes_new"
changes_old_dir = output_dir / "changes_old"

# Clean/create output
if output_dir.exists():
    shutil.rmtree(output_dir)
for d in [added_dir, removed_dir, diffs_dir, changes_new_dir, changes_old_dir]:
    d.mkdir(parents=True, exist_ok=True)

summary_path = output_dir / "summary.csv"

# Helper to copy files
def copy_file(src, dest_dir, rel_path):
    dest_path = dest_dir / rel_path
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest_path)

# Compare directories recursively
def compare_dirs(d1, d2, rel_path=""):
    cmp = filecmp.dircmp(d1, d2)

    # Added files
    for f in cmp.right_only:
        src_file = d2 / f
        if src_file.is_file() and f.endswith(".md"):
            copy_file(src_file, added_dir, Path(rel_path) / f)
            summary_rows.append([rel_path + f, "ADDED"])
    
    # Removed files
    for f in cmp.left_only:
        src_file = d1 / f
        if src_file.is_file() and f.endswith(".md"):
            copy_file(src_file, removed_dir, Path(rel_path) / f)
            summary_rows.append([rel_path + f, "REMOVED"])
    
    # Modified files
    for f in cmp.common_files:
        if f.endswith(".md"):
            old_file = d1 / f
            new_file = d2 / f
            with open(old_file, encoding="utf-8") as of, open(new_file, encoding="utf-8") as nf:
                old_lines = of.readlines()
                new_lines = nf.readlines()
                if old_lines != new_lines:
                    rel_file_path = Path(rel_path) / f
                    
                    # --- Create diff with line numbers ---
                    diff_lines = []
                    old_line_num = 0
                    new_line_num = 0

                    for line in difflib.unified_diff(
                        old_lines, new_lines,
                        fromfile=str(old_file),
                        tofile=str(new_file),
                        lineterm=""
                    ):
                        if line.startswith("@@"):
                            # Parse hunk header for resetting counters
                            # Format: @@ -old_start,old_len +new_start,new_len @@
                            parts = line.split()
                            old_start = int(parts[1].split(",")[0][1:])
                            new_start = int(parts[2].split(",")[0][1:])
                            old_line_num = old_start
                            new_line_num = new_start
                            diff_lines.append(line)
                        elif line.startswith("-") and not line.startswith("---"):
                            diff_lines.append(f"- [OLD:{old_line_num}] {line[1:]}")
                            old_line_num += 1
                        elif line.startswith("+") and not line.startswith("+++"):
                            diff_lines.append(f"+ [NEW:{new_line_num}] {line[1:]}")
                            new_line_num += 1
                        else:
                            diff_lines.append(line)
                            if not line.startswith("\\"):
                                old_line_num += 1
                                new_line_num += 1

                    diff_file_path = diffs_dir / f"{rel_file_path}.diff"
                    diff_file_path.parent.mkdir(parents=True, exist_ok=True)
                    with open(diff_file_path, "w", encoding="utf-8") as df:
                        df.write("\n".join(diff_lines))
                    
                    # --- Extract changes_new and changes_old ---
                    new_changed_lines = []
                    old_changed_lines = []
                    old_line_num = 0
                    new_line_num = 0
                    for line in difflib.ndiff(old_lines, new_lines):
                        if line.startswith("  "):
                            old_line_num += 1
                            new_line_num += 1
                        elif line.startswith("- "):
                            old_line_num += 1
                            old_changed_lines.append(f"[Line {old_line_num}] {line[2:]}")
                        elif line.startswith("+ "):
                            new_line_num += 1
                            new_changed_lines.append(f"[Line {new_line_num}] {line[2:]}")
                    
                    # Save changes_new
                    if new_changed_lines:
                        new_changes_file = changes_new_dir / rel_file_path
                        new_changes_file.parent.mkdir(parents=True, exist_ok=True)
                        with open(new_changes_file, "w", encoding="utf-8") as nf:
                            nf.writelines(new_changed_lines)
                    
                    # Save changes_old
                    if old_changed_lines:
                        old_changes_file = changes_old_dir / rel_file_path
                        old_changes_file.parent.mkdir(parents=True, exist_ok=True)
                        with open(old_changes_file, "w", encoding="utf-8") as of:
                            of.writelines(old_changed_lines)

                    summary_rows.append([str(rel_file_path), "MODIFIED"])

    # Recurse into common subdirectories
    for subdir in cmp.common_dirs:
        compare_dirs(d1 / subdir, d2 / subdir, rel_path + subdir + "/")

# Collect summary rows
summary_rows = []
compare_dirs(old_version, new_version)

# Write summary.csv
with open(summary_path, "w", encoding="utf-8", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["File", "Status"])
    writer.writerows(summary_rows)

print(f" Diff completed. Results saved in: {output_dir}")
