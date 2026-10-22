"""
Benchmark Consolidator for MetricsThinking™
Gathers audit results from target repositories and outputs a detailed comparative benchmark.
"""

import json
import shutil
from pathlib import Path


def main():
    root_dir = Path(__file__).resolve().parent.parent
    benchmark_dir = root_dir / "artifacts" / "benchmark"
    benchmark_dir.mkdir(parents=True, exist_ok=True)

    repos = [
        {
            "id": "flowagentic",
            "name": "FlowAgentic",
            "path": Path(r"D:\0001 HyperScale Thinking\PROYECTOS CLOUD\iContext\FlowAgentic"),
        },
        {
            "id": "thinkingseed",
            "name": "ThinkingSeed",
            "path": Path(r"D:\0001 HyperScale Thinking\PROYECTOS CLOUD\iContext\ThinkingSeed"),
        },
        {
            "id": "semanticflow",
            "name": "SemanticFlow",
            "path": Path(r"D:\0001 HyperScale Thinking\PROYECTOS CLOUD\Data & AI Strategy\SemanticFlow"),
        },
    ]

    benchmark_data = []

    for r in repos:
        artifacts_path = r["path"] / "artifacts"
        json_path = artifacts_path / "MetricsThinking.json"
        md_path = artifacts_path / "MetricsThinking.md"
        roadmap_path = artifacts_path / "plans" / "active" / "INFERRED_ROADMAP.md"

        dest_json = benchmark_dir / f"{r['name']}_MetricsThinking.json"
        dest_md = benchmark_dir / f"{r['name']}_MetricsThinking.md"
        dest_roadmap = benchmark_dir / f"{r['name']}_INFERRED_ROADMAP.md"

        if json_path.exists():
            shutil.copy2(json_path, dest_json)
            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            fpai = data.get("fpai_vector", {})
            spectral_pf = fpai.get("spectral_power_factor", 1.0)
            
            # Calculate total files from evidence_primitives
            ev_prims = data.get("evidence_primitives", {})
            total_files = sum(p.get("file_count", 0) for p in ev_prims.values())

            # Calculate fulfilled criteria
            all_criteria = []
            for m in data.get("modules", []):
                for c in m.get("criteria", []):
                    all_criteria.append(c)

            criteria_met = sum(1 for c in all_criteria if c.get("fulfilled", False))
            criteria_total = len(all_criteria)

            repo_summary = {
                "repo_name": r["name"],
                "repo_path": str(r["path"]),
                "score": data.get("consolidated_score", 0.0),
                "maturity_band": data.get("maturity_band", ""),
                "archetype": data.get("domain_archetype", ""),
                "inspection_mode": data.get("inspection_mode", ""),
                "active_bottleneck": data.get("active_bottleneck", ""),
                "total_files": total_files,
                "criteria_met": criteria_met,
                "criteria_total": criteria_total,
                "spectral_pf": spectral_pf,
                "modules": []
            }

            for m in data.get("modules", []):
                repo_summary["modules"].append({
                    "id": m.get("module_id"),
                    "name": m.get("name"),
                    "weight": m.get("weight"),
                    "pct": m.get("phase_completion_pct"),
                    "status": m.get("status")
                })

            benchmark_data.append(repo_summary)

        if md_path.exists():
            shutil.copy2(md_path, dest_md)
        if roadmap_path.exists():
            shutil.copy2(roadmap_path, dest_roadmap)

    # Write JSON summary
    summary_json_file = benchmark_dir / "benchmark_summary.json"
    with open(summary_json_file, "w", encoding="utf-8") as f:
        json.dump(benchmark_data, f, indent=2, ensure_ascii=False)

    # Generate Comparative Markdown Report
    md_lines = [
        "# METRICSTHINKING™: Repositories Forensic Benchmark Report",
        "",
        "> **Target Repositories:** `FlowAgentic`, `ThinkingSeed`, `SemanticFlow`  ",
        "> **Audit Engine:** `MetricsThinking™ Universal Auditor (Ground Truth First)`  ",
        "> **Location:** `artifacts/benchmark/`  ",
        "",
        "---",
        "",
        "## 1. Executive Summary & Benchmark Matrix",
        "",
        "| Repositorio | Arquetipo | Modo Inspección | Archivos Clasificados | Criterios Cumplidos | Score Global | Banda de Madurez | Cuello de Botella Activo |",
        "|:---|:---|:---|:---:|:---:|:---:|:---|:---|"
    ]

    for item in benchmark_data:
        crit_str = f"`{item['criteria_met']} / {item['criteria_total']}`"
        score_str = f"**`{item['score']:.2f}%`**"
        bottleneck_short = item['active_bottleneck'].split('.')[0] if item['active_bottleneck'] else "Ninguno"
        md_lines.append(
            f"| **{item['repo_name']}** | `{item['archetype']}` | `{item['inspection_mode']}` | `{item['total_files']}` | {crit_str} | {score_str} | {item['maturity_band']} | {bottleneck_short} |"
        )

    md_lines.extend([
        "",
        "---",
        "",
        "## 2. Canonical Modules Cross-Comparison (M01 - M10)",
        "",
        "| ID | Módulo Canónico | FlowAgentic | ThinkingSeed | SemanticFlow |",
        "|:---|:---|:---:|:---:|:---:|"
    ])

    module_ids = ["M01", "M02", "M03", "M04", "M05", "M06", "M07", "M08", "M09", "M10"]
    canonical_names = {
        "M01": "Descubrimiento / Definición",
        "M02": "Arquitectura y Diseño",
        "M03": "Gobernanza y Guardrails",
        "M04": "Aprovisionamiento / Readiness",
        "M05": "Construcción Núcleo (Core)",
        "M06": "Integración / Interoperabilidad",
        "M07": "Aseguramiento de Calidad (QA)",
        "M08": "Validación y Operación",
        "M09": "Despliegue y CI/CD",
        "M10": "Cierre, Roadmap y Extensibilidad"
    }

    for mid in module_ids:
        row = [f"`{mid}`", canonical_names.get(mid, mid)]
        for item in benchmark_data:
            mod_data = next((m for m in item["modules"] if m["id"] == mid), None)
            if mod_data:
                pct = mod_data["pct"]
                badge = f"✅ `{pct:.1f}%`" if pct == 100.0 else (f"⚠️ `{pct:.1f}%`" if pct >= 50.0 else f"❌ `{pct:.1f}%`")
                row.append(badge)
            else:
                row.append("N/A")
        md_lines.append(f"| {' | '.join(row)} |")

    md_lines.extend([
        "",
        "---",
        "",
        "## 3. Repositorios y Rutas Locales",
        "",
        "- **FlowAgentic:**",
        "  - Ruta física auditada: `D:\\0001 HyperScale Thinking\\PROYECTOS CLOUD\\iContext\\FlowAgentic`",
        "  - Artefactos locales generados: `FlowAgentic\\artifacts\\MetricsThinking.md`, `.json`, `INFERRED_ROADMAP.md`",
        "  - Copia de benchmarking: [FlowAgentic_MetricsThinking.md](./FlowAgentic_MetricsThinking.md) | [JSON](./FlowAgentic_MetricsThinking.json)",
        "- **ThinkingSeed:**",
        "  - Ruta física auditada: `D:\\0001 HyperScale Thinking\\PROYECTOS CLOUD\\iContext\\ThinkingSeed`",
        "  - Artefactos locales generados: `ThinkingSeed\\artifacts\\MetricsThinking.md`, `.json`, `INFERRED_ROADMAP.md`",
        "  - Copia de benchmarking: [ThinkingSeed_MetricsThinking.md](./ThinkingSeed_MetricsThinking.md) | [JSON](./ThinkingSeed_MetricsThinking.json)",
        "- **SemanticFlow:**",
        "  - Ruta física auditada: `D:\\0001 HyperScale Thinking\\PROYECTOS CLOUD\\Data & AI Strategy\\SemanticFlow`",
        "  - Artefactos locales generados: `SemanticFlow\\artifacts\\MetricsThinking.md`, `.json`, `INFERRED_ROADMAP.md`",
        "  - Copia de benchmarking: [SemanticFlow_MetricsThinking.md](./SemanticFlow_MetricsThinking.md) | [JSON](./SemanticFlow_MetricsThinking.json)",
        "",
        "---",
        "",
        "## 4. Hallazgos y Análisis Comparativo",
        "",
        "1. **ThinkingSeed (`97.00%` - Excelencia Operativa / Producción):**",
        "   - **Arquetipo:** `agent-skill` (Modo: `governance_spec`).",
        "   - Auto-detectado con alta precisión a partir de la presencia de `SKILL.md` y estructura de agentes.",
        "   - 9 de 10 módulos al 100%. Cuello de botella en `M06: Interoperabilidad Multi-Agente` (80.0%).",
        "2. **SemanticFlow (`95.00%` - Excelencia Operativa / Producción):**",
        "   - **Arquetipo:** `software-engineering` (Modo: `source_code`).",
        "   - Repositorio corporativo de gran envergadura (más de 1,300 archivos escaneados).",
        "   - Cobertura total de Core Engine, QA y CI/CD. Cuello de botella en `M06: Integración e Interoperabilidad` (80.0%) y `M08: Validación` (80.0%).",
        "3. **FlowAgentic (`63.42%` - Construcción Activa / Madurez Media):**",
        "   - **Arquetipo:** `software-engineering` (Modo: `source_code`).",
        "   - Proyecto en fase constructiva. Posee cimientos sólidos en diseño y alcance (M01: 100%, M02: 100%, M04: 100%).",
        "   - Cuello de botella activo: `M03: Gobernanza y Cumplimiento` (66.7%). Requiere atención prioritaria en QA (`M07: 33.3%`), Integración (`M06: 40.0%`) y Validación organizativa (`M08: 20.0%`)."
    ])

    report_file = benchmark_dir / "BENCHMARK_REPORT.md"
    with open(report_file, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))

    print(f"Benchmark completed successfully! Artifacts stored at: {benchmark_dir}")


if __name__ == "__main__":
    main()
