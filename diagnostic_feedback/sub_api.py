# -*- coding: utf-8 -*-
#
# Copyright (c) 2014-2015 Harvard, edX & OpenCraft
#
# This software's license gives you freedom; you can copy, convey,
# propagate, redistribute and/or modify this program under the terms of
# the GNU Affero General Public License (AGPL) as published by the Free
# Software Foundation (FSF), either version 3 of the License, or (at your
# option) any later version of the AGPL published by the FSF.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero
# General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program in a file in the toplevel directory called
# "AGPLv3".  If not, see <http://www.gnu.org/licenses/>.
#
"""
Integrations between these XBlocks and the edX Submissions API
"""

from __future__ import absolute_import

import logging

import six

log = logging.getLogger(__name__)


class SubmittingXBlockMixin(object):
    """ Simplifies use of the submissions API by an XBlock """

    @property
    def student_item_key(self):
        """ Get the student_item_dict required for the submissions API """
        location = self.location.replace(branch=None, version=None)  # Standardize the key in case it isn't already
        return dict(
            student_id=self.runtime.anonymous_student_id,
            course_id=six.text_type(location.course_key),
            item_id=six.text_type(location),
            item_type=self.scope_ids.block_type,
        )
