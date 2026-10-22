use std::collections::{HashMap, HashSet};
use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct CouplingMetricsRs {
    pub afferent_ca: HashMap<String, usize>,
    pub efferent_ce: HashMap<String, usize>,
    pub instability_i: HashMap<String, f64>,
    pub spof_nodes: Vec<String>,
}

pub fn analyze_python_dependencies(files: &HashMap<String, String>) -> CouplingMetricsRs {
    let mut import_graph: HashMap<String, HashSet<String>> = HashMap::new();
    let mut all_modules: HashSet<String> = HashSet::new();

    for path in files.keys() {
        let mod_name = path
            .trim_end_matches(".py")
            .replace('/', ".")
            .replace('\\', ".");
        all_modules.insert(mod_name.clone());
        import_graph.insert(mod_name, HashSet::new());
    }

    // Simple regex-free scanner for imports
    for (path, content) in files {
        let mod_name = path
            .trim_end_matches(".py")
            .replace('/', ".")
            .replace('\\', ".");

        let mut deps = HashSet::new();
        for line in content.lines() {
            let trimmed = line.trim();
            if trimmed.starts_with("import ") || trimmed.starts_with("from ") {
                for other in &all_modules {
                    if other != &mod_name && (trimmed.contains(other) || trimmed.contains(&other.replace('.', "/"))) {
                        deps.insert(other.clone());
                    }
                }
            }
        }
        import_graph.insert(mod_name, deps);
    }

    let mut ca: HashMap<String, usize> = HashMap::new();
    let mut ce: HashMap<String, usize> = HashMap::new();
    let mut instability: HashMap<String, f64> = HashMap::new();

    for m in &all_modules {
        ca.insert(m.clone(), 0);
        ce.insert(m.clone(), 0);
    }

    for (src, targets) in &import_graph {
        ce.insert(src.clone(), targets.len());
        for target in targets {
            *ca.entry(target.clone()).or_insert(0) += 1;
        }
    }

    let mut spof_nodes = Vec::new();

    for m in &all_modules {
        let aff = *ca.get(m).unwrap_or(&0) as f64;
        let eff = *ce.get(m).unwrap_or(&0) as f64;
        let total = aff + eff;
        let inst = if total > 0.0 { eff / total } else { 0.0 };
        instability.insert(m.clone(), (inst * 1000.0).round() / 1000.0);

        // SPOF: high afferent coupling (>= 3) and zero or single redundancy
        if aff >= 3.0 && eff <= 1.0 {
            spof_nodes.push(m.clone());
        }
    }

    spof_nodes.sort();

    CouplingMetricsRs {
        afferent_ca: ca,
        efferent_ce: ce,
        instability_i: instability,
        spof_nodes,
    }
}
