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

from django import forms

class PlaceForm(forms.Form):
    place_name = forms.CharField()
    type = forms.TypedChoiceField(choices=(
        ('','Default (Local Mentors)'), ('lm','Local Mentors'),
        ('sp','Speakers'),
      ), 
      required=False,
      widget=forms.HiddenInput,
      label="Type of Person",
    )
    rows = forms.IntegerField(
      required = False, 
      initial = 10, 
      widget=forms.HiddenInput,)
    
    def set_type(self, type):
      for opt,name in self.fields["type"].choices:
         if opt == type:
            self.initial["type"] = opt
    
    def enableTypeField(self):
      self.fields["type"].widget = forms.Select(
           choices=self.fields["type"].choices
      )

class LocationForm(forms.Form):
    latitude = forms.FloatField()
    longitude = forms.FloatField()

