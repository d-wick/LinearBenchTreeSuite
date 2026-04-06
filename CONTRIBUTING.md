# Contributing to LinearBenchTreeSuite

> All development work and pull requests should target the `main` branch.

Thank you for your interest in contributing to LinearBenchTreeSuite!

This project is designed around a **stable public API** with room for
future extension. Contributions are welcome, but we are intentionally
selective to preserve clarity, consistency, and backward compatibility.

---

## How Contributions Work

LinearBenchTreeSuite uses the standard GitHub workflow:

1. Fork the repository
2. Create a feature branch in your fork
3. Make your changes
4. Open a Pull Request (PR) against the `main` branch
5. Participate in review and iterate if requested

Only maintainers can merge changes into `main`.

---

## What We Welcome

We are especially open to contributions that:

- add **new models** following the existing architecture
- add **new metrics** that are model‑agnostic
- improve **documentation or examples**
- fix **bugs** without changing public APIs
- improve **tests or reliability**

All contributions should be:
- well‑scoped
- clearly motivated
- consistent with the project’s design philosophy

---

## Public API Stability

The following namespaces are considered **public and stable**:

```

linearbenchtree.data
linearbenchtree.models
linearbenchtree.metrics

```

Changes that break these APIs will not be accepted without a clear
justification and a planned major version bump.

Everything outside these namespaces is considered **internal** and may
change more freely.

---

## Adding New Models

New models should:

1. Live in their own internal module
2. Expose `train_<model>()` and `predict_<model>()` functions
3. Be registered through `linearbenchtree.models`
4. Avoid embedding evaluation logic (metrics live in `metrics/`)
5. Include basic documentation and examples where appropriate

See `EXTENDING.md` for architectural guidance.

---

## What We Are Careful About

To keep the project maintainable, we are cautious about:

- expanding the public API surface
- adding implicit behavior or hidden defaults
- tightly coupling models, metrics, and data logic
- introducing dependencies without strong justification

This does not mean ideas are unwelcome — it means design discussion
comes first.

---

## Code Style & Quality

- Keep changes focused and readable
- Prefer clarity over cleverness
- Include tests where practical
- Ensure existing tests continue to pass

If a contribution changes behavior, please explain *why* in the PR
description.

---

## Questions & Discussion

If you’re unsure whether a change fits the project:

- open an issue to discuss the idea first
- explain the motivation and intended use case

We’re happy to discuss direction before reviewing code.

---

## License

By contributing, you agree that your contributions will be licensed
under the project’s MIT License.
