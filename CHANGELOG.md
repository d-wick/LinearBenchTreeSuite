# Changelog

All notable changes to LinearBenchTreeSuite will be documented in this file.

This project follows **Semantic Versioning (SemVer)**:
`MAJOR.MINOR.PATCH`

---

## [0.3.0] – Public API Formalization & Metrics Domain

### Added
- Introduced a first‑class `linearbenchtree.metrics` API domain.
- Added `mae_percent()` as the canonical, model‑agnostic evaluation metric.
- Added public feature‑importance helpers for tree‑based models:
  - `get_feature_importance_forest`
  - `get_feature_importance_extratrees`
- Added explicit public API layers:
  - `linearbenchtree.data`
  - `linearbenchtree.models`
  - `linearbenchtree.metrics`
- Added import tests to lock public API surfaces and enforce stability.
- Added `EXTENDING.md` with contributor guidance and extension rules.
- Added `ARCHITECTURE.md` documenting internal vs public boundaries.
- Added an explicit API versioning policy.

### Changed
- Centralized MAE% computation into the `metrics` domain.
- Refactored model‑specific evaluation helpers to delegate to `mae_percent`.
- Clarified that hyperparameter optimization utilities are internal.
- Clarified that benchmarking and experiment orchestration are not public API.
- Updated README to reflect new architecture and API domains.

### Fixed
- Removed duplicated MAE% implementations across model modules.
- Resolved public API namespace collisions in model exports.
- Corrected `__all__` definitions to prevent import errors.

---

## [0.2.0] – Tree Model Expansion

### Added
- Decision Tree regression model.
- Random Forest regression model with feature importance.
- Extra Trees regression model with feature importance.
- Baseline linear regression benchmark.

### Changed
- Expanded dataset creation utilities for rolling‑window time‑series regression.
- Improved modular separation between data processing and modeling.

---

## [0.1.0] – Initial Prototype

### Added
- Initial project structure.
- Dataset loading and preprocessing utilities.
- Linear regression benchmark model.
- Exploratory notebooks and experiments.

---

## Versioning Notes

- Versions prior to `1.0.0` are considered **experimental**.
- Public APIs may evolve more rapidly before `1.0.0`.
- Once `1.0.0` is released, breaking changes will require a MAJOR version bump.

See `VERSIONING.md` for full API compatibility guarantees.
```
