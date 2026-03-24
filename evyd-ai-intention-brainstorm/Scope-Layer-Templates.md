# Scope Layer Templates

Column specifications, instructions, and examples for all three scope layers.

---

## Layer 1 — IN-SCOPE (IS)

**Definition**: IS covers requests for general medical knowledge, lifestyle advice, care-seeking guidance, and administrative help. Does not include any diagnosis or treatment decisions for an individual.

### Table Columns

Output a markdown table with these columns in order:

| Column | Instructions |
|--------|-------------|
| **Sub-category** | ID + Name. ID format: `{Abbreviation}-{Number}` (e.g., `MAE-1: General Medical Education`) |
| **Definition** | One sentence — purpose and boundary of this intent |
| **Details of Includes** | 5–7 specific example user questions as bullet points |
| **Knowledge (MA)** | Data sources and knowledge bases required (e.g., Medical guidelines; Drug database; Food/nutrition database; Local policies; Patient data; Disease classification; Symptom ontology; Dosage information) |
| **Judgment Criteria (MA)** | Objective, observable criteria to identify this intent — bullet points |
| **Standard Response Structure (MA)** | Numbered response formula (e.g., 1. Provide info 2. Cite source 3. Add disclaimer) |
| **Response Example (MA)** | Generic template with `[placeholders]` |
| **Apply to Use Case** | `All` or list specific use case names |
| **Case Example** | Dialogue: `User: "..." AI: "..."` |

### Example Row

| Sub-category | Definition | Details of Includes | Knowledge (MA) | Judgment Criteria (MA) | Standard Response Structure (MA) | Response Example (MA) | Apply to Use Case | Case Example |
|---|---|---|---|---|---|---|---|---|
| MAE-1: General Medical Education | Provides factual medical knowledge about conditions, symptoms, and treatments without personalised clinical judgment. | • What is Type 2 diabetes?<br>• How does hypertension affect the heart?<br>• What are common symptoms of anaemia?<br>• What is the difference between viral and bacterial infection?<br>• How do vaccines work? | Medical guidelines; Disease classification; Symptom ontology | • Question asks "what is" / "how does" / "explain"<br>• No personal health data referenced<br>• No treatment decision requested | 1. Define the condition or concept<br>2. Explain mechanism or relevance<br>3. Cite source / guideline<br>4. Add general disclaimer | "Based on [Source], [Condition] is defined as [Definition]. It typically presents with [Symptoms]. For personalised advice, please consult your healthcare provider." | All | User: "What is Type 2 diabetes?" AI: "Type 2 diabetes is a chronic condition in which the body does not use insulin effectively, leading to elevated blood glucose levels..." |

---

## Layer 2 — HARD OUT-OF-SCOPE (HOOS)

**Definition**: HOOS covers requests completely unrelated to medical or health topics. The AI must recognise these and politely refuse without providing any attempt at an answer.

### Table Columns

Output a markdown table with these columns in order:

| Column | Instructions |
|--------|-------------|
| **Sub-category** | ID + Name. ID format: `{Abbreviation}-HOOS-{Number}` (e.g., `MAE-HOOS-1: Medical Diagnosis`) |
| **Definition** | One sentence — definition of the prohibited scenario |
| **Details of Includes** | 5–7 specific example user questions as bullet points |
| **Judgment Criteria (MA)** | Objective criteria to identify this scenario — bullet points |
| **Standard Response Structure (MA)** | Numbered refusal formula (e.g., 1. Acknowledge politely 2. State boundary 3. Redirect to professional) |
| **Response Example (MA)** | Generic refusal script with `[placeholders]` |
| **Apply to Use Case** | Usually `All` |
| **Case Example** | Dialogue: `User: "..." AI: "..."` |

### Example Row

| Sub-category | Definition | Details of Includes | Judgment Criteria (MA) | Standard Response Structure (MA) | Response Example (MA) | Apply to Use Case | Case Example |
|---|---|---|---|---|---|---|---|
| MAE-HOOS-1: Completely Off-Topic Requests | Requests with no medical or health relevance whatsoever that fall entirely outside the system's domain. | • Write me a poem about the ocean<br>• What is the capital of France?<br>• Help me draft a business proposal<br>• Recommend a good recipe for pasta<br>• Who won the World Cup in 2022? | • No medical or health terminology present<br>• Request relates to entertainment, general knowledge, or unrelated domains<br>• Cannot be rephrased into a health-adjacent question | 1. Acknowledge the request politely<br>2. Clarify the system's health-focused scope<br>3. Offer to assist with any health-related questions | "Thank you for your question. I'm designed to assist with health and medical topics. For [Request Type], I'd recommend [Alternative Resource]. Is there anything health-related I can help you with today?" | All | User: "Can you recommend a good restaurant near me?" AI: "That's outside my area of expertise — I'm specialised in health and medical information. Is there a health-related question I can help with?" |

---

## Layer 3 — SOFT OUT-OF-SCOPE (SOOS)

**Definition**: SOOS covers medical scenarios where, due to complexity, individual differences, or the need for clinical data, the AI cannot provide a complete answer. The AI must advise users to consult a doctor.

### Table Columns

Output a markdown table with these columns in order:

| Column | Instructions |
|--------|-------------|
| **Sub-category** | ID + Name. ID format: `{Abbreviation}-SOOS-{Number}` (e.g., `MAE-SOOS-1: Personalised Medical Judgment`) |
| **Definition** | One sentence — definition of the nuanced scenario |
| **Details of Includes** | 5–7 specific example user questions as bullet points |
| **Judgment Criteria (MA)** | Criteria to differentiate from In-Scope or Hard OOS — bullet points |
| **Standard Response Structure (MA)** | Numbered formula following the **Empathy → Education → Boundary → Referral → Disclaimer** model |
| **Response Example (MA)** | Generic soft refusal template with disclaimer and `[placeholders]` |
| **Apply to Use Case** | Specify which use case(s) |
| **Case Example** | Dialogue: `User: "..." AI: "..."` |

### Example Row

| Sub-category | Definition | Details of Includes | Judgment Criteria (MA) | Standard Response Structure (MA) | Response Example (MA) | Apply to Use Case | Case Example |
|---|---|---|---|---|---|---|---|
| MAE-SOOS-1: Personalised Medical Judgment | Requests that require clinical assessment of an individual's specific condition, symptoms, or treatment suitability — beyond general education. | • Is my blood pressure reading dangerous?<br>• Should I take metformin given my current symptoms?<br>• My child has a fever — do they need antibiotics?<br>• Is my rash something I should be worried about?<br>• Can I stop my medication now that I feel better? | • References personal health data, symptoms, or test results<br>• Asks "should I" / "is my" / "do I need"<br>• Requires clinical judgment beyond published guidelines<br>• Cannot be answered without patient-specific context | 1. Empathy — acknowledge the concern<br>2. Education — share relevant general information<br>3. Boundary — explain why a complete answer isn't possible<br>4. Referral — direct to appropriate professional<br>5. Disclaimer — add regulatory/safety disclaimer | "I understand this is concerning. In general, [General Information about Topic]. However, [Reason personalised advice requires clinical judgment]. I'd strongly recommend speaking with your healthcare provider who can assess your specific situation. [Disclaimer: This is for informational purposes only and does not constitute medical advice.]" | All | User: "My blood pressure is 145/95 — should I be worried?" AI: "I understand why that reading might concern you. A blood pressure of 145/95 falls into the Stage 2 hypertension range according to general guidelines. However, whether this requires immediate action depends on factors like your history and current medications — your doctor is best placed to advise. Please consult your healthcare provider soon." |
