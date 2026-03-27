import frappe
from frappe.model.document import Document


class FormNumberCard(Document):
    def validate(self):
        if frappe.db.exists(
            self.doctype,
            {"number_card_name": self.number_card_name, "doctype_form": self.doctype_form, "name": ("!=", self.name)},
        ):
            frappe.throw(frappe._("This card already exist in doctype form."))
