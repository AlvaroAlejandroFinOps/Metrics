use std::collections::HashSet;

pub fn extract_shingles(text: &str, k: usize) -> HashSet<String> {
    let words: Vec<&str> = text.split_whitespace().collect();
    let mut shingles = HashSet::new();
    if words.len() < k {
        for w in words {
            shingles.insert(w.to_lowercase());
        }
        return shingles;
    }
    for i in 0..=(words.len() - k) {
        let shingle = words[i..i + k].join(" ").to_lowercase();
        shingles.insert(shingle);
    }
    shingles
}

pub fn calculate_shingling_jaccard(a: &str, b: &str, k: usize) -> f64 {
    let set_a = extract_shingles(a, k);
    let set_b = extract_shingles(b, k);

    let intersection = set_a.intersection(&set_b).count();
    let union = set_a.union(&set_b).count();

    if union == 0 {
        return 0.0;
    }
    (intersection as f64) / (union as f64)
}

pub fn estimate_tokens(text: &str) -> usize {
    // Standard rule: ~4 chars per token, minimum 1 if text is non-empty
    if text.is_empty() {
        0
    } else {
        (text.len() / 4).max(1)
    }
}
