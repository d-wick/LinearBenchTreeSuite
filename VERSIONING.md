# API Versioning Policy

LinearBenchTreeSuite follows **Semantic Versioning (SemVer)** to communicate
API stability and manage breaking changes clearly.

Version numbers follow the format:

```

MAJOR.MINOR.PATCH

```

Example: `1.2.3`

This policy applies to **all public APIs** defined in this project.

---

## Public API Definition

Only the following namespaces are considered **public and versioned**:

- `linearbenchtree.data`
- `linearbenchtree.models`
- `linearbenchtree.metrics`
- Any symbols explicitly documented in `README.md`

Anything outside these namespaces is **internal** and may change without notice.

---

## Version Number Meaning

### PATCH version (`X.Y.Z → X.Y.(Z+1)`)

Increment PATCH for:
- Bug fixes
- Documentation fixes
- Performance improvements
- Internal refactoring that does **not** affect public APIs

✅ Backward compatible  
✅ Safe to upgrade  

Example:
```

1.2.0 → 1.2.1

```

---

### MINOR version (`X.Y.Z → X.(Y+1).0`)

Increment MINOR for:
- New public functions
- New metrics (e.g. adding `rmse`)
- New models added to the public API
- Backward‑compatible API extensions

✅ Backward compatible  
✅ No required code changes for users  

Example:
```

1.2.0 → 1.3.0

```

---

### MAJOR version (`X.Y.Z → (X+1).0.0`)

Increment MAJOR for:
- Removing public functions
- Renaming public symbols
- Changing function signatures
- Changing return types
- Any change that breaks existing user code

❌ Not backward compatible  
❗ Requires user migration  

Example:
```

1.2.0 → 2.0.0

```

---

## Pre‑1.0 Policy

Before version `1.0.0`:

- The API is considered **experimental**
- Breaking changes may occur in MINOR versions
- Version numbers may advance rapidly

Once `1.0.0` is released:
- SemVer rules apply strictly
- Breaking changes require a MAJOR bump

---

## Metrics Versioning Rules

Metrics are **first‑class API objects**.

- Adding a new metric → MINOR bump
- Changing a metric’s formula → MAJOR bump
- Bug fix in metric implementation → PATCH bump

Metric behavior must remain stable within a major version.

---

## Model Versioning Rules

- Adding a new model → MINOR bump
- Changing training behavior without API change → PATCH bump
- Changing public model signatures → MAJOR bump

Optimization utilities are internal and do **not** affect versioning.

---

## Import Tests as Enforcement

Public API stability is enforced through **import tests**.

If a public symbol is:
- renamed
- removed
- moved

without a MAJOR version bump, CI **must fail**.

This ensures version numbers reflect real compatibility.

---

## Release Discipline

Every release must include:
- A version bump consistent with this policy
- Updated documentation (README / ARCHITECTURE if needed)
- Passing CI and import tests

Optional but recommended:
- `CHANGELOG.md` entry describing changes

---

## Summary

- ✅ Semantic Versioning
- ✅ Explicit public API boundaries
- ✅ Import tests enforce stability
- ✅ Internal freedom preserved
- ✅ Clear upgrade expectations

> **Version numbers are a contract with users.**
> This policy ensures that contract is explicit and reliable.

