# ErpTronix ERPNext v16 Theme

Professional and modern theme package for ERPNext/Frappe v16.

## What this changes

- Modern Desk UI styling and polish
- Custom branded login page (`/login`) with ErpTronix identity
- Additional custom DocTypes for dashboard and card mappings
- Focus on backend usability and visual consistency

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
