from odoo import http
from odoo.http import request

#to extend to another class do the below import and pass "ProperyController" as args in class function
#from odoo.addons.real_estate_ads.controllers.main import PropertyController

class Property_Controller(http.Controller):

#because we are not authenticating this route we need to have super user access to implement
    @http.route(['/properties'], type='http', website=True, auth="public")
    def show_properties(self):
        property_ids = request.env['estate.property'].sudo().search([])
        print(property_ids)
        return request.render("real_estate_ads.property_list", {"property_ids": property_ids})