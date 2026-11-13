# Preserve the original website design

The user explicitly requires the original Jekyll template design to remain unchanged. “Keep the template” means keep its visual design exactly, not merely its framework.

- Do not redesign the site, change its palette, typography, spacing, header, footer, home/CV layout, or replace its theme.
- The original design baseline is commit `f25f182c00dbd1e625bb355571cc352bb9f40612`. Protected source files and their Git blob identities are recorded in `scripts/template-baseline.json`.
- Add requested functionality using existing Bootstrap components and the original layouts. Do not add a global override stylesheet or inject a new visual theme.
- New blog behavior belongs in notebook-specific layouts, includes, and scripts. Preserve the original header/footer and Bootstrap navigation.
- Run `python3 scripts/check_template.py` and the relevant build/functional checks before publishing changes.
- Content changes must be based on the user's sources. The requested Google Drive CV has not been identified; do not invent or substitute other people's details.
