/** @odoo-module **/
import { registry } from '@web/core/registry';

import { Component } from '@odoo/owl';

class MyCustomAction extends Component{}
MyCustomAction.template = "CustomActions";

registry.category("actions").add("real_estate_ads.custom_client_action", MyCustomAction);


