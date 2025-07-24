# Neural Conformality Toolkit 🧠

[![Hugging Face Spaces](https://img.shields.io/badge/🤗%20Hugging%20Face-Spaces-yellow)](https://huggingface.co/spaces/Tnsr-q/neural-conformality-toolkit)
[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Tnsr-Q/neural-conformality/issues)

This repository is an open-source research project designed to test the **Neural Conformality Hypothesis**. This theory posits that integrated information in the brain corresponds to a specific geometric property—conformality—in its dynamics, emerging when the brain operates at a critical phase transition.

Our goal is to provide the tools and framework for the scientific community to test this theory transparently and collaboratively.

## Key Components

* **[📄 The Theory Paper](papers/theory_paper.pdf):** Lays out the first-principles derivation of emergent conformality from neural dynamics.
* **[🛠️ The Methods Paper](papers/methods_paper.pdf):** Details the methodology, the Conformality Residual (CR) metric, and the analysis pipeline.
* **[🚀 The Interactive Toolkit](https://huggingface.co/spaces/Tnsr-q/neural-conformality-toolkit):** A live web application where you can run simulations, analyze your own data, and view community results.

## How to Participate

You can contribute to this project in two primary ways:

1.  **Explore the Simulations:** Use the interactive toolkit to run Ginzburg-Landau simulations and develop an intuition for how conformality behaves near a critical point.
2.  **Analyze Your Data:** If you have pre-processed MEG/EEG source-space data, you can upload it to the toolkit to calculate its Conformality Residual. Please follow the specific data formatting rules outlined in our **[Data Submission Guidelines](DATA_GUIDELINES.md)**.

## Live Results Dashboard

To ensure intellectual honesty and transparency, all valid community submissions are tracked on a public dashboard. The raw data for this dashboard is stored in [`results.csv`](results.csv).

You can view the live, auto-updating dashboard here: **[Community Dashboard](https://huggingface.co/spaces/Tnsr-q/neural-conformality-toolkit?page=Community+Dashboard)**.

## Local Development

To run the toolkit on your own machine:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Tnsr-Q/neural-conformality.git](https://github.com/Tnsr-Q/neural-conformality.git)
    cd neural-conformality
    ```
2.  **Set up a Python environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```

## Contributing

We welcome contributions of all kinds! Please feel free to open a [GitHub Issue](https://github.com/Tnsr-Q/neural-conformality/issues) to report bugs, suggest features, or discuss the theory.

