# EAHS Science + Math Learning Campus

A static website with a course-selection landing page, student learning portals and teacher figure studios. Built for GitHub Pages without accounts, a server, paid APIs or a package installation.

## Included courses

| Course | Units | Course investigations |
|---|---:|---:|
| AP Biology — retained existing portal | 8 plus data/laboratory collection | 82 |
| AP Chemistry | 9 | 45 |
| Anatomy & Physiology | 14 body-system sections | 47 |
| AP Calculus AB | 8 | 39 |
| AP Calculus BC | 10 | 59 |

There are 190 new course investigations. Calculus BC includes all 39 AB investigations and 20 additional BC investigations: integration by parts, partial fractions, improper integrals, Euler approximation, logistic equations, arc length, parametric/vector/polar models and series. The new courses use 151 distinct model implementations because the AB models are shared with BC. Biology's existing model engine is retained separately.

These are collections of quantitative models, numerical approximations, conceptual structures and evidence investigations. A schematic is identified as a schematic. They supplement a complete curriculum; they do not claim to simulate every topic or replace a textbook, laboratory course, anatomical atlas or graphing calculator.

## Publish in the existing GitHub Pages repository

1. Extract EAHS-Science-Math-Learning-Campus.zip.
2. Upload the extracted contents into the root of Zelensky-EA/EAHSScience-Studio, replacing matching files and preserving the course folders. index.html must remain at the repository root.
3. Commit the upload. Keep Pages deploying from the existing branch and /(root).
4. After the deployment finishes, open your existing site address: https://zelensky-ea.github.io/EAHSScience-Studio/ . The landing page now offers all five courses.
5. Keep that same link on the EAHS Science page, or link directly to a course:
   - ap-biology/index.html
   - ap-chemistry/index.html
   - anatomy-physiology/index.html
   - ap-calculus-ab/index.html
   - ap-calculus-bc/index.html

Uploading the ZIP alone does not publish the website. Its extracted files and folders must be uploaded. Teacher studios are available at each course's teacher.html.

Each new course also has an independent ZIP and a portable HTML edition. For a separate GitHub Pages repository, extract the course ZIP and upload its contents to that repository's root. For a local preview, open the portable HTML in a browser; its student and teacher unit routes use the page query parameter. A hosted normal index.html is recommended for classroom use.

## Student learning workflow

Descriptions, goals, equations and limitations accompany every investigation.

1. Predict from the starting settings, using a numeric estimate or a concept choice, and explain the reasoning.
2. Reveal the model; manipulate controls using numeric fields and sliders. Scientific parameters spanning many orders of magnitude have logarithmic sliders. Capture observations, units and settings, up to 12 observations per activity.
3. Design a fair comparison and write a claim, evidence and mechanism/mathematical argument. Record at least two distinct settings and check four self-review criteria.
4. Complete the workflow and compare feedback with the saved prediction. Feedback is calculated from the original settings, so moving a control does not change the prediction's expected answer.

Completion marks workflow completion, not demonstrated mastery. Written explanations are not automatically graded and do not receive AP scores. A mistaken prediction can still lead to a completed, well-reasoned investigation.

Numeric estimate checks use the model-specific relative tolerance, usually 5% or 10%. For an expected answer of zero, the absolute tolerance is 1e-6. Nonzero tiny quantities, including photon energy, use relative tolerance rather than a fixed absolute floor. Concept choices are reordered deterministically so correct responses do not always occupy the first position.

Download a readable HTML journal for submission or printing, or export JSON with settings, notes, metrics and a bounded sample of model data. Full available model rows are exported separately with Data CSV. Journals cover the current course across its visited units. JSON re-import is not implemented.

## Teacher studio

Live parameter controls, custom figure titles, grayscale, PNG/SVG exports, printing, data CSV, settings links and browser-saved presets. Selected Anatomy models also provide a separate structure schematic and Diagram SVG export. Enlarge model preserves parameter controls while giving the figure more screen space.

## Progress and accounts

Progress is stored locally on this browser/device and website origin. There is no shared teacher dashboard, login, assignment distribution or gradebook. Students submit downloaded journals using your usual LMS. Export before changing devices, clearing browser data or using a shared computer. Work in one portal tab at a time to avoid concurrent browser-storage writes. Local-file storage behavior varies by browser; storage failures are shown in the portal.

The new courses use the eahs-campus-journal-v1 storage key. Biology retains its existing eahs-learning-journal-v1 key, so progress can persist when hosted under the same origin. Teacher presets and journals use separate storage keys. Settings links include model parameters, not student journal text.

## Scientific references and scope

AP course unit organization checked October 3, 2026:
- AP Chemistry: https://apcentral.collegeboard.org/courses/ap-chemistry
- AP Calculus AB/BC: https://apcentral.collegeboard.org/media/pdf/ap-calculus-ab-and-bc-course-and-exam-description.pdf
- Anatomy & Physiology organization and mechanisms: https://openstax.org/details/books/anatomy-and-physiology-2e

Chemistry titles reflect the current AP Central unit names, including Compound Structure and Properties, Properties of Substances and Mixtures, and Thermodynamics and Electrochemistry. College extensions such as quantitative van ’t Hoff calculations are marked in model notes. Anatomy's 14 sections are a body-system teaching organization, not an AP course designation.

Limits are explicit: ideal gases and solutions, simplified pathways, illustrative—not measured—curves, bounded numerical integration, simplified tissue and organ drawings, and restricted function families. Anatomy models are educational mechanisms, not diagnosis, treatment recommendations or patient-specific predictions. Calculus uses radians. Polar area over a retraced interval is marked as area with multiplicity; interval endpoints are checked separately for power series. Euler, logistic and other BC-only additions are excluded from the AB catalog.

## Validation and source

The build-source folder contains readable source, the builder and checks:
- node build-source/test-models.cjs: scientific/mathematical invariants, course scope, 151 default model checks/figures, 798 parameter variants with 34 expected model-domain errors.
- node build-source/test-portal.cjs: all 190 new student workspaces and teacher unit workspaces, prediction gating, controls, evidence, baseline feedback, progress reload, exports, reset and portable routing, using a DOM fixture.
- SVG XML validation and raster inspection of representative chemistry, anatomy and calculus figures.
- Static page/asset/route validation, including the retained Biology pages.

Full real-browser layout, download, printing, mobile and accessibility verification remains outstanding because no browser binary is available in the build environment. A DOM fixture is not a browser. Preview desktop and phone layouts and try downloads after deployment before assigning the portal to students.

Rebuild with python build-source/build.py; the output is written to build-source/site. Copy that generated site's contents into the repository root. The builder uses Python and Node's standard libraries; no npm dependencies are required. Model catalogs in each course folder list all investigations, fields, equations, limits and learning goals.

Independent resource; not endorsed by College Board.
