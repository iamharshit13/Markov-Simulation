# Markov-Based Vowel-Consonant Simulation

This project demonstrates a **Markov prediction dependent event** where the probability of generating a vowel or consonant depends on the previous outcome.  
The simulation models this as a **two-state Markov chain** and visualizes the percentage trends of vowels and consonants over time.

---

## 🔹 Concept

Unlike independent random events, here the probability of the next state depends on the **current state**:

- **Vowel → Vowel**: 13%  
- **Vowel → Consonant**: 87%  
- **Consonant → Consonant**: 33%  
- **Consonant → Vowel**: 67%  

This makes the process **history-sensitive**, which is the essence of a Markov chain.

---

## 🔹 Features
- Simulates vowel/consonant generation using **Markov transitions**.
- Stores **percentages** of vowels and consonants at reporting intervals.
- Prints intermediate results in the notebook.
- Provides a **trend graph** for vowel/consonant percentages over time.
- Fully compatible with **Jupyter Notebook** (`SimulatePrediction.ipynb`).
- Includes a **basic `test.py` file** with a crude version of the code for easier understanding of the core logic.

---

## 🔹 Usage

### 1. Run the Simulation
Inside **`SimulatePrediction.ipynb`**, run:
```python
vowel_data, consonant_data = run_simulation(
    report_interval=25,   # record stats every 25 steps
    max_iterations=500    # stop after 500 iterations
)
