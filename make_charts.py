"""
GridScore v0 -- publication charts for essay-final.md.
Palette matched exactly to flexvalue/src/outputs.py so both pieces read as one series.
"""
import csv
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = os.path.dirname(__file__)
CHART_DIR = os.path.join(ROOT, "charts")
os.makedirs(CHART_DIR, exist_ok=True)

# --- palette, copied verbatim from flexvalue/src/outputs.py ---
C_ENERGY = "#2a78d6"     # slot 1 blue
C_ANCILLARY = "#eb6834"  # slot 2 orange
C_4CP = "#1baf7a"        # slot 3 aqua
INK_PRIMARY = "#0b0b0b"
INK_SECONDARY = "#52514e"
INK_MUTED = "#898781"
GRIDLINE = "#e1e0d9"
SURFACE = "#fcfcfb"

TIER_COLOR = {
    "Evidenced": C_4CP,
    "Progressing": C_ANCILLARY,
    "Announced-only": C_ENERGY,
}

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica", "Arial", "DejaVu Sans"],
    "text.color": INK_PRIMARY,
    "axes.edgecolor": GRIDLINE,
    "axes.labelcolor": INK_SECONDARY,
    "xtick.color": INK_SECONDARY,
    "ytick.color": INK_SECONDARY,
    "figure.facecolor": SURFACE,
    "axes.facecolor": SURFACE,
    "savefig.facecolor": SURFACE,
})

FIGSIZE = (8, 4.5)  # 1200x675 @150dpi
DPI = 150


def footer(fig, note):
    fig.text(0.015, 0.015, "GridScore v0 — flexvalue project", fontsize=7,
              color=INK_MUTED, ha="left", va="bottom")
    if note:
        fig.text(0.985, 0.015, note, fontsize=7, color=INK_MUTED, ha="right", va="bottom")


def load_rows():
    with open(os.path.join(ROOT, "scored_table.csv")) as f:
        rows = list(csv.DictReader(f))
    rows.sort(key=lambda r: -int(r["total_score"]))
    return rows


# ---------------------------------------------------------------------------
# Chart 1: the approval-to-energize funnel
# ---------------------------------------------------------------------------

def chart1_funnel():
    labels = [
        "Requested\n(large-load queue, press-reported)",
        "Approved to energize\n(ERCOT, Jun 2026)",
        "Observed operating\n(ERCOT, Jun 2026)",
    ]
    values_gw = [474.7, 8.926, 3.966]
    colors = [C_ENERGY, C_ANCILLARY, C_4CP]

    fig, ax = plt.subplots(figsize=FIGSIZE, dpi=DPI)
    y = range(len(labels))
    bars = ax.barh(list(y), values_gw, color=colors, height=0.55, zorder=3)
    ax.set_yticks(list(y))
    ax.set_yticklabels(labels, fontsize=10)
    ax.invert_yaxis()
    ax.set_xlabel("Gigawatts (GW)", fontsize=9.5)
    ax.set_xlim(0, 560)
    ax.xaxis.grid(True, color=GRIDLINE, linewidth=0.8, zorder=0)
    ax.set_axisbelow(True)
    for spine in ["top", "right", "left"]:
        ax.spines[spine].set_visible(False)
    ax.spines["bottom"].set_color(GRIDLINE)

    for bar, val in zip(bars, values_gw):
        label = f"{val:,.1f} GW" if val >= 100 else f"{val:.3f} GW"
        if val > 100:
            ax.text(bar.get_width() - 8, bar.get_y() + bar.get_height() / 2, label,
                     va="center", ha="right", fontsize=10, fontweight="bold", color="white")
        else:
            ax.text(bar.get_width() + 6, bar.get_y() + bar.get_height() / 2, label,
                     va="center", ha="left", fontsize=10, fontweight="bold", color=INK_PRIMARY)

    ax.set_title("Texas large-load queue: requested vs. approved vs. operating",
                  fontsize=12.5, fontweight="bold", loc="left", pad=14, color=INK_PRIMARY)
    fig.subplots_adjust(left=0.30, right=0.96, top=0.85, bottom=0.16)
    footer(fig, "Requested vs. approved/operating: different ERCOT tracking systems, not one ratio")
    fig.savefig(os.path.join(CHART_DIR, "chart1_funnel.png"))
    plt.close(fig)


# ---------------------------------------------------------------------------
# Chart 2: all 21 projects, sorted by score, colored by tier
# ---------------------------------------------------------------------------

def chart2_all_projects():
    rows = load_rows()
    names = [r["project_name"].split(" (")[0] for r in rows]
    scores = [int(r["total_score"]) for r in rows]
    colors = [TIER_COLOR[r["tier"]] for r in rows]
    reversals = [r["documented_reversal_flag"] == "YES" for r in rows]

    fig, ax = plt.subplots(figsize=FIGSIZE, dpi=DPI)
    y = range(len(rows))
    bars = ax.barh(list(y), scores, color=colors, height=0.68, zorder=3)
    ax.set_yticks(list(y))
    ytlabels = [f"{'[R] ' if rev else ''}{n}" for n, rev in zip(names, reversals)]
    ax.set_yticklabels(ytlabels, fontsize=6.6)
    ax.invert_yaxis()
    ax.set_xlim(0, 100)
    ax.set_xlabel("GridScore total (0–100)", fontsize=9)
    ax.xaxis.grid(True, color=GRIDLINE, linewidth=0.8, zorder=0)
    ax.set_axisbelow(True)
    for spine in ["top", "right", "left"]:
        ax.spines[spine].set_visible(False)
    ax.spines["bottom"].set_color(GRIDLINE)

    for tier, x0 in [(40, "Progressing"), (70, "Evidenced")]:
        ax.axvline(tier, color=INK_MUTED, linewidth=0.9, linestyle=(0, (3, 2)), zorder=2)

    for bar, val in zip(bars, scores):
        ax.text(bar.get_width() + 1.2, bar.get_y() + bar.get_height() / 2, str(val),
                 va="center", ha="left", fontsize=6.6, color=INK_PRIMARY)

    handles = [plt.Rectangle((0, 0), 1, 1, color=TIER_COLOR[t]) for t in
               ["Evidenced", "Progressing", "Announced-only"]]
    ax.legend(handles, ["Evidenced (70–100)", "Progressing (40–69)", "Announced-only (0–39)"],
              loc="lower right", fontsize=7, frameon=False)

    ax.set_title("All 21 projects, ranked by GridScore total  ([R] = documented reversal)",
                  fontsize=10.8, fontweight="bold", loc="left", pad=10, color=INK_PRIMARY)
    fig.subplots_adjust(left=0.34, right=0.96, top=0.90, bottom=0.145)
    footer(fig, "9 scores renormalized — Physical excluded per §106.511 (see methodology.md)")
    fig.savefig(os.path.join(CHART_DIR, "chart2_all_projects.png"))
    plt.close(fig)


# ---------------------------------------------------------------------------
# Chart 3: disclosed MW stacked by tier
# ---------------------------------------------------------------------------

def chart3_mw_by_tier():
    rows = load_rows()
    mw_by_tier = {"Evidenced": 0, "Progressing": 0, "Announced-only": 0}
    for r in rows:
        if r["announced_mw"] == "not disclosed":
            continue
        mw_by_tier[r["tier"]] += int(r["announced_mw"])

    tiers = ["Evidenced", "Progressing", "Announced-only"]
    values = [mw_by_tier[t] / 1000 for t in tiers]  # GW
    total = sum(values)
    colors = [TIER_COLOR[t] for t in tiers]

    fig, ax = plt.subplots(figsize=FIGSIZE, dpi=DPI)
    left = 0
    bar_height = 0.5
    for t, v, c in zip(tiers, values, colors):
        ax.barh(0, v, left=left, color=c, height=bar_height, zorder=3,
                edgecolor=SURFACE, linewidth=1.5)
        pct = v / total * 100
        if v / total > 0.05:
            ax.text(left + v / 2, 0, f"{t}\n{v:,.1f} GW ({pct:.0f}%)",
                     ha="center", va="center", fontsize=9.5, fontweight="bold",
                     color="white" if t != "Progressing" else INK_PRIMARY)
        left += v

    ax.set_xlim(0, total)
    ax.set_ylim(-1.3, 1.3)
    ax.set_yticks([])
    ax.set_xlabel("Disclosed announced MW, by tier (GW)", fontsize=9.5)
    for spine in ["top", "right", "left"]:
        ax.spines[spine].set_visible(False)
    ax.spines["bottom"].set_color(GRIDLINE)
    ax.xaxis.grid(True, color=GRIDLINE, linewidth=0.8, zorder=0)
    ax.set_axisbelow(True)

    ax.set_title(f"{total:,.1f} GW of disclosed announced capacity, by evidence tier",
                  fontsize=12.5, fontweight="bold", loc="left", pad=16, color=INK_PRIMARY)
    fig.subplots_adjust(left=0.05, right=0.97, top=0.82, bottom=0.20)
    footer(fig, "19 of 21 projects disclose per-site MW; 2 (Google Armstrong & Haskell Co.) excluded")
    fig.savefig(os.path.join(CHART_DIR, "chart3_mw_by_tier.png"))
    plt.close(fig)




# ---------------------------------------------------------------------------
# Chart 4: Fermi/Project Matador capacity ladder
# ---------------------------------------------------------------------------

def chart4_fermi_capacity_ladder():
    import csv as _csv
    with open(os.path.join(ROOT, "fermi_capacity_ladder.csv")) as f:
        rows = list(_csv.DictReader(f))

    labels = [r["rung"] for r in rows]
    values = [int(r["mw"]) for r in rows]
    is_company_claim = ["company claim" in r["claim_type"] for r in rows]
    colors = [C_ANCILLARY if c else C_4CP for c in is_company_claim]

    fig, ax = plt.subplots(figsize=FIGSIZE, dpi=DPI)
    y = range(len(labels))
    bars = ax.barh(list(y), values, color=colors, height=0.55, zorder=3)
    ax.set_yticks(list(y))
    ax.set_yticklabels(labels, fontsize=10.5)
    ax.invert_yaxis()
    ax.set_xlabel("Megawatts (MW)", fontsize=9.5)
    ax.set_xlim(0, 17000 * 1.14)
    ax.xaxis.grid(True, color=GRIDLINE, linewidth=0.8, zorder=0)
    ax.set_axisbelow(True)
    for spine in ["top", "right", "left"]:
        ax.spines[spine].set_visible(False)
    ax.spines["bottom"].set_color(GRIDLINE)

    for bar, val, r in zip(bars, values, rows):
        label = f"{val:,} MW" if val > 0 else "None shown in the public record"
        if val > 1500:
            ax.text(bar.get_width() - 220, bar.get_y() + bar.get_height() / 2, label,
                     va="center", ha="right", fontsize=9.5, fontweight="bold", color="white")
        else:
            ax.text(bar.get_width() + 220, bar.get_y() + bar.get_height() / 2, label,
                     va="center", ha="left", fontsize=9.5, fontweight="bold", color=INK_PRIMARY)

    handles = [plt.Rectangle((0, 0), 1, 1, color=C_ANCILLARY),
               plt.Rectangle((0, 0), 1, 1, color=C_4CP)]
    ax.legend(handles, ["Company claim", "Independent record"],
              loc="lower right", fontsize=8, frameon=False)

    ax.set_title("Project Matador: capacity ladder, marketed to operating",
                  fontsize=12.5, fontweight="bold", loc="left", pad=14, color=INK_PRIMARY)
    fig.subplots_adjust(left=0.19, right=0.96, top=0.85, bottom=0.16)
    footer(fig, "As of 2026-09-21 — see evidence/01-fermi-america-project-matador.md")
    fig.savefig(os.path.join(CHART_DIR, "chart4_fermi_capacity_ladder.png"))
    plt.close(fig)


if __name__ == "__main__":
    chart1_funnel()
    chart2_all_projects()
    chart3_mw_by_tier()
    chart4_fermi_capacity_ladder()
    print("Wrote 4 charts to", CHART_DIR)
