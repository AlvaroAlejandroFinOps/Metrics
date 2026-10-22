use pyo3::prelude::*;
use std::collections::HashMap;

mod ast_graph;
mod ballast_tokens;
mod entropy_sec;
mod walker;

use ast_graph::analyze_python_dependencies;
use ballast_tokens::calculate_shingling_jaccard as calc_jaccard;
use entropy_sec::fast_shannon_entropy as calc_entropy;
use walker::walk_directory;

#[pyfunction]
#[pyo3(signature = (path, ignore_patterns=None, include_content=true))]
fn scan_directory(
    py: Python<'_>,
    path: &str,
    ignore_patterns: Option<Vec<String>>,
    include_content: Option<bool>,
) -> PyResult<PyObject> {
    let pats = ignore_patterns.unwrap_or_default();
    let inc = include_content.unwrap_or(true);

    match walk_directory(path, &pats, inc) {
        Ok(records) => {
            let json_str = serde_json::to_string(&records)
                .map_err(|e| pyo3::exceptions::PyValueError::new_err(e.to_string()))?;
            let json_module = py.import("json")?;
            let py_val = json_module.call_method1("loads", (json_str,))?;
            Ok(py_val.into())
        }
        Err(e) => Err(pyo3::exceptions::PyIOError::new_err(e)),
    }
}

#[pyfunction]
fn fast_shannon_entropy(data: &str) -> PyResult<f64> {
    Ok(calc_entropy(data))
}

#[pyfunction]
#[pyo3(signature = (a, b, k=3))]
fn calculate_shingling_jaccard(a: &str, b: &str, k: Option<usize>) -> PyResult<f64> {
    Ok(calc_jaccard(a, b, k.unwrap_or(3)))
}

#[pyfunction]
fn compute_ast_coupling(
    py: Python<'_>,
    python_files: HashMap<String, String>,
) -> PyResult<PyObject> {
    let metrics = analyze_python_dependencies(&python_files);
    let json_str = serde_json::to_string(&metrics)
        .map_err(|e| pyo3::exceptions::PyValueError::new_err(e.to_string()))?;
    let json_module = py.import("json")?;
    let py_val = json_module.call_method1("loads", (json_str,))?;
    Ok(py_val.into())
}

#[pymodule]
fn _core_rs(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(scan_directory, m)?)?;
    m.add_function(wrap_pyfunction!(fast_shannon_entropy, m)?)?;
    m.add_function(wrap_pyfunction!(calculate_shingling_jaccard, m)?)?;
    m.add_function(wrap_pyfunction!(compute_ast_coupling, m)?)?;
    Ok(())
}
