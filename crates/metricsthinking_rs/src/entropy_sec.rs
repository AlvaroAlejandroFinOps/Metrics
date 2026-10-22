use std::collections::HashMap;

pub fn fast_shannon_entropy(data: &str) -> f64 {
    if data.is_empty() {
        return 0.0;
    }
    let len = data.len() as f64;
    let mut counts: HashMap<char, usize> = HashMap::new();
    for c in data.chars() {
        *counts.entry(c).or_insert(0) += 1;
    }

    let mut entropy = 0.0;
    for &count in counts.values() {
        let p = (count as f64) / len;
        entropy -= p * p.log2();
    }
    entropy
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_zero_entropy() {
        assert_eq!(fast_shannon_entropy(""), 0.0);
        assert_eq!(fast_shannon_entropy("aaaaaaaa"), 0.0);
    }

    #[test]
    fn test_high_entropy() {
        let ent = fast_shannon_entropy("placeholder_key_abcdefghijklmnopqrstuvwxyz0123456789+/=");
        assert!(ent > 4.5);
    }
}
