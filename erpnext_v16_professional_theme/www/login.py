import frappe
from frappe import _

no_cache = True


def get_context(context):
    if frappe.session.user != "Guest":
        frappe.local.flags.redirect_location = "/app"
        raise frappe.Redirect

    context.no_header = True
    context.title = _("Login")
    context.disable_signup = frappe.utils.cint(
        frappe.db.get_single_value("Website Settings", "disable_signup")
    )
    context.login_label = _("Email or Username")
    context.app_name = "ErpTronix"
    context.logo = (
        frappe.db.get_single_value("Theme Settings", "app_logo")
        or "/assets/frappe/images/frappe-framework-logo.svg"
    )
    return context
