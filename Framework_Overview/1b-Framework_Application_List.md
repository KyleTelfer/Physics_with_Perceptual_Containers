# 1b Framework Application Summary

---

## 1b.1 Computerized Modeling

- **Framework Application**:
  - **First-Person POV**: Used to model the internal state of the volume being simulated.
  - **Second-Person POV**: Used to model interactions with other volumes in the system.
  - **Third-Person POV**: Used to describe the overall system behavior and degradation.

- **Definition**: Theoretical simulations using computational tools to predict system behavior.
- **Key Characteristics**:
  - **Output**: Best-guess predictions, not real-world results.
  - **Purpose**: To explore "what-if" scenarios, optimize designs, or identify trends.
  - **Challenges**: Limited by computational resources, model accuracy, and input data quality.
- **Framework Application**:
  - **Degradation Factor**: Used to account for uncertainties in the model (e.g., incomplete data, approximations).
  - **Disengaging Thresholds**:
    - Computational limits: If the model exceeds 80% of available memory or processing power, disengage and simplify.
    - Precision: If the desired output cannot be calculated within ±5% precision, disengage and request better input data.
  - **Example**: Simulating the mass of recycled copper in a waste processing system, adjusting for uncertainties in waste composition.

---

## 1b.2 Theoretical Viability (Mind Boxing)
- **Definition**: Exploring conceptual feasibility through thought experiments and theoretical analysis.
- **Key Characteristics**:
  - **Output**: Conceptual insights, not real-world results.
  - **Purpose**: To push boundaries, explore radical ideas, or identify theoretical limits.
  - **Challenges**: Scope creep (expanding beyond the original goal) and scope blowout (losing focus on the desired result).
- **Framework Application**:
  - **Degradation Factor**: Used to account for theoretical uncertainties (e.g., unobserved interactions, open volumes).
  - **Disengaging Thresholds**:
    - Theoretical limits: If assumptions become too unrealistic (e.g., mass of input waste exceeds known material densities), disengage and revisit assumptions.
    - Scope control: Regularly check if the analysis aligns with the desired result to avoid scope creep.
  - **Example**: Exploring the theoretical maximum efficiency of a shredder, assuming ideal conditions and no energy losses.

---

## 1b.3 Engineering Development/Prototyping
- **Definition**: Designing and building prototypes to assess the practicality of a system.
- **Key Characteristics**:
  - **Output**: Functional prototypes that demonstrate the feasibility of the design.
  - **Purpose**: To translate theoretical concepts into tangible systems and identify design flaws early.
  - **Challenges**: Balancing cost, time, and performance while ensuring the prototype meets design specifications.
- **Framework Application**:
  - **Degradation Factor**: Used to account for uncertainties in materials, manufacturing processes, and design assumptions.
  - **Disengaging Thresholds**:
    - Design limits: If the prototype exceeds design tolerances (e.g., dimensions, weight), disengage and redesign.
    - Resource limits: If the cost or time required exceeds the project budget, disengage and optimize.
  - **Example**: Building a prototype shredder to test its ability to process real-world waste inputs.

---

## 1b.4 Rigor/Failure Testing
- **Definition**: Subjecting the system to rigorous testing to identify failure points and validate performance.
- **Key Characteristics**:
  - **Output**: Identification of failure modes, safety margins, and performance limits.
  - **Purpose**: To ensure the system can operate safely and reliably under real-world conditions.
  - **Challenges**: Simulating extreme conditions, ensuring repeatability, and interpreting test results accurately.
- **Framework Application**:
  - **Degradation Factor**: Used to account for uncertainties in testing conditions and measurement accuracy.
  - **Disengaging Thresholds**:
    - Safety margins: If the system fails below the expected safety threshold (e.g., stress exceeds 90% of yield strength), disengage and redesign.
    - Performance limits: If the system cannot meet performance requirements (e.g., throughput, efficiency), disengage and optimize.
  - **Example**: Testing the shredder prototype under extreme conditions (e.g., high load, continuous operation) to identify failure points.

---

### Key Insights
1. **Clear Phases**: Splitting engineering feasibility into **development/prototyping** and **rigor/failure testing** ensures a more structured approach to system design and validation.
2. **Degradation Factor**: Used differently in each phase—accounting for design uncertainties in prototyping and testing uncertainties in failure testing.
3. **Disengaging Thresholds**: Tailored to the specific challenges of each phase, ensuring safety, performance, and resource limits are respected.

---

### Next Steps
1. Refine the disengaging thresholds for each phase (e.g., prototyping vs. failure testing).
2. Explore specific examples of how the framework applies to each phase (e.g., building a shredder prototype, testing it under extreme conditions).
3. Analyze how the degradation factor impacts the transition from prototyping to failure testing.