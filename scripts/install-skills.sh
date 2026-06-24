#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source_dir="$repo_root/skills"
codex_home="${CODEX_HOME:-$HOME/.codex}"
target_dir="$codex_home/skills"
mode="${1:-copy}"
strict_prereqs="${NAHIDA_STRICT_PREREQS:-0}"
required_skills=(obsidian-markdown obsidian-note)
preferred_skills=(obsidian-bases json-canvas)

if [[ ! -d "$source_dir" ]]; then
  echo "Nahida skills directory not found: $source_dir" >&2
  exit 1
fi

mkdir -p "$target_dir"

for skill in "$source_dir"/nahida-*; do
  [[ -d "$skill" ]] || continue
  name="$(basename "$skill")"
  dest="$target_dir/$name"

  case "$mode" in
    copy)
      rm -rf "$dest"
      cp -R "$skill" "$dest"
      echo "installed $name -> $dest"
      ;;
    link)
      rm -rf "$dest"
      ln -s "$skill" "$dest"
      echo "linked $name -> $dest"
      ;;
    dry-run)
      echo "would install $name -> $dest"
      ;;
    *)
      echo "usage: $0 [copy|link|dry-run]" >&2
      exit 2
      ;;
  esac
done

if [[ "$mode" == "dry-run" ]]; then
  echo "Dry run complete. Nahida skills would be installed in $target_dir"
else
  echo "Nahida skills installed in $target_dir"
fi

missing_required=()
for prereq in "${required_skills[@]}"; do
  if [[ ! -f "$target_dir/$prereq/SKILL.md" ]]; then
    missing_required+=("$prereq")
  fi
done

missing_preferred=()
for prereq in "${preferred_skills[@]}"; do
  if [[ ! -f "$target_dir/$prereq/SKILL.md" ]]; then
    missing_preferred+=("$prereq")
  fi
done

if (( ${#missing_required[@]} > 0 )); then
  echo "Missing required prerequisite skills: ${missing_required[*]}" >&2
  echo "Nahida can install, but full-fidelity vault writes should stop with prerequisite_gap until these are installed." >&2
  if [[ "$strict_prereqs" == "1" ]]; then
    exit 3
  fi
fi

if (( ${#missing_preferred[@]} > 0 )); then
  echo "Missing preferred prerequisite skills: ${missing_preferred[*]}" >&2
  echo "Bases/Canvas features will be skipped or recorded as fallback gaps when needed." >&2
fi
