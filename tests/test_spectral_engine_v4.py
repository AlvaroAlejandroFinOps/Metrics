"""
Automated validation of FEP-003: Spectral Engine and Statistical Confidence.
"""
import math
from metricsthinking.fpai.spectral_engine import compute_spectral_vector
from metricsthinking.fpai.confidence import calculate_confidence_envelope


def test_spectral_vector_orthogonality_and_invariants():
    # P=1000, Q_dead=200, Q_dup=100, D=50
    # Q_total = 300
    # S_linear = 1000 + 300 + 50 = 1350
    # S_spectral = sqrt(1000^2 + 300^2 + 50^2) = sqrt(1000000 + 90000 + 2500) = sqrt(1092500) ≈ 1045.2272
    vec = compute_spectral_vector(
        p_active=1000.0,
        q_dead=200.0,
        q_dup=100.0,
        d_structural=50.0,
        gain_coefficient=1.0,
    )
    assert vec.p_active == 1000.0
    assert vec.q_dead == 200.0
    assert vec.q_dup == 100.0
    assert vec.d_structural == 50.0

    assert vec.s_linear == 1350.0
    expected_s_spectral = math.sqrt(1000**2 + 300**2 + 50**2)
    assert math.isclose(vec.s_spectral, expected_s_spectral, rel_tol=1e-3)

    # Invariant: S_spectral <= S_linear
    assert vec.s_spectral <= vec.s_linear

    # Power factors
    assert vec.power_factor_spectral > vec.power_factor_linear
    assert math.isclose(vec.power_factor_spectral, 1000.0 / expected_s_spectral, rel_tol=1e-3)
    assert math.isclose(vec.power_factor_linear, 1000.0 / 1350.0, rel_tol=1e-3)

    assert vec.calibration_state == "DETERMINISTIC"


def test_spectral_vector_decoupled_gain():
    vec = compute_spectral_vector(
        p_active=800.0,
        q_dead=200.0,
        q_dup=100.0,
        d_structural=0.0,
        gain_coefficient=1.1,
    )
    assert vec.calibration_state == "CALIBRATED"
    assert vec.gain_coefficient == 1.1
    # Raw PF = 800 / sqrt(800^2 + 300^2) = 800 / 854.4 = 0.9363
    # Calibrated PF = min(1.0, 0.9363 * 1.1) = 1.0
    assert vec.power_factor_spectral == 1.0


def test_spectral_vector_zero_tokens():
    vec = compute_spectral_vector(0.0, 0.0, 0.0, 0.0)
    assert vec.s_spectral == 0.0
    assert vec.s_linear == 0.0
    assert vec.power_factor_spectral == 1.0
    assert vec.power_factor_linear == 1.0
    assert vec.active_ratio == 1.0


def test_confidence_envelope():
    # Empty
    res_empty = calculate_confidence_envelope([])
    assert res_empty["sample_size"] == 0
    assert res_empty["mean"] == 0.0

    # Single
    res_one = calculate_confidence_envelope([0.85])
    assert res_one["sample_size"] == 1
    assert res_one["mean"] == 0.85
    assert res_one["ci_lower"] == 0.85

    # Multi sample
    samples = [0.80, 0.82, 0.85, 0.84, 0.86, 0.83, 0.85, 0.87]
    res = calculate_confidence_envelope(samples, confidence_level=0.95)
    assert res["sample_size"] == len(samples)
    assert 0.80 <= res["mean"] <= 0.88
    assert res["ci_lower"] < res["mean"] < res["ci_upper"]
    assert res["margin_of_error"] > 0.0
