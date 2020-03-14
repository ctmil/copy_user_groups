# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError,ValidationError
from odoo.tools import float_is_zero, pycompat
from odoo.addons import decimal_precision as dp
from datetime import date
import os
import base64
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import XML, fromstring, tostring
from collections import defaultdict
import logging

_logger = logging.getLogger(__name__)

class ResUsers(models.Model):
	_inherit = 'res.users'

	def copy_user_groups(self):
                vals = {
                        'origin_user_id': self.id,
                        }
                wizard_id = self.env['copy.groups.wizard'].create(vals)
                return {
                        'type': 'ir.actions.act_window',
                        'name': 'Copiar groups',
                        'res_model': 'copy.groups.wizard',
                        'res_id': wizard_id.id,
                        'view_type': 'form',
                        'view_mode': 'form',
                        'target': 'new',
                        'nodestroy': True,}

