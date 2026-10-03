# EAHS Science Figure & Model Studio

A standalone, original science tool site for AP and introductory college instruction. Link to it from the EAHS Science Department website. All calculations happen in the browser; no account, server, paid API, analytics, or network-dependent library is required.

</a>
```

## Tools and instructional scope

| Tool | Implemented capabilities |
| --- | --- |
| Punnett squares | One- and two-locus crosses, complete dominance, one-locus incomplete dominance and codominance, X-linked recessive crosses, genotype/phenotype probabilities and expected counts |
| Pedigrees | Three-generation fixed family; editable affected/unaffected/unknown status; random Mendelian families; exhaustive compatibility checks for AR, AD, XLR, XLD and Y-linked inheritance; possible genotypes; conditional recessive-carrier probabilities |
| Population growth | Analytic exponential and logistic solutions; positive or negative intrinsic growth; starting population and carrying capacity; population, total growth and per-capita growth plots |
| Predator–prey | Classic Lotka–Volterra and logistic-prey extension; adjustable rates; time series and phase plane; positive coexistence equilibrium; 12,000-step fourth-order Runge–Kutta integration |
| Gel electrophoresis | DNA ladders and up to six sample lanes; 100–10,000 bp linear DNA fragments; schematic log-size migration; unresolved-band merging and optional size labels |
| Micropipettes | Conventional P20/P200/P1000 three-digit readings; valid ranges and increments; µL/mL conversion; reading practice; entered-replicate mean, sample SD, CV and signed bias |
| pH | Direct pH, strong monoprotic acid, weak monoprotic acid equilibrium including water autoionization, Henderson–Hasselbalch buffer ratios, digital display and illustrative pH paper |

The interface includes Figure Builder and Explore Model views, equations, assumptions, reasoning prompts, PNG/SVG export, CSV data, figure-only printing, black-and-white figures, browser presets, and share links that encode current settings.

The answer toggle hides result tables and answer annotations. It is a worksheet convenience, not an access-control mechanism: data exports and the local source contain computed answers. Micropipette practice remains available when answers are hidden.

## Scientific boundaries

These models support reasoning at AP/introductory college level; they are not comprehensive physical or clinical simulators.

- Pedigree structure is fixed in this version. Status is editable; relationships, sex and generation count are not. The solver assumes one fully penetrant locus, unrelated founders and no new mutation. It can report multiple compatible modes. Equal founder-genotype priors are teaching assumptions, not population-frequency or clinical estimates.
- Two-locus Punnett squares assume independent assortment. Linkage, epistasis, selection and unequal viability are outside this version.
- Ecology plots are deterministic continuous-time model outputs. They do not represent real field datasets. Time units are arbitrary but must be consistent with entered rates.
- Gel migration is schematic. It does not predict actual migration from agarose percentage, voltage, running time or conformation. The default undigested sample represents linear DNA, not a circular plasmid. Fragment sizes are entered manually rather than calculated from a DNA sequence or enzyme recognition sites.
- Pipette hardware varies; verify the display and range on your own instruments. Statistical metrics describe the entered measurements and do not certify calibration.
- pH assumes ideal dilute water at 25 °C. The buffer equation is an approximation and does not model titration or buffer capacity. Paper colors are illustrative.

## Validation

Run `node test-models.cjs` to check genetic probabilities, recessive carrier inference, inheritance exclusions, valid random families, analytic population solutions, predator–prey equilibria and numerical convergence, pipette display/range behavior, measurement statistics, pH equilibria and gel migration direction.

Run `node test-renderers.cjs` to generate the seven default SVG figures and ten advanced or blank variants. The resulting `qa-figures` directory is for local review.

Completed checks: JavaScript syntax; the model test suite; all 17 renderer scenarios; XML parsing and SVG rasterization; visual inspection of the rendered figure set. Visual review identified and corrected an overly rounded small-volume unit conversion.

Full browser interaction, mobile layout, PNG downloading, print layout, and clipboard behavior could not be verified in the build environment: no browser executable was installed and browser downloads were blocked. Check those features in your browser before classroom deployment. A Playwright smoke-check script is included for environments with Node, Playwright and Chromium installed: start `python -m http.server 8765` in this folder, then run `node browser-check.cjs` from a second terminal. Scripts are development checks and are not needed for hosting.

## Scientific references

- OpenStax Biology 2e, environmental limits to growth: https://openstax.org/books/biology-2e/pages/45-3-environmental-limits-to-population-growth
- OpenStax Biology 2e, inheritance: https://openstax.org/books/biology-2e/pages/12-2-characteristics-and-traits
- Jeffrey R. Chasnov, *Mathematical Biology*, HKUST, sections 1.2 and 1.4: https://www.math.ust.hk/~machas/mathematical-biology.pdf
- NHGRI, electrophoresis: https://www.genome.gov/genetics-glossary/Electrophoresis
- Gilson, PIPETMAN user guide: https://www.gilson.com/pub/media/docs/PIPETMAN_USER_GUIDE_LT801122-I.pdf
- OpenStax Chemistry 2e, acid–base equilibrium: https://openstax.org/books/chemistry-2e/pages/14-3-relative-strengths-of-acids-and-bases
- OpenStax Chemistry 2e, buffers: https://openstax.org/books/chemistry-2e/pages/14-6-buffers

Original implementation created for EAHS Science. Reference-site code, branding and artwork were not copied. AP is a College Board trademark; the resource is independent and is not endorsed by the College Board.
