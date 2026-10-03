# EAHS Science — AP Biology Unit Edition

Eight unit pages, an eight-card landing page, and a shared data/investigation page. The collection contains **82 tools**, including quantitative simulations, figure builders, qualitative mechanism models and evidence activities. College extensions and model limitations are identified in the notes.

## Update the existing GitHub site

1. Extract `EAHS-Science-Unit-Edition.zip` on your computer.
2. Open the **Code** tab of `Zelensky-EA/EAHSScience-Studio`.
3. Choose **Add file → Upload files**.
4. Upload the extracted files and folders to the repository's main directory. Upload files, not the ZIP itself. Replace the existing `index.html`, `styles.css`, `models.js`, `app.js`, and `EAHS-Science-Studio.html` with the updated versions.
5. Commit directly to `main`.
6. Keep Pages configured as **Deploy from a branch → main → /(root)**. GitHub Pages will rebuild after the commit.
7. Check the **Actions** deployment status, then open the site. If an older version appears, refresh while bypassing cache.

The public address remains:

https://zelensky-ea.github.io/EAHSScience-Studio/

The department website's existing link can continue to use that address.

GitHub documentation:
https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

For the site itself, the required files are `index.html`, `unit-1.html` through `unit-8.html`, `data-tools.html`, `styles.css`, `models.js`, `extra.js` and `app.js`. Everything uses relative paths compatible with a GitHub Pages project repository. No build step, backend, paid API or external JavaScript library is required.

## Offline copy

`EAHS-Science-Studio.html` is a self-contained copy of the entire unit collection. Open it in a current browser. Its unit navigation uses a page query parameter to load an embedded page. Browser presets and clipboard behavior depend on the browser's permissions. Hosted links are useful for sharing with others; local file links generally are not.

## Collection

| Page | Tools | Examples |
| --- | ---: | --- |
| Unit 1 — Chemistry of Life | 8 | Water, elements, polymers, carbohydrates, lipids, nucleic acids, proteins, pH |
| Unit 2 — Cells | 10 | Trafficking, cell size, permeability, diffusion, water potential, tonicity, osmosis data, pumps, compartments, endosymbiosis |
| Unit 3 — Cellular Energetics | 9 | Enzymes, activation energy, ATP coupling, photosystems, light response, respiration, fermentation, respirometry, pigments |
| Unit 4 — Communication & Cell Cycle | 6 | Receptors, signaling, feedback, chromosome/DNA accounting, mitotic index, checkpoints |
| Unit 5 — Heredity | 7 | Punnett squares, pedigrees, meiosis/nondisjunction, linkage, ABO/epistasis, polygenic traits, reaction norms |
| Unit 6 — Gene Expression & Regulation | 11 | Gels, replication, transcription/processing, translation, operons, specialization, mutations, PCR, restriction digest, transformation, primer binding |
| Unit 7 — Natural Selection | 10 | Selection, trait distributions, artificial selection, drift, gene flow, Hardy–Weinberg, sequence comparison, phylogeny, isolation, origins evidence |
| Unit 8 — Ecology | 17 | Population growth, predators/prey, behavior, trophic energy, matter pools, population accounting, sampling, density/disturbance, competition, food webs, mutualism/parasitism, diversity, nutrient enrichment, circadian cues, invasion, habitat patches, functional response |
| Shared data & investigations | 4 | Micropipettes, graphing with SD/SE, chi-square, synthetic replicate experiments |

`model-catalog.json` contains the full tool inventory, topic mappings, field labels and assumptions. Some models connect multiple topics or units. Topic mapping refers to the current course organization; it is not a claim that every adjustable parameter is required AP content.

## Common interactions

- Select a tool within a unit, change inputs and generate an updated figure.
- Figure Builder emphasizes output; Explore Model opens assumptions and a reasoning prompt.
- Show/hide result tables and annotations. Certain figure-specific options also produce blank student versions. The results checkbox does not blank every quantitative figure or protect answers from students.
- Download high-resolution PNG, editable SVG, or CSV when data is available.
- Print the current figure without controls or page navigation.
- Save named browser presets for each tool.
- Copy a link containing the exact settings. Random models use entered seeds for reproducibility.
- On small screens, figure panels scroll horizontally to preserve readable diagram labels.

## Scientific scope

Quantitative models state their equations and assumptions. Schematic mechanisms and evidence activities use qualitative comparisons instead of invented physical predictions.

Examples of boundaries:

- Water potential uses ideal solute potential plus entered pressure in MPa. It predicts initial direction rather than tissue mass change or transport rate. Osmosis mass-change analysis uses entered measurements.
- Enzyme kinetics uses Michaelis–Menten steady-state assumptions. Temperature/pH responses are illustrative functions. It does not compute a real enzyme's kinetics from its name, nor irreversible unfolding from exposure time.
- The photosynthesis electron-flow figure branches electron transfer and proton-driven ATP production. Its stoichiometric output is an assumed upper bound, not a measured light-response rate.
- Protein interaction, membrane packing, endosymbiosis, checkpoint and origins tools are schematic reasoning models.
- The pedigree structure is a fixed three-generation family; phenotypes are editable. Conditional probabilities depend on declared founder-genotype priors, not clinical population frequencies.
- DNA/RNA conversion, standard-code translation, specified sequence mutations, primer exact-match positions and restriction fragments are sequence computations. They do not predict arbitrary protein function or primer melting temperature.
- Quantitative ecological systems use explicit example parameters. They are not calibrated forecasts for a named ecosystem. Trophic pyramid widths are explicitly schematic; numerical labels carry the energy accounting.
- The selection model is diploid. The resistance option is an allele-fitness teaching interpretation, not a clinical or bacterial treatment predictor.
- Phenotype distributions, breeder's equation, Nernst potential, patch occupancy and diversity indices are labeled as extensions or explicitly assumed models.
- SD/SE tools require independent replicates. Chi-square alerts on low expected counts and uses fixed 0.05 critical values for df 1–10. Failure to reject does not prove a null hypothesis.

## Validation and limitations

Completed:

- JavaScript syntax checks.
- Original seven-tool quantitative test suite.
- `test-extended.cjs`: 82 default renderer checks, 82 grayscale/result-hidden variants, 679 individual parameter scenarios, and quantitative checks for water potential, base complementarity, translation, digest conservation, PCR doubling, neutral selection, chi-square and inhibitor behavior. Parameter combinations that violate explicit constraints return errors rather than invalid figures.
- All 164 generated SVG variants parsed as XML. Every default figure rasterized and was visually inspected in unit montages. Visual review corrected branch topology in energy pathways and trophic-pyramid label visibility.
- Local link, asset and control-ID checks across the landing page and nine workspaces.

Full browser rendering and interactions could not be run in the build environment because no browser executable was available and downloading one was blocked. Before classroom deployment, check unit navigation, input changes, saved presets, share links, PNG download and printing in your browser. A Playwright smoke test is included for an environment with Chromium available. The checks are useful development checks, not proof that every possible multi-parameter combination has been validated.

Run from this directory:

```bash
node test-models.cjs
node test-extended.cjs
python check-links.py
```

Optional browser verification, with Playwright and Chromium installed:

```bash
python -m http.server 8765
# In a second terminal:
node browser-check.cjs
```

To regenerate the HTML pages and offline edition after editing source:

```bash
python build-pages.py
```

Generated QA images are not needed for hosting and are omitted from the package. Tests create their own `qa-figures` folder.

## References

Course organization and topic mappings:
https://apcentral.collegeboard.org/media/pdf/ap-biology-course-and-exam-description.pdf
https://apcentral.collegeboard.org/media/pdf/ap-biology-course-at-a-glance.pdf

OpenStax Biology 2e:
https://openstax.org/books/biology-2e

OpenStax Chemistry 2e:
https://openstax.org/books/chemistry-2e

Jeffrey R. Chasnov, HKUST, Mathematical Biology:
https://www.math.ust.hk/~machas/mathematical-biology.pdf

NHGRI, electrophoresis:
https://www.genome.gov/genetics-glossary/Electrophoresis

Gilson, PIPETMAN user guide:
https://www.gilson.com/pub/media/docs/PIPETMAN_USER_GUIDE_LT801122-I.pdf

Original implementation for EAHS Science. Reference-site source code and artwork were not copied. AP is a College Board trademark; this independent resource is not endorsed by College Board.
