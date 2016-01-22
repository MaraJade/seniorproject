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

from django.http import HttpRequest, HttpResponseRedirect, Http404, \
    HttpResponseForbidden, HttpResponse

from django.shortcuts import render_to_response
from django.template import RequestContext

mimetypes = {
   "json": "application/json",
   "rdf":  "application/rdf+xml"
}

def render(request, template_name, data_dict=None, content_type=None):
    assert isinstance(request, HttpRequest)
    return render_to_response(
        template_name, data_dict or {},
        context_instance=RequestContext(request),
        mimetype=content_type
    )

def identify_type(request, allowed_types=None):
    """Identifies, based on Content Type, Accept Headers etc, the required
       response type, such as HTML or JSON"""
    if allowed_types == None or len(allowed_types) == 0:
        allowed_types = ["html", "json"]

    # Did they specify a format?
    if request.GET.has_key("format"):
        format = request.GET.get("format")
        if format in allowed_types:
            return format

    # Check the inbound Content Type, then the Accept Header
    meta_checks = ["CONTENT_TYPE", "HTTP_ACCEPT"]
    for meta in meta_checks:
        meta_value = request.META.get(meta, "")
        if meta_value in mimetypes.values():
            for type in mimetypes.keys():
                if mimetypes[type] == meta_value:
                   if type in allowed_types:
                      return type

    # Otherwise default to the first allowed type (normally html)
    return allowed_types[0]

def add_message(request, message):
    "Adds a message to be shown on next page load."
    request.user.message_set.create(message=message)
