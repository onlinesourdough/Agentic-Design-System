# CryptoClub Home Dashboard

Multi-page interactive preview for `home.cryptoclub.dk`. The Home surface was rebuilt from a blank composition around a narrow LibreChat-related shell, direct ecosystem launchers, and an asymmetric intelligence grid.

## Surfaces

| File                | Route (prod)    | Purpose                                                                          |
| ------------------- | --------------- | -------------------------------------------------------------------------------- |
| `index.html`        | `/`             | Home med software-launchers, intelligence-resumé, portfolio, læring og aktivitet |
| `intelligence.html` | `/intelligence` | Heatmaps, AI Market Scanner, algo-signaler og backtests                          |
| `portfolio.html`    | `/portfolio`    | Beholdning, allokering, signaler                                                 |
| `classroom.html`    | `/classroom`    | Kursusgrid, fortsæt-kursus, filtre, progress og Inner Circle                     |
| `lesson.html`       | `/lesson`       | Video, modulnavigation, noter, ressourcer og næste lektion                       |
| `chat.html`         | `/chat`         | Kanaler + mock tråd-panel                                                        |
| `settings.html`     | `/settings`     | Testprofil, Inner Circle-medlemskab, præferencer og sikkerhed                    |
| `ecosystem.html`    | `/ecosystem`    | Live services fra cryptoclub-dk repos                                            |

Shared: `assets/app.css`, `assets/app.js`, `assets/mock-data.js`, branding fra VPS.

## Interactivity (preview)

- Sidebar navigation mellem sider
- App-switcher (dialog) med internal vs subdomain labels
- Produktikoner i app-switcher og neutral AI-launcher med navy hover/focus
- Profilmenu nederst i sidebaren med adgang til profil og settings
- Global søgning (sider, agenter, aktiver, kanaler)
- App-launchers til AI Matthæus, Portfolio og Classroom
- Code-native market- og porteføljevisualiseringer
- Classroom course grid, filtre og selvstændig lesson player
- Market Intelligence tabs, heatmap-accordions, scanner-watchlist, chart-dialog og backtest-accordions
- Chat: søg og filtrér kanaler, vælg samtale, læs pinned kontekst og mock-tråd, afprøv composer
- Demo toasts på wallet/konto-handlinger

## Preview

```sh
npm run preview
```

http://127.0.0.1:4174/examples/cryptoclub-home-dashboard/

Mock data er **CryptoClub-specifik** (AI Matthæus, heatmap, køb/salg, Inner Circle) — ikke Value Profits Protocol.

## References and assets

- The provided dashboard screenshot informed density, sidebar proportion, and asymmetric grouping only. Tesla branding, copy, chart construction, and page structure were not copied.
- Existing Crypto Club / LibreChat material informed near-black chrome, navy accent, product naming, and routes only.
- `assets/logo.png` and `assets/favicon-32x32.png` are customer-provided Crypto Club assets.
- `assets/images/heatmap-*.png` and `assets/images/algo-*.png` are user-provided Crypto Club charts, resized for browser delivery.
- Discord screenshots were used only to understand content hierarchy; Discord chrome and bot embeds are not copied.
- Interface icons and summary graphics are original inline SVG with no external dependency.
