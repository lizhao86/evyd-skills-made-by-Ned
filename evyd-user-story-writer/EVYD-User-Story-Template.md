# EVYD User Story Template

---

### Title

[Platform] [System] [Module] - As a [Role], I [action/goal]


Example:
> `[App] Routines Logging - As an Admin, I Can View Inherited Read-Only Permissions When Assigning Permissions to Accounts linked with Roles`

---

### Description

2–3 sentences describing the feature context and purpose from the user's perspective.

---

### Figma Section Link(s)


- User flow: N/A _(Remove if Applicable)_
- LoFi wireframe: _N/A (Remove if Applicable)_
- HiFi wireframe (final design): _N/A (Remove if Applicable)_

---

### Acceptance Criteria

Use **Given-When-Then-And** format. Requirements:

- Include **at least 5 scenarios**
- Cover all four path types:
  - **Happy Path** — primary success flow
  - **Alternative Paths** — other valid usage flows
  - **Edge Cases** — uncommon but possible situations
  - **Error Handling** — invalid input or system failures
- Each scenario must consider: user operation flow, system response, and data changes
- Add `And` clauses to make criteria more comprehensive
- Define conditions QA can verify — leave no room for interpretation

**Scenario format:**

```
**Scenario N: [Scenario Name]**
- **Given** [precondition],
- **When** [action],
- **Then** [expected result],
- **And** [additional result] _(if applicable)_
```
