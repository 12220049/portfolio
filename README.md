# Novin Rai — Professional AI & Data Science Portfolio

A complete static portfolio website with **four project case-study pages**, a **low-/high-fidelity design gallery**, your actual supplied portrait and a responsive navy / blue / warm-gold visual system.

## Open the portfolio

Open `index.html` in a browser, or (recommended for reliable relative links) run from this directory:

```bash
python -m http.server 8000
```

Then open `http://localhost:8000` in your browser.

No `npm install`, backend, paid services or database required. The Google Fonts import gracefully falls back to local system fonts when offline.

## File map

```text
Novin_Rai_Professional_Portfolio/
├── index.html                       Homepage
├── design.html                      Low and high fidelity design gallery
├── case-studies/
│   ├── index.html                   Case study index
│   ├── blood-group-detection.html   Blood Group Detection AI
│   ├── dancetutor.html              DanceTutor
│   ├── deforestation-detection.html Deforestation Detection AI
│   └── dzen-ai.html                 Dzen AI
├── assets/
│   ├── novin-rai-portrait.jpg       ONLY user-supplied photo
│   ├── mark.svg                     Custom NR vector logo
│   └── projects/                    Four original concept SVG graphics
├── css/site.css                     Fully responsive styling
├── js/site-config.js                Contact, resume and public Figma URL settings
├── js/site.js                       Mobile nav, design switch, year, links
├── figma/
│   ├── low_home_desktop.svg         Low-fidelity desktop homepage
│   ├── low_home_mobile.svg          Low-fidelity mobile homepage
│   ├── low_case_desktop.svg         Low-fidelity case-study page
│   ├── high_home_desktop.svg        High-fidelity desktop homepage
│   ├── high_home_mobile.svg         High-fidelity mobile homepage
│   ├── high_case_desktop.svg        High-fidelity case-study page
│   ├── design-tokens.json          Color/typography/spacing reference
│   ├── FIGMA_IMPORT.md              How to import and publish the design
│   └── previews/                    Browser-rendered website screenshots
├── build_pages.py                   Site content generator (optional)
└── README.md
```

## Change your information

1. Open `js/site-config.js`.
2. Confirm the GitHub username and enter your real email, LinkedIn URL, CV URL and, after publication, Figma public URL.
3. Links with blank values are hidden rather than pointing to fake accounts or inactive buttons.
4. For prose and case studies, edit `build_pages.py`, run `python build_pages.py`, and review the generated HTML.
5. Replace the project diagrams with your own actual project screenshots when available.

**Important:** Running `build_pages.py` regenerates all seven HTML pages. If you edit HTML directly, do not regenerate until you have transferred those changes into the generator.

### What needs your verification

The four project titles and their general descriptions came from you. Specific code repositories, individual contributions, model architectures, datasets, performance metrics, implementation screenshots, dates and outcomes were **not** provided. The case studies therefore explain the problem and likely validation direction rather than inventing technical achievements. Add the real evidence before using them as a graded technical portfolio.

The blood-group model is explicitly described as exploratory and **not clinically validated**. Fingerprints must not substitute for standard laboratory blood typing.

## Put the designs in Figma

See `figma/FIGMA_IMPORT.md`.

The bundle includes six **Figma-importable SVG artboards** with editable vector layout elements, plus screenshots of the working website. These are **not a native `.fig` file** and a public Figma URL has **not** been created: sharing requires a connected Figma account and the user's sharing settings.

After you import, set Figma Share to **Anyone with the link → Can view**, copy the actual URL, and paste it into `figmaPublicUrl` in `js/site-config.js`. Your website's Design page will then display a working public Figma link.

## Deploy to Render (Static Site)

1. Unzip and upload the **contents of this directory** to a GitHub repository (keep `index.html` at repository root).
2. In Render: **New → Static Site** and connect the repository.
3. Branch: `main` (or your actual branch).
4. Build command: `echo "No build required"`.
5. Publish directory: `.` (a period, meaning repository root).
6. Deploy. Your root URL serves `index.html`; case studies have direct `.html` URLs.
7. Test one case study and `design.html` after deployment.

> Do not configure this as a Node.js Web Service. It is a static HTML/CSS/JS site.

## Privacy and ownership

- Portrait: the single image uploaded for this conversation, used with your permission in the portfolio.
- Logo, project concept drawings and design artboards: new SVG graphics created for this portfolio.
- No photographs or illustrations from the friend's master ZIP were used.
- No account passwords, addresses, invented email addresses or fabricated social profiles are included.
- GitHub in config defaults to `https://github.com/12220049` based on the earlier setup conversation; **confirm it belongs to you** before publication.
