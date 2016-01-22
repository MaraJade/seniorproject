# ====================================================================
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ====================================================================

from django import template
from django.template.defaultfilters import stringfilter

from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()

def format_email(email, autoescape):
   if autoescape:
      email = conditional_escape(email)

   at = email.find("@")
   if at > 0:
      partA = email[0:at]
      partB = email[(at+1):]
      email = "%s &#0065;&#0084; %s" % (partA, partB)
   return mark_safe( email )


# As a filter
@register.filter
@stringfilter
def emailformat(value, autoescape=None):
    return format_email(value, autoescape)
emailformat.needs_autoescape = True
