# -*- coding: utf-8 -*-

from odoo import fields, models, api
from odoo.tools import pycompat

class mail_followers(models.Model):
    _inherit = 'mail.followers'

    def _add_followers(self, res_model, res_ids, partner_ids, partner_subtypes, channel_ids, channel_subtypes,
                       check_existing=False, existing_policy='skip'):
        """ Internal method that generates values to insert or update followers. Callers have to
        handle the result, for example by making a valid ORM command, inserting or updating directly
        follower records, ... This method returns two main data

         * first one is a dict which keys are res_ids. Value is a list of dict of values valid for
           creating new followers for the related res_id;
         * second one is a dict which keys are follower ids. Value is a dict of values valid for
           updating the related follower record;

        :param check_existing: if True, check for existing followers for given documents and handle
        them according to existing_policy parameter. Setting to False allows to save some computation
        if caller is sure there are no conflict for followers;
        :param existing policy: if check_existing, tells what to do with already-existing followers:

          * skip: simply skip existing followers, do not touch them;
          * force: update existing with given subtypes only;
          * replace: replace existing with nex subtypes (like force without old / new follower);
          * update: gives an update dict allowing to add missing subtypes (no subtype removal);
        """
        if res_model != 'helpdesk.ticket':
            return super(mail_followers, self)._add_followers(res_model=res_model, res_ids=res_ids, partner_ids=partner_ids, partner_subtypes=partner_subtypes, channel_ids=channel_ids, channel_subtypes=channel_subtypes,
                       check_existing=False, existing_policy='skip')
        return dict(), dict()

