use serde::{Deserialize, Serialize};
use sha2::{Digest, Sha256};
use std::fs;
use std::path::Path;

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ScannedFileRecord {
    pub path: String,
    pub size_bytes: usize,
    pub line_count: usize,
    pub sha256: String,
    pub token_estimate: usize,
    pub content: Option<String>,
}

pub fn walk_directory(
    root_path: &str,
    ignore_patterns: &[String],
    include_content: bool,
) -> Result<Vec<ScannedFileRecord>, String> {
    let root = Path::new(root_path);
    if !root.exists() {
        return Err(format!("Root directory does not exist: {}", root_path));
    }

    let mut records = Vec::new();
    let mut stack = vec![root.to_path_buf()];

    while let Some(current_dir) = stack.pop() {
        let entries = match fs::read_dir(&current_dir) {
            Ok(e) => e,
            Err(_) => continue,
        };

        for entry in entries.flatten() {
            let path = entry.path();
            let rel_path = match path.strip_prefix(root) {
                Ok(p) => p.to_string_lossy().replace('\\', "/"),
                Err(_) => path.to_string_lossy().replace('\\', "/"),
            };

            // Check ignore patterns
            let mut skip = false;
            for pat in ignore_patterns {
                if rel_path.starts_with(pat) || rel_path.contains(&format!("/{}/", pat)) || rel_path.ends_with(pat) {
                    skip = true;
                    break;
                }
            }
            if skip || rel_path == ".git" || rel_path.starts_with(".git/") || rel_path.contains("__pycache__") {
                continue;
            }

            if path.is_dir() {
                stack.push(path);
            } else if path.is_file() {
                if let Ok(metadata) = entry.metadata() {
                    let size_bytes = metadata.len() as usize;

                    // Read content safely up to 2MB
                    let content_str = if size_bytes < 2 * 1024 * 1024 {
                        fs::read_to_string(&path).ok()
                    } else {
                        None
                    };

                    let line_count = content_str.as_ref().map(|s| s.lines().count()).unwrap_or(0);
                    let token_estimate = size_bytes / 4;

                    // Compute SHA-256
                    let mut hasher = Sha256::new();
                    if let Some(ref c) = content_str {
                        hasher.update(c.as_bytes());
                    } else if let Ok(bytes) = fs::read(&path) {
                        hasher.update(&bytes);
                    }
                    let hash_str = format!("{:x}", hasher.finalize());

                    records.push(ScannedFileRecord {
                        path: rel_path,
                        size_bytes,
                        line_count,
                        sha256: hash_str,
                        token_estimate,
                        content: if include_content { content_str } else { None },
                    });
                }
            }
        }
    }

    records.sort_by(|a, b| a.path.cmp(&b.path));
    Ok(records)
}
