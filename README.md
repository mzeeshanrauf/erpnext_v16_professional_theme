# ERPNext v16 Professional Desk Theme

Professional and clean desk theme for ERPNext/Frappe v16.

## What this changes

- Professional blue-gray brand palette
- Refined navbar, cards, buttons, and list view styling
- Better contrast, softer shadows, modern spacing
- Focus on Desk (backend) UX

## Install

From your bench folder:

```bash
bench get-app /Users/zeeshanrauf/Downloads/erpnext_v16_professional_theme
bench --site yoursite install-app erpnext_v16_professional_theme
bench build --app erpnext_v16_professional_theme
bench --site yoursite clear-cache
```

Then hard refresh browser (`Cmd + Shift + R` on Mac).

## Notes

- Theme is injected through `app_include_css` and applies on Desk.
- If another theme app overrides the same selectors, load order can affect final look..
