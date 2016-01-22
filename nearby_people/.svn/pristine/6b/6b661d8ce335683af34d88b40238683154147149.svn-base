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

register = template.Library()

def format_distance(distance):
   if distance < 1000:
      return "%d m" % distance
   elif distance < 50 * 1000:
      return "%0.1f km" % (distance/1000)
   else:
      return "%d km" % (distance/1000)


# As a filter
@register.filter
@stringfilter
def distanceformat(value):
    return format_distance(float(value))

# As a tag
class DistanceNode(template.Node):
    def __init__(self, distance):
        self.distance = distance
    def render(self,context):
        return self.nodelist.render( format_distance(self.distance) )

@register.tag
def distance(parser, token):
    bits = token.split_contents()
    return DistanceNode(bits[1])
