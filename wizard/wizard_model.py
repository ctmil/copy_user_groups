# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError,ValidationError
from odoo.tools import float_is_zero, pycompat
from odoo.addons import decimal_precision as dp
from datetime import date
import os
import xml.etree.ElementTree as ET

class CopyGroupsWizard(models.TransientModel):
	_name = 'copy.groups.wizard'
	_description = 'copy.groups.wizard'

	def action_confirm(self):
		if not self.user_id:
			raise ValidationError('Debe seleccionar un usuario')
		if self.user_id.id == self.origin_user_id.id:
			raise ValidationError('El usuario seleccionado no puede ser el mismo que el usuario original')
		groups = self.origin_user_id.groups_id
		res = []
		for group in groups:
			res.append(group.id)
		vals = {
			'groups_id': [(6, 0, res)],
			}
		user_id = self.user_id
		user_id.write(vals)
		return

	origin_user_id = fields.Many2one('res.users',string='Usuario Original')
	user_id = fields.Many2one('res.users',string='Usuario')

