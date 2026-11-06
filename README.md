# ShipRoom AI

**An AI-powered engineering release coordination room built with Switch.**

ShipRoom AI brings developers and AI coding agents together to prepare, validate, review, and approve software releases.

## Problem

Software releases require developers to coordinate code reviews, test execution, release notes, and deployment decisions across different tools.

Important findings often remain buried in individual developer terminals, making release decisions difficult to review and reproduce.

## Solution

ShipRoom AI uses Switch to create a shared engineering workspace where specialized AI agents collaborate with developers.

### AI Team

- Release Planner: Breaks down release requests and coordinates tasks.
- Code Auditor: Inspects repository changes and identifies potential risks.
- QA Agent: Executes tests and reports actual results.
- Release Coordinator: Consolidates findings and prepares the release report.

## Key Features

- Shared agent and human collaboration through Switch.
- Repository-aware code analysis.
- Automated test execution.
- Evidence-based release readiness reports.
- Human approval before release actions.
- Persistent room history and decisions.

## Technology

- Switch
- Codex
- GitHub
- Docker
- Mattermost

**Evidence-First AI Release Coordination Using Switch**

ShipRoom AI is a multi-agent release coordination workflow built using Switch. It brings together specialized AI agents that inspect code, analyze test evidence, coordinate remediation, and prepare release-readiness reports.

Rather than allowing an AI agent to independently declare a release safe, ShipRoom AI follows an evidence-first approach with a human approval gate.

## 1. Project Overview

Software releases often require developers to inspect code, review test results, identify potential regressions, coordinate fixes, and determine whether an application is ready for release.

ShipRoom AI demonstrates how multiple specialized AI agents can collaborate on these activities through Switch.

The system uses two specialized agents:

- **Release Auditor:** Inspects source code, identifies defects, reviews implementation changes, and evaluates technical risks.
- **Release Preparer:** Coordinates the release-readiness workflow, consolidates findings, tracks blockers, and prepares a final readiness assessment.

The agents collaborate in a shared private Mattermost channel, with the human developer retaining control over code modifications and final release decisions.

## 2. How Switch Is Used

Switch acts as the central collaboration and orchestration layer.

It connects the configured AI agents and enables them to communicate through a shared channel.

The workflow uses:

- Switch Console as the agent coordination environment.
- Codex as the configured agent provider.
- Specialized Release Auditor and Release Preparer agents.
- A private Mattermost channel named `shiproom-ai`.
- A local Python demonstration repository used for code inspection and testing.

### Connected Agents

| Agent | Responsibility |
|---|---|
| `release-auditor` | Source-code inspection, defect identification, edge-case analysis, independent verification |
| `release-preparer` | Agent coordination, evidence consolidation, blocker tracking, readiness reporting |

### Agent Collaboration

The Release Preparer coordinates with the Release Auditor to gather technical findings.

For example:

1. The human requests a release investigation.
2. The Release Preparer acknowledges the task and requests an independent audit.
3. The Release Auditor inspects the repository and shares findings in the channel.
4. The Release Preparer incorporates those findings into the readiness assessment.
5. The human authorizes a specific remediation scope.
6. A coding agent implements the approved changes.
7. The human executes tests and provides actual runtime evidence.
8. The Release Auditor independently reviews the remediation.
9. The Release Preparer consolidates the final report.

This separation helps prevent unverified claims and unauthorized release actions.

## 3. Switch Channel Setup

A private Mattermost channel named `shiproom-ai` is used as the shared collaboration space.

The channel contains:
- The human project owner.
- The `release-auditor` agent.
- The `release-preparer` agent.

The channel is used to:
- Start new investigations.
- Share source-code findings.
- Request independent reviews.
- Coordinate remediation requirements.
- Share test evidence.
- Track release blockers.
- Produce consolidated readiness reports.

The private channel provides a centralized record of agent communication and human authorization decisions.

## 4. Repository Structure

The demonstration repository is organized as follows:

```text
shiproom-ai/
│
├── README.md
│
└── demo-repo/
    │
    ├── README.md
    │
    ├── src/
    │   ├── __init__.py
    │   ├── checkout.py
    │   └── inventory.py
    │
    └── tests/
        ├── test_checkout.py
        └── test_inventory.py
```

The demo repository contains two independent Python modules.

### Checkout API

Implements checkout total calculation, including item pricing and percentage discounts.

The initial implementation contained validation defects involving negative quantities, negative prices, and invalid discount percentages.

### Inventory Reservation API

Implements stock reservation through:

`reserve_stock(inventory, sku, quantity)`

The initial implementation deliberately contained defects involving:
- Negative reservation quantities.
- Reservations exceeding available stock.
- Boolean quantities being accepted as integers.
- Unknown SKUs producing unhandled exceptions.

These defects provide realistic scenarios for agent-driven investigation and remediation.

## 5. Prerequisites

- Windows environment.
- Python installed and available through the `py` launcher.
- Switch Console installed and configured.
- Codex provider authenticated in Switch.
- `release-auditor` and `release-preparer` agents configured.
- Private Mattermost `shiproom-ai` channel available.
- Project repository available locally.

No external Python dependencies are required by the demonstration application.

## 6. Running the Demonstration

### Step 1: Start Switch

1. Launch Switch Console.
2. Start or connect to the configured Switch environment.
3. Verify that the Codex provider is authenticated.
4. Verify that both agents are registered and available.
5. Open the private Mattermost `shiproom-ai` channel.

Use the existing Switch Console configuration and agent setup.

### Step 2: Open the Demo Repository

Open PowerShell:

```powershell
cd C:\Users\sneha\OneDrive\Desktop\shiproom-ai\demo-repo
```

### Step 3: Run the Test Suite

Execute:

```powershell
py -m unittest discover -s tests -v
```

This runs both Checkout API and Inventory API tests.

### Step 4: Start an Investigation

Post an investigation request in the `shiproom-ai` channel.

Ask the Release Auditor to:
- Inspect the relevant source files.
- Identify defects.
- Examine additional edge cases.
- Reference exact source and test locations.
- Distinguish source findings from actual runtime evidence.

Ask the Release Preparer to coordinate the investigation and prepare a readiness assessment.

### Step 5: Authorize Remediation

Review the findings and explicitly authorize a limited remediation scope.

The coding agent should modify only the authorized files.

The Release Preparer coordinates the work, while the Release Auditor provides technical requirements and performs independent verification.

### Step 6: Verify the Changes

Run the focused tests:

```powershell
py -m unittest tests.test_inventory -v
```

Then run the full suite:

```powershell
py -m unittest discover -s tests -v
```

Share the actual output in the collaboration channel.

### Step 7: Request Final Review

Ask the Release Auditor to perform a read-only independent review.

The Release Preparer then consolidates:
- Original defects.
- Authorized changes.
- Test evidence.
- Independent review findings.
- Remaining risks.
- Final readiness recommendation.

The human owner makes the final release decision.

## 7. Demonstration Results

The project has completed two investigation and remediation scenarios.

### Scenario 1: Checkout API

Initial test results:

- 7 tests executed.
- 3 passed.
- 4 failed.

After remediation and additional large-number edge-case checks:

- 7 original tests passed.
- 2 additional edge-case checks passed.
- Independent source review reported satisfactory findings.

### Scenario 2: Inventory Reservation API

Initial full-suite results:

- 13 tests executed.
- 9 passed.
- 3 failed.
- 1 errored.

After remediation:

- 9 focused Inventory API tests passed.
- 16 full-suite tests passed.
- 0 failures.
- 0 errors.

The original seven Checkout API tests continued to pass.

These are owner-provided local runtime results. The final independent review and consolidated release-readiness assessment are separate verification steps.

## 8. Human Approval and Safety

ShipRoom AI is designed around controlled autonomy.

The agents can investigate, communicate, analyze evidence, and prepare recommendations.

However:

- Code modifications require explicit authorization.
- Remediation must stay within the approved file scope.
- Existing tests must not be weakened to manufacture passing results.
- Runtime evidence must be attributed to the person or environment that actually executed the tests.
- Independent review must be distinguished from test execution.
- Commits, pushes, merges, and deployments require separate authorization.
- Final release approval always remains with the human owner.

A recommendation of **Ready for Human Release Decision** does not mean the application has been deployed or automatically approved.

## 9. Key Features Demonstrated

- Multi-agent collaboration through Switch.
- Specialized agent responsibilities.
- Shared private Mattermost coordination channel.
- Evidence-backed source-code investigations.
- Root-cause and edge-case analysis.
- Controlled remediation authorization.
- Regression testing and runtime evidence tracking.
- Independent read-only source review.
- Consolidated release-readiness reporting.
- Human-in-the-loop release approval.

## 10. Future Enhancements

Potential extensions include:

- Git integration for commit and change-diff analysis.
- CI/CD pipeline integration.
- Automated test execution with verifiable logs.
- Deployment health monitoring.
- Historical incident and release memory.
- Risk scoring based on evidence.
- Approval workflows for staging and production releases.

## 11. Project Goal

ShipRoom AI demonstrates how a team of specialized AI agents can work together as a release coordination team rather than as isolated coding assistants.

By combining Switch-powered collaboration, evidence-backed investigations, controlled remediation, independent verification, and human approval, ShipRoom AI aims to make software release decisions more transparent, accountable, and reliable.

**Built for the WeMakeDevs Flip the Switch Hackathon 2026.**