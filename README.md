<picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/identity-static.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/identity-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/identity-light.svg">
  <img src="assets/identity-static.svg" alt="Yash Rai — from signal to system. AI and ML engineering." width="100%">
</picture>

**I build models, agents, and the software around them.**

I'm Yash, a final-year AI/ML student at **BIT Mesra**. I work on physiological sensing, LLMs, and agents, alongside the APIs, interfaces, and infrastructure that turn experiments into working applications.

[LinkedIn](https://www.linkedin.com/in/yash-rai-5235241a5/) · [Email](mailto:yashrai4426@gmail.com) · [LeetCode](https://leetcode.com/u/yashrai4426/)

## Selected work

### 01 · [PRISM](https://github.com/yash-rai-93/prism-rppg)

**Physics-aware model selection for contactless heart-rate estimation.**

A team research project at BIT Mesra. A **10-dimensional optical and motion representation** feeds a meta-regressor that predicts specialist rPPG errors and selects the lowest-error model. Kalman-stabilized face regions, a FastAPI video pipeline, remote inference, and a React analysis interface connect the research to an application.

[Source & architecture](https://github.com/yash-rai-93/prism-rppg#-core-architecture) · [Reported experiments](https://github.com/yash-rai-93/prism-rppg#-performance--evaluation) · [Web demo](https://prism-rppg.onrender.com/)

### 02 · [Agentic Customer Support](https://github.com/yash-rai-93/Agentic-Customer-Support-System)

**Tool-using agents with policy enforced at the write boundary.**

A LangGraph agent handles order questions and refunds; application code rechecks identity, ownership, and refund policy before committing a decision. **PostgreSQL row locks and a unique approval index** guard against duplicate refunds. Redis coordination, streamed audit events, model fallback, and Opik traces support the deployed application.

The committed Gemini baseline covers **82 cases**, with all four deterministic metrics at **100%**; this describes the recorded evaluation.

[Try the app](https://agentic-customer-support-system.yashrai4426.workers.dev) · [Architecture](https://github.com/yash-rai-93/Agentic-Customer-Support-System#architecture) · [Evaluation record](https://github.com/yash-rai-93/Agentic-Customer-Support-System/blob/main/backend/evals/baseline.json)

### 03 · [Legal LLM Fine-Tuning](https://github.com/yash-rai-93/Legal-LLM-Fine-Tuning-and-MLOps)

**Long contracts, limited GPU memory, and an inspectable model lifecycle.**

A contract-analysis pipeline adapts Hermes-4-14B to classify **17 ContractNLI hypotheses** and return supporting clauses. The training recipe combines QLoRA, 4-bit NF4, BF16, gradient checkpointing, and PyTorch DDP. MLRun artifacts, versioned adapters, and SageMaker/vLLM serving code extend the work beyond training. Historical evaluation and serving measurements are documented with their scope and limitations.

[Training & evaluation](https://github.com/yash-rai-93/Legal-LLM-Fine-Tuning-and-MLOps/blob/main/docs/training-and-evaluation.md) · [Lifecycle & implementation status](https://github.com/yash-rai-93/Legal-LLM-Fine-Tuning-and-MLOps#implementation-status)

### 04 · [TaskForge CloudOps](https://github.com/yash-rai-93/taskforge-cloudops)

**An independently built application, from interface to infrastructure.**

I built the task-management application and its engineering implementation end to end: **Next.js, a NestJS API, PostgreSQL, and a dedicated BullMQ worker**. Docker Compose, Terraform-provisioned AWS infrastructure, and GitHub Actions deliver digest-pinned releases. Background reports expose real queue state; verification covers worker recovery, persistence, and deployment rollback in CI.

[Application & architecture](https://github.com/yash-rai-93/taskforge-cloudops#architecture) · [Background jobs](https://github.com/yash-rai-93/taskforge-cloudops/blob/main/docs/BACKGROUND_JOBS.md) · [Delivery pipeline](https://github.com/yash-rai-93/taskforge-cloudops/blob/main/docs/CI_CD.md)

### 05 · [AstraDrive](https://github.com/yash-rai-93/astradrive)

**A perception-to-control loop in autonomous-driving simulation.**

A simulation pipeline connects BeamNG.tech camera and radar inputs to **hybrid CV/UFLDv2 lane perception, YOLO detection, and PID steering**. It includes cruise control and a separate radar/TTC braking mode. The active loop runs perception locally; HTTP aggregation and Docker services are experimental alternatives. Recorded demos show individual experiments in this research prototype.

[Architecture & scope](https://github.com/yash-rai-93/astradrive#architecture) · [Demos & project site](https://yash-rai-93.github.io/astradrive/)

## Working toolkit

- **Models & experiments** — Python, PyTorch, OpenCV, Transformers, PEFT/QLoRA.
- **Applications & data** — TypeScript, React/Next.js, FastAPI, NestJS, PostgreSQL, Redis.
- **Delivery & operations** — Docker, GitHub Actions, AWS, Terraform, Google Cloud Run.

---

Interested in AI/ML engineering, agent reliability, applied research, and backend systems. If you're working on a problem in these areas, [let's talk](mailto:yashrai4426@gmail.com).
