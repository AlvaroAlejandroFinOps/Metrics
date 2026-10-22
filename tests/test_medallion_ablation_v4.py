"""
Automated validation of FEP-006: Medallion Pipeline, Ablation, and Attribution.
"""
import json
from pathlib import Path
from metricsthinking.fpai.medallion import run_local_medallion_pipeline
from metricsthinking.fpai.ablation import run_ablation_sampling
from metricsthinking.fpai.attribution import resolve_context_attribution
from scripts.hnsw_index_rebuild import rebuild_hnsw_index


def test_local_medallion_pipeline(tmp_path):
    raw_dir = tmp_path / "raw"
    processed_dir = tmp_path / "processed"
    raw_dir.mkdir()

    event1 = {
        "event_id": "evt-001",
        "timestamp": "2026-10-21T12:00:00Z",
        "repo_id": "repo-alpha",
        "tokens_by_phase": {"stored_tokens": 1000, "scanned_tokens": 800},
        "attribution_summary": {"active_tokens": 600, "reactive_tokens": 200, "fpai_spectral": 0.88, "fpai_linear": 0.75},
    }
    # Duplicate event
    event2 = dict(event1)
    event3 = {
        "event_id": "evt-002",
        "timestamp": "2026-10-21T12:01:00Z",
        "repo_id": "repo-alpha",
        "tokens_by_phase": {"stored_tokens": 2000, "scanned_tokens": 1500},
        "attribution_summary": {"active_tokens": 1400, "reactive_tokens": 100, "fpai_spectral": 0.95, "fpai_linear": 0.93},
    }

    f1 = raw_dir / "events_1.jsonl"
    with open(f1, "w", encoding="utf-8") as f:
        f.write(json.dumps(event1) + "\n")
        f.write(json.dumps(event2) + "\n")
        f.write(json.dumps(event3) + "\n")

    summary = run_local_medallion_pipeline(str(raw_dir), str(processed_dir))
    assert summary["raw_read"] == 3
    assert summary["new_silver_written"] == 2
    assert summary["duplicates_dropped"] == 1

    silver_file = processed_dir / "silver_events.jsonl"
    gold_file = processed_dir / "gold_metrics.json"
    assert silver_file.exists()
    assert gold_file.exists()

    gold = json.loads(gold_file.read_text(encoding="utf-8"))
    assert gold["total_events"] == 2
    assert gold["total_active_tokens"] == 2000
    assert gold["average_fpai_spectral"] > 0.90


def test_ablation_sampling():
    chunks = [
        {"chunk_id": f"chunk_{i}", "content": f"def function_{i}(param_a, param_b):\n    return param_a + {i}\n"}
        for i in range(25)
    ]
    res = run_ablation_sampling(chunks, sample_ratio=0.08)
    assert res["total_chunks"] == 25
    assert res["sampled_chunks_count"] == 2  # ceil(25 * 0.08) = 2
    assert len(res["marginal_values"]) == 2
    assert res["average_marginal_value"] > 0.0


def test_context_attribution():
    chunks = [
        {
            "chunk_id": "c1",
            "content": "from metricsthinking.models import ProjectAuditReport\ndef evaluate_project():\n    pass\n",
        },
        {
            "chunk_id": "c2",
            "content": "import pandas as pd\ndf = pd.read_parquet('data.parquet')\n",
        },
    ]

    # Query matching c1
    query = "Where is ProjectAuditReport defined and how is it imported?"
    attrib = resolve_context_attribution(query, chunks)
    assert len(attrib) == 2

    c1_res = next(c for c in attrib if c["chunk_id"] == "c1")
    c2_res = next(c for c in attrib if c["chunk_id"] == "c2")

    assert c1_res["composite_score"] > c2_res["composite_score"]
    assert c1_res["power_type"] == "ACTIVE"


def test_hnsw_index_rebuild_script(tmp_path):
    idx_dir = tmp_path / "hnsw"
    idx_dir.mkdir()
    manifest_file = idx_dir / "index_manifest.json"
    manifest_file.write_text(
        json.dumps({
            "nodes": {
                "v1": {"tombstone": False, "dim": 384},
                "v2": {"tombstone": True, "dim": 384},
                "v3": {"tombstone": False, "dim": 384},
            }
        }),
        encoding="utf-8",
    )

    res = rebuild_hnsw_index(str(idx_dir), compact=True, dry_run=False)
    assert res["tombstones_pruned"] == 1
    assert res["nodes_remaining"] == 2

    updated = json.loads(manifest_file.read_text(encoding="utf-8"))
    assert "v2" not in updated["nodes"]
    assert "v1" in updated["nodes"]
