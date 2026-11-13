# Keep the Allan Lab theme; personalize its content

The user requires the original Allan Lab design, not merely Jekyll as a framework. They subsequently explicitly authorized rebuilding the CV from scratch, filling all personal sections from the CV, making the blog English, and preparing an editable Publications section.

- Keep the original palette, typography, stylesheets, fonts, Bootstrap navigation, page grid, and theme. Do not add a global override theme or decorative redesign.
- CV layout and page content may be redesigned using the existing template components. Personalize header/footer text, the home-page heading/content, research, and publications without replacing their visual foundation.
- The original design baseline is commit `f25f182c00dbd1e625bb355571cc352bb9f40612`. Protected source files and their Git blob identities are recorded in `scripts/template-baseline.json`.
- Add requested functionality using existing Bootstrap components and the original layouts. Do not add a global override stylesheet or inject a new visual theme.
- Blog posts, controls, templates, status messages, and writing/publication instructions must default to English. Keep the original Bootstrap navigation and footer structure.
- Run `python3 scripts/check_template.py` and the relevant build/functional checks before publishing changes.
- Content changes must be based on the user's sources. Use the existing repository CV for now; its data is recorded in `_data/cv.yml`. The intended Google Drive CV has not been identified. Do not invent or substitute other people's details, papers, degrees, or positions.
- Keep conference presentations distinct from journal publications. Publications data may remain empty until the user supplies an entry; preserve the Allan Lab YAML field names and provide a non-public template.
