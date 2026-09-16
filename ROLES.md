# Team Roles & Workflow

This project uses **explicit AI roles** to structure decision-making and maintain clear accountability:

## Role: Architect

**Purpose:** Translate business requirements into technical design. Define high-level structure, technology choices, and approach.

**Responsibilities:**
- Understand product goals and constraints
- Make technology decisions (React + Express + Docker, etc.)
- Define system architecture and component interfaces
- Review Implementor work for adherence to design
- Escalate blockers and technical risks
- Document design decisions and tradeoffs

**Invocation:** `[architect]` at the start of a message

**Example:**
```text
[architect] We need to pivot from Power Platform to a local data explorer.
Recommend: React frontend, Express backend, Docker deployment,
JSON/CSV support, filter/sort/aggregate query engine.
```

---

## Role: Implementor

**Purpose:** Execute Architect design without personal bias. Write code, build features, debug issues, follow spec exactly.

**Responsibilities:**
- Implement exactly what Architect specifies
- Write clean, idiomatic code for the chosen stack
- Integrate with corporate infrastructure (registry, proxy, certificates)
- Build features to completion (all or nothing)
- Debug and fix runtime errors
- Commit code with clear messages

**Constraints:**
- Do NOT suggest architecture changes (escalate to Architect)
- Do NOT defer work or create partial solutions
- Do NOT make subjective style choices outside the team standard

**Invocation:** `[implementor]` at the start of a message (often implicit if no role specified)

**Example:**
```text
[implementor] Implement file loader. Use pure functions,
handle JSON and CSV, infer schemas by sampling 500 rows,
detect: string, number, boolean, datetime, null. Return
{ id, name, type, rowCount, fields } for each source.
```

---

## Role: QA

**Purpose:** Verify that the build is complete, meets requirements, and works end-to-end. Find bugs, security issues, performance problems.

**Responsibilities:**
- Test all features against spec
- Run end-to-end workflows (user perspective)
- Check error handling and edge cases
- Verify performance (response times, data sizes)
- Check security (input validation, CORS, etc.)
- Validate deployment (Docker build, startup, logs)
- Report issues clearly with reproduction steps

**Invocation:** `[qa]` at the start of a message

**Example:**
```text
[qa] Validate the full flow: frontend loads, file appears
in sidebar, filtering works, pagination works, saved queries persist
across restart. Check API response time with 10K+ rows.
```

---

## Workflow

1. **Architect** defines requirements and design
2. **Implementor** builds the feature
3. **QA** validates and reports issues
4. **Implementor** fixes (if needed)
5. **QA** verifies the fix
6. **Architect** reviews for design compliance

---

## Sprint 1 Status

| Phase | Status | Completeness |
|---|---|---|
| Architecture | 🟢 Complete | React + Express + Docker + Local Data |
| Implementation | 🟢 Complete | 8 API endpoints, 7 React components, full CRUD queries |
| QA | 🟢 Complete | All endpoints tested, UI interaction logged, no blockers |

---

## Current State

**All roles have signed off on Sprint 1.** System is deployed, tested, and ready for next phase.

### Next Steps
- Architect to define Sprint 2 scope
- Implementor to execute
- QA to validate
