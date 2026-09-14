# Coverage Matrix — query phrase → atomic item mapping

| Query phrase (verbatim) | Mapped atomic item(s) | Scope check | Gap? |
|---|---|---|---|
| "Briyo" | Entity: Briyo brand; Sub-Q1: company background | OK — full brand scope | No |
| "Vitamin D3" | Entity: Vitamin D3 product; Sub-Q3: formulation quality | OK — D3 form/bioavailability covered | No |
| "2000 IU" | Entity: product dosage field; Sub-Q3: dosage appropriateness | OK — dosage adequacy for claimed benefits | No |
| "90 Softgels" | Entity: product form field; Sub-Q3: softgel bioavailability | OK — softgel vs tablet bioavailability explicitly covered | No |
| "Bone Health" | Entity: claimed benefit; Sub-Q3: scientific support for dosage | OK — 2000 IU D3 and bone health evidence covered | No |
| "Muscle Function" | Entity: claimed benefit; Sub-Q3: scientific support | OK — muscle function evidence for D3 covered | No |
| "Immune Support" | Entity: claimed benefit; Sub-Q3: scientific support | OK — immune function evidence for D3 covered | No |
| "Men/Women" | Scope condition: general adult population supplement | OK — no gender-specific deep dive needed, general population | No |
| "research this brand" | Sub-Q1–Q9: full brand intelligence package | OK — all 9 sub-questions map to brand research | No |

## Result: 0 gaps. All query phrases mapped to atomic items. Decomposition passes.
