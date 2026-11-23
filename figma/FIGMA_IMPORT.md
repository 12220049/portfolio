# Figma design package — Novin Rai

## What is supplied

There are **six importable vector artboards**:

| Fidelity | Desktop homepage | Mobile homepage | Desktop case study |
|---|---|---|---|
| Low (wireframe) | `low_home_desktop.svg` | `low_home_mobile.svg` | `low_case_desktop.svg` |
| High (visual UI) | `high_home_desktop.svg` | `high_home_mobile.svg` | `high_case_desktop.svg` |

The high-fidelity homepage SVGs contain Novin's supplied photograph embedded as a single image element, while the rest of the layout consists of SVG vector/text objects. The exact degree of text-layer editability may depend on Figma's importer and installed fonts.

Screenshots of the **actual website rendering** are in `previews/`, for reference when reviewing the design.

## Import into Figma

1. Open Figma and create a **new Design file**, e.g. `Novin Rai | Portfolio UI`.
2. Drag each of the six `.svg` files onto the canvas, or use Figma's SVG import/paste options.
3. Group/artboard the screens into sections: **01 Wireframes** and **02 High-fidelity**.
4. Check text/font conversion and replace any imported text elements that Figma treats as outlines if you need to edit the wording.
5. Use `design-tokens.json` for colors, typography and spacing.
6. Keep the attached codebase as the functioning implementation source.

## Create the publicly viewable link

1. In Figma, click **Share** on your new design file.
2. Under **General access**, choose **Anyone with the link**.
3. Choose **Can view**, not **Can edit**, for public portfolio visitors.
4. Copy the real Figma share URL. It will typically be a `figma.com/design/...` link.
5. Edit `js/site-config.js`:

```js
figmaPublicUrl: 'https://www.figma.com/design/YOUR-ACTUAL-FILE-ID/YOUR-ACTUAL-FILE-NAME'
```

6. Re-deploy the website. A public design link will appear automatically on `design.html`.

**No public URL has been created by this package.** A ZIP, SVG, or screenshot is not itself a hosted or shared Figma design.

## Design tokens

- Ink navy `#15283C`
- Blue `#235A97`
- Slate `#61758A`
- Warm gold `#B8884F`
- Page gray `#F6F8FA`
- Primary font: Manrope
- Body font: DM Sans

## Scope of designs

These boards represent the **portfolio website**, not verified low/high fidelity Figma designs for the individual student projects. The original project files and real project screenshots were not supplied.
