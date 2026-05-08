import sys
import importlib

# -- Dependency check --
DEPENDENCIES = {
    "pandas":     "Data manipulation ready",
    "numpy":      "Numerical computation ready",
    "matplotlib": "Visualization ready",
}

print("LOADING STATUS: Loading programs...")
print("Checking dependencies:")

missing = []
for pkg, msg in DEPENDENCIES.items():
    try:
        mod = importlib.import_module(pkg)
        version = getattr(mod, "__version__", "?.?.?")
        print(f"  [OK] {pkg} ({version}) - {msg}")
    except ImportError:
        print(f"  [MISSING] {pkg} - {msg}")
        missing.append(pkg)

if missing:
    print(f"\nMissing: {', '.join(missing)}")
    print("  pip:    -pip install -r requirements.txt")
    print("  poetry: -poetry install")
    sys.exit(1)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -- Generate Matrix data --
print("\nAnalyzing Matrix data...")
N = 1000
rng = np.random.default_rng(42)

print(f"Processing {N} data points...")
df = pd.DataFrame({
    "x":       rng.uniform(-100, 100, N),
    "y":       rng.uniform(-100, 100, N),
    "signal":  rng.exponential(5.0, N),
    "anomaly": rng.choice([False, True], N, p=[0.9, 0.1]),
})

# -- Visualization --
print("Generating visualization...")
normal, anom = df[~df.anomaly], df[df.anomaly]

fig, ax = plt.subplots()
sc = ax.scatter(normal.x, normal.y, c=normal.signal, cmap="plasma", s=15, alpha=0.7, label="Normal")
ax.scatter(anom.x, anom.y, s=60, facecolors="none", edgecolors="red", linewidths=1.2, label="Anomaly")
plt.colorbar(sc, label="Signal")
ax.set(title="Matrix Agents", xlabel="X", ylabel="Y")
ax.legend()
plt.savefig("matrix_analysis.png", dpi=120, bbox_inches="tight")

print("\nAnalysis complete!")
print("Results saved to: matrix_analysis.png")