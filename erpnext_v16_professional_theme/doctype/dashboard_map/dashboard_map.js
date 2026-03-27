frappe.ui.form.on("Dashboard Map", {
  refresh(frm) {
    const fieldsList = [];
    const titleFields = [];
    if (!frm.doc.doctype_name) return;

    frappe.model.with_doctype(frm.doc.doctype_name, () => {
      frappe.get_meta(frm.doc.doctype_name).fields.forEach((df) => {
        if (df.fieldtype === "Geolocation") fieldsList.push({ label: df.label, value: df.fieldname });
        if (df.fieldtype === "Data") titleFields.push({ label: df.label, value: df.fieldname });
      });
      frm.set_df_property("doctype_field", "options", fieldsList);
      frm.set_df_property("title_field", "options", titleFields);
    });
  },
});
