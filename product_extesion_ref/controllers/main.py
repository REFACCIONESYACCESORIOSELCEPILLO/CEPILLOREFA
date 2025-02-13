#################################################################################
import base64
import datetime
import json
import os
import logging
import re
import requests
import werkzeug.urls
import werkzeug.utils
import werkzeug.wrappers

from odoo import http, models, fields, _
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale

_logger = logging.getLogger(__name__)


# class Website(Home):

#     @http.route(['/website/pages', '/website/pages/page/<int:page>'], type='http', auth="user", website=True)
#     def pages_management(self, page=1, sortby='url', search='', **kw):
#         # only website_designer should access the page Management

#         print("################ search >>>>>>>>>>>>>>>>>>>>>> ", search)
#         if not request.env.user.has_group('website.group_website_designer'):
#             raise werkzeug.exceptions.NotFound()

#         Page = request.env['website.page']
#         searchbar_sortings = {
#             'url': {'label': _('Sort by Url'), 'order': 'url'},
#             'name': {'label': _('Sort by Name'), 'order': 'name'},
#         }
#         # default sortby order
#         sort_order = searchbar_sortings.get(sortby, 'url')['order'] + ', website_id desc, id'

#         domain = request.website.website_domain()
#         if search:
#             domain += ['|', ('name', 'ilike', search), ('url', 'ilike', search)]

#         pages = Page.search(domain, order=sort_order)
#         if sortby != 'url' or not request.session.debug:
#             pages = pages._get_most_specific_pages()
#         pages_count = len(pages)

#         step = 50
#         pager = portal_pager(
#             url="/website/pages",
#             url_args={'sortby': sortby},
#             total=pages_count,
#             page=page,
#             step=step
#         )

#         pages = pages[(page - 1) * step:page * step]

#         values = {
#             'pager': pager,
#             'pages': pages,
#             'search': search,
#             'sortby': sortby,
#             'searchbar_sortings': searchbar_sortings,
#             'search_count': pages_count,
#         }
#         return request.render("website.list_website_pages", values)


# Overrides WebsiteSale from website_sale module
class Website(WebsiteSale):

    def _get_search_options(
            self, category=None, attrib_values=None, pricelist=None, min_price=0.0, max_price=0.0, conversion_rate=1,
            **post
    ):
        res = super()._get_search_options(category, attrib_values, pricelist, min_price, max_price, conversion_rate,
                                          **post)
        res.update({'search_brand': post.get('search_brand'), 'search_year': post.get('search_year'),
                    'search_model': post.get('search_model'), 'search_piece': post.get('search_piece')})
        return res

    def _get_additional_shop_values(self, values):
        values = super()._get_additional_shop_values(values)
        values.update(
            {'search_brand': request.params.get('search_brand'), 'search_year': request.params.get('search_year'),
             'search_model': request.params.get('search_model'), 'search_piece': request.params.get('search_piece'), })
        return values
