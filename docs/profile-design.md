# Profile design and source notes

## Design

The identity is **from signal to system**: a quiet signal trace becomes a routing
circuit. It connects physiological sensing and model selection to application
engineering without borrowing any project's logo. The illustration is decorative,
not an architecture diagram or a chart of measured data.

- One muted teal accent, generous spacing, and numbered project headings.
- Native Markdown keeps descriptions selectable, searchable, and readable on mobile.
- Five projects show the engineering decisions; three short toolkit lines summarize
  the technologies already demonstrated in those projects.
- No third-party badge, statistics, typing-animation, or activity-image services.
  GitHub already presents contribution activity below the profile.

`assets/identity-light.svg` and `assets/identity-dark.svg` are self-contained SVGs
selected with GitHub's supported `<picture>` pattern. The fallback is the light
asset. They use local system fonts and an optional 12-second CSS trace animation.
There are no scripts, external fonts, network references, or embedded HTML. The
static circuit is complete without animation; `prefers-reduced-motion: reduce`
disables the moving trace. Important profile content remains in native Markdown.

Regenerate both assets after changing the palette or geometry:

```sh
python3 scripts/generate-profile-assets.py
```

## Sources checked

Reviewed on 14 November 2026. References below pin the reviewed source snapshots.
The profile links follow each project's current `main` branch for visitors.

### PRISM

Reviewed commit: [`76ae945`](https://github.com/yash-rai-93/prism-rppg/tree/76ae9456d460153c80ed3cab8b15bc5c3f7d3fb3).

- [`feature_engine.py`](https://github.com/yash-rai-93/prism-rppg/blob/76ae9456d460153c80ed3cab8b15bc5c3f7d3fb3/ai_models/prism/feature_engine.py): optical/motion features, Kalman face-region stabilization, `(1, 10)` output.
- [`router.py`](https://github.com/yash-rai-93/prism-rppg/blob/76ae9456d460153c80ed3cab8b15bc5c3f7d3fb3/ai_models/prism/router.py): feature scaling, predicted errors, and minimum-error model selection.
- [`video.py`](https://github.com/yash-rai-93/prism-rppg/blob/76ae9456d460153c80ed3cab8b15bc5c3f7d3fb3/backend/app/routers/video.py): FastAPI uploads, local routing, remote specialist inference, temporary-file cleanup.
- README research overview, team credits, experiment descriptions, and interface screenshots.

The previous profile's 1.08 BPM result, patent filing, and paper-submission claim
are omitted because these claims were not established by the reviewed public
implementation. The project remains identified as team research.

### Agentic Customer Support

Reviewed commit: [`3f73368`](https://github.com/yash-rai-93/Agentic-Customer-Support-System/tree/3f73368b80c014d0597598a5200345fd138a052b).

- [`tools.py`](https://github.com/yash-rai-93/Agentic-Customer-Support-System/blob/3f73368b80c014d0597598a5200345fd138a052b/backend/app/agent/tools.py): authenticated tool context, ownership, row locking, policy revalidation, and ledger writes.
- [`engine.py`](https://github.com/yash-rai-93/Agentic-Customer-Support-System/blob/3f73368b80c014d0597598a5200345fd138a052b/backend/app/policy/engine.py) and [`models.py`](https://github.com/yash-rai-93/Agentic-Customer-Support-System/blob/3f73368b80c014d0597598a5200345fd138a052b/backend/app/db/models.py): deterministic rules and the unique approval index.
- [`baseline.json`](https://github.com/yash-rai-93/Agentic-Customer-Support-System/blob/3f73368b80c014d0597598a5200345fd138a052b/backend/evals/baseline.json): 82 cases for the committed Gemini baseline; all four deterministic rates are `1.0`.
- README deployment/architecture, model-factory source, Redis coordination, and recorded chat/console screenshots.

The baseline is explicitly historical. Simulated-model load tests are not presented
as capacity measurements for the deployed Gemini application.

### Legal LLM Fine-Tuning

Reviewed commit: [`3d81016`](https://github.com/yash-rai-93/Legal-LLM-Fine-Tuning-and-MLOps/tree/3d81016cf620436161761b0a00f18187bc2cc5b4).

- [`train_multi.py`](https://github.com/yash-rai-93/Legal-LLM-Fine-Tuning-and-MLOps/blob/3d81016cf620436161761b0a00f18187bc2cc5b4/src/scripts/training/train_multi.py): NF4, BF16, PEFT, gradient checkpointing, optimizer settings, and local-rank GPU assignment.
- [`training-and-evaluation.md`](https://github.com/yash-rai-93/Legal-LLM-Fine-Tuning-and-MLOps/blob/3d81016cf620436161761b0a00f18187bc2cc5b4/docs/training-and-evaluation.md), GPU evaluator scripts, benchmark summaries, and platform diagrams.
- Model/adapter deployment and registry files, plus the README implementation-status section.

Historical accuracy summaries do not fully identify matched runs and exclude some
invalid responses. The README and detailed evaluation document also disagree on
the baseline scored count. No controlled accuracy gain or production-completion
claim is made in the profile; visitors can inspect the linked evaluation scope.

### TaskForge CloudOps

Reviewed commit: [`ab70eb1`](https://github.com/yash-rai-93/taskforge-cloudops/tree/ab70eb1898fc9d3ff5851d6a38d5eeefc434e46f).

- Application modules, UI source, [`report.worker.ts`](https://github.com/yash-rai-93/taskforge-cloudops/blob/ab70eb1898fc9d3ff5851d6a38d5eeefc434e46f/backend/src/modules/reports/report.worker.ts), and [`BACKGROUND_JOBS.md`](https://github.com/yash-rai-93/taskforge-cloudops/blob/ab70eb1898fc9d3ff5851d6a38d5eeefc434e46f/docs/BACKGROUND_JOBS.md).
- Container definitions, [`containers.yml`](https://github.com/yash-rai-93/taskforge-cloudops/blob/ab70eb1898fc9d3ff5851d6a38d5eeefc434e46f/.github/workflows/containers.yml), Terraform, and release/deployment scripts.
- Recorded dashboard screenshot, release/verification notes, worker recovery, and digest validation.

Application ownership follows Yash's explicit clarification for this redesign:
Yash independently built both the application and its engineering implementation.
Legacy inherited-project wording in the reference README is not repeated. Source
repositories have not been changed. CI rollback verification is not described as
a live production rollback.

The current IP-based demo URL failed TLS hostname validation during link checks.
The profile links to architecture, worker behavior, and delivery evidence instead.

### AstraDrive

Reviewed commit: [`707c209`](https://github.com/yash-rai-93/astradrive/tree/707c2090789a2f82b2dd8271ddfd4717a5228189).

- [`beamng.py`](https://github.com/yash-rai-93/astradrive/blob/707c2090789a2f82b2dd8271ddfd4717a5228189/simulation/beamng.py): local perception calls, lane-based steering, cruise, and the separate radar/TTC branch.
- UFLDv2 inference, HTTP aggregator, service wrapper, Docker Compose, README scope/architecture, and recorded simulation demos.
- Recursive source-tree metadata confirms that several planning/fusion modules are empty placeholders.

The profile identifies a simulation research prototype, distinguishes the active
local loop from experimental services, and makes no autonomous-driving safety,
FPS, complete sensor-fusion, or physical-vehicle claim.

## Links and content maintenance

The PRISM demo, customer-support demo and showcase, AstraDrive site, and LeetCode
returned successful HTTP responses during checks. LinkedIn's public endpoint
returned its automated-client restriction (HTTP 999); the URL is preserved from
the previous profile, without claiming a successful automated verification.

No public résumé URL was present in the inspected profile or repositories. The
profile has no placeholder résumé link. Add a verified public URL beside LinkedIn
and email when one is supplied.

The profile intentionally omits dated experience and recognition claims that the
five project repositories do not establish. Refresh source evidence before adding
metrics, deployment claims, or publication status.
