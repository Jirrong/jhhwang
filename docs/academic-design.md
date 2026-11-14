# Academic UI refinement

The author requested a broader review of type, hierarchy, images, and shared record widths while keeping the Allan Lab foundation and restrained palette. The implementation keeps Bootstrap navigation, footer, data conventions, and template attribution. Original portrait, logos, and CV PDF are unchanged.

## References and decisions

| Reference | Useful observation | Application here |
| --- | --- | --- |
| [Allan Lab](https://www.allanlab.org/aboutwebsite.html) | Familiar academic navigation, muted palette, editable publication data | Retain the foundation and YAML fields; extend the shared card components |
| [Baran Lab publications](https://baranlab.org/publications/) | Graphical abstracts and publication citations communicate different kinds of information | Give images a separate white figure area below the title, authors, and citation; retain full image boundaries |
| [Engle Lab publications](https://www.englelab.com/publications/) | Repeated publication records pair scientific imagery with structured citations | Use consistent record geometry and spacing, with figures separate from metadata |
| [Junseo Lee](https://harris-junseo-lee.github.io/) | Restrained personal profile and academic type hierarchy | Compact right-edge portrait, serif major headings, sans-serif reading text and card titles |
| [Cory Simon](https://corysimon.github.io/) | A direct personal introduction and clear article/project entry points | Keep Home concise, with distinct Research, Posts, and News sections |

The Baran page's direct request returned a site security redirect; its publication structure was checked through publicly indexed page text and image references. Other sites' biographies, publication records, images, and CSS are not reused. The native collapsed Abstract control is an implementation choice for this site.

## Geometry and type

- All pages use a 1360px maximum container and the same page gutters.
- Research and Publications use the same notebook layout; research, paper, conference, and news records share `.record-card` and `.record-main`. Their inner widths, padding, and body type match. The previous selected-paper grid is removed; selected papers receive a badge in their single full-width record.
- Source Sans 3 is used for reading text, controls, and card titles. Source Serif 4 identifies major page and section headings. Both are variable fonts hosted locally with SIL Open Font Licenses. Sans-only and mixed-heading variants were compared in the real browser before choosing the mixed hierarchy.
- Card titles, authors/context, compact labelled facts, supporting figures, and disclosure controls form separate visual groups. Rules separate major sections; grey cards keep related material together.
- The Home portrait sits at the right content edge; the original aspect ratio and compact display size are retained. Institution logo heights account for their original white margins through CSS.

## Optional content and interaction

News can include one photo or a gallery. Papers and conference presentations support photographs, graphical abstracts, captions, and a full text abstract. Scientific images use `contain` sizing and link to the original; no diagram is cropped. Abstracts use initially closed native `details`/`summary`, supporting touch, keyboard input, and disabled JavaScript. Optional MathJax reflows equations when an abstract is opened.

Missing media or abstract text leaves no empty controls. Actual scientific abstract text and photographs are supplied by the author; test fixtures remain outside the public data. The Site guide and excluded templates document the format, and content checks reject missing local images or missing descriptive alt text.

## Verification

The refinement was inspected at desktop and mobile sizes. Browser checks compare actual card and inner body rectangles across Research, Publications, and News, check all page gutters and the right portrait edge, test the responsive navbar, and verify local font loading. Separate fixture pages exercise long abstracts, inline equations, portrait and landscape images, galleries, original-image links, keyboard disclosure, and operation without JavaScript. The ordinary Jekyll, content, source-baseline, PDF, blog, and importer checks remain required.
