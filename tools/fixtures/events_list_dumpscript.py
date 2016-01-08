#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file has been automatically generated.
# Instead of changing it, create a file called import_helper.py
# and put there a class called ImportHelper(object) in it.
#
# This class will be specially casted so that instead of extending object,
# it will actually extend the class BasicImportHelper()
#
# That means you just have to overload the methods you want to
# change, leaving the other ones inteact.
#
# Something that you might want to do is use transactions, for example.
#
# Also, don't forget to add the necessary Django imports.
#
# This file was generated with the following command:
# manage.py dumpscript events_list
#
# to restore it, run
# manage.py runscript module_name.this_script_name
#
# example: if manage.py is at ./manage.py
# and the script is at ./some_folder/some_script.py
# you must make sure ./some_folder/__init__.py exists
# and run  ./manage.py runscript some_folder.some_script

from django.db import transaction

class BasicImportHelper(object):

    def pre_import(self):
        pass

    # You probably want to uncomment on of these two lines
    # @transaction.atomic  # Django 1.6
    # @transaction.commit_on_success  # Django <1.6
    def run_import(self, import_data):
        import_data()

    def post_import(self):
        pass

    def locate_similar(self, current_object, search_data):
        # You will probably want to call this method from save_or_locate()
        # Example:
        #   new_obj = self.locate_similar(the_obj, {"national_id": the_obj.national_id } )

        the_obj = current_object.__class__.objects.get(**search_data)
        return the_obj

    def locate_object(self, original_class, original_pk_name, the_class, pk_name, pk_value, obj_content):
        # You may change this function to do specific lookup for specific objects
        #
        # original_class class of the django orm's object that needs to be located
        # original_pk_name the primary key of original_class
        # the_class      parent class of original_class which contains obj_content
        # pk_name        the primary key of original_class
        # pk_value       value of the primary_key
        # obj_content    content of the object which was not exported.
        #
        # You should use obj_content to locate the object on the target db
        #
        # An example where original_class and the_class are different is
        # when original_class is Farmer and the_class is Person. The table
        # may refer to a Farmer but you will actually need to locate Person
        # in order to instantiate that Farmer
        #
        # Example:
        #   if the_class == SurveyResultFormat or the_class == SurveyType or the_class == SurveyState:
        #       pk_name="name"
        #       pk_value=obj_content[pk_name]
        #   if the_class == StaffGroup:
        #       pk_value=8

        search_data = { pk_name: pk_value }
        the_obj = the_class.objects.get(**search_data)
        #print(the_obj)
        return the_obj


    def save_or_locate(self, the_obj):
        # Change this if you want to locate the object in the database
        try:
            the_obj.save()
        except:
            print("---------------")
            print("Error saving the following object:")
            print(the_obj.__class__)
            print(" ")
            print(the_obj.__dict__)
            print(" ")
            print(the_obj)
            print(" ")
            print("---------------")

            raise
        return the_obj


importer = None
try:
    import import_helper
    # We need this so ImportHelper can extend BasicImportHelper, although import_helper.py
    # has no knowlodge of this class
    importer = type("DynamicImportHelper", (import_helper.ImportHelper, BasicImportHelper ) , {} )()
except ImportError as e:
    # From Python 3.3 we can check e.name - string match is for backward compatibility.
    if 'import_helper' in str(e):
        importer = BasicImportHelper()
    else:
        raise

import datetime
from decimal import Decimal
from django.contrib.contenttypes.models import ContentType

try:
    import dateutil.parser
except ImportError:
    print("Please install python-dateutil")
    sys.exit(os.EX_USAGE)

def run():
    importer.pre_import()
    importer.run_import(import_data)
    importer.post_import()

def import_data():
    # Initial Imports

    # Processing model: Topic

    from events_list.models import Topic


    # Processing model: Group

    from events_list.models import Group

    events_list_group_1 = Group()
    events_list_group_1.name = u'Istanbul Spark Meetup'
    events_list_group_1.city = u'Istanbul'
    events_list_group_1.state = u''
    events_list_group_1.country = u'TR'
    events_list_group_1.meetupID = 18697603L
    events_list_group_1.is_applicable = True
    events_list_group_1 = importer.save_or_locate(events_list_group_1)

    events_list_group_2 = Group()
    events_list_group_2.name = u'Bangalore-Whitefield PhoneGap Meetup'
    events_list_group_2.city = u'Bangalore'
    events_list_group_2.state = u''
    events_list_group_2.country = u'IN'
    events_list_group_2.meetupID = 18551744L
    events_list_group_2.is_applicable = True
    events_list_group_2 = importer.save_or_locate(events_list_group_2)

    events_list_group_3 = Group()
    events_list_group_3.name = u'Seattle Solr/Lucene Meetup'
    events_list_group_3.city = u'Seattle'
    events_list_group_3.state = u'WA'
    events_list_group_3.country = u'US'
    events_list_group_3.meetupID = 17009672L
    events_list_group_3.is_applicable = True
    events_list_group_3 = importer.save_or_locate(events_list_group_3)

    events_list_group_4 = Group()
    events_list_group_4.name = u'Sydney Cassandra Users'
    events_list_group_4.city = u'Sydney'
    events_list_group_4.state = u''
    events_list_group_4.country = u'AU'
    events_list_group_4.meetupID = 7568672L
    events_list_group_4.is_applicable = True
    events_list_group_4 = importer.save_or_locate(events_list_group_4)

    events_list_group_5 = Group()
    events_list_group_5.name = u'The Boston Area Cloud Foundry Meetup'
    events_list_group_5.city = u'Waltham'
    events_list_group_5.state = u'MA'
    events_list_group_5.country = u'US'
    events_list_group_5.meetupID = 10702282L
    events_list_group_5.is_applicable = True
    events_list_group_5 = importer.save_or_locate(events_list_group_5)

    events_list_group_6 = Group()
    events_list_group_6.name = u'Houston Hadoop Meetup Group'
    events_list_group_6.city = u'Houston'
    events_list_group_6.state = u'TX'
    events_list_group_6.country = u'US'
    events_list_group_6.meetupID = 1795155L
    events_list_group_6.is_applicable = True
    events_list_group_6 = importer.save_or_locate(events_list_group_6)

    events_list_group_7 = Group()
    events_list_group_7.name = u'Austin PaaS, Cloud and Bluemix meetup'
    events_list_group_7.city = u'Austin'
    events_list_group_7.state = u'TX'
    events_list_group_7.country = u'US'
    events_list_group_7.meetupID = 15599312L
    events_list_group_7.is_applicable = True
    events_list_group_7 = importer.save_or_locate(events_list_group_7)

    events_list_group_8 = Group()
    events_list_group_8.name = u"US.CA.OrangeCounty's JavaScript Community Group"
    events_list_group_8.city = u'Laguna Hills'
    events_list_group_8.state = u'CA'
    events_list_group_8.country = u'US'
    events_list_group_8.meetupID = 16925932L
    events_list_group_8.is_applicable = True
    events_list_group_8 = importer.save_or_locate(events_list_group_8)

    events_list_group_9 = Group()
    events_list_group_9.name = u'Data Science Phoenix'
    events_list_group_9.city = u'Phoenix'
    events_list_group_9.state = u'AZ'
    events_list_group_9.country = u'US'
    events_list_group_9.meetupID = 4844022L
    events_list_group_9.is_applicable = True
    events_list_group_9 = importer.save_or_locate(events_list_group_9)

    events_list_group_10 = Group()
    events_list_group_10.name = u'corkdev.io'
    events_list_group_10.city = u'Cork'
    events_list_group_10.state = u''
    events_list_group_10.country = u'IE'
    events_list_group_10.meetupID = 12225002L
    events_list_group_10.is_applicable = True
    events_list_group_10 = importer.save_or_locate(events_list_group_10)

    events_list_group_11 = Group()
    events_list_group_11.name = u'Advanced Apache Spark Meetup'
    events_list_group_11.city = u'San Francisco'
    events_list_group_11.state = u'CA'
    events_list_group_11.country = u'US'
    events_list_group_11.meetupID = 18712511L
    events_list_group_11.is_applicable = True
    events_list_group_11 = importer.save_or_locate(events_list_group_11)

    events_list_group_12 = Group()
    events_list_group_12.name = u'[ Contain ]'
    events_list_group_12.city = u'London'
    events_list_group_12.state = u'17'
    events_list_group_12.country = u'GB'
    events_list_group_12.meetupID = 18445714L
    events_list_group_12.is_applicable = True
    events_list_group_12 = importer.save_or_locate(events_list_group_12)

    events_list_group_13 = Group()
    events_list_group_13.name = u'East Midlands Front-End'
    events_list_group_13.city = u'Nottingham'
    events_list_group_13.state = u'J9'
    events_list_group_13.country = u'GB'
    events_list_group_13.meetupID = 18718170L
    events_list_group_13.is_applicable = True
    events_list_group_13 = importer.save_or_locate(events_list_group_13)

    events_list_group_14 = Group()
    events_list_group_14.name = u'H2O and Data Science!'
    events_list_group_14.city = u'Mountain View'
    events_list_group_14.state = u'CA'
    events_list_group_14.country = u'US'
    events_list_group_14.meetupID = 4978932L
    events_list_group_14.is_applicable = True
    events_list_group_14 = importer.save_or_locate(events_list_group_14)

    events_list_group_15 = Group()
    events_list_group_15.name = u'The Atlanta Scala Meetup Group'
    events_list_group_15.city = u'Atlanta'
    events_list_group_15.state = u'GA'
    events_list_group_15.country = u'US'
    events_list_group_15.meetupID = 1475328L
    events_list_group_15.is_applicable = True
    events_list_group_15 = importer.save_or_locate(events_list_group_15)

    events_list_group_16 = Group()
    events_list_group_16.name = u'ScalaSyd'
    events_list_group_16.city = u'Sydney'
    events_list_group_16.state = u''
    events_list_group_16.country = u'AU'
    events_list_group_16.meetupID = 2313331L
    events_list_group_16.is_applicable = True
    events_list_group_16 = importer.save_or_locate(events_list_group_16)

    events_list_group_17 = Group()
    events_list_group_17.name = u'Savannah Open Source'
    events_list_group_17.city = u'Savannah'
    events_list_group_17.state = u'GA'
    events_list_group_17.country = u'US'
    events_list_group_17.meetupID = 13677082L
    events_list_group_17.is_applicable = True
    events_list_group_17 = importer.save_or_locate(events_list_group_17)

    events_list_group_18 = Group()
    events_list_group_18.name = u'Big Data Warehousing'
    events_list_group_18.city = u'New York'
    events_list_group_18.state = u'NY'
    events_list_group_18.country = u'US'
    events_list_group_18.meetupID = 5775892L
    events_list_group_18.is_applicable = True
    events_list_group_18 = importer.save_or_locate(events_list_group_18)

    events_list_group_19 = Group()
    events_list_group_19.name = u'Cosmopolitan Connections Inc. dba My Vegas Friends'
    events_list_group_19.city = u'Las Vegas'
    events_list_group_19.state = u'NV'
    events_list_group_19.country = u'US'
    events_list_group_19.meetupID = 1461697L
    events_list_group_19.is_applicable = True
    events_list_group_19 = importer.save_or_locate(events_list_group_19)

    events_list_group_20 = Group()
    events_list_group_20.name = u'OC-U-PY'
    events_list_group_20.city = u'Irvine'
    events_list_group_20.state = u'CA'
    events_list_group_20.country = u'US'
    events_list_group_20.meetupID = 13069882L
    events_list_group_20.is_applicable = True
    events_list_group_20 = importer.save_or_locate(events_list_group_20)

    events_list_group_21 = Group()
    events_list_group_21.name = u'Elastic Silicon Valley User group'
    events_list_group_21.city = u'Mountain View'
    events_list_group_21.state = u'CA'
    events_list_group_21.country = u'US'
    events_list_group_21.meetupID = 10000042L
    events_list_group_21.is_applicable = True
    events_list_group_21 = importer.save_or_locate(events_list_group_21)

    events_list_group_22 = Group()
    events_list_group_22.name = u'Pepperdata - NYC'
    events_list_group_22.city = u'New York'
    events_list_group_22.state = u'NY'
    events_list_group_22.country = u'US'
    events_list_group_22.meetupID = 18474414L
    events_list_group_22.is_applicable = True
    events_list_group_22 = importer.save_or_locate(events_list_group_22)

    events_list_group_23 = Group()
    events_list_group_23.name = u'Everyday Spacer Phoenix'
    events_list_group_23.city = u'Phoenix'
    events_list_group_23.state = u'AZ'
    events_list_group_23.country = u'US'
    events_list_group_23.meetupID = 18526838L
    events_list_group_23.is_applicable = True
    events_list_group_23 = importer.save_or_locate(events_list_group_23)

    events_list_group_24 = Group()
    events_list_group_24.name = u'Dayton Data Visualization Meetup'
    events_list_group_24.city = u'Dayton'
    events_list_group_24.state = u'OH'
    events_list_group_24.country = u'US'
    events_list_group_24.meetupID = 16874292L
    events_list_group_24.is_applicable = True
    events_list_group_24 = importer.save_or_locate(events_list_group_24)

    events_list_group_25 = Group()
    events_list_group_25.name = u'Code.Brew'
    events_list_group_25.city = u'Sterling'
    events_list_group_25.state = u'VA'
    events_list_group_25.country = u'US'
    events_list_group_25.meetupID = 14979942L
    events_list_group_25.is_applicable = True
    events_list_group_25 = importer.save_or_locate(events_list_group_25)

    events_list_group_26 = Group()
    events_list_group_26.name = u'Baltimore Washington Java Meetup Group'
    events_list_group_26.city = u'Hanover'
    events_list_group_26.state = u'MD'
    events_list_group_26.country = u'US'
    events_list_group_26.meetupID = 1434679L
    events_list_group_26.is_applicable = True
    events_list_group_26 = importer.save_or_locate(events_list_group_26)

    events_list_group_27 = Group()
    events_list_group_27.name = u'Seattle JS'
    events_list_group_27.city = u'Seattle'
    events_list_group_27.state = u'WA'
    events_list_group_27.country = u'US'
    events_list_group_27.meetupID = 1619342L
    events_list_group_27.is_applicable = True
    events_list_group_27 = importer.save_or_locate(events_list_group_27)

    events_list_group_28 = Group()
    events_list_group_28.name = u'RMOUG Big Data SIG Meetup'
    events_list_group_28.city = u'Westminster'
    events_list_group_28.state = u'CO'
    events_list_group_28.country = u'US'
    events_list_group_28.meetupID = 18486184L
    events_list_group_28.is_applicable = True
    events_list_group_28 = importer.save_or_locate(events_list_group_28)

    events_list_group_29 = Group()
    events_list_group_29.name = u'ATL Tech Tastings Meetup'
    events_list_group_29.city = u'Atlanta'
    events_list_group_29.state = u'GA'
    events_list_group_29.country = u'US'
    events_list_group_29.meetupID = 18712503L
    events_list_group_29.is_applicable = True
    events_list_group_29 = importer.save_or_locate(events_list_group_29)

    events_list_group_30 = Group()
    events_list_group_30.name = u'Utah Cassandra Meetup'
    events_list_group_30.city = u'American Fork'
    events_list_group_30.state = u'UT'
    events_list_group_30.country = u'US'
    events_list_group_30.meetupID = 18752599L
    events_list_group_30.is_applicable = True
    events_list_group_30 = importer.save_or_locate(events_list_group_30)

    events_list_group_31 = Group()
    events_list_group_31.name = u'LJC - London Java Community'
    events_list_group_31.city = u'London'
    events_list_group_31.state = u'17'
    events_list_group_31.country = u'GB'
    events_list_group_31.meetupID = 841735L
    events_list_group_31.is_applicable = True
    events_list_group_31 = importer.save_or_locate(events_list_group_31)

    events_list_group_32 = Group()
    events_list_group_32.name = u'LA Mobile Developers Group (Cordova, PhoneGap, AIR)'
    events_list_group_32.city = u'Los Angeles'
    events_list_group_32.state = u'CA'
    events_list_group_32.country = u'US'
    events_list_group_32.meetupID = 1807374L
    events_list_group_32.is_applicable = True
    events_list_group_32 = importer.save_or_locate(events_list_group_32)

    events_list_group_33 = Group()
    events_list_group_33.name = u'NJ Data Science - Apache Spark'
    events_list_group_33.city = u'Princeton'
    events_list_group_33.state = u'NJ'
    events_list_group_33.country = u'US'
    events_list_group_33.meetupID = 13876422L
    events_list_group_33.is_applicable = True
    events_list_group_33 = importer.save_or_locate(events_list_group_33)

    events_list_group_34 = Group()
    events_list_group_34.name = u'Big Data & NoSQL Meetup Hamburg'
    events_list_group_34.city = u'Hamburg'
    events_list_group_34.state = u''
    events_list_group_34.country = u'DE'
    events_list_group_34.meetupID = 4798602L
    events_list_group_34.is_applicable = True
    events_list_group_34 = importer.save_or_locate(events_list_group_34)

    events_list_group_35 = Group()
    events_list_group_35.name = u'JavaScript & jQuery LA Meetup'
    events_list_group_35.city = u'Los Angeles'
    events_list_group_35.state = u'CA'
    events_list_group_35.country = u'US'
    events_list_group_35.meetupID = 2587952L
    events_list_group_35.is_applicable = True
    events_list_group_35 = importer.save_or_locate(events_list_group_35)

    events_list_group_36 = Group()
    events_list_group_36.name = u'IoT para Miner\xeda, Agro y Smartcities'
    events_list_group_36.city = u'Santiago'
    events_list_group_36.state = u''
    events_list_group_36.country = u'CL'
    events_list_group_36.meetupID = 18493711L
    events_list_group_36.is_applicable = True
    events_list_group_36 = importer.save_or_locate(events_list_group_36)

    events_list_group_37 = Group()
    events_list_group_37.name = u'Get Out!  Adventures For Gay Single Men'
    events_list_group_37.city = u'Phoenix'
    events_list_group_37.state = u'AZ'
    events_list_group_37.country = u'US'
    events_list_group_37.meetupID = 16874992L
    events_list_group_37.is_applicable = True
    events_list_group_37 = importer.save_or_locate(events_list_group_37)

    events_list_group_38 = Group()
    events_list_group_38.name = u'Strangers 2 Friends'
    events_list_group_38.city = u'Portishead'
    events_list_group_38.state = u'M3'
    events_list_group_38.country = u'GB'
    events_list_group_38.meetupID = 17067972L
    events_list_group_38.is_applicable = True
    events_list_group_38 = importer.save_or_locate(events_list_group_38)

    events_list_group_39 = Group()
    events_list_group_39.name = u'DataStax Cassandra South Bay Users'
    events_list_group_39.city = u'Cupertino'
    events_list_group_39.state = u'CA'
    events_list_group_39.country = u'US'
    events_list_group_39.meetupID = 7037352L
    events_list_group_39.is_applicable = True
    events_list_group_39 = importer.save_or_locate(events_list_group_39)

    events_list_group_40 = Group()
    events_list_group_40.name = u'Data Science Melbourne'
    events_list_group_40.city = u'Melbourne'
    events_list_group_40.state = u''
    events_list_group_40.country = u'AU'
    events_list_group_40.meetupID = 13634822L
    events_list_group_40.is_applicable = True
    events_list_group_40 = importer.save_or_locate(events_list_group_40)

    events_list_group_41 = Group()
    events_list_group_41.name = u'Melbourne Chef'
    events_list_group_41.city = u'Melbourne'
    events_list_group_41.state = u''
    events_list_group_41.country = u'AU'
    events_list_group_41.meetupID = 15910382L
    events_list_group_41.is_applicable = True
    events_list_group_41 = importer.save_or_locate(events_list_group_41)

    events_list_group_42 = Group()
    events_list_group_42.name = u'Skyway Software Symposium'
    events_list_group_42.city = u'Minneapolis'
    events_list_group_42.state = u'MN'
    events_list_group_42.country = u'US'
    events_list_group_42.meetupID = 14862952L
    events_list_group_42.is_applicable = True
    events_list_group_42 = importer.save_or_locate(events_list_group_42)

    events_list_group_43 = Group()
    events_list_group_43.name = u'Jozi Linux User Group (JLUG)'
    events_list_group_43.city = u'Johannesburg'
    events_list_group_43.state = u''
    events_list_group_43.country = u'ZA'
    events_list_group_43.meetupID = 2154521L
    events_list_group_43.is_applicable = True
    events_list_group_43 = importer.save_or_locate(events_list_group_43)

    events_list_group_44 = Group()
    events_list_group_44.name = u'Integration Stockholm'
    events_list_group_44.city = u'Stockholm'
    events_list_group_44.state = u''
    events_list_group_44.country = u'SE'
    events_list_group_44.meetupID = 18538138L
    events_list_group_44.is_applicable = True
    events_list_group_44 = importer.save_or_locate(events_list_group_44)

    events_list_group_45 = Group()
    events_list_group_45.name = u'Downtown SF Apache Lucene/Solr Meetup'
    events_list_group_45.city = u'San Francisco'
    events_list_group_45.state = u'CA'
    events_list_group_45.country = u'US'
    events_list_group_45.meetupID = 15059142L
    events_list_group_45.is_applicable = True
    events_list_group_45 = importer.save_or_locate(events_list_group_45)

    events_list_group_46 = Group()
    events_list_group_46.name = u'Washington DC Area Apache Spark Interactive'
    events_list_group_46.city = u'Washington'
    events_list_group_46.state = u'DC'
    events_list_group_46.country = u'US'
    events_list_group_46.meetupID = 14077672L
    events_list_group_46.is_applicable = True
    events_list_group_46 = importer.save_or_locate(events_list_group_46)

    events_list_group_47 = Group()
    events_list_group_47.name = u'/dev/070'
    events_list_group_47.city = u'Den Haag'
    events_list_group_47.state = u''
    events_list_group_47.country = u'NL'
    events_list_group_47.meetupID = 14194182L
    events_list_group_47.is_applicable = True
    events_list_group_47 = importer.save_or_locate(events_list_group_47)

    events_list_group_48 = Group()
    events_list_group_48.name = u'Meetup Tempe  |  Character Areas'
    events_list_group_48.city = u'Tempe'
    events_list_group_48.state = u'AZ'
    events_list_group_48.country = u'US'
    events_list_group_48.meetupID = 18584447L
    events_list_group_48.is_applicable = True
    events_list_group_48 = importer.save_or_locate(events_list_group_48)

    events_list_group_49 = Group()
    events_list_group_49.name = u'The Indianapolis PHP Meetup Group'
    events_list_group_49.city = u'Indianapolis'
    events_list_group_49.state = u'IN'
    events_list_group_49.country = u'US'
    events_list_group_49.meetupID = 577068L
    events_list_group_49.is_applicable = True
    events_list_group_49 = importer.save_or_locate(events_list_group_49)

    events_list_group_50 = Group()
    events_list_group_50.name = u'St. Louis Hadoop Users Group'
    events_list_group_50.city = u'Saint Louis'
    events_list_group_50.state = u'MO'
    events_list_group_50.country = u'US'
    events_list_group_50.meetupID = 1706946L
    events_list_group_50.is_applicable = True
    events_list_group_50 = importer.save_or_locate(events_list_group_50)

    events_list_group_51 = Group()
    events_list_group_51.name = u'Denver Cordova/Ionic Meetup'
    events_list_group_51.city = u'Denver'
    events_list_group_51.state = u'CO'
    events_list_group_51.country = u'US'
    events_list_group_51.meetupID = 18808450L
    events_list_group_51.is_applicable = True
    events_list_group_51 = importer.save_or_locate(events_list_group_51)

    events_list_group_52 = Group()
    events_list_group_52.name = u'Ionic-AZ'
    events_list_group_52.city = u'Scottsdale'
    events_list_group_52.state = u'AZ'
    events_list_group_52.country = u'US'
    events_list_group_52.meetupID = 18748757L
    events_list_group_52.is_applicable = True
    events_list_group_52 = importer.save_or_locate(events_list_group_52)

    events_list_group_53 = Group()
    events_list_group_53.name = u'Business Leads Group'
    events_list_group_53.city = u'Las Vegas'
    events_list_group_53.state = u'NV'
    events_list_group_53.country = u'US'
    events_list_group_53.meetupID = 4072452L
    events_list_group_53.is_applicable = True
    events_list_group_53 = importer.save_or_locate(events_list_group_53)

    events_list_group_54 = Group()
    events_list_group_54.name = u'Spark Global Online Meetup'
    events_list_group_54.city = u'San Francisco'
    events_list_group_54.state = u'CA'
    events_list_group_54.country = u'US'
    events_list_group_54.meetupID = 18654127L
    events_list_group_54.is_applicable = True
    events_list_group_54 = importer.save_or_locate(events_list_group_54)

    events_list_group_55 = Group()
    events_list_group_55.name = u'Tech Confluence'
    events_list_group_55.city = u'Denver'
    events_list_group_55.state = u'CO'
    events_list_group_55.country = u'US'
    events_list_group_55.meetupID = 9402002L
    events_list_group_55.is_applicable = True
    events_list_group_55 = importer.save_or_locate(events_list_group_55)

    events_list_group_56 = Group()
    events_list_group_56.name = u'Red Hat User Group Oslo'
    events_list_group_56.city = u'Oslo'
    events_list_group_56.state = u''
    events_list_group_56.country = u'NO'
    events_list_group_56.meetupID = 8910652L
    events_list_group_56.is_applicable = True
    events_list_group_56 = importer.save_or_locate(events_list_group_56)

    events_list_group_57 = Group()
    events_list_group_57.name = u'Mobile Meetup Oslo'
    events_list_group_57.city = u'Oslo'
    events_list_group_57.state = u''
    events_list_group_57.country = u'NO'
    events_list_group_57.meetupID = 7282482L
    events_list_group_57.is_applicable = True
    events_list_group_57 = importer.save_or_locate(events_list_group_57)

    events_list_group_58 = Group()
    events_list_group_58.name = u'OC Big Data Meetup'
    events_list_group_58.city = u'Irvine'
    events_list_group_58.state = u'CA'
    events_list_group_58.country = u'US'
    events_list_group_58.meetupID = 13860942L
    events_list_group_58.is_applicable = True
    events_list_group_58 = importer.save_or_locate(events_list_group_58)

    events_list_group_59 = Group()
    events_list_group_59.name = u'Big Data Application Meetup'
    events_list_group_59.city = u'Palo Alto'
    events_list_group_59.state = u'CA'
    events_list_group_59.country = u'US'
    events_list_group_59.meetupID = 18576339L
    events_list_group_59.is_applicable = True
    events_list_group_59 = importer.save_or_locate(events_list_group_59)

    events_list_group_60 = Group()
    events_list_group_60.name = u'The Colorado Springs Open Source Software Meetup Group'
    events_list_group_60.city = u'Colorado Springs'
    events_list_group_60.state = u'CO'
    events_list_group_60.country = u'US'
    events_list_group_60.meetupID = 945214L
    events_list_group_60.is_applicable = True
    events_list_group_60 = importer.save_or_locate(events_list_group_60)

    events_list_group_61 = Group()
    events_list_group_61.name = u'SF Big Analytics'
    events_list_group_61.city = u'San Francisco'
    events_list_group_61.state = u'CA'
    events_list_group_61.country = u'US'
    events_list_group_61.meetupID = 18354966L
    events_list_group_61.is_applicable = True
    events_list_group_61 = importer.save_or_locate(events_list_group_61)

    events_list_group_62 = Group()
    events_list_group_62.name = u'Cincinnati Apache Spark Meetup'
    events_list_group_62.city = u'West Chester'
    events_list_group_62.state = u'OH'
    events_list_group_62.country = u'US'
    events_list_group_62.meetupID = 18367457L
    events_list_group_62.is_applicable = True
    events_list_group_62 = importer.save_or_locate(events_list_group_62)

    events_list_group_63 = Group()
    events_list_group_63.name = u'Learn Data Science'
    events_list_group_63.city = u'Vancouver'
    events_list_group_63.state = u'BC'
    events_list_group_63.country = u'CA'
    events_list_group_63.meetupID = 18532714L
    events_list_group_63.is_applicable = True
    events_list_group_63 = importer.save_or_locate(events_list_group_63)

    events_list_group_64 = Group()
    events_list_group_64.name = u'Apex Meetup, Bay Area Chapter'
    events_list_group_64.city = u'Santa Clara'
    events_list_group_64.state = u'CA'
    events_list_group_64.country = u'US'
    events_list_group_64.meetupID = 18649828L
    events_list_group_64.is_applicable = True
    events_list_group_64 = importer.save_or_locate(events_list_group_64)

    events_list_group_65 = Group()
    events_list_group_65.name = u'Hacker Lab'
    events_list_group_65.city = u'Sacramento'
    events_list_group_65.state = u'CA'
    events_list_group_65.country = u'US'
    events_list_group_65.meetupID = 3361722L
    events_list_group_65.is_applicable = True
    events_list_group_65 = importer.save_or_locate(events_list_group_65)

    events_list_group_66 = Group()
    events_list_group_66.name = u'Atlanta Hadoop Users Group'
    events_list_group_66.city = u'Atlanta'
    events_list_group_66.state = u'GA'
    events_list_group_66.country = u'US'
    events_list_group_66.meetupID = 1444478L
    events_list_group_66.is_applicable = True
    events_list_group_66 = importer.save_or_locate(events_list_group_66)

    events_list_group_67 = Group()
    events_list_group_67.name = u'Montevideo BigData & DataScience Meetup'
    events_list_group_67.city = u'Montevideo'
    events_list_group_67.state = u''
    events_list_group_67.country = u'UY'
    events_list_group_67.meetupID = 18481501L
    events_list_group_67.is_applicable = True
    events_list_group_67 = importer.save_or_locate(events_list_group_67)

    events_list_group_68 = Group()
    events_list_group_68.name = u'Triangle JavaScript'
    events_list_group_68.city = u'Durham'
    events_list_group_68.state = u'NC'
    events_list_group_68.country = u'US'
    events_list_group_68.meetupID = 1546066L
    events_list_group_68.is_applicable = True
    events_list_group_68 = importer.save_or_locate(events_list_group_68)

    events_list_group_69 = Group()
    events_list_group_69.name = u'Elastic Los Angeles User Group'
    events_list_group_69.city = u'Santa Monica'
    events_list_group_69.state = u'CA'
    events_list_group_69.country = u'US'
    events_list_group_69.meetupID = 11432172L
    events_list_group_69.is_applicable = True
    events_list_group_69 = importer.save_or_locate(events_list_group_69)

    events_list_group_70 = Group()
    events_list_group_70.name = u'Oz Big Data - Melbourne'
    events_list_group_70.city = u'Melbourne'
    events_list_group_70.state = u''
    events_list_group_70.country = u'AU'
    events_list_group_70.meetupID = 5881002L
    events_list_group_70.is_applicable = True
    events_list_group_70 = importer.save_or_locate(events_list_group_70)

    events_list_group_71 = Group()
    events_list_group_71.name = u'Geekfest Seattle'
    events_list_group_71.city = u'Seattle'
    events_list_group_71.state = u'WA'
    events_list_group_71.country = u'US'
    events_list_group_71.meetupID = 14870552L
    events_list_group_71.is_applicable = True
    events_list_group_71 = importer.save_or_locate(events_list_group_71)

    events_list_group_72 = Group()
    events_list_group_72.name = u'Data Scientists Project Group'
    events_list_group_72.city = u'San Francisco'
    events_list_group_72.state = u'CA'
    events_list_group_72.country = u'US'
    events_list_group_72.meetupID = 14136242L
    events_list_group_72.is_applicable = True
    events_list_group_72 = importer.save_or_locate(events_list_group_72)

    events_list_group_73 = Group()
    events_list_group_73.name = u'Bay Area Apache Flink Meetup'
    events_list_group_73.city = u'Mountain View'
    events_list_group_73.state = u'CA'
    events_list_group_73.country = u'US'
    events_list_group_73.meetupID = 18617234L
    events_list_group_73.is_applicable = True
    events_list_group_73 = importer.save_or_locate(events_list_group_73)

    events_list_group_74 = Group()
    events_list_group_74.name = u"Phoenix Laughter Club's"
    events_list_group_74.city = u'Phoenix'
    events_list_group_74.state = u'AZ'
    events_list_group_74.country = u'US'
    events_list_group_74.meetupID = 3020182L
    events_list_group_74.is_applicable = True
    events_list_group_74 = importer.save_or_locate(events_list_group_74)

    events_list_group_75 = Group()
    events_list_group_75.name = u'IGTCloud'
    events_list_group_75.city = u'Tel Aviv-Yafo'
    events_list_group_75.state = u''
    events_list_group_75.country = u'IL'
    events_list_group_75.meetupID = 1724101L
    events_list_group_75.is_applicable = True
    events_list_group_75 = importer.save_or_locate(events_list_group_75)

    events_list_group_76 = Group()
    events_list_group_76.name = u'Stockholm Sporty People'
    events_list_group_76.city = u'Stockholm'
    events_list_group_76.state = u''
    events_list_group_76.country = u'SE'
    events_list_group_76.meetupID = 3478512L
    events_list_group_76.is_applicable = False
    events_list_group_76 = importer.save_or_locate(events_list_group_76)

    events_list_group_77 = Group()
    events_list_group_77.name = u'Las Cruces Motorcycle Riders'
    events_list_group_77.city = u'Las Cruces'
    events_list_group_77.state = u'NM'
    events_list_group_77.country = u'US'
    events_list_group_77.meetupID = 2166511L
    events_list_group_77.is_applicable = False
    events_list_group_77 = importer.save_or_locate(events_list_group_77)

    events_list_group_78 = Group()
    events_list_group_78.name = u'Nevada Scooter Brigade'
    events_list_group_78.city = u'North Las Vegas'
    events_list_group_78.state = u'NV'
    events_list_group_78.country = u'US'
    events_list_group_78.meetupID = 1382333L
    events_list_group_78.is_applicable = False
    events_list_group_78 = importer.save_or_locate(events_list_group_78)

    events_list_group_79 = Group()
    events_list_group_79.name = u'2-NetworkTogether-AJ GoldCanyon'
    events_list_group_79.city = u'Apache Junction'
    events_list_group_79.state = u'AZ'
    events_list_group_79.country = u'US'
    events_list_group_79.meetupID = 3201402L
    events_list_group_79.is_applicable = False
    events_list_group_79 = importer.save_or_locate(events_list_group_79)

    events_list_group_80 = Group()
    events_list_group_80.name = u'East Valley Desert Gardening'
    events_list_group_80.city = u'Apache Junction'
    events_list_group_80.state = u'AZ'
    events_list_group_80.country = u'US'
    events_list_group_80.meetupID = 14617802L
    events_list_group_80.is_applicable = False
    events_list_group_80 = importer.save_or_locate(events_list_group_80)

    events_list_group_81 = Group()
    events_list_group_81.name = u'Apache Junction Channeled Messages'
    events_list_group_81.city = u'Mesa'
    events_list_group_81.state = u'AZ'
    events_list_group_81.country = u'US'
    events_list_group_81.meetupID = 18733464L
    events_list_group_81.is_applicable = False
    events_list_group_81 = importer.save_or_locate(events_list_group_81)

    events_list_group_82 = Group()
    events_list_group_82.name = u'Senior Healthcare Professionals'
    events_list_group_82.city = u'Phoenix'
    events_list_group_82.state = u'AZ'
    events_list_group_82.country = u'US'
    events_list_group_82.meetupID = 1696507L
    events_list_group_82.is_applicable = False
    events_list_group_82 = importer.save_or_locate(events_list_group_82)

    events_list_group_83 = Group()
    events_list_group_83.name = u'Hiking Hikers Hiking Group'
    events_list_group_83.city = u'Phoenix'
    events_list_group_83.state = u'AZ'
    events_list_group_83.country = u'US'
    events_list_group_83.meetupID = 359190L
    events_list_group_83.is_applicable = False
    events_list_group_83 = importer.save_or_locate(events_list_group_83)

    events_list_group_84 = Group()
    events_list_group_84.name = u'The Phoenix Atheists Meetup Group'
    events_list_group_84.city = u'Phoenix'
    events_list_group_84.state = u'AZ'
    events_list_group_84.country = u'US'
    events_list_group_84.meetupID = 12920L
    events_list_group_84.is_applicable = False
    events_list_group_84 = importer.save_or_locate(events_list_group_84)

    events_list_group_85 = Group()
    events_list_group_85.name = u'SFBay Apache Lucene/Solr  Meetup'
    events_list_group_85.city = u'San Mateo'
    events_list_group_85.state = u'CA'
    events_list_group_85.country = u'US'
    events_list_group_85.meetupID = 1460078L
    events_list_group_85.is_applicable = True
    events_list_group_85 = importer.save_or_locate(events_list_group_85)

    events_list_group_86 = Group()
    events_list_group_86.name = u'Pivotal Open Source Hub'
    events_list_group_86.city = u'San Francisco'
    events_list_group_86.state = u'CA'
    events_list_group_86.country = u'US'
    events_list_group_86.meetupID = 9723552L
    events_list_group_86.is_applicable = True
    events_list_group_86 = importer.save_or_locate(events_list_group_86)

    events_list_group_87 = Group()
    events_list_group_87.name = u'Los Angeles Apache Spark Users Group'
    events_list_group_87.city = u'Los Angeles'
    events_list_group_87.state = u'CA'
    events_list_group_87.country = u'US'
    events_list_group_87.meetupID = 16041812L
    events_list_group_87.is_applicable = True
    events_list_group_87 = importer.save_or_locate(events_list_group_87)

    events_list_group_88 = Group()
    events_list_group_88.name = u'Austin Cassandra Users'
    events_list_group_88.city = u'Austin'
    events_list_group_88.state = u'TX'
    events_list_group_88.country = u'US'
    events_list_group_88.meetupID = 8984182L
    events_list_group_88.is_applicable = True
    events_list_group_88 = importer.save_or_locate(events_list_group_88)

    events_list_group_89 = Group()
    events_list_group_89.name = u'Research Triangle Analysts'
    events_list_group_89.city = u'Durham'
    events_list_group_89.state = u'NC'
    events_list_group_89.country = u'US'
    events_list_group_89.meetupID = 8855722L
    events_list_group_89.is_applicable = True
    events_list_group_89 = importer.save_or_locate(events_list_group_89)

    events_list_group_90 = Group()
    events_list_group_90.name = u'Michigan Spark Users Group'
    events_list_group_90.city = u'Detroit'
    events_list_group_90.state = u'MI'
    events_list_group_90.country = u'US'
    events_list_group_90.meetupID = 18532292L
    events_list_group_90.is_applicable = True
    events_list_group_90 = importer.save_or_locate(events_list_group_90)

    events_list_group_91 = Group()
    events_list_group_91.name = u'South-West Elastic Community'
    events_list_group_91.city = u'Bath'
    events_list_group_91.state = u'A4'
    events_list_group_91.country = u'GB'
    events_list_group_91.meetupID = 15140232L
    events_list_group_91.is_applicable = True
    events_list_group_91 = importer.save_or_locate(events_list_group_91)

    events_list_group_92 = Group()
    events_list_group_92.name = u'Toronto Scala & Typesafe User Group'
    events_list_group_92.city = u'Toronto'
    events_list_group_92.state = u'ON'
    events_list_group_92.country = u'CA'
    events_list_group_92.meetupID = 8500592L
    events_list_group_92.is_applicable = True
    events_list_group_92 = importer.save_or_locate(events_list_group_92)

    events_list_group_93 = Group()
    events_list_group_93.name = u'Promoting Open Source/Libre to the Canadian government'
    events_list_group_93.city = u'Ottawa'
    events_list_group_93.state = u'ON'
    events_list_group_93.country = u'CA'
    events_list_group_93.meetupID = 9959852L
    events_list_group_93.is_applicable = True
    events_list_group_93 = importer.save_or_locate(events_list_group_93)

    events_list_group_94 = Group()
    events_list_group_94.name = u'Primitive Skills & Wilderness Living (San Antonio Region)'
    events_list_group_94.city = u'San Antonio'
    events_list_group_94.state = u'TX'
    events_list_group_94.country = u'US'
    events_list_group_94.meetupID = 965563L
    events_list_group_94.is_applicable = True
    events_list_group_94 = importer.save_or_locate(events_list_group_94)

    events_list_group_95 = Group()
    events_list_group_95.name = u'Grupy-SP'
    events_list_group_95.city = u'S\xe3o Paulo'
    events_list_group_95.state = u''
    events_list_group_95.country = u'BR'
    events_list_group_95.meetupID = 18253440L
    events_list_group_95.is_applicable = True
    events_list_group_95 = importer.save_or_locate(events_list_group_95)

    events_list_group_96 = Group()
    events_list_group_96.name = u'London Kaggle Meetup'
    events_list_group_96.city = u'London'
    events_list_group_96.state = u'17'
    events_list_group_96.country = u'GB'
    events_list_group_96.meetupID = 18654966L
    events_list_group_96.is_applicable = True
    events_list_group_96 = importer.save_or_locate(events_list_group_96)

    events_list_group_97 = Group()
    events_list_group_97.name = u'Shanghai Big Data Streaming Meetup'
    events_list_group_97.city = u'Shanghai'
    events_list_group_97.state = u''
    events_list_group_97.country = u'CN'
    events_list_group_97.meetupID = 18743046L
    events_list_group_97.is_applicable = True
    events_list_group_97 = importer.save_or_locate(events_list_group_97)

    events_list_group_98 = Group()
    events_list_group_98.name = u'Xian Apache Spark Meetup'
    events_list_group_98.city = u'Xian'
    events_list_group_98.state = u''
    events_list_group_98.country = u'CN'
    events_list_group_98.meetupID = 18215148L
    events_list_group_98.is_applicable = True
    events_list_group_98 = importer.save_or_locate(events_list_group_98)

    events_list_group_99 = Group()
    events_list_group_99.name = u'Spark User Beijing Meetup'
    events_list_group_99.city = u'Beijing'
    events_list_group_99.state = u''
    events_list_group_99.country = u'CN'
    events_list_group_99.meetupID = 15469022L
    events_list_group_99.is_applicable = True
    events_list_group_99 = importer.save_or_locate(events_list_group_99)

    events_list_group_100 = Group()
    events_list_group_100.name = u'SE Valley Filipino American Families & Friends (SEVFAF) - AZ'
    events_list_group_100.city = u'Chandler'
    events_list_group_100.state = u'AZ'
    events_list_group_100.country = u'US'
    events_list_group_100.meetupID = 1430942L
    events_list_group_100.is_applicable = True
    events_list_group_100 = importer.save_or_locate(events_list_group_100)

    events_list_group_101 = Group()
    events_list_group_101.name = u'ambariCloud Big Data Meetup'
    events_list_group_101.city = u'Bolingbrook'
    events_list_group_101.state = u'IL'
    events_list_group_101.country = u'US'
    events_list_group_101.meetupID = 18538766L
    events_list_group_101.is_applicable = True
    events_list_group_101 = importer.save_or_locate(events_list_group_101)

    events_list_group_102 = Group()
    events_list_group_102.name = u'Sydney Big Data and Analytics'
    events_list_group_102.city = u'Sydney'
    events_list_group_102.state = u''
    events_list_group_102.country = u'AU'
    events_list_group_102.meetupID = 18324087L
    events_list_group_102.is_applicable = True
    events_list_group_102 = importer.save_or_locate(events_list_group_102)

    events_list_group_103 = Group()
    events_list_group_103.name = u'DFW Analytics : Big Data and Beyond'
    events_list_group_103.city = u'Dallas'
    events_list_group_103.state = u'TX'
    events_list_group_103.country = u'US'
    events_list_group_103.meetupID = 11490362L
    events_list_group_103.is_applicable = True
    events_list_group_103 = importer.save_or_locate(events_list_group_103)

    events_list_group_104 = Group()
    events_list_group_104.name = u'Big Data Madison'
    events_list_group_104.city = u'Madison'
    events_list_group_104.state = u'WI'
    events_list_group_104.country = u'US'
    events_list_group_104.meetupID = 3315552L
    events_list_group_104.is_applicable = True
    events_list_group_104 = importer.save_or_locate(events_list_group_104)

    events_list_group_105 = Group()
    events_list_group_105.name = u'Melbourne Apache Spark Meetup'
    events_list_group_105.city = u'Melbourne'
    events_list_group_105.state = u''
    events_list_group_105.country = u'AU'
    events_list_group_105.meetupID = 18282806L
    events_list_group_105.is_applicable = True
    events_list_group_105 = importer.save_or_locate(events_list_group_105)

    events_list_group_106 = Group()
    events_list_group_106.name = u'Houston Meteor Meetup'
    events_list_group_106.city = u'Houston'
    events_list_group_106.state = u'TX'
    events_list_group_106.country = u'US'
    events_list_group_106.meetupID = 18632193L
    events_list_group_106.is_applicable = True
    events_list_group_106 = importer.save_or_locate(events_list_group_106)

    events_list_group_107 = Group()
    events_list_group_107.name = u'Apache Lucene/Solr SG'
    events_list_group_107.city = u'Singapore'
    events_list_group_107.state = u''
    events_list_group_107.country = u'SG'
    events_list_group_107.meetupID = 18650303L
    events_list_group_107.is_applicable = True
    events_list_group_107 = importer.save_or_locate(events_list_group_107)

    events_list_group_108 = Group()
    events_list_group_108.name = u'Bay Area Spark Meetup'
    events_list_group_108.city = u'San Francisco'
    events_list_group_108.state = u'CA'
    events_list_group_108.country = u'US'
    events_list_group_108.meetupID = 3138542L
    events_list_group_108.is_applicable = True
    events_list_group_108 = importer.save_or_locate(events_list_group_108)

    events_list_group_109 = Group()
    events_list_group_109.name = u'South West Data'
    events_list_group_109.city = u'Bristol'
    events_list_group_109.state = u'B7'
    events_list_group_109.country = u'GB'
    events_list_group_109.meetupID = 2710112L
    events_list_group_109.is_applicable = True
    events_list_group_109 = importer.save_or_locate(events_list_group_109)

    events_list_group_110 = Group()
    events_list_group_110.name = u'Charlotte Hadoop Users Group'
    events_list_group_110.city = u'Charlotte'
    events_list_group_110.state = u'NC'
    events_list_group_110.country = u'US'
    events_list_group_110.meetupID = 1831741L
    events_list_group_110.is_applicable = True
    events_list_group_110 = importer.save_or_locate(events_list_group_110)

    events_list_group_111 = Group()
    events_list_group_111.name = u'Pepperdata Meetup Group'
    events_list_group_111.city = u'Sunnyvale'
    events_list_group_111.state = u'CA'
    events_list_group_111.country = u'US'
    events_list_group_111.meetupID = 14306312L
    events_list_group_111.is_applicable = True
    events_list_group_111 = importer.save_or_locate(events_list_group_111)

    events_list_group_112 = Group()
    events_list_group_112.name = u'Google Developer Group Ha Noi'
    events_list_group_112.city = u'Ha Noi'
    events_list_group_112.state = u''
    events_list_group_112.country = u'VN'
    events_list_group_112.meetupID = 18675964L
    events_list_group_112.is_applicable = True
    events_list_group_112 = importer.save_or_locate(events_list_group_112)

    events_list_group_113 = Group()
    events_list_group_113.name = u'DataStax Cassandra SF Users'
    events_list_group_113.city = u'San Francisco'
    events_list_group_113.state = u'CA'
    events_list_group_113.country = u'US'
    events_list_group_113.meetupID = 8567532L
    events_list_group_113.is_applicable = True
    events_list_group_113 = importer.save_or_locate(events_list_group_113)

    events_list_group_114 = Group()
    events_list_group_114.name = u'East Bay  Java User Group'
    events_list_group_114.city = u'Oakland'
    events_list_group_114.state = u'CA'
    events_list_group_114.country = u'US'
    events_list_group_114.meetupID = 1791369L
    events_list_group_114.is_applicable = True
    events_list_group_114 = importer.save_or_locate(events_list_group_114)

    events_list_group_115 = Group()
    events_list_group_115.name = u"The Atlanta WordPress Coder's Guild\u2122"
    events_list_group_115.city = u'Atlanta'
    events_list_group_115.state = u'GA'
    events_list_group_115.country = u'US'
    events_list_group_115.meetupID = 18241772L
    events_list_group_115.is_applicable = True
    events_list_group_115 = importer.save_or_locate(events_list_group_115)

    events_list_group_116 = Group()
    events_list_group_116.name = u'Bay Area Search'
    events_list_group_116.city = u'San Jose'
    events_list_group_116.state = u'CA'
    events_list_group_116.country = u'US'
    events_list_group_116.meetupID = 1875611L
    events_list_group_116.is_applicable = True
    events_list_group_116 = importer.save_or_locate(events_list_group_116)

    events_list_group_117 = Group()
    events_list_group_117.name = u'Apache Flink Meetup Berlin'
    events_list_group_117.city = u'Berlin'
    events_list_group_117.state = u''
    events_list_group_117.country = u'DE'
    events_list_group_117.meetupID = 17066872L
    events_list_group_117.is_applicable = True
    events_list_group_117 = importer.save_or_locate(events_list_group_117)

    events_list_group_118 = Group()
    events_list_group_118.name = u'Indy Big Data'
    events_list_group_118.city = u'Carmel'
    events_list_group_118.state = u'IN'
    events_list_group_118.country = u'US'
    events_list_group_118.meetupID = 2307701L
    events_list_group_118.is_applicable = True
    events_list_group_118 = importer.save_or_locate(events_list_group_118)

    events_list_group_119 = Group()
    events_list_group_119.name = u'Pivotal Toronto User Group'
    events_list_group_119.city = u'Toronto'
    events_list_group_119.state = u'ON'
    events_list_group_119.country = u'CA'
    events_list_group_119.meetupID = 6015342L
    events_list_group_119.is_applicable = True
    events_list_group_119 = importer.save_or_locate(events_list_group_119)

    events_list_group_120 = Group()
    events_list_group_120.name = u'ElasticSearch Usergroup Frankfurt'
    events_list_group_120.city = u'Frankfurt'
    events_list_group_120.state = u''
    events_list_group_120.country = u'DE'
    events_list_group_120.meetupID = 12970172L
    events_list_group_120.is_applicable = True
    events_list_group_120 = importer.save_or_locate(events_list_group_120)

    events_list_group_121 = Group()
    events_list_group_121.name = u'Seattle Scalability Meetup'
    events_list_group_121.city = u'Seattle'
    events_list_group_121.state = u'WA'
    events_list_group_121.country = u'US'
    events_list_group_121.meetupID = 1580512L
    events_list_group_121.is_applicable = True
    events_list_group_121 = importer.save_or_locate(events_list_group_121)

    events_list_group_122 = Group()
    events_list_group_122.name = u'Oslo Hadoop Big Data Meetup'
    events_list_group_122.city = u'Oslo'
    events_list_group_122.state = u''
    events_list_group_122.country = u'NO'
    events_list_group_122.meetupID = 18591596L
    events_list_group_122.is_applicable = True
    events_list_group_122 = importer.save_or_locate(events_list_group_122)

    events_list_group_123 = Group()
    events_list_group_123.name = u'Melbourne Cassandra Users'
    events_list_group_123.city = u'Melbourne'
    events_list_group_123.state = u''
    events_list_group_123.country = u'AU'
    events_list_group_123.meetupID = 14919652L
    events_list_group_123.is_applicable = True
    events_list_group_123 = importer.save_or_locate(events_list_group_123)

    events_list_group_124 = Group()
    events_list_group_124.name = u'Toronto Java Users Group'
    events_list_group_124.city = u'Toronto'
    events_list_group_124.state = u'ON'
    events_list_group_124.country = u'CA'
    events_list_group_124.meetupID = 12543492L
    events_list_group_124.is_applicable = True
    events_list_group_124 = importer.save_or_locate(events_list_group_124)

    events_list_group_125 = Group()
    events_list_group_125.name = u'SoCal Talend Meetup'
    events_list_group_125.city = u'Irvine'
    events_list_group_125.state = u'CA'
    events_list_group_125.country = u'US'
    events_list_group_125.meetupID = 18784646L
    events_list_group_125.is_applicable = True
    events_list_group_125 = importer.save_or_locate(events_list_group_125)

    events_list_group_126 = Group()
    events_list_group_126.name = u'Moscow Big Systems/Big Data'
    events_list_group_126.city = u'Moscow'
    events_list_group_126.state = u''
    events_list_group_126.country = u'RU'
    events_list_group_126.meetupID = 4035302L
    events_list_group_126.is_applicable = True
    events_list_group_126 = importer.save_or_locate(events_list_group_126)

    events_list_group_127 = Group()
    events_list_group_127.name = u'Cascading'
    events_list_group_127.city = u'San Francisco'
    events_list_group_127.state = u'CA'
    events_list_group_127.country = u'US'
    events_list_group_127.meetupID = 4627532L
    events_list_group_127.is_applicable = True
    events_list_group_127 = importer.save_or_locate(events_list_group_127)

    events_list_group_128 = Group()
    events_list_group_128.name = u'Derbyshire Dot Net'
    events_list_group_128.city = u'Derby'
    events_list_group_128.state = u'D3'
    events_list_group_128.country = u'GB'
    events_list_group_128.meetupID = 18710153L
    events_list_group_128.is_applicable = True
    events_list_group_128 = importer.save_or_locate(events_list_group_128)

    events_list_group_129 = Group()
    events_list_group_129.name = u'Big Data DC'
    events_list_group_129.city = u'Mc Lean'
    events_list_group_129.state = u'VA'
    events_list_group_129.country = u'US'
    events_list_group_129.meetupID = 1810133L
    events_list_group_129.is_applicable = True
    events_list_group_129 = importer.save_or_locate(events_list_group_129)

    events_list_group_130 = Group()
    events_list_group_130.name = u'Berliner Apache Cordova Network'
    events_list_group_130.city = u'Berlin'
    events_list_group_130.state = u''
    events_list_group_130.country = u'DE'
    events_list_group_130.meetupID = 18457296L
    events_list_group_130.is_applicable = True
    events_list_group_130 = importer.save_or_locate(events_list_group_130)

    events_list_group_131 = Group()
    events_list_group_131.name = u'Lansing  Big Data and Hadoop Users Group Meetup'
    events_list_group_131.city = u'Okemos'
    events_list_group_131.state = u'MI'
    events_list_group_131.country = u'US'
    events_list_group_131.meetupID = 18384747L
    events_list_group_131.is_applicable = True
    events_list_group_131 = importer.save_or_locate(events_list_group_131)

    events_list_group_132 = Group()
    events_list_group_132.name = u'Seoul Apache Tajo Meetup'
    events_list_group_132.city = u'Seoul'
    events_list_group_132.state = u''
    events_list_group_132.country = u'KR'
    events_list_group_132.meetupID = 7802752L
    events_list_group_132.is_applicable = True
    events_list_group_132 = importer.save_or_locate(events_list_group_132)

    events_list_group_133 = Group()
    events_list_group_133.name = u'Arizona Backpacking Club'
    events_list_group_133.city = u'Phoenix'
    events_list_group_133.state = u'AZ'
    events_list_group_133.country = u'US'
    events_list_group_133.meetupID = 1181021L
    events_list_group_133.is_applicable = True
    events_list_group_133 = importer.save_or_locate(events_list_group_133)

    events_list_group_134 = Group()
    events_list_group_134.name = u'Composers-Lyricists-Songwriters Workshop and Showcase.'
    events_list_group_134.city = u'Austin'
    events_list_group_134.state = u'TX'
    events_list_group_134.country = u'US'
    events_list_group_134.meetupID = 18671368L
    events_list_group_134.is_applicable = True
    events_list_group_134 = importer.save_or_locate(events_list_group_134)

    events_list_group_135 = Group()
    events_list_group_135.name = u"ALT-Lanta: Atlanta's new Indie music scene and culture"
    events_list_group_135.city = u'Atlanta'
    events_list_group_135.state = u'GA'
    events_list_group_135.country = u'US'
    events_list_group_135.meetupID = 18522371L
    events_list_group_135.is_applicable = True
    events_list_group_135 = importer.save_or_locate(events_list_group_135)

    events_list_group_136 = Group()
    events_list_group_136.name = u'Bangalore Apache Spark Meetup'
    events_list_group_136.city = u'Bangalore'
    events_list_group_136.state = u''
    events_list_group_136.country = u'IN'
    events_list_group_136.meetupID = 18407383L
    events_list_group_136.is_applicable = True
    events_list_group_136 = importer.save_or_locate(events_list_group_136)

    events_list_group_137 = Group()
    events_list_group_137.name = u'WSDEVS:  Mobile, SOA, BigData, Webapp, Alm/Scrum, IOT'
    events_list_group_137.city = u'S\xe3o Paulo'
    events_list_group_137.state = u''
    events_list_group_137.country = u'BR'
    events_list_group_137.meetupID = 18479181L
    events_list_group_137.is_applicable = True
    events_list_group_137 = importer.save_or_locate(events_list_group_137)

    events_list_group_138 = Group()
    events_list_group_138.name = u'Big Data Denmark'
    events_list_group_138.city = u'\xc5rhus'
    events_list_group_138.state = u''
    events_list_group_138.country = u'DK'
    events_list_group_138.meetupID = 16615762L
    events_list_group_138.is_applicable = True
    events_list_group_138 = importer.save_or_locate(events_list_group_138)

    events_list_group_139 = Group()
    events_list_group_139.name = u'Big things'
    events_list_group_139.city = u'Tel Aviv-Yafo'
    events_list_group_139.state = u''
    events_list_group_139.country = u'IL'
    events_list_group_139.meetupID = 18423322L
    events_list_group_139.is_applicable = True
    events_list_group_139 = importer.save_or_locate(events_list_group_139)

    events_list_group_140 = Group()
    events_list_group_140.name = u'Adobe Developers & Designers, Sydney (ADDS)'
    events_list_group_140.city = u'Sydney'
    events_list_group_140.state = u''
    events_list_group_140.country = u'AU'
    events_list_group_140.meetupID = 5747682L
    events_list_group_140.is_applicable = True
    events_list_group_140 = importer.save_or_locate(events_list_group_140)

    events_list_group_141 = Group()
    events_list_group_141.name = u'Toronto Apache Spark'
    events_list_group_141.city = u'Toronto'
    events_list_group_141.state = u'ON'
    events_list_group_141.country = u'CA'
    events_list_group_141.meetupID = 18742524L
    events_list_group_141.is_applicable = True
    events_list_group_141 = importer.save_or_locate(events_list_group_141)

    events_list_group_142 = Group()
    events_list_group_142.name = u'Scala Developers in Manchester'
    events_list_group_142.city = u'Manchester'
    events_list_group_142.state = u'18'
    events_list_group_142.country = u'GB'
    events_list_group_142.meetupID = 7554702L
    events_list_group_142.is_applicable = True
    events_list_group_142 = importer.save_or_locate(events_list_group_142)

    events_list_group_143 = Group()
    events_list_group_143.name = u'HUGNOFA'
    events_list_group_143.city = u'Saint Augustine'
    events_list_group_143.state = u'FL'
    events_list_group_143.country = u'US'
    events_list_group_143.meetupID = 4173572L
    events_list_group_143.is_applicable = True
    events_list_group_143 = importer.save_or_locate(events_list_group_143)

    events_list_group_144 = Group()
    events_list_group_144.name = u'Cloudera Tech Meetup'
    events_list_group_144.city = u'Budapest'
    events_list_group_144.state = u''
    events_list_group_144.country = u'HU'
    events_list_group_144.meetupID = 18568847L
    events_list_group_144.is_applicable = True
    events_list_group_144 = importer.save_or_locate(events_list_group_144)

    events_list_group_145 = Group()
    events_list_group_145.name = u'Phoenix Hadoop User Group'
    events_list_group_145.city = u'Phoenix'
    events_list_group_145.state = u'AZ'
    events_list_group_145.country = u'US'
    events_list_group_145.meetupID = 12321952L
    events_list_group_145.is_applicable = True
    events_list_group_145 = importer.save_or_locate(events_list_group_145)

    events_list_group_146 = Group()
    events_list_group_146.name = u'Austin Data Geeks'
    events_list_group_146.city = u'Austin'
    events_list_group_146.state = u'TX'
    events_list_group_146.country = u'US'
    events_list_group_146.meetupID = 1784720L
    events_list_group_146.is_applicable = True
    events_list_group_146 = importer.save_or_locate(events_list_group_146)

    events_list_group_147 = Group()
    events_list_group_147.name = u'Atlanta Web Performance Group'
    events_list_group_147.city = u'Atlanta'
    events_list_group_147.state = u'GA'
    events_list_group_147.country = u'US'
    events_list_group_147.meetupID = 2283171L
    events_list_group_147.is_applicable = True
    events_list_group_147 = importer.save_or_locate(events_list_group_147)

    events_list_group_148 = Group()
    events_list_group_148.name = u'SeaLang'
    events_list_group_148.city = u'Redmond'
    events_list_group_148.state = u'WA'
    events_list_group_148.country = u'US'
    events_list_group_148.meetupID = 7501092L
    events_list_group_148.is_applicable = True
    events_list_group_148 = importer.save_or_locate(events_list_group_148)

    events_list_group_149 = Group()
    events_list_group_149.name = u'AEM Developer Meetup'
    events_list_group_149.city = u'Amsterdam'
    events_list_group_149.state = u''
    events_list_group_149.country = u'NL'
    events_list_group_149.meetupID = 18741010L
    events_list_group_149.is_applicable = True
    events_list_group_149 = importer.save_or_locate(events_list_group_149)

    events_list_group_150 = Group()
    events_list_group_150.name = u'LAPHP: The Los Angeles PHP Developers Group'
    events_list_group_150.city = u'Santa Monica'
    events_list_group_150.state = u'CA'
    events_list_group_150.country = u'US'
    events_list_group_150.meetupID = 582093L
    events_list_group_150.is_applicable = True
    events_list_group_150 = importer.save_or_locate(events_list_group_150)

    events_list_group_151 = Group()
    events_list_group_151.name = u'Data Science LA'
    events_list_group_151.city = u'Santa Monica'
    events_list_group_151.state = u'CA'
    events_list_group_151.country = u'US'
    events_list_group_151.meetupID = 11488322L
    events_list_group_151.is_applicable = True
    events_list_group_151 = importer.save_or_locate(events_list_group_151)

    events_list_group_152 = Group()
    events_list_group_152.name = u'NYC BIG DATA VISIONARIES'
    events_list_group_152.city = u'New York'
    events_list_group_152.state = u'NY'
    events_list_group_152.country = u'US'
    events_list_group_152.meetupID = 15612262L
    events_list_group_152.is_applicable = True
    events_list_group_152 = importer.save_or_locate(events_list_group_152)

    events_list_group_153 = Group()
    events_list_group_153.name = u'New York Web Performance Group'
    events_list_group_153.city = u'New York'
    events_list_group_153.state = u'NY'
    events_list_group_153.country = u'US'
    events_list_group_153.meetupID = 1428523L
    events_list_group_153.is_applicable = True
    events_list_group_153 = importer.save_or_locate(events_list_group_153)

    events_list_group_154 = Group()
    events_list_group_154.name = u'North Phoenix Cruisers'
    events_list_group_154.city = u'Phoenix'
    events_list_group_154.state = u'AZ'
    events_list_group_154.country = u'US'
    events_list_group_154.meetupID = 3575632L
    events_list_group_154.is_applicable = True
    events_list_group_154 = importer.save_or_locate(events_list_group_154)

    events_list_group_155 = Group()
    events_list_group_155.name = u'Taa-naash-kaa-da Sanctuary'
    events_list_group_155.city = u'Las Vegas'
    events_list_group_155.state = u'NM'
    events_list_group_155.country = u'US'
    events_list_group_155.meetupID = 14848302L
    events_list_group_155.is_applicable = True
    events_list_group_155 = importer.save_or_locate(events_list_group_155)

    events_list_group_156 = Group()
    events_list_group_156.name = u'Phoenix Motorcycle Riders Group'
    events_list_group_156.city = u'Phoenix'
    events_list_group_156.state = u'AZ'
    events_list_group_156.country = u'US'
    events_list_group_156.meetupID = 444077L
    events_list_group_156.is_applicable = True
    events_list_group_156 = importer.save_or_locate(events_list_group_156)

    events_list_group_157 = Group()
    events_list_group_157.name = u'Big Data Hyderabad'
    events_list_group_157.city = u'Hyderabad'
    events_list_group_157.state = u''
    events_list_group_157.country = u'IN'
    events_list_group_157.meetupID = 14467182L
    events_list_group_157.is_applicable = True
    events_list_group_157 = importer.save_or_locate(events_list_group_157)

    events_list_group_158 = Group()
    events_list_group_158.name = u'Atlanta Ionic Developers'
    events_list_group_158.city = u'Atlanta'
    events_list_group_158.state = u'GA'
    events_list_group_158.country = u'US'
    events_list_group_158.meetupID = 18418431L
    events_list_group_158.is_applicable = True
    events_list_group_158 = importer.save_or_locate(events_list_group_158)

    events_list_group_159 = Group()
    events_list_group_159.name = u'Haifa  Big Data'
    events_list_group_159.city = u'Haifa'
    events_list_group_159.state = u''
    events_list_group_159.country = u'IL'
    events_list_group_159.meetupID = 18616619L
    events_list_group_159.is_applicable = True
    events_list_group_159 = importer.save_or_locate(events_list_group_159)

    events_list_group_160 = Group()
    events_list_group_160.name = u'Data Innovation Training Hub'
    events_list_group_160.city = u'Brussels'
    events_list_group_160.state = u''
    events_list_group_160.country = u'BE'
    events_list_group_160.meetupID = 18631365L
    events_list_group_160.is_applicable = True
    events_list_group_160 = importer.save_or_locate(events_list_group_160)

    events_list_group_161 = Group()
    events_list_group_161.name = u'Minneapolis St. Paul Cassandra Meetup'
    events_list_group_161.city = u'Minneapolis'
    events_list_group_161.state = u'MN'
    events_list_group_161.country = u'US'
    events_list_group_161.meetupID = 4653912L
    events_list_group_161.is_applicable = True
    events_list_group_161 = importer.save_or_locate(events_list_group_161)

    events_list_group_162 = Group()
    events_list_group_162.name = u'Z\xfcrich Apache Spark Meetup'
    events_list_group_162.city = u'Z\xfcrich'
    events_list_group_162.state = u''
    events_list_group_162.country = u'CH'
    events_list_group_162.meetupID = 18614547L
    events_list_group_162.is_applicable = True
    events_list_group_162 = importer.save_or_locate(events_list_group_162)

    events_list_group_163 = Group()
    events_list_group_163.name = u'Apache Lucene/Solr - London User Group'
    events_list_group_163.city = u'London'
    events_list_group_163.state = u'17'
    events_list_group_163.country = u'GB'
    events_list_group_163.meetupID = 17892732L
    events_list_group_163.is_applicable = True
    events_list_group_163 = importer.save_or_locate(events_list_group_163)

    events_list_group_164 = Group()
    events_list_group_164.name = u'Bohemian Circus Figure Drawing Group at Apache Cafe'
    events_list_group_164.city = u'Atlanta'
    events_list_group_164.state = u'GA'
    events_list_group_164.country = u'US'
    events_list_group_164.meetupID = 1758814L
    events_list_group_164.is_applicable = False
    events_list_group_164 = importer.save_or_locate(events_list_group_164)

    # Processing model: Hashtag

    from events_list.models import Hashtag

    events_list_hashtag_1 = Hashtag()
    events_list_hashtag_1.name = u'Apache'
    events_list_hashtag_1 = importer.save_or_locate(events_list_hashtag_1)

    # Processing model: Person

    from events_list.models import Person


    # Processing model: Event

    from events_list.models import Event

    events_list_event_1 = Event()
    events_list_event_1.name = u'Mining Camp to Siphon Draw - Superstition Mountains'
    events_list_event_1.event_url = u'http://www.meetup.com/threeh/events/224453399/'
    events_list_event_1.group = events_list_group_83
    events_list_event_1.meetupID = u'224453399'
    events_list_event_1.description = u'<p><b>Distance:</b> Approximately\xa04 miles.</p> <p><b>Difficulty:</b> Moderate to difficult depending on one\'s ability.</p> <p><b>Elevation gain:</b>\xa01000 feet +/- from the Mining Camp Trailhead.</p> <p><b>Time:</b>\xa0 Expect\xa02-3 hours for this hike.</p> <p><b>Fun factor:</b> High!</p> <p>\xa0Off we go, again, into the Superstitions!\xa0 Regardless of the season, we hike here every few weeks, because we love it just that much.\xa0 We\'ll use\xa0the Mining Camp Trailhead.\xa0 There is some shade on this hike during the morning hours, and the temps are forecast to be in the 80\'s at the posted\xa0start time.\xa0</p> <p>Here is an excellent link with descriptions, photos, and stats.\xa0 Please read it to make sure this\xa0hike matches your abilities, but\xa0do\xa0note, we will start at a different trailhead than that noted in this link.\xa0 <a href="http://hikearizona.com/decoder.php?ZTN=686"><a href="http://hikearizona.com/decoder.php?ZTN=686" class="linkified">http://hikearizona.com/decoder.php?ZTN=686</a></a></p> <p><b>What to Bring:</b> Plenty of water (we\'d suggest 2-3 liters at a minimum), sunscreen, a hat, proper hiking shoes, a snack, your camera and your love of the trails.\xa0 We\'ll stop in the\xa0Draw for a snack before heading back down.</p> <p><b>Directions to the trailhead:</b> Take U.S. 60 to Idaho Road (exit 196) and go north for 2.25 miles to SR88, the Apache Trail. Turn NE (slight right) on SR88 and continue about 5.5 miles or so to Nodak Rd. (It is the turn for the Mining Camp Restaurant, so look for the signs for that turn). Turn right at Nodak Rd. and then left at the 2nd Rd. (Mining Camp Rd.) and continue to follow the signs to the restaurant. At the restaurant, turn to the left into the parking lot, and park away from the restaurant on the west end of the lot.</p> <p>Please note these are all paved roads\xa0ending into\xa0a gravel parking lot.\xa0 There is no fee to park here, but there are no facilities available, either, so plan accordingly.\xa0</p> <p>For those coming down the 101 to the 202, it is suggested that you exit at Brown Road (rather than going down to US 60) and take it east about 5 miles to AZ 88. From there, turn left, and head to the Mining Camp restaurant turnoff.</p> <p><b>Suggested carpool location:</b> 6:30 am at the Home Depot at Power and US 60. Go east on the Superstition Freeway (US 60) to Superstition Springs Blvd. exit 187. Take that exit, turn right and go 1/2 mile east, across Power Road. Then turn left, toward Home Depot, at the second driveway. Park in the southwest corner of the lot, behind Burger King. The Home Depot address is 6838 E Superstition Springs Blvd., Mesa, AZ 85208.</p> <p><b>VERY</b> <b>IMPORTANT:</b> Please state if you will be at the carpool spot, or, in the alternative, whether you will meet at the trailhead. You are responsible for yourself in this regard. There is no guarantee that anyone will be at the carpool location. If no one has indicated they will be there, please consider proceeding to the trailhead.</p> <p>The forest service imposes a 15 hiker limit on all Superstition Wilderness hikes.\xa0</p>'
    events_list_event_1.local_start = dateutil.parser.parse("2015-08-09T07:00:00")
    events_list_event_1.local_end = dateutil.parser.parse("2015-08-09T07:00:00")
    events_list_event_1.utc_offset = -25200L
    events_list_event_1.is_applicable = False
    events_list_event_1 = importer.save_or_locate(events_list_event_1)

    events_list_event_1.hashtags.add(events_list_hashtag_1)

    events_list_event_2 = Event()
    events_list_event_2.name = u'Hadoop ile Merhaba D\xfcnya (Workshop)'
    events_list_event_2.event_url = u'http://www.meetup.com/Istanbul-Spark-Meetup/events/223599737/'
    events_list_event_2.group = events_list_group_1
    events_list_event_2.meetupID = u'223599737'
    events_list_event_2.description = u'<p>Merhaba,</p> <p><br/>Hadoop ile tan\u0131\u015fmak i\xe7in g\xfczel bir etkinlik yapmay\u0131 planl\u0131yoruz. (Java temelli olacakt\u0131r.)</p> <p><br/>Konu ba\u015fl\u0131klar\u0131:</p> <p>\u2022\xa0Hadoop Genel Anlat\u0131m</p> <p>\u2022\xa0Hadoop Kurulum ( YARN )</p> <p>\u2022\xa0Eclipse i\xe7in Ortam Haz\u0131rl\u0131\u011f\u0131 ve Maven ile kullan\u0131m\u0131</p> <p><br/>\u2022\xa0Word Count \xd6rne\u011fi\xa0</p> <p>\u2022\xa0Ve Di\u011fer \xd6rnekler</p> <p><br/>Sadece sanal makine olarak CentOS 6.6 kurulu olmas\u0131 yeterli olacakt\u0131r.</p>'
    events_list_event_2.local_start = dateutil.parser.parse("2015-08-08T11:00:00")
    events_list_event_2.local_end = dateutil.parser.parse("2015-08-08T11:00:00")
    events_list_event_2.utc_offset = 10800L
    events_list_event_2.is_applicable = True
    events_list_event_2 = importer.save_or_locate(events_list_event_2)

    events_list_event_2.hashtags.add(events_list_hashtag_1)

    events_list_event_3 = Event()
    events_list_event_3.name = u'HIKE - WEST FORK TRAIL ... Oak Creek (Sedona)'
    events_list_event_3.event_url = u'http://www.meetup.com/phoenix-atheists/events/224381579/'
    events_list_event_3.group = events_list_group_84
    events_list_event_3.meetupID = u'224381579'
    events_list_event_3.description = u'<p><img src="http://photos2.meetupstatic.com/photos/event/b/d/6/c/event_221328492.jpeghttp://photos1.meetupstatic.com/photos/event/b/d/1/2/event_221328402.jpeghttp://photos2.meetupstatic.com/photos/event/b/c/e/0/event_221328352.jpeghttp://photos4.meetupstatic.com/photos/event/b/c/6/8/event_221328232.jpeghttp://photos1.meetupstatic.com/photos/event/b/c/4/0/event_221328192.jpeghttp://photos1.meetupstatic.com/photos/event/1/5/2/4/event_221285412.jpeghttp://photos4.meetupstatic.com/photos/event/1/c/6/7/event_45787271.jpeg" /></p> <p>One of the top 10 trails in the U.S... the West Fork trail will usher you through a tremendous variety of natural wonders. Here, you can enjoy a "secret and magical forest" feel, as you meander along a shallow and perfectly clear creek that runs at the foot of towering canyon walls amid emerald evergreens and lush leafy trees.</p> <p><img src="http://photos1.meetupstatic.com/photos/event/1/c/c/1/event_45787361.jpeg" /></p> <p>There are a number of reasons why West Fork is the most popular trail of the Coconino National Forest. You\'ll know some of them once you\'ve strolled beside the pleasant little stream that ripples along the canyon floor and looked up, way up, at the dizzying cliffs that tower above it.</p> <p>As for the trail itself, it\'s an easy stroll, but you do have to cross the stream in a number of places. Usually, that involves negotiating a few strategically placed stepping stones or taking a couple of steps in shallow water. Some hikers will enjoy walking within the stream itself.</p> <p>Our hikes are generally at a pace conducive to social banter of interest to heathens, and allowing for time for photography of the local geology and wildlife. However, this will be an out-n-back with a time limit to be determined by the group. This will allow for hikers to go at their own pace and turn around at the agreed upon time. Expect this hike to last 3-4 hours.</p> <p>The Trailhead of the West Fork Trail is at <i>The Call of the Canyon Day-Use Area</i>. This is set in a clearing next to a grassy meadow which in summer is filled with wildflowers of every color and frequented by humming birds and large butterflies.</p> <p>A path crosses Oak Creek and follows it downstream for a short distance, through an abandoned apple orchard, passing by the site of the ruins of the Mayhew Lodge with overgrown remnants of fireplaces, stone floors, and even the swimming pool. See below for historical discussion of the orchard and the resort.</p> <p>The official trail starts just beyond, near the West Fork confluence. The canyon is hundreds of feet deep and moderately narrow from the start, wooded, overgrown and shaded with many fallen trees and old logs, often lying in the stream way. The path crosses the creek many times and\xa0in places there are paths at both sides.</p> <p>Occasionally the creek has pools 3-5 feet deep which harbor trout and other fish although usually the water (in summer) is only a few inches deep. The stream flows gently, and the hike is very pleasant and relaxing.\xa0Only occasional sunlight reaches the canyon floor so the trip is ideal for the hot summer months.</p> <p>Wildlife is quite abundant. Typical are butterflies, colorful birds, squirrels, lizards and snakes.</p> <p>Here are links to more info:</p> <p><a href="http://hikearizona.com/decoder.php?ZTN=147"><a href="http://hikearizona.com/decoder.php?ZTN=147" class="linkified">http://hikearizona.com/decoder.php?ZTN=147</a></a></p> <p><a href="http://www.americansouthwest.net/arizona/sedona/west_oak_creek.html"><a href="http://www.americansouthwest.net/arizona/sedona/west_oak_creek.html" class="linkified">http://www.americansouthwest.net/arizona/sedona/west_oak_creek.html</a></a></p> <p>Here are links to photos from our previous hikes to this destination:</p> <p>8/13/11</p> <p><a href="http://www.meetup.com/phoenix-atheists/photos/all_photos/?photoAlbumId=2912701"><a href="http://www.meetup.com/phoenix-atheists/photos/all_photos/?photoAlbumId=2912701" class="linkified">http://www.meetup.com/phoenix-atheists/photos/all_photos/?photoAlbumId=2912701</a></a></p> <p>7/15/12</p> <p><a href="http://www.meetup.com/phoenix-atheists/photos/all_photos/?photoAlbumId=9727282"><a href="http://www.meetup.com/phoenix-atheists/photos/all_photos/?photoAlbumId=9727282" class="linkified">http://www.meetup.com/phoenix-atheists/photos/all_photos/?photoAlbumId=9727282</a></a></p> <p>4/14/13</p> <p><a href="http://www.meetup.com/phoenix-atheists/photos/all_photos/?photoAlbumId=14322972"><a href="http://www.meetup.com/phoenix-atheists/photos/all_photos/?photoAlbumId=14322972" class="linkified">http://www.meetup.com/phoenix-atheists/photos/all_photos/?photoAlbumId=14322972</a></a></p> <p>10/19/14</p> <p><a href="http://www.meetup.com/phoenix-atheists/photos/all_photos/?photoAlbumId=25285272"><a href="http://www.meetup.com/phoenix-atheists/photos/all_photos/?photoAlbumId=25285272" class="linkified">http://www.meetup.com/phoenix-atheists/photos/all_photos/?photoAlbumId=25285272</a></a></p> <p>10/27/13</p> <p><a href="http://www.meetup.com/phoenix-atheists/photos/all_photos/?photoAlbumId=18229792"><a href="http://www.meetup.com/phoenix-atheists/photos/all_photos/?photoAlbumId=18229792" class="linkified">http://www.meetup.com/phoenix-atheists/photos/all_photos/?photoAlbumId=18229792</a></a></p> <p>10/21/12</p> <p><a href="http://www.meetup.com/phoenix-atheists/photos/all_photos/?photoAlbumId=11368012"><a href="http://www.meetup.com/phoenix-atheists/photos/all_photos/?photoAlbumId=11368012" class="linkified">http://www.meetup.com/phoenix-atheists/photos/all_photos/?photoAlbumId=11368012</a></a></p> <p>10/30/11</p> <p><a href="http://www.meetup.com/phoenix-atheists/photos/all_photos/?photoAlbumId=4202602"><a href="http://www.meetup.com/phoenix-atheists/photos/all_photos/?photoAlbumId=4202602" class="linkified">http://www.meetup.com/phoenix-atheists/photos/all_photos/?photoAlbumId=4202602</a></a></p> <p><b>HIKE SUMMARY:</b></p> <p><b>Distance</b>: &lt;6 miles TBD (timed)</p> <p><b>Time</b>: 3-5 hrs. TBD at time of hike.</p> <p><b>Difficulty</b>: easy</p> <p><b>Trail</b>: forest paths and stream crossings</p> <p><b>Elevation:</b> 5260 ft.</p> <p>change <b>:</b> 200ft.</p> <p><b>Parking</b>: paved parking lot near trailhead</p> <p><b>Tailhead GPS:</b>[masked] [masked]</p> <p>34\xb0[masked] -111\xb0[masked]</p> <p>34\xb0 59\'26.624" -111\xb0 44\'33.979"</p> <p>Entry <b>fees</b> : $9 per vehicle (up to 5 people), walk-in is $2 per person.</p> <p><b>Dogs</b>: OK leashed</p> <p><b>REMINDERS:</b></p> <p>Always carry and drink plenty of water!</p> <p>Sunscreen and insect repellant is advised.</p> <p>Supportive footwear is also advisable.</p> <p>Water shoes may be especially useful on this hike due to creek crossings.</p> <p>Have light rain gear available.</p> <p>(Scattered afternoon thunderstorms are common at high altitudes July \u2013 September.)</p> <p>SAFETY FIRST\u2026 we have no medical provisions . . . and be alert for \u201cpoison ivy\u201d.</p> <p><b>How to find us:</b></p> <p>Meet at <i>The Call of the Canyon Day-Use Area</i> on the west side of AZ 89A between mileposts 384 and 385... If lost or late, my cell is[masked]\u2026 but cell phone reception is poor throughout canyon.</p> <p><b>To get there...</b></p> <p>From the 101 &amp; I-17, take I-17 north about 83 miles to exit 298 for AZ-179 north to Sedona. Follow AZ-179 north about 15 miles through several traffic circles and turn right at the traffic circle for US Highway 89A. Then drive north 10.5 miles to the Call of the Canyon Day Use Area (between mileposts 384 &amp; 385) on the left (west) side of the road. Roads are 100% paved.</p> <p>\xa0Google says this parking lot is about 2 hr. from the intersection of the 101 and I-17. HOWEVER this location is very popular and especially so during the fall. EXPECT A FULL PARKING LOT and you may be PARKING ALONG THE ROAD\u2026 and perhaps several hundred yards away. SO <b>PLAN EXTRA TIME</b> JUST FOR PARKING.</p> <p><b>MESSAGE FOR CARPOOLERS</b>:</p> <p>Carpooling can save gas and entry fees and also enhance the social experience. If you\u2019d like to carpool, you must contact others for arrangements. You could email members or post comments on this announcement page.</p> <p><b>Following the hike</b>\u2026 we will reconvene in Sedona at a location TBD for rehydration and lunch .</p> <p><b>HISTORY</b></p> <p>In the early 1880\'s, one of the pioneers traveling up Oak Creek Canyon noticed a rather level area on either side of the creek where the soil was deep and the temperature just right to grow apples and other fruit.</p> <p>The first pioneer to plant fruit trees at West Fork was C.S. (Bear) Howard. He sold his rights to John L.V. Thomas and his son and they expanded the orchard and also grew vegetables and other cash crops to sell to the lumberjacks in Flagstaff. The land was sold to the Mayhews in 1925.</p> <p>Carl Mayhew expanded the original cabin and turned it into a hunting and fishing lodge \u2013 and a remote \u201cgetaway\u201d for early Hollywood stars and other notables, including President Hoover, Clark Gable, Susan Hayward, Cesar Romero, Jimmy Stewart, Walt Disney, and Maureen O\'Hara.</p> <p>During that time, the lodge was nearly self-sufficient with fruits from the orchard, fish from the creek, vegetables from plots planted near the orchard, and meat and eggs from chickens housed in a coop still seen today at the foot of the cliff near the remains of the lodge.</p> <p>The mystic beauty of the area inspired novelist Zane Grey to write Call of the Canyon here in the early 1920\'s. He reportedly stayed at the Mayhew Lodge during part of his sojourn here, as well as in a smaller cabin north of the orchard. The novel later inspired Sedona\'s first movie by the same name.</p> <p>The U. S. Forest Service acquired the property in 1969 as an historic site, only to have the lodge burn down in 1980.</p> <p>Over time, the orchards at West Fork became known as the "Mayhew Orchard" on the west side of the creek, and the "Call of the Canyon Orchard" on the east side.</p> <p>Through the last half of the twentieth century, the ancient trees suffered increasing neglect, injury and decline. The irrigation ditch, which can still be seen slightly upslope from the Mayhew Orchard, slowly filled in with debris, fallen trees, and duff. Insects, woodpeckers, and flycatchers drilled thousands of holes in the bark, some in neat little rows. Storm damage, drought, and bears climbing to reach the fruit contributed to increasing numbers of dead and broken branches, where disease could find easy entry. In the last decades of the 1900\u2019s, the gnarled old trees were largely abandoned.</p> <p>In 2002, the <i>Friends of the Forest</i> created the Orchard Committee to begin caring for the trees. Initial work revolved around heavy pruning of dead and diseased limbs, suckers, and crossed branches. As the work progressed, the orchard crew began slowly reducing the height of the trees, so that visitors (both human and animal) could reach the apples more easily, without climbing or damaging the trees. Some of the trees were easily thirty feet high at the outset. All visitors are welcome to pick the apples in the fall. To facilitate this and reduce damage to the trees, the Friends purchased several \u201capple-pickers\u201d on poles that visitors can check out at the entry booth.</p> <p><b>GEOLOGY</b></p> <p>The colorful eroded walls of the canyon record environmental conditions on the far western edge of the Pangea supercontinent[masked] million years ago.</p> <p>The Kaibab limestone on top is the youngest rock unit on the southern Colorado Plateau and caps the Mogollon Rim in the Sedona area (wherever basalt is absent). It was deposited in an open marine setting that became shallower and more restricted towards the east.</p> <p>The Toroweap formation underlies the Kaibab. We saw this combination at Walnut Canyon National Park.</p> <p>A green line often indicates this Toroweap layering above the Coconino Sandstone below. The golden buff-colored Coconino sandstone is pure quartz deposited in a migrating windblown sand dune environment.</p> <p>The lowermost rock deposits are the Sycamore Pass member of the Schnebly Hill Formation. The Schnebly Hill Formation records depositions at the margins of the Pedregosa Sea when it encroached from the southeast of Sedona. Briefly marine deposits were laid down (the narrow white layer, known as the Fort Apache Member, we saw at Chicken Point). Above that layer, as the Sea regressed, red, cross-stratified and ripple-laminated, sandstones were laid down from wind-blown deposits about 280 million years ago.</p> <p>Above it all are the youngest rocks exposed in the canyon - a series of <a href="http://en.wikipedia.org/wiki/Basalt">basalt</a> <a href="http://en.wikipedia.org/wiki/Lava_flow">lava flows</a> about 6 million years old form the east rim of the canyon.</p>'
    events_list_event_3.local_start = dateutil.parser.parse("2015-08-09T09:45:00")
    events_list_event_3.local_end = dateutil.parser.parse("2015-08-09T09:45:00")
    events_list_event_3.utc_offset = -25200L
    events_list_event_3.is_applicable = False
    events_list_event_3 = importer.save_or_locate(events_list_event_3)

    events_list_event_3.hashtags.add(events_list_hashtag_1)

    events_list_event_4 = Event()
    events_list_event_4.name = u'Checking out Cloudcroft'
    events_list_event_4.event_url = u'http://www.meetup.com/Las-Cruces-Motorcycle-Riders/events/224453701/'
    events_list_event_4.group = events_list_group_77
    events_list_event_4.meetupID = u'224453701'
    events_list_event_4.description = u"<p>The Plan:\xa0Meet at\xa08:30 am, KSU at 9:00 am</p> <p>\xa0Hwy. \xa070 East, 70 By Pass to 82 East. We'll stop at the Chevron station on 82 for a top off and other requirements. Then head on up to Cloudcroft. Oh yeah this will be Gwen's first ride!! We will do a quick stop and check out the Trestle. Once in\xa0Cloudcroft\xa0we'll have some time to kill and check out the some shops then lunch. After lunch head up towards Sunspot, we'll do a quick stop at Apache Point then ride over Sunspot. It will be mid afternoon by then and we can discuss if we want to ride anywhere else. Weather for Cloudcroft on Sat is: High of 74 and 40% chance of rain in the late afternoon. Leaving LC Saturday morning temps will be in the low 70s. So have your\xa0rain gear as always. Hope to see some of you Saturday!</p> <p>Bill Chambers will be lead for this ride/gathering.\xa0 If there are any updates or changes Bill will post them Friday night.</p>"
    events_list_event_4.local_start = dateutil.parser.parse("2015-08-08T08:30:00")
    events_list_event_4.local_end = dateutil.parser.parse("2015-08-08T08:30:00")
    events_list_event_4.utc_offset = -21600L
    events_list_event_4.is_applicable = False
    events_list_event_4 = importer.save_or_locate(events_list_event_4)

    events_list_event_4.hashtags.add(events_list_hashtag_1)

    events_list_event_5 = Event()
    events_list_event_5.name = u"What's New in Solr 5 Security & Solr Custom Collector: The Anti-Score"
    events_list_event_5.event_url = u'http://www.meetup.com/Seattle-Solr-Lucene-Meetup/events/223899316/'
    events_list_event_5.group = events_list_group_3
    events_list_event_5.meetupID = u'223899316'
    events_list_event_5.description = u"<p>Join us for an evening of networking, food &amp; drinks, and the below presentation from Lucene/Solr committer &amp; PMC member, Anshum Gupta.</p> <p><br/><b><i>What's New in Solr 5 Security</i></b>, Presented by Anshum Gupta, Lucidworks</p> <p><br/>Apache Solr has evolved into a highly scalable system, capable of handling a lot of data and high number of queries, but only recently was a mechanism to secure access in Solr provided. Apache Solr 5.2 shipped with pluggable authentication and authorization modules. These modules enable users to write their own plugins for managing security in Solr.</p> <p>This talk will cover an overview of both the authentication and authorization frameworks, and how they work together within Solr. It will also provide an overview of existing plugins and how to enable them to restrict user access to resources within Solr.</p> <p><b>Speaker Bio: </b>Anshum Gupta is a committer and PMC member on the Apache Lucene / Solr project with over 10 years of experience with search and related technologies. He currently works at Lucidworks and spends most of his time working on SolrCloud i.e. the distributed feature set of Apache Solr. Prior to joining Lucidworks, he was a member of the team that developed and launched AWS CloudSearch - The AWS search as a service offering. He was also a key contributor in the search teams at various start ups. Anshum is also the release manager for Solr 5.</p> <p><br/><i><b>Solr Custom Collector: The Anti-Score,</b> </i>Presented by Michael Kosten, Getty Images</p> <p>Sometimes, you don't want to return just the top scoring documents as your search results.\xa0 If you have an eCommerce site, you may want to ensure that multiple lines of business are represented. If you incorporate customer interaction in your score, you may want to ensure that newer documents or certain categories are still represented and that your results don't become stale. This requirement could be handled in middleware that post processes the search results, by requesting extra rows and rearranging them or by interleaving multiple queries. A better solution is to implement your own custom collector in Solr, so that search results can be arranged in any order. I'll demonstrate a solution that returns top scoring documents, but grouped within categories. For example, a search for books could interweave the best fiction and non-fiction in a single query result. I'll also demonstrate how to implement a custom priority queue to reduce memory requirements if there are many categories, and how the custom collector can be integrated into Solr without modifying the base distribution.</p> <p><b>Speaker Bio: </b>Michael Kosten Principal Engineer at Getty Images attached to Search. He's been working on the Search team at Getty Images for the past 8 years. Before that, he was a software development consultant for 17 years to the insurance and construction industries, both in a solo-practice and as a partner in a consulting firm. Getty Images is a premier site for stock photographs and footage as well for stills and videos from news, sports, fashion and entertainment events.</p>"
    events_list_event_5.local_start = dateutil.parser.parse("2015-08-11T18:00:00")
    events_list_event_5.local_end = dateutil.parser.parse("2015-08-11T20:00:00")
    events_list_event_5.utc_offset = -25200L
    events_list_event_5.is_applicable = True
    events_list_event_5 = importer.save_or_locate(events_list_event_5)

    events_list_event_5.hashtags.add(events_list_hashtag_1)

    events_list_event_6 = Event()
    events_list_event_6.name = u"August Meetup: What's New With Hortonworks 2.3 - Product Review and IoT Demo"
    events_list_event_6.event_url = u'http://www.meetup.com/DFW-Analytics-Big-Data-and-Beyond/events/224423660/'
    events_list_event_6.group = events_list_group_103
    events_list_event_6.meetupID = u'224423660'
    events_list_event_6.description = u"<p>All,\xa0</p> <p>Our next Meetup will be Tuesday, August 25. We are returning to the Arlington Hilton.</p> <p>We will be looking at the new features included in the Hortonworks HDP Sandbox, version 2.3 and then walking through an 'Internet of Things' demo utilizing some of the enhanced capabilities, namely Apache Storm and Apache Kafka.</p> <p>More details to follow!</p> <p>Thanks,</p> <p>DFWA</p>"
    events_list_event_6.local_start = dateutil.parser.parse("2015-08-25T18:00:00")
    events_list_event_6.local_end = dateutil.parser.parse("2015-08-25T20:00:00")
    events_list_event_6.utc_offset = -18000L
    events_list_event_6.is_applicable = True
    events_list_event_6 = importer.save_or_locate(events_list_event_6)

    events_list_event_6.hashtags.add(events_list_hashtag_1)

    events_list_event_7 = Event()
    events_list_event_7.name = u'SUNRISE to SUNSET RIDE'
    events_list_event_7.event_url = u'http://www.meetup.com/www-nevadascooterbrigade-com/events/222206591/'
    events_list_event_7.group = events_list_group_78
    events_list_event_7.meetupID = u'222206591'
    events_list_event_7.description = u'<p><img src="http://photos2.meetupstatic.com/photos/event/c/4/b/0/600_436910352.jpeg" /></p> <p><img src="http://photos4.meetupstatic.com/photos/event/c/4/8/7/600_436910311.jpeg" /></p> <p><a href="http://photo.net/photodb/photo?photo_id=11325353" class="linkified">http://photo.net/photodb/photo?photo_id=11325353</a></p> <p>I have found in all these years we have very few that like to ride in the hotter summer heat . So i\'m trying a first for NSB. This is for the early birds in the group-and still want to get their fix of scooter riding in before the afternoon heat- Well this is for you :)\xa0 We will meet MAJESTIC PARK ( in the far NW\xa0 Hualapai/gowen)-<a href="http://www.lasvegasnevada.gov/TextOnly/Find/19179.htm"><a href="http://www.lasvegasnevada.gov/TextOnly/Find/19179.htm" class="linkified">http://www.lasvegasnevada.gov/TextOnly/Find/19179.htm</a></a>\xa0 ) @ 530am\xa0 or a bit sooner to watch the beautiful sunrise ( 554am). We will then have a bit of time to pass before\xa0riding \xa0to our breakfast destination at SUNSET BUFFET(<a href="https://sunsetstation.sclv.com/Dining/Feast-Buffet.aspx"><a href="https://sunsetstation.sclv.com/Dining/Feast-Buffet.aspx" class="linkified">https://sunsetstation.sclv.com/Dining/Feast-Buffet.aspx</a></a>\xa0\xa0 )\xa0 by 8am price wcard $9.99\xa0 :)\xa0 .\xa0\xa0Once we leave MAJESTIC Park we will then take the fun/fast hill ride down\xa0 Cheyenne\xa0to FORT APACHE then turn right an head SOUTH (not to be riding into the morning sun/also to kill a little time before the buffet opens) then when we approach sunset that is where we will turn left.\xa0 This will be a must do for the members who have never seen the great views from the park and those who haven\'t explored that side of town yet REMEMBER: by scooter or by car no Meetup too far!!!!\xa0 SCOOT SAFE!!!!</p>'
    events_list_event_7.local_start = dateutil.parser.parse("2015-08-09T05:30:00")
    events_list_event_7.local_end = dateutil.parser.parse("2015-08-09T05:30:00")
    events_list_event_7.utc_offset = -25200L
    events_list_event_7.is_applicable = False
    events_list_event_7 = importer.save_or_locate(events_list_event_7)

    events_list_event_7.hashtags.add(events_list_hashtag_1)

    events_list_event_8 = Event()
    events_list_event_8.name = u'Make a PhoneGap App - Presentation and Workshop'
    events_list_event_8.event_url = u'http://www.meetup.com/Bangalore-Whitefield-PhoneGap-Meetup/events/224117603/'
    events_list_event_8.group = events_list_group_2
    events_list_event_8.meetupID = u'224117603'
    events_list_event_8.description = u'<p><img src="http://photos1.meetupstatic.com/photos/event/9/f/4/a/600_440320778.jpeg" /></p> <p>Do you have an idea for an app? Know basic HTML, JavaScript and CSS? Then you can attend this presentation + hands-on workshop session to build your first Android or iOS app.\xa0</p> <p><br/>This is what we\'re going to cover in this meetup:</p> <p><b>## (Presentation) Introduction</b></p> <p>- What is PhoneGap?</p> <p>- History</p> <p>- How does it work?</p> <p>- Native vs. Hybrid</p> <p>- Architecture overview</p> <p>- App structure</p> <p>- Debugging</p> <p>- Testing</p> <p>- Problems and concerns</p> <p>- Alternatives\xa0</p> <p>- Summary</p> <p><br/><b>## (Workshop) Installing PhoneGap</b></p> <p>- Introduction</p> <p>- Install package manager</p> <p>- Install nodejs</p> <p>- Install and configure SDKs</p> <p>- Install PhoneGap and simulators</p> <p><br/><b>## (Workshop) Creating your first app</b></p> <p>- Introduction</p> <p>- Create your first app</p> <p>- Configure platforms</p> <p>- Configure plugins</p> <p>- Build the app</p> <p>- Deploy to simulator and actual device</p> <p>- Walkthrough</p> <p>\n\n\n<b>Prerequisites</b></p> <p>- You should have a basic understanding of HTML, JavaScript and CSS</p> <p>- Laptop and mobile phone for the hands-on workshops.\xa0</p> <p>- Laptop can be either Windows, Linux or Mac.\xa0</p> <p>- For making iOS apps, you need a developer account (which costs USD 99)</p> <p>\n\n\n<b>Cost</b></p> <p>A nominal cost of Rs. 500 per participant, to cover the cost of the premise charges and effort to organise the training material. <i>Only if you feel it was worth it, at the end of the meetup</i>.\xa0</p>'
    events_list_event_8.local_start = dateutil.parser.parse("2015-08-09T12:00:00")
    events_list_event_8.local_end = dateutil.parser.parse("2015-08-09T17:00:00")
    events_list_event_8.utc_offset = 19800L
    events_list_event_8.is_applicable = True
    events_list_event_8 = importer.save_or_locate(events_list_event_8)

    events_list_event_8.hashtags.add(events_list_hashtag_1)

    events_list_event_9 = Event()
    events_list_event_9.name = u'Work on homework in advance; Algorithms: Design and Analysis Week 2'
    events_list_event_9.event_url = u'http://www.meetup.com/StudyGroups/events/224225303/'
    events_list_event_9.group = events_list_group_72
    events_list_event_9.meetupID = u'224225303'
    events_list_event_9.description = u'<p>We had a great discussion on August 2 (week 1). Instead of talking about answers to the homework, we discussed the key ideas in the lectures, problem sets, and programming questions.</p> <p>Let\'s continue to meet for 5 more weeks.</p> <p>Algorithm is the foundation of hacking skill. Work on homework in advance. Come to discuss homework:<br/><a href="https://class.coursera.org/algo-008/wiki/Syllabus" class="linkified">https://class.coursera.org/algo-008/wiki/Syllabus</a></p>'
    events_list_event_9.local_start = dateutil.parser.parse("2015-08-09T13:00:00")
    events_list_event_9.local_end = dateutil.parser.parse("2015-08-09T15:00:00")
    events_list_event_9.utc_offset = -25200L
    events_list_event_9.is_applicable = True
    events_list_event_9 = importer.save_or_locate(events_list_event_9)

    events_list_event_9.hashtags.add(events_list_hashtag_1)

    events_list_event_10 = Event()
    events_list_event_10.name = u'Realtime Advanced Analytics: Spark Streaming+Kafka, MLlib/GraphX, SQL/DataFrames'
    events_list_event_10.event_url = u'http://www.meetup.com/Advanced-Apache-Spark-Meetup/events/223910462/'
    events_list_event_10.group = events_list_group_11
    events_list_event_10.meetupID = u'223910462'
    events_list_event_10.description = u'<p>[Replay for the Peninsula/South Bay]</p> <p>We\'ll present a real-world, open source, advanced analytics and machine learning pipeline using all "15" Open Source technologies listed below.</p> <p><br/>This Meetup is based on my recent "Top-5" Hadoop Summit/Data Science talk called "Spark After Dark". Spark After Dark is a mock online dating site that uses Spark, Spark SQL, DataFrames, MLlib, GraphX, Cassandra, and ElasticSearch - among many other technologies listed below - to generate quality, real-time dating recommendations for its users.</p> <p>Here are the Spark After Dark slides: <a href="http://www.slideshare.net/cfregly/spark-after-dark-real-time-advanced-analytics-and-machine-learning-with-spark" class="linkified">http://www.slideshare.net/cfregly/spark-after-dark-real-time-advanced-analytics-and-machine-learning-with-spark</a></p> <p>All code - and the entire pipeline runtime - will be dockerized and made publicly available on Github and the Docker Hub Registry.</p> <p>Technologies to be demo\'d:<br/>1) Apache Zeppelin and Spark-Notebook (notebook-based development)\xa0</p> <p>2) Apache Spark SQL/DataFrames (Ad hoc Data Analysis and ETL)\xa0</p> <p>3) Apache Spark Streaming + Apache Kafka (Real-time Collection of Live Data from Interactive Demo)\xa0</p> <p>4) Spark Streaming + Real-time Machine Learning (K-Means Clustering, Log/Lin Regression)\xa0</p> <p>5) Apache Spark MLlib + GraphX (Generate personalized and non-personalized recommendations using various algorithms and feature engineering techniques including one hot encoding)\xa0</p> <p>6) MLlib + PMML Integration (Open Standard Markup Language for Predictive Models)\xa0</p> <p>7) Zeppelin + Python-based scikit-learn Machine Learning \xa0+ Advanced Visualizations with matplotlib and ggplot</p> <p>8) Spark R (Distributed R algorithmns)\xa0</p> <p><br/>9) Apache Spark JDBC/ODBC Thrift Server (Beeline and Tableau Analytics Explorer Integration)\xa0</p> <p>10) Tachyon (Off-heap storage)\xa0</p> <p>11) Spark + Cassandra</p> <p>12) Spark + ElasticSearch (Distributed Search Engine)\xa0</p> <p>13) Logstash (Log Agent + Collection)\xa0</p> <p>14) Kibana (ElasticSearch-based Analytics Explorer UI)\xa0</p> <p>15) HDFS + Parquet (Columnar Storage Format, Tight Compression, Lightning Fast Columnar Aggregations)\xa0</p> <p>\n\n\nReminder that we\'ve Docker-ized *everything* for you to take home.</p> <p><br/>Here\'s the Github Repo and Docker Hub Registry links:</p> <p>1) <a href="https://github.com/fluxcapacitor"><a href="https://github.com/fluxcapacitor" class="linkified">https://github.com/fluxcapacitor</a></a></p> <p>2)\xa0<a href="https://registry.hub.docker.com/repos/fluxcapacitor/"><a href="https://registry.hub.docker.com/repos/fluxcapacitor/" class="linkified">https://registry.hub.docker.com/repos/fluxcapacitor/</a></a></p> <p>Feel free to clone and contribute! \xa0Every contributor will be made a committer.</p> <p>\n\n\nBonus: \xa0Free 30-day Trial @\xa0&lt;a&gt;www.databricks.com&lt;/a&gt;</p> <p>Databricks Cloud Notebook-based Development and Cluster Management.</p> <p>Thanks, Databricks!\xa0</p> <p>\n\n\nSee everyone soon!</p>'
    events_list_event_10.local_start = dateutil.parser.parse("2015-08-10T18:30:00")
    events_list_event_10.local_end = dateutil.parser.parse("2015-08-10T21:00:00")
    events_list_event_10.utc_offset = -25200L
    events_list_event_10.is_applicable = True
    events_list_event_10 = importer.save_or_locate(events_list_event_10)

    events_list_event_10.hashtags.add(events_list_hashtag_1)

    events_list_event_11 = Event()
    events_list_event_11.name = u'Start your week with Marketing Mondays'
    events_list_event_11.event_url = u'http://www.meetup.com/2-NetworkTogetherApacheJunction-GoldCanyon/events/224454403/'
    events_list_event_11.group = events_list_group_79
    events_list_event_11.meetupID = u'qclnflytlbnb'
    events_list_event_11.description = u'<p>Get to know one another and build relationships of trust. Commerce for all will follow. You get to join 12 chapters of networking without worrying about any exclusion rules. Come join us at 8:30AM for a great breakfast at a reasonable price on Marketing Mondays at the Mirage Sports Grill!</p> <p>\n\nThere will be plenty of opportunity for us to get to know you and what you are good at so that we can promote you.</p> <p>We will do announcements, shout outs for referrals, 30 second commercials and workshops or special presentations.</p> <p>\n\nGreat food at a reasonable price at this meeting!</p> <p>\n\n\n\n\n\n\n\n\n\n\xa0</p>'
    events_list_event_11.local_start = dateutil.parser.parse("2015-08-10T08:30:00")
    events_list_event_11.local_end = dateutil.parser.parse("2015-08-10T09:30:00")
    events_list_event_11.utc_offset = -25200L
    events_list_event_11.is_applicable = False
    events_list_event_11 = importer.save_or_locate(events_list_event_11)

    events_list_event_11.hashtags.add(events_list_hashtag_1)

    events_list_event_12 = Event()
    events_list_event_12.name = u'Cassandra Financial Services Use Cases'
    events_list_event_12.event_url = u'http://www.meetup.com/Sydney-Cassandra-Users/events/223463715/'
    events_list_event_12.group = events_list_group_4
    events_list_event_12.meetupID = u'vfxzglytlbzb'
    events_list_event_12.description = u'<p>We\'ve had to bring this months meetup a week forward from the usual 3rd Wednesday in the month schedule. \xa0My apologises for the late change of date.</p> <p><br/>This month we will hear from Amy McNee (VP, \xa0Customer Operations, Datastax US) along with Matt Stump (Chief Architect, Datastax US) who are both in Sydney next week to discuss the following topic:</p> <p><b>Cassandra Financial Services Use Cases</b></p> <p>A discussion of production financial services use cases utilising Cassandra. What are they, why Cassandra, how to do them, and who\'s been successful. <img src="http://photos3.meetupstatic.com/photos/event/9/4/7/b/600_440618011.jpeg" /></p> <p>For regular meetup attendees, please make note of the new start time for the meetups going forward. \xa0Instead of the 7pm start, we\'ve moved the meetup to start at 6pm. \xa0Hopefully this fits in with most people, so as not to make a late evening for everyone.</p> <p><br/>Look forward to seeing you next week.</p> <p>Regards</p> <p>Tim Steele</p> <p>Datastax Australia</p> <p>\n\n\n<b>Hosts</b></p> <p><br/>DataStax and RoZetta Technology.</p> <p><b>Address</b></p> <p>Level 4/55 Harrington Street, The Rocks, 2000</p> <p><b>Agenda</b></p> <p>6:00 - Pizza &amp; Drinks</p> <p>6:15 - Presentation &amp; discussion</p>'
    events_list_event_12.local_start = dateutil.parser.parse("2015-08-11T18:00:00")
    events_list_event_12.local_end = dateutil.parser.parse("2015-08-11T18:00:00")
    events_list_event_12.utc_offset = 36000L
    events_list_event_12.is_applicable = True
    events_list_event_12 = importer.save_or_locate(events_list_event_12)

    events_list_event_12.hashtags.add(events_list_hashtag_1)

    events_list_event_13 = Event()
    events_list_event_13.name = u'A Cloud Foundry Framework for Apache Mesos'
    events_list_event_13.event_url = u'http://www.meetup.com/Boston-Area-Cloud-Foundry-Meetup/events/224306788/'
    events_list_event_13.group = events_list_group_5
    events_list_event_13.meetupID = u'224306788'
    events_list_event_13.description = u'<p>Speakers: Idit Levine, CTO of Cloud Management Division at EMC &amp; Luke Woydziak, Engineering Director of Cloud Management at EMC</p> <p><br/>Cloud Foundry is a popular Platform as a Service open source project. Supported by a fast growing community, Cloud Foundry is being adopted by many Fortune 500 companies that are keen to deliver CI &amp; CD to their developers. To leverage the rich functionality of Cloud Foundry, we modified Diego (Cloud Foundry cluster manger) to use Mesos as a resource manger.</p> <p>In the meetup we will share the motivation for that project, discuss implementation details, show a demo, and review how Cloud Foundry could complement the existing Mesos frameworks. \xa0</p>'
    events_list_event_13.local_start = dateutil.parser.parse("2015-08-11T18:00:00")
    events_list_event_13.local_end = dateutil.parser.parse("2015-08-11T18:00:00")
    events_list_event_13.utc_offset = -14400L
    events_list_event_13.is_applicable = True
    events_list_event_13 = importer.save_or_locate(events_list_event_13)

    events_list_event_13.hashtags.add(events_list_hashtag_1)

    events_list_event_14 = Event()
    events_list_event_14.name = u'Michael Drob: Solr & Cloudera'
    events_list_event_14.event_url = u'http://www.meetup.com/Houston-Hadoop-Meetup-Group/events/223231943/'
    events_list_event_14.group = events_list_group_6
    events_list_event_14.meetupID = u'223231943'
    events_list_event_14.description = u'<p><b>Topic: </b>Mike will introduce Apache Solr and highlight some of the use cases for search and the features that it can offer. After the audience reaches a comfortable understanding of Search, he will then discuss various integration points with the Apache Hadoop ecosystem including scalable Indexing, Queries, and Security.</p> <p>\n\n<b>Bio: </b>Mike has been immersed in Big Data for over 5 years, previously with the US Government and now with Cloudera. He works on Apache Solr, a world-class search engine built on top of Apache Lucene. He is also a hobbyist contributor to several other open source projects including Apache Curator, Apache NiFi (Incubating), JUnit, JLine, and JCommander. When not coding, he likes to mentor middle school students in robotics, go running along the bayous with his wife and dog, and to tend his vegetable garden.</p>'
    events_list_event_14.local_start = dateutil.parser.parse("2015-08-11T18:00:00")
    events_list_event_14.local_end = dateutil.parser.parse("2015-08-11T18:00:00")
    events_list_event_14.utc_offset = -18000L
    events_list_event_14.is_applicable = True
    events_list_event_14 = importer.save_or_locate(events_list_event_14)

    events_list_event_14.hashtags.add(events_list_hashtag_1)

    events_list_event_15 = Event()
    events_list_event_15.name = u"Learn about IBM Bluemix's Cloud Data Services"
    events_list_event_15.event_url = u'http://www.meetup.com/Austin-PaaS-Cloud-and-Bluemix-meetup/events/224456741/'
    events_list_event_15.group = events_list_group_7
    events_list_event_15.meetupID = u'224456741'
    events_list_event_15.description = u"<p>Learn about the Cloud Data Services on Bluemix:</p> <p>\u2022\xa0Cloudant - JSON, NoSQL DB</p> <p>\u2022\xa0dashDB -\xa0cloud data warehouse with integrated analytics</p> <p>\u2022\xa0BigInsights on Cloud - IBM's enhanced Hadoop platform</p> <p>\u2022\xa0DB2 on Cloud - Industrial strength Relational DBMS in the cloud</p> <p>\u2022\xa0DataWorks - Find, shape, enrich, curate, catalog and expose data confidently</p> <p>\u2022\xa0IBM Analytics for Apache Spark -\xa0managed Spark environment on-demand</p> <p>\u2022 plus some new offerings now on Bluemix via IBM's acquisition of Compose!</p>"
    events_list_event_15.local_start = dateutil.parser.parse("2015-08-11T18:00:00")
    events_list_event_15.local_end = dateutil.parser.parse("2015-08-11T20:00:00")
    events_list_event_15.utc_offset = -18000L
    events_list_event_15.is_applicable = True
    events_list_event_15 = importer.save_or_locate(events_list_event_15)

    events_list_event_15.hashtags.add(events_list_hashtag_1)

    events_list_event_16 = Event()
    events_list_event_16.name = u'OCJavaScript&friends Simulsquad\u2122 Coworking/training+Social on your topics'
    events_list_event_16.event_url = u'http://www.meetup.com/OCJavaScript/events/223274455/'
    events_list_event_16.group = events_list_group_8
    events_list_event_16.meetupID = u'jkknjlytlbpb'
    events_list_event_16.description = u'<p><a href="http://www.meetup.com/OCJavaScript/photos/25970905/">&lt;/a&gt;</p> <p>&lt;a href="http://www.meetup.com/OCJavaScript/photos/25970905/"&gt;</a></p> <p><a href="http://www.meetup.com/OCJavaScript/photos/25970905/">&lt;/a&gt;</p> <p>&lt;a href="http://www.meetup.com/OCJavaScript/photos/25970905/"&gt;<img src="http://photos1.meetupstatic.com/photos/event/2/c/1/6/600_435131286.jpeg" /></a></p> <p><a href="http://1.jothere.com/NRHRK5">\u2022\xa0</a>\u2018Please ASAP RSVP YES &amp; ATTEND SOME! As we work very hard to see you\'ve every reason to...\u2019<br/><a href="http://1.JotHere.com/NJ4TE9">\u2022\u2022\xa0</a>\u2018<b>All who attend pretty much always </b><b><i>have a great time &amp; get stuff done!</i></b>\u2019<br/><a href="http://1.JotHere.com/NRHSS5">\u2022\u2022\xa0</a>\u2018<b>These events are designed for attending all <i>or part</i>.</b>\xa0If attending part, just where possible:\xa0still ASAP RSVP YES plus let us know when roughly you\'ll be arriving &amp; leaving and your reasoning.\u2019<br/><a href="http://1.JotHere.com/NLHG9M">\u2022\u2022 </a>\u2018<b>Attendance is typically much higher than shown</b>\xa0on the average event posting as every happening has multiple postings announcing it as <b><i>this is a joint event series between multiple local groups which works quite well.</i></b>\u2019<br/><a href="http://1.JotHere.com/NMTNFO">\u2022\u2022\xa0</a>\u2018 \u2018As a regular attendee who always brings my laptop, <i><b>I\'m pleasantly surprised by how much work I regularly get done at these routine-fun Simulsquad\u2122 meetings</b>... often more than I would get done at home!</i>\u2019 says\xa0<a href="http://www.meetup.com/OCJavaScript/members/26563032/">Lucy</a> on\xa02015.04.14.\u2019<br/><a href="http://1.JotHere.com/NLOSXA">\u2022\u2022\xa0</a>\u2018<b>not-yet-members welcome!</b>\xa0<i>Please still attend this (and/or our other in-person events) and let event hosts know you\'re not yet a member,</i> then while you\'re attending we\'ll also work our darnedest to get you approved as a member!\u2019<br/><a href="http://1.JotHere.com/NLY4T6">\u2022\u2022\xa0</a>\u2018<b>Fun venues: Most every happening is at a <i>different &amp; changing</i> good ethnic restaurant or fun picnic adventure!</b> ...and<br/>\xa0<i>all higher-rated</i> (as <a href="http://en.wikipedia.org/wiki/Yelp">Yelp</a> 3.5 stars or above),<br/>\xa0<i>all affordable routinely</i> (as no more than \u2018$$\u2019 on Yelp),<br/>\xa0<i>all within a 4 mile radius</i> of the event host(s) (including so they can easily host plus easily share, discover, &amp; appreciate their neighborhood), and<br/>\xa0<i>all made suitable by us for you</i> to <b>do at least 4 excellent hours of <i><a href="http://en.wikipedia.org/wiki/Coworking">coworking</a>\xad/training on your laptop/tablet</i> plus <a href="http://www.lifehack.org/articles/communication/how-not-to-suck-at-socializing-dos-donts.html"><i>socializing</i></a>\xad and have a great meal!</b><br/>For every happening, a day or so before it, event hosts select its special venue &amp; matching end-time then update it and email their pick to <i>all who have RSVPed YES to it</i> or attended our previous one.\u2019<br/><a href="http://1.JotHere.com/NLOUBK">\u2022\u2022\xa0</a>\u2018<b>All levels of experience &amp; skill welcome!</b>\u2019</p> <p><a href="http://1.JotHere.com/NLQR5C">\u2022</a>\xa0\u201c<b>Want this with/at some other place(s), times, or even activities?</b> Simply <i>comment here</i> with the places &amp; times &amp; activities &amp; frequency you can commit to attending, and also if you could be willing to host that (and we\'re here to help you, and at least these activities are very easy to host); then we\'ll gather feedback and let you know when we schedule that, too!\u201d</p> <p><a href="http://1.jothere.com/NO9CLB">\u2022\xa0</a>\u2018<b>To help ensure seriousness, a small fee is charged to attend.</b> Official helpers exempted. If you\'re paying the fee, it also includes some fast 4G wifi Internet for your laptop &amp; devices, with more available, in case you didn\'t bring any or enough.\xa0<a href="http://www.meetup.com/OCJavaScript/messages/boards/thread/48074802/40/?SEE.POINT=NNZP1P#[masked]">Details</a>.\'</p> <p><a href="http://1.jothere.com/NELDZP">\u2022\xa0</a><b>THE EVENT SERIES\' CENTRAL NOTES...<br/></b><a href="http://1.jothere.com/NLS6HY">\u2022\u2022\xa0</a>\xa0<b><a href="http://www.meetup.com/OCJavaScript/messages/boards/thread/48074802?SEE.POINT=NDVBGQ">for our group</a>\xa0+\xa0<a href="http://www.meetup.com/OCJavaScript/messages/boards/thread/48074802?SEE.POINT=NDVBGQ">for the core group</a></b><br/><a href="http://1.JotHere.com/NLS6G8">\u2022\u2022\xa0</a><b>for every happening:</b><br/><a href="http://www.meetup.com/OCJavaScript/messages/boards/thread/48074802?SEE.POINT=NEL74Z#[masked]">[masked]WedEvery2</a>,<br/><a href="http://www.meetup.com/OCJavaScript/messages/boards/thread/48074802?SEE.POINT=NEL74Z#[masked]">[masked]WedEvery2</a>,<br/>:\n<a href="http://www.meetup.com/OCJavaScript/messages/boards/thread/48074802/30/?SEE.POINT=NMT922#[masked]">[masked]TueEvery2</a> (<a href="http://www.meetup.com/OCJavaScript/messages/boards/thread/48074802/30/?SEE.POINT=NMT9D3#[masked]">includes\xa0Cinco de Mayo\xa0party!</a>),<br/><a href="http://www.meetup.com/OCJavaScript/messages/boards/thread/48074802/40?SEE.POINT=NMTIB7#[masked]">[masked]TueEvery2</a>,<br/><a href="http://www.meetup.com/OCJavaScript/messages/boards/thread/48074802/40?SEE.POINT=NMTIO1#[masked]">[masked]TueEvery2</a>,<br/><a href="http://www.meetup.com/OCJavaScript/messages/boards/thread/48074802/40?SEE.POINT=NQ0HL5#[masked]">[masked]TueEvery2</a>,<br/><a href="http://www.meetup.com/OCJavaScript/messages/boards/thread/48074802/50?SEE.POINT=NQ0JK5#[masked]">[masked]TueEvery2</a>,<br/><a href="http://www.meetup.com/OCJavaScript/messages/boards/thread/48074802/50?SEE.POINT=NQ0M85#[masked]">[masked]TueEvery2</a>,<br/><b><a href="http://www.meetup.com/OCJavaScript/messages/boards/thread/48074802/50?SEE.POINT=NQ0JK5#[masked]">[masked]TueEvery2</a>,<br/><a href="http://www.meetup.com/OCJavaScript/messages/boards/thread/48074802/60?SEE.POINT=NQ0MW5#[masked]">[masked]TueEvery2</a>, </b><br/>and <b><i>more on <a href="http://www.meetup.com/OCJavaScript/?scroll=true">our upcoming event listings</a>!</i></b></p> <p><a href="http://1.JotHere.com/NLJ9OX">\u2022\xa0</a>\u2018<i>Space is limited.</i>\xa0<b>ASAP, RSVP YES and comment here!</b><br/>--<a href="http://1.jothere.com/4535?N46Ref=NLKP91#NEFI64">RSVP policy</a>\xa0and\xa0<a href="http://1.jothere.com/N235ZE?N46Ref=NLKP91">comment/posting guide</a>.\u2019</p> <p>\n\n<b>_________________________________________________________ </b><br/><b>This particular listing\'s history\xa0</b>in start-time order<a href="http://1.jothere.com/NCMS6M">:</a></p> <p><a href="http://1.jothere.com/NCMS76">\u2022\xa0</a><a href="http://www.meetup.com/OCJavaScript/messages/boards/thread/48325042/0/?SEE.POINT=NFB0V0#[masked]">Destiny authored this listing, including via assistants as needed, </a>except as otherwise correctly specified on it.</p> <p><a href="http://1.jothere.com/NCOIK7">\u2022\xa0</a>This listing is initially a Meetup auto-duplicate of the previous listing in its series where we\'ve then removed the non-essential previous history (so see the previous listings for the previous history) then made changes noted next:</p> <p>:</p> <p><a href="http://1.jothere.com/NS6SRM">\u2022\xa0</a>[masked]Tue0010~pst-\xa0<a href="http://www.meetup.com/OCJavaScript/members/169755982/">CoderBud</a>:\xa0{private RSVP Qs: all missing; set to new NS6SDO; -0029}\xa0</p>'
    events_list_event_16.local_start = dateutil.parser.parse("2015-08-11T18:15:00")
    events_list_event_16.local_end = dateutil.parser.parse("2015-08-12T00:15:00")
    events_list_event_16.utc_offset = -25200L
    events_list_event_16.is_applicable = True
    events_list_event_16 = importer.save_or_locate(events_list_event_16)

    events_list_event_16.hashtags.add(events_list_hashtag_1)

    events_list_event_17 = Event()
    events_list_event_17.name = u'Container Infrastructure'
    events_list_event_17.event_url = u'http://www.meetup.com/Contain/events/223782347/'
    events_list_event_17.group = events_list_group_12
    events_list_event_17.meetupID = u'223782347'
    events_list_event_17.description = u'<p><b>1830: </b>Drinks and Finger Food</p> <p><br/><b>1900: </b>Welcome and Updates</p> <p><b>1910: </b>Panel Introductions and short presentations</p> <p><b>"Microsoft &lt;3 Linux Containers"<br/></b>Boris Devouge;\xa0Director\xa0Open Source Strategy,\xa0Microsoft</p> <p><b>"A Short History of Docker in the Red Hat World"<br/></b>Alex Drahon; EMEA Cloud Architect, RedHat</p> <p><b>"What\'s RKT and where is it going"<br/></b>Iago L\xf3pez; Senior Developer, CoreOS/Endocode</p> <p><b>1945: </b>Panel discussion on <b>\'Container Infrastructure\'</b> featuring all speakers</p> <p>Moderated by @ric_harvey</p> <p><b>2040: </b><a href="http://www.markettaverns.co.uk/the_market_porter.html">The Market Porter</a>, 9 Stoney St, Borough Market</p>'
    events_list_event_17.local_start = dateutil.parser.parse("2015-08-11T18:30:00")
    events_list_event_17.local_end = dateutil.parser.parse("2015-08-11T18:30:00")
    events_list_event_17.utc_offset = 3600L
    events_list_event_17.is_applicable = True
    events_list_event_17 = importer.save_or_locate(events_list_event_17)

    events_list_event_17.hashtags.add(events_list_hashtag_1)

    events_list_event_18 = Event()
    events_list_event_18.name = u'Sports and Predictive Analytics'
    events_list_event_18.event_url = u'http://www.meetup.com/Data-Science-Phoenix/events/223781094/'
    events_list_event_18.group = events_list_group_9
    events_list_event_18.meetupID = u'pqlkglytlbpb'
    events_list_event_18.description = u'<p>We are very excited to have data scientist, author, sport analytics expert,\xa0<b><i>Eric Blabac</i></b>, give a talk at our August 2015 meeting.\xa0</p> <p><i>Please note our new meeting location at <a href="http://www.asu.edu/tour/tempe/usb.html">ASU\'s University Services Building</a> on Rural Rd.</i></p> <p><b>Abstract:</b></p> <p>When someone says sports and predictive analytics, two questions tend to immediately surface: Can you predict the outcome of a game? And can you predict the performance of a certain player? Partnerships between SAP, the NFL and the NHL has allowed us to answer yes to both of these questions in certain cases. Here we present predictive schemes for predicting player performance for the NFL and predicting the outcome of playoff games for the NHL.</p> <p><br/><b>Speaker Bio:</b></p> <p>Eric Blabac is a global analytics expert and evangelist in the SAP Data Science group within SAP. His background is based on advanced analytics with substantial experience in statistical modeling, predictive analytics, big data, data mining, forecasting, optimization and management consulting. Eric has worked across a variety of industries including retail, sports and entertainment. financial services, consumer product goods and healthcare. He is also the author of <i>The Encyclopedia of Baseball Statistics - From A to ZR</i>, a complete reference of all modern baseball statistics, what they really mean, how to calculate them and how to use them.\xa0Eric holds two Masters degrees (MS), Statistics and Applied Mathematics from Iowa State University, a Master\u2019s in Business Administration (MBA) from Grand Canyon University and a \xa0Bachelors (BSc) degree in Mathematics from Iowa State University.</p> <p><br/><b>Agenda:</b>\xa0</p> <p>\u2022\xa06:30-7:00pm: Sign-in &amp; network (with Food &amp; Beverages from Potbelly Sandwich Works sponsored by SAP)\xa0<br/>\u2022\xa07:00-7:15pm: Introduction &amp; announcements\xa0<br/>\u2022\xa07:15-8:15pm: Presentation by Eric Blabac\xa0<br/>\u2022 8:15-8:30pm: Q&amp;A &amp; wrap-up</p> <p><b>Sponsor:</b>\xa0</p> <p>Speaker, food and beverages for this event sponsored by John Barton from SAP. John is Database Specialist, SAP Platform and Analytics Architect for the HANA Solution Foundations Team.</p> <p><b>Parking Options:</b>\xa0</p> <p><img src="http://photos2.meetupstatic.com/photos/event/e/8/0/d/600_440279405.jpeg" /></p> <p>\n\n\n- Free covered parking! Address is\xa0<a href="https://www.google.com/maps?q=1551+S.+Rural+Rd.,+Tempe,+AZ">1551 S. Rural Rd., Tempe, AZ</a></p>'
    events_list_event_18.local_start = dateutil.parser.parse("2015-08-11T18:30:00")
    events_list_event_18.local_end = dateutil.parser.parse("2015-08-11T20:30:00")
    events_list_event_18.utc_offset = -25200L
    events_list_event_18.is_applicable = True
    events_list_event_18 = importer.save_or_locate(events_list_event_18)

    events_list_event_18.hashtags.add(events_list_hashtag_1)

    events_list_event_19 = Event()
    events_list_event_19.name = u'Tuesday, August 11th Meetup'
    events_list_event_19.event_url = u'http://www.meetup.com/corkdev-io/events/224256026/'
    events_list_event_19.group = events_list_group_10
    events_list_event_19.meetupID = u'224256026'
    events_list_event_19.description = u'<p><b>Cross-platform application development with QML and JavaScript<br/></b></p> <p>By <i>Antony Guinard</i></p> <p>This talk will introduce you to Qt Quick, a part of the Qt framework that allows us to build cross-platform mobile and desktop applications, using QML and JavaScript. Without writing a single line of C++ code, we can attain close to native application performance, while allowing developers and designers to work productively.</p> <p><br/><b>Distributed Computing and the Functional Programming model<br/></b></p> <p>By\xa0<i>Johannes\xa0Ahlmann</i> (<a href="http://codinguncut.com/">codinguncut.com</a>)</p> <p>Distributed Computing is becoming more and more prevalent with the rise of big data, multicore processors and scale-out architecture. This talk will give an introduction to core functional principles in the context of Distributed Computing and Apache Spark.</p> <p>\n\n\n\n<b>Thank you to this meetups sponsor <a href="https://www.teamwork.com/">teamwork.com</a>.</b></p> <p><img src="https://www.teamwork.com/downloads/presskit/Teamwork.com%20Logo%20Default.png" /></p>'
    events_list_event_19.local_start = dateutil.parser.parse("2015-08-11T18:30:00")
    events_list_event_19.local_end = dateutil.parser.parse("2015-08-11T18:30:00")
    events_list_event_19.utc_offset = 3600L
    events_list_event_19.is_applicable = True
    events_list_event_19 = importer.save_or_locate(events_list_event_19)

    events_list_event_19.hashtags.add(events_list_hashtag_1)

    events_list_event_20 = Event()
    events_list_event_20.name = u'Find a Group for a Kaggle Competition'
    events_list_event_20.event_url = u'http://www.meetup.com/StudyGroups/events/224386999/'
    events_list_event_20.group = events_list_group_72
    events_list_event_20.meetupID = u'224386999'
    events_list_event_20.description = u'<p>Kaggle competitions are a good way to improve (and showcase) your skills in predictive analytics. (RESCHEDULED TO)\xa0Next Tuesday, Kaggle\'s CEO, Anthony Goldbloom, is\xa0<a href="http://www.meetup.com/DS-ProD-SF/events/224334581/">talking about ramping up your data science skills</a> to the\xa0Data Science Professional Development San Francisco meetup group at Segment HQ. \xa0While \'doing\' may be a better learning opportunity than \'listening\', this talk might be a superb place to meet other people (in person) that are interested in participating in a Kaggle competition.</p> <p>Go hear Anthony talk about ramping up your data science skills (and Kaggle), and then find a group to work with on a Kaggle competition!!</p> <p>((Please only RSVP for one event))</p>'
    events_list_event_20.local_start = dateutil.parser.parse("2015-08-11T18:30:00")
    events_list_event_20.local_end = dateutil.parser.parse("2015-08-11T18:30:00")
    events_list_event_20.utc_offset = -25200L
    events_list_event_20.is_applicable = True
    events_list_event_20 = importer.save_or_locate(events_list_event_20)

    events_list_event_20.hashtags.add(events_list_hashtag_1)

    events_list_event_21 = Event()
    events_list_event_21.name = u'First Meetup!'
    events_list_event_21.event_url = u'http://www.meetup.com/East-Midlands-Front-End/events/223700811/'
    events_list_event_21.group = events_list_group_13
    events_list_event_21.meetupID = u'223700811'
    events_list_event_21.description = u"<p>Calling all Javascript, CSS, HTML, Ionic, Angularjs, Cordova/Phonegap devs!</p> <p>If you are excited about front-end design or development, are eager to learn or share your knowledge, looking for team mates, or get sometimes itchy to start coding, this meetup group may be a perfect fit for you.\xa0</p> <p>Not being able to find a similar group, I decided to create one! I was wondering if there are people interested in things like AngularJS, Ionic, Bootstrap, Cordova or any other web or mobile framework. Thumbs up and join the group to show if you're interested in starting something cool!\xa0</p> <p>Why to attend?</p> <p>Answer:</p> <p>1) To network</p> <p>2) To learn new skills</p> <p>3) To learn as to what others are doing</p> <p><br/>4) To find devs to help with your projects</p> <p>5) To build or to retain old connections</p> <p>If we have enough members, we will agree on a place and date. RSVP if you are curious to check it out.</p>"
    events_list_event_21.local_start = dateutil.parser.parse("2015-08-11T19:00:00")
    events_list_event_21.local_end = dateutil.parser.parse("2015-08-11T19:00:00")
    events_list_event_21.utc_offset = 3600L
    events_list_event_21.is_applicable = True
    events_list_event_21 = importer.save_or_locate(events_list_event_21)

    events_list_event_21.hashtags.add(events_list_hashtag_1)

    events_list_event_22 = Event()
    events_list_event_22.name = u'Breakfast Meeting - Business Leads Group'
    events_list_event_22.event_url = u'http://www.meetup.com/Business-Leads-Group/events/224451061/'
    events_list_event_22.group = events_list_group_53
    events_list_event_22.meetupID = u'dvlvzdytlbqb'
    events_list_event_22.description = u'<p>Business Leads Group is an independent professional business leads organization that meets at Mimi\'s in Summerlin Las Vegas\xa0Nevada. We build business success through personal referrals.</p> <p>Business Leads Group structure set the standard in the word-of-mouth referral industry. Members are known for their professionalism, dedication, and loyalty to one another.</p> <p>Business Leads Group meet weekly to exchange qualified leads, build solid business relationships, develop strong presentation skills and become proficient net-workers. Only one representative of any given profession is accepted, and members are chosen for their occupational expertise.</p> <p>Meeting Times: Every Wednesday (Summerlin)</p> <p><b>(7:00am Sharp - 8:30am)</b></p> <p><b>Cost:</b> $14.00 for an Excellent Breakfast\xa0<i><b>(Cash Only)</b></i></p> <p>Weekly Meeting located at Mimi\'s Cafe in Summerlin.</p> <p><b>Mimi\'s Cafe</b> <a href="http://maps.google.com/maps?oe=utf-8&amp;rls=org.mozilla:en-US:official&amp;client=firefox-a&amp;um=1&amp;ie=UTF-8&amp;cid=0,0,1953440017319352890&amp;fb=1&amp;split=1&amp;gl=us&amp;dq=1121+S.+Fort+Apache+Rd.,las+vegas,+nv&amp;daddr=1121+S+Fort+Apache+Rd,+Las+Vegas,+NV+89117&amp;geocode=11458847154916060578,36.158701,-115.291436&amp;sa=X&amp;oi=local_result&amp;resnum=1&amp;ct=directions-to">1121 S. Fort Apache Rd.</a> Las Vegas, NV 89117 <a href="http://maps.google.com/maps?oe=utf-8&amp;rls=org.mozilla:en-US:official&amp;client=firefox-a&amp;um=1&amp;ie=UTF-8&amp;cid=0,0,1953440017319352890&amp;fb=1&amp;split=1&amp;gl=us&amp;dq=1121+S.+Fort+Apache+Rd.,las+vegas,+nv&amp;daddr=1121+S+Fort+Apache+Rd,+Las+Vegas,+NV+89117&amp;geocode=11458847154916060578,36.158701,-115.291436&amp;sa=X&amp;oi=local_result&amp;resnum=1&amp;ct=directions-to">(Southwest Corner of Fort Apache and Rampart)</a> <b>Walkins Welcome!</b></p> <p>\xa0</p>'
    events_list_event_22.local_start = dateutil.parser.parse("2015-08-12T07:00:00")
    events_list_event_22.local_end = dateutil.parser.parse("2015-08-12T08:30:00")
    events_list_event_22.utc_offset = -25200L
    events_list_event_22.is_applicable = True
    events_list_event_22 = importer.save_or_locate(events_list_event_22)

    events_list_event_22.hashtags.add(events_list_hashtag_1)

    events_list_event_23 = Event()
    events_list_event_23.name = u'Meetup with Lin Nease - IoT Chief Technologist, HP'
    events_list_event_23.event_url = u'http://www.meetup.com/IGTCloud/events/224253296/'
    events_list_event_23.group = events_list_group_75
    events_list_event_23.meetupID = u'224253296'
    events_list_event_23.description = u"<p><b>\u05ea\u05d5\u05db\u05e0\u05d9\u05ea \u05d4\u05de\u05e4\u05d2\u05e9</b></p> <p>\n\n16:30 \u2013 16:00 \xa0 \xa0 \xa0 \u05db\u05d9\u05d1\u05d5\u05d3, \u05d4\u05ea\u05db\u05e0\u05e1\u05d5\u05ea</p> <p><br/>16:40 \u2013 16:30 \xa0 \xa0 \xa0 \u05d3\u05d1\u05e8\u05d9 \u05e4\u05ea\u05d9\u05d7\u05d4 \u2013 \u05d3\u05e8' \u05d0\u05de\u05d9\u05e8 \u05e2\u05e6\u05d9\u05d5\u05e0\u05d9, \u05de\u05e0\u05d4\u05dc \u05e7\u05d1\u05d5\u05e6\u05ea \u05d4\u05e4\u05e8\u05d9\u05e1\u05d9\u05d9\u05dc, HP \u05d9\u05e9\u05e8\u05d0\u05dc</p> <p><br/>18:00 \u2013 16:40 \xa0 \xa0 \xa0 <b>Lin Nease - IoT Chief Technologist, HP</b><br/>Partnering with HP on advanced IoT solutions\xa0</p> <p><br/>18:20 \u2013 18:00 \xa0 \xa0 \xa0\xa0<b>Oleg Logvinov Chair of IEEE P2413 WG, Chair of IEEE Internet Initiative, Director, Special \xa0Assignments, STMicroelectronics<br/></b>IEEE \xa0and the architectural framework for IoT</p>"
    events_list_event_23.local_start = dateutil.parser.parse("2015-08-12T16:00:00")
    events_list_event_23.local_end = dateutil.parser.parse("2015-08-12T16:00:00")
    events_list_event_23.utc_offset = 10800L
    events_list_event_23.is_applicable = True
    events_list_event_23 = importer.save_or_locate(events_list_event_23)

    events_list_event_23.hashtags.add(events_list_hashtag_1)

    events_list_event_24 = Event()
    events_list_event_24.name = u'"Connecting Professional Resources" Monthly Meeting'
    events_list_event_24.event_url = u'http://www.meetup.com/Senior-Healthcare-Professionals/events/223660443/'
    events_list_event_24.group = events_list_group_82
    events_list_event_24.meetupID = u'223660443'
    events_list_event_24.description = u'<p><b>"Connecting Professional Resources"</b>\u200b<b>\u200b Monthly Meeting\xa0</b></p> <p><br/><b>Brookdale Apache Junction</b>\xa0@ 2080 S. Ironwood Apache\xa0Junction, AZ 85219.\xa0</p> <p>Second Wednesday of the month at\xa011:30 am. Lunch Meeting\xa0</p> <p><b>COST $5.00\xa0</b></p> <p>RSVP to Elaine at \xa0&lt;a&gt;[masked]\xa0&lt;/a&gt;</p>'
    events_list_event_24.local_start = dateutil.parser.parse("2015-08-12T11:30:00")
    events_list_event_24.local_end = dateutil.parser.parse("2015-08-12T11:30:00")
    events_list_event_24.utc_offset = -25200L
    events_list_event_24.is_applicable = False
    events_list_event_24 = importer.save_or_locate(events_list_event_24)

    events_list_event_24.hashtags.add(events_list_hashtag_1)

    events_list_event_25 = Event()
    events_list_event_25.name = u'Introduction to using H2O for Data Science'
    events_list_event_25.event_url = u'http://www.meetup.com/H2Omeetup/events/223610740/'
    events_list_event_25.group = events_list_group_14
    events_list_event_25.meetupID = u'223610740'
    events_list_event_25.description = u'<p>Title: Introduction to using H2O for Data Science\xa0</p> <p>\n\nAbstract: Come learn about H2O, the best machine learning software since sliced bread (please insert something appropriate here).\xa0 We will show how to download, install, start, and use H2O version 3.\xa0 Then we will interact with H2O using some favorite data science tools: R and Python. Supervised and unsupervised learning examples will be used.\xa0 This is a hands on session; please bring your computers for the best experience.</p> <p>\n\nSpeaker: Hank Roark</p> <p>\n\nBio: Hank is a Data Scientist &amp; Hacker at H2O. Hank comes to H2O with a background turning data into products and system solutions and loves helping others find value in their data. He has a deep background in the the application domains of telematics, remote sensing, logistics, manufacturing, agriculture, and the Internet of Things. Before becoming passionate about machine intelligence, Hank managed international software teams and worked as IT consultant. In his spare time Hank likes to read non-fiction, make photographs, and compete in data science challenges. Hank has an SM from MIT in Engineering and Management and BS Physics from Georgia Tech.</p>'
    events_list_event_25.local_start = dateutil.parser.parse("2015-08-12T17:00:00")
    events_list_event_25.local_end = dateutil.parser.parse("2015-08-12T19:00:00")
    events_list_event_25.utc_offset = -25200L
    events_list_event_25.is_applicable = True
    events_list_event_25 = importer.save_or_locate(events_list_event_25)

    events_list_event_25.hashtags.add(events_list_hashtag_1)

    events_list_event_26 = Event()
    events_list_event_26.name = u'Summer Scala'
    events_list_event_26.event_url = u'http://www.meetup.com/atlanta-scala/events/223977006/'
    events_list_event_26.group = events_list_group_15
    events_list_event_26.meetupID = u'223977006'
    events_list_event_26.description = u'<p>Whats happening?</p> <p>\u2022 \xa0[530PM] Meet, greet, socialize. *Free* food and drink provided Memberclicks! \xa0[90 mins]\xa0</p> <p>\u2022 \xa0[700PM] Welcome &amp; Announcements\xa0</p> <p>\u2022 \xa0[705PM] Beginner presentation: Lance Gatlin @ IES "Thinking Monadically" [50min]</p> <p>\u2022 \xa0Break [5 minutes]\xa0</p> <p>\u2022 \xa0[800PM]\xa0Presentation: "Battle-tested Apache Spark: An Introduction" Eran Medan @ [55 mins]</p> <p>\u2022 \xa0Who\'s Hiring? [5 mins]\xa0</p>'
    events_list_event_26.local_start = dateutil.parser.parse("2015-08-12T17:30:00")
    events_list_event_26.local_end = dateutil.parser.parse("2015-08-12T21:00:00")
    events_list_event_26.utc_offset = -14400L
    events_list_event_26.is_applicable = True
    events_list_event_26 = importer.save_or_locate(events_list_event_26)

    events_list_event_26.hashtags.add(events_list_hashtag_1)

    events_list_event_27 = Event()
    events_list_event_27.name = u'Episode 39'
    events_list_event_27.event_url = u'http://www.meetup.com/scalasyd/events/224460821/'
    events_list_event_27.group = events_list_group_16
    events_list_event_27.meetupID = u'224460821'
    events_list_event_27.description = u'<p><b>Origami, monadic folds for Scala\xa0</b><br/>this talk presents Origami, a library providing "monadic folds" to accumulate values (like mean, standard deviation, min/max) on "streams" of values which can be coming from iterators, scalaz-stream processes or Akka data flows.<br/><i>Eric Torreborre</i></p> <p><b>i18n \xe0 la gettext</b></p> <p><br/>x.properties file (or its variants) is a popular way to add i18n to programs. But x.properties file is not very easy to manage. This lightning talk introduces an alternative, easier workflow, in the\xa0<a href="http://en.wikipedia.org/wiki/Gettext">GNU gettext</a>\xa0style.<br/><i>Ngoc Dao</i></p> <p><b>Scala for Business Automation - Solving Real Business Problems with Streams, POI and a dash of BDD</b><br/>Entry level talk on automating spreadsheet workflows with a bit of help from Streams, FlatSpecs and the Apache POI project. Plus a brief history lesson...<br/><i>Conor Svensson</i></p>'
    events_list_event_27.local_start = dateutil.parser.parse("2015-08-12T18:00:00")
    events_list_event_27.local_end = dateutil.parser.parse("2015-08-12T18:00:00")
    events_list_event_27.utc_offset = 36000L
    events_list_event_27.is_applicable = True
    events_list_event_27 = importer.save_or_locate(events_list_event_27)

    events_list_event_27.hashtags.add(events_list_hashtag_1)

    events_list_event_28 = Event()
    events_list_event_28.name = u'[Intermediate] DS In Practice'
    events_list_event_28.event_url = u'http://www.meetup.com/LearnDataScience/events/223162369/'
    events_list_event_28.group = events_list_group_63
    events_list_event_28.meetupID = u'zprbhlytlbhb'
    events_list_event_28.description = u"<p>As a group, we've decided to pursue Kaggle competitions as a way to practice data science skills.\xa0</p> <p>The competition for the upcoming week is still TBD. Same goes with location =]</p>"
    events_list_event_28.local_start = dateutil.parser.parse("2015-08-12T18:00:00")
    events_list_event_28.local_end = dateutil.parser.parse("2015-08-12T20:30:00")
    events_list_event_28.utc_offset = -25200L
    events_list_event_28.is_applicable = True
    events_list_event_28 = importer.save_or_locate(events_list_event_28)

    events_list_event_28.hashtags.add(events_list_hashtag_1)

    events_list_event_29 = Event()
    events_list_event_29.name = u'Dance The Night Away'
    events_list_event_29.event_url = u'http://www.meetup.com/Strangers-2-Friends/events/224116756/'
    events_list_event_29.group = events_list_group_38
    events_list_event_29.meetupID = u'224116756'
    events_list_event_29.description = u"<p>The Bawa Club Reggae Night</p> <p>\xa36</p> <p>Summer Reggae Party with live music from Sensational Jamaica Party Band 'Reggae Magic'</p> <p>Reggae Magic was formed by musicians whose lives have been dedicated to reggae music. They all grew up hearing and playing music at an early age. They have toured and worked with some of the world\u2019s greatest reggae artistes such as Denis Brown, Gregory Isaac, Alton Ellis, Frankie Paul, Pato Banton, Apache Indian, just to mention a few.</p> <p>They have come together to bring to the world some of the greatest reggae hits to be played on national radio worldwide. With their unique and energetic show they intend to keep you dancing and singing all night to your favourite reggae songs.<br/>Tickets on the door NO CHARGE FOR MEET UP....</p>"
    events_list_event_29.local_start = dateutil.parser.parse("2015-08-15T20:00:00")
    events_list_event_29.local_end = dateutil.parser.parse("2015-08-16T00:30:00")
    events_list_event_29.utc_offset = 3600L
    events_list_event_29.is_applicable = True
    events_list_event_29 = importer.save_or_locate(events_list_event_29)

    events_list_event_29.hashtags.add(events_list_hashtag_1)

    events_list_event_30 = Event()
    events_list_event_30.name = u'Big Data Scala By the Bay Conference: 20% off for group members, with Flink Talk'
    events_list_event_30.event_url = u'http://www.meetup.com/Bay-Area-Apache-Flink-Meetup/events/224213826/'
    events_list_event_30.group = events_list_group_73
    events_list_event_30.meetupID = u'224213826'
    events_list_event_30.description = u'<p><b>Big Data Scala by the Bay</b> is a new conference for data engineers, data scientists, developers, and data managers who use the Scala language to build big data pipelines.</p> <p><br/>The conference has one talk about Apache Flink: "<a href="http://scalabythebay2015.sched.org/event/2924807a263d424c939b33cdb7f3e6e8?iframe=no#">Why Apache Flink is the 4G of Big Data Analytics Frameworks?</a>" (<a href="http://sched.co/3WJr"><a href="http://sched.co/3WJr" class="linkified">http://sched.co/3WJr</a></a>) by Slim Baltagi.</p> <p>Members of the Apache Flink meetup group can use the\xa0code <b>FLINKBYTHEBAY20</b> for a 20% off discount on the whole conference, including Twitter FinagleCon (free for Scala By the Bay attendees) + Scala By the Bay + Complete Data Pipeline Training + Big Data Scala.</p> <p>\n\n\nNote that you can not sign up for the conference in this meetup group.</p>'
    events_list_event_30.local_start = dateutil.parser.parse("2015-08-16T19:00:00")
    events_list_event_30.local_end = dateutil.parser.parse("2015-08-18T22:00:00")
    events_list_event_30.utc_offset = -25200L
    events_list_event_30.is_applicable = True
    events_list_event_30 = importer.save_or_locate(events_list_event_30)

    events_list_event_30.hashtags.add(events_list_hashtag_1)

    events_list_event_31 = Event()
    events_list_event_31.name = u'Samsung Business Partners Reception'
    events_list_event_31.event_url = u'http://www.meetup.com/laphonegap/events/224278400/'
    events_list_event_31.group = events_list_group_32
    events_list_event_31.meetupID = u'224278400'
    events_list_event_31.description = u'<p><a href="https://cdn.evbuc.com/images/14330521/147658529735/1/original.jpg?timestamp=1438238361690" class="linkified">https://cdn.evbuc.com/images/14330521/147658529735/1/original.jpg?timestamp=1438238361690</a></p> <p>Join fellow developers and entrepreneurs to learn about the tools and resources available to Samsung Business Partners.\xa0</p> <p>Presenting \xa0will be\xa0William Vablais, North American Head of B2B Developer Relations. William will be speaking about Samsung\'s\xa0Enterprise Alliance Program (SEAP). SEAP provides free, quick and easy access to Samsung Knox, authentication, identification and experts so that you can create rich, secure applications.</p> <p>\n\n<img src="https://media.licdn.com/mpr/mpr/shrinknp_400_400/p/5/005/019/002/156be9b.jpg" /></p> <p><br/>William Vablais,<br/>Samsung Head of Business to Business<br/>Developer Relations</p> <p>\n\nJoin us in Los Angeles to hear what becoming a partner can do for your business. \xa0Please be sure to register on Eventbrite for this one as space is limited at this venue:</p> <p><a href="http://www.eventbrite.com/e/building-the-secure-enterprise-tickets-17773894196"><a href="http://www.eventbrite.com/e/building-the-secure-enterprise-tickets-17773894196" class="linkified">http://www.eventbrite.com/e/building-the-secure-enterprise-tickets-17773894196</a></a></p> <p>\n\n\n<img src="http://seap.samsung.com/web/html/front/images/en/partner/img_overview_seap.jpg" /></p> <p><br/>To learn more about the resources, tools, knowledge base, and receive the monthly SEAP newsletter. Join here: <a href="https://seap.samsung.com/developer" class="linkified">https://seap.samsung.com/developer</a></p>'
    events_list_event_31.local_start = dateutil.parser.parse("2015-08-12T18:30:00")
    events_list_event_31.local_end = dateutil.parser.parse("2015-08-12T18:30:00")
    events_list_event_31.utc_offset = -25200L
    events_list_event_31.is_applicable = True
    events_list_event_31 = importer.save_or_locate(events_list_event_31)

    events_list_event_31.hashtags.add(events_list_hashtag_1)

    events_list_event_32 = Event()
    events_list_event_32.name = u'BDW Meetup: Dimensional Modeling Still Matters!!!'
    events_list_event_32.event_url = u'http://www.meetup.com/Big-Data-Warehousing/events/224245340/'
    events_list_event_32.group = events_list_group_18
    events_list_event_32.meetupID = u'224245340'
    events_list_event_32.description = u"<p>Joe Caserta will go over the details inside the big data ecosystem and the Caserta Concepts Data Pyramid, which includes Data Ingestion, Data Lake/Data Science Workbench and the Big Data Warehouse. \xa0And then dive into the foundation of dimensional data modeling, which is as important as ever in the top tier of the Data Pyramid. \xa0Topics covered:</p> <p>The 3 grains of Fact Tables</p> <p>Modeling the different types of Slowly Changing Dimensions</p> <p>Advanced Modeling techniques like Ragged Hierarchies, Bridge Tables, etc.</p> <p>And touch on ETL Architecture.</p> <p>We'll also talk about ModelStorming, a technique used to quickly convert business requirements into an Event Matrix and Dimensional Data Model.</p> <p>This will be a jam-packed abbreviated version of 4 days of rigorous training of these techniques being taught in September by Joe Caserta (Co-Author, with Ralph Kimball, The Data Warehouse ETL Toolkit) and Lawrence Corr (Author, Agile Data Warehouse Design).</p>"
    events_list_event_32.local_start = dateutil.parser.parse("2015-08-12T18:30:00")
    events_list_event_32.local_end = dateutil.parser.parse("2015-08-12T20:30:00")
    events_list_event_32.utc_offset = -14400L
    events_list_event_32.is_applicable = True
    events_list_event_32 = importer.save_or_locate(events_list_event_32)

    events_list_event_32.hashtags.add(events_list_hashtag_1)

    events_list_event_33 = Event()
    events_list_event_33.name = u'CC Presents "The Spot Light Mingle Mixer Games & Red, Yellow & Green Party! 8/12'
    events_list_event_33.event_url = u'http://www.meetup.com/CosmopolitanConnections-dba-My-Vegas-Friends/events/224459324/'
    events_list_event_33.group = events_list_group_19
    events_list_event_33.meetupID = u'224459324'
    events_list_event_33.description = u'<p><img src="http://photos4.meetupstatic.com/photos/event/8/7/7/0/600_440614672.jpeg" /></p> <p><b>Yvette Auger\'s Cosmopolitan Connections Presents "The Spot Light Mingle Mixer Games &amp; Red, Yellow and Green Fashion &amp; Model Networking Event!" 8/12<br/></b> <b><br/>You\'re invited to our Free Networking Event on Wednesday, August[masked], from 7pm-9pm, at "Via Brasil Steakhouse," 1225 South Fort Apache Road, Las Vegas, NV 89117. (Nearest Cross Streets: W. Charleston/ S. Fort Apache Road.)<br/></b> <b><br/>Special Spot Light Mingle Mixer Games... Join us for a fun surprise game to mix and mingle during the event! (Optional.)<br/></b> <b><br/>Featuring ECCOCI at Boca Park Models &amp; Fashion &amp; Dunia Antunez\'s Fab Spa Parties featuring Customblends Cosmetics! Come &amp; Meet them &amp; have your photo taken with them by our event photographer Roger Bennett.<br/></b> <b><br/>Also Featuring Live Interviews on T.V Show "Surviving Sin City with Tiffani Neilson," on the night! Come &amp; Get Yourself &amp; your Business Interviewed for Free!<br/></b> <b><br/>Guests are encouraged to wear Red, Yellow or Green Clothing! (optional.)<br/></b> <b><br/>Free Admission &amp; Happy Hour Food &amp; Cocktails from 7pm-9pm at the Bar &amp; on the Patio.<br/></b> <b><br/>You are welcome to come &amp; network yourself &amp; your business. An evening of socializing, networking &amp; friendship for singles, couples &amp; business professionals.<br/></b> <b><br/>Prize for the person who brings the most friends on the night wins: $100 gift card for x2 people for Rodizio Dinner at Via Brasil Steakhouse!<br/></b> <b><br/>Business Card Prize Drawings x27: $50 ECCOCI Boca Park Gift Cards, A Free Dam Helicopter Ride of the Hoover Dam for x2 people ($118 Value!) $500 towards closing costs when buying or selling a home through Yvette &amp; Eric Auger, 1 Free Private Gaming Lesson (blackjack, craps, or roulette) from John Kawano Gaming ($100 Value,) Ninon Speaks- Media Image Coaching ($300 Value!) Free Consultation &amp; $250 off Credit Repair Services from Malik Lewis, Prime National Credit Repair, 1 week unlimited membership with 35 classes at Pole Fitness Studio ($79 value,) 10\xd715 inch photo from photoscenes .net ($30 Value,) Allwritey 45 minute free Pitch Polishing Session, ($100 Value!) $50 in free services at PB Contempo Spa, 1 Free 16oz Kitty or Kanine Koture, Free 5 Day Pass with fitness assessment, body fat analysis, nutrition consultation &amp; workout program by UFC GYM (Value $100!) 1 Free SEACRET\u2122 Skin Treatment - by Meri Howard ($350 Value!) Free 45 Min. Hot Stone Aromatherapy Massage at Violeta\'s Organic Spa ($90 Value!) 1 Free weekly session of Yalanda Baldon\'s CampCut Fitness Boot Camp ($10 Value!) Free Gene Wood Racing Experience VIP Ticket, Free Light Enzyme Facial Peel by Bonnie Fraser M.D- Ambrosia Medical Aesthetics, 1 free hour of social media consultation from SocialMedia AMP\'d ($120 value!) A Free complimentary financial plan from Marco Contreras, First Command Financial Services (Value up to $1,500!) Trapeze Las Vegas ~ 90 Min. Flying Trapeze Session for x2 people ($120 Vale!) Club Pilates Las Vegas ~ x2 Free Group Pilates Classes ($36 Value!) &amp; x2 Free Tickets to "The Speakeasy Swingers ~ Swanky Supper Club Soiree Show" ($20 Value!) Free Nutrition Consultation &amp; Analysis, 1 Free Month Elite Membership from Intermix Fitness ($416 value!) &amp; The Salt Room LV ~ Free 45 Min. Halotherapy Session ($35 Value!) &amp; Total Life Changes Health Plan Consult &amp; 1 week Supply of Detox/ Weight loss Tea ($30 Value!)<br/></b> <b><br/>We look forward to you joining us... Space is limited, so RSVP is required!<br/></b> <b><br/>Cheers Yvette Auger :)<br/>Owner ~ <a href="https://www.facebook.com/cosmopolitanconnections">Cosmopolitan Connections Inc.</a></b></p>'
    events_list_event_33.local_start = dateutil.parser.parse("2015-08-12T19:00:00")
    events_list_event_33.local_end = dateutil.parser.parse("2015-08-12T21:00:00")
    events_list_event_33.utc_offset = -25200L
    events_list_event_33.is_applicable = True
    events_list_event_33 = importer.save_or_locate(events_list_event_33)

    events_list_event_33.hashtags.add(events_list_hashtag_1)

    events_list_event_34 = Event()
    events_list_event_34.name = u'Polyglot comms - Protocol Buffers and Thrift and what they do for you'
    events_list_event_34.event_url = u'http://www.meetup.com/oc-u-py/events/224081660/'
    events_list_event_34.group = events_list_group_20
    events_list_event_34.meetupID = u'224081660'
    events_list_event_34.description = u'<p>We live in a world where it is more and more commonplace to work in a polyglot environment, communications between disparate services is commonplace, and the need to transmit messages between those services (likely written in various languages) is a must. \xa0</p> <p>Come learn about Google\'s <a href="https://github.com/google/protobuf">Protocol Buffers</a> and Facebook\'s (now Apache) <a href="https://thrift.apache.org/">Thrift</a> and why they are often times a better "wire-protocol" than the more ubiquitous formats of JSON and XML. \xa0Take a look at the pros and cons of each and see a demo of how they can be used to achieve data sanity in a multi-language environment.</p> <p><b>7:00 - 7:15 </b>- Introductions</p> <p><br/><b>7:15 - 7:30</b> - Announcements</p> <p><b>7:30 - 8:30</b>\xa0- Main talk</p> <p><b>8:30 - ?</b> - Lightning talks / general discussion</p> <p><i><b>I am looking for anyone interested in doing a 5-15 minute lightning talk\xa0</b></i></p>'
    events_list_event_34.local_start = dateutil.parser.parse("2015-08-12T19:00:00")
    events_list_event_34.local_end = dateutil.parser.parse("2015-08-12T19:00:00")
    events_list_event_34.utc_offset = -25200L
    events_list_event_34.is_applicable = True
    events_list_event_34 = importer.save_or_locate(events_list_event_34)

    events_list_event_34.hashtags.add(events_list_hashtag_1)

    events_list_event_35 = Event()
    events_list_event_35.name = u'Elastic Meetup at Netflix'
    events_list_event_35.event_url = u'http://www.meetup.com/Silicon-Valley-Elastic-Fantastics/events/224400110/'
    events_list_event_35.group = events_list_group_21
    events_list_event_35.meetupID = u'224400110'
    events_list_event_35.description = u"<p>Join us for this meetup at Netflix HQ! We'll have great presentations and conversation, and food and beverages will be provided. \xa0</p> <p><b>Event Agenda</b></p> <p>\u2022\xa06:30 pm - Registration\xa0</p> <p>\u2022\xa07:00 pm- Talks start\xa0</p> <p>\u2022\xa09:00 pm - Event concludes</p> <p>\n\n\n<b>Elasticsearch as a Service @ Netflix\xa0</b></p> <p>Netflix runs &gt;2000 ElasticSearch nodes across &gt;100 Elasticsearch clusters. The use cases vary from running it as a back-end to Logstash all the way to using it as a source of truth DB. In this talk Homajeet Cheema and Sagar Loke will discuss among other topics, how we deploy, maintain, upgrade and monitor our Elasticsearch fleet.\xa0</p> <p><b>Sagar Loke</b> is a Cloud Infrastructure Engineer at Netflix. Having spent many years in open source development, Sagar has extensive experience with Elasticsearch, MongoDB, and Cassandra among many others. Sagar is the author of Raigad - Netflix's open source project managing their Elasticsearch deployments, node discover, AWS Setup, Index Management, and system monitoring.\xa0</p> <p><b>Homajeet Cheema</b> is a Cloud Platform Engineer at Netflix and has been working with Elasticsearch for over a year. He spends his time building automation for Elasticsearch and Cassandra.</p>"
    events_list_event_35.local_start = dateutil.parser.parse("2015-08-12T19:00:00")
    events_list_event_35.local_end = dateutil.parser.parse("2015-08-12T21:00:00")
    events_list_event_35.utc_offset = -25200L
    events_list_event_35.is_applicable = True
    events_list_event_35 = importer.save_or_locate(events_list_event_35)

    events_list_event_35.hashtags.add(events_list_hashtag_1)

    events_list_event_36 = Event()
    events_list_event_36.name = u'Meteor Madness With Dr. Sky'
    events_list_event_36.event_url = u'http://www.meetup.com/EverydaySpacer-com6/events/224072545/'
    events_list_event_36.group = events_list_group_23
    events_list_event_36.meetupID = u'224072545'
    events_list_event_36.description = u'<p>Meteor Madness<br/>KMG<br/>Wednesday, August 12, 2015 from 8:00 PM to 10:30 PM (MST)<br/>Apache Junction, AZ</p> <p><img src="http://photos1.meetupstatic.com/photos/event/d/7/b/8/600_440035224.jpeg" /></p> <p>Join Dr. Sky (Steve Kates), a leading authority on the skies, at the BEST meteor shower of the year, the Perseids. What makes it so specisl is that we get to experience the Perseids, with NO MOON... creating the best dark sky conditions for viewing and the best place for viewing is in the lost Dutchman State Park at the foot of the beautiful Superstition Mountain. Event Activities</p> <p>8:00 - 9:30 pm - Enjoy food and beverage service, musical entertainment, prizes; cool off in the FREE beer grotto (for adult guests) and relax in the mister station<br/>9:30 - 10:30 pm - Star Talk with Dr. Sky, he\'ll be showing you how to best view the meteors<br/>10:30 - 11:00 - Intermission (grab your lawn chair)<br/>11:00 - dawn - Sit back and enjoy the show (this part is open to the public, see rules below)</p> <p>Admission Information &amp; Rules</p> <p>Adult admission includes park entrance (for one adult and one minor), event admission, free beer grotto. Must present ticket at ranger station.<br/>One minor accompanied by a ticketed adult is free, if more than one minor, must purchase a ticket.<br/>Food is an additional cost. Select local food vendors have been invited, so please enjoy some of the finest AZ cuisine around.<br/>20 prime tent spaces have been reserved for event guests. These spaces are right next to the event, premium parking for one vehicle is included. Four occupants per site. You must purchase the space from this web site, additional $15 required. First-come-first-serve on these sites, check-in is after 2:00 pm, check-out is noon. Must present ticket at ranger station.<br/>Additional RV and tent camping sites can be reserved from the park\'s reservation site: <a href="http://www.azstateparks.com">www.azstateparks.com</a><br/>No alcohol allowed inside the event perimeter (during event hours 8:00 pm - 10:00 pm). Must show proof of age for admittance to beer grotto.<br/>Meteor viewing is open to the public (10:30 - dawn) with park entrance fee/camping fee paid at the ranger station.<br/>Bring plenty of water, dress comfortably.<br/>In case of severe weather that forces cancellation of the event all together, $10 per admission ticket price will be reimbursed. We cannot reimburse for camp sites (see park rules).</p> <p><img src="http://photos1.meetupstatic.com/photos/event/d/7/d/0/600_440035248.jpeg" /></p> <p>Source(s):<br/><a href="http://drsky.com/" class="linkified">http://drsky.com/</a><br/><a href="http://drsky.com/769/" class="linkified">http://drsky.com/769/</a><br/>Reserve tickets here...<br/><a href="http://www.eventbrite.com/e/meteor-madness-tickets-17568759633" class="linkified">http://www.eventbrite.com/e/meteor-madness-tickets-17568759633</a></p>'
    events_list_event_36.local_start = dateutil.parser.parse("2015-08-12T20:00:00")
    events_list_event_36.local_end = dateutil.parser.parse("2015-08-12T22:30:00")
    events_list_event_36.utc_offset = -25200L
    events_list_event_36.is_applicable = True
    events_list_event_36 = importer.save_or_locate(events_list_event_36)

    events_list_event_36.hashtags.add(events_list_hashtag_1)

    events_list_event_37 = Event()
    events_list_event_37.name = u'DDV - Visualizing Big Data and Exploratory Data Analysis with R'
    events_list_event_37.event_url = u'http://www.meetup.com/daytondv/events/222477218/'
    events_list_event_37.group = events_list_group_24
    events_list_event_37.meetupID = u'jmwqglytlbrb'
    events_list_event_37.description = u'<p>Thanks to Sean McCarty and Steve Varner for volunteering to speak at our August event! Come enjoy great content from our speakers plus we\'ll have some more JetBrains licenses to raffle off!</p> <p>- <b><i>11:30am</i></b>: Pizza, Sponsors, and Announcements</p> <p>- <b><i>12:00pm</i></b>: <b>Exploring the\xa0Consumer Financial Protection Bureau Dataset with R</b>:\xa0Sean McCarty will present an exploratory data analysis of the Consumer Financial Protection Bureau Data.gov dataset. He performed this analysis using the R programming language and two R data visualization libraries. Sean is an image &amp; signal processing engineer that has experience implementing synthetic aperture radar image formation, signal processing, and real-time communication waveform generation solutions.</p> <p>- <b><i>12:30pm</i></b>: <b>Big Data Visualization:</b>\xa0Steve Varner will explore techniques for visualizing data stored on \u201cBig Data\u201d cluster computing environments. Steve will demonstrate how to work with massive data sets and gaining insights from both structured and unstructured data. Technologies used will include Apache Hadoop, Hive, Spark, and the Hadoop Distributed File System.</p> <p>- <b><i>1:00pm</i></b>: End</p> <p>The Dayton Data Visualization group will meet quarterly unless I get enough volunteers to make it happen more frequently. Please volunteer to share a topic with the group! What makes a good presentation topic for DDV? Here are some ideas:</p> <p>- <b>Case Studies</b> - Show us how you made a cool visualization or infographic</p> <p>- <b>Development Tips</b> - Show us how to use a cool new tool or framework</p> <p>- <b>Benchmarks</b> - Comparisons between tools or frameworks</p> <p>- <b>Data Mining</b> - Show us how you mine/retrieve data to use in your visualizations</p> <p>- <b>Optimization</b> - Show us how you optimize your visualizations for performance on the web and mobile devices</p> <p><i>Presentations are only twenty minutes long</i>. This is to lower the barrier of entry for new speakers and to make the talks less of a time commitment from the speakers (and audience). Keep them short, sweet, and specific.</p> <p>Thanks!</p> <p>Map to Applied Information Sciences:</p> <p><a href="https://www.google.com/maps/place/2681+Commons+Blvd,+Beavercreek,+OH+45431/@39.76859,-84.060064,19z/"><a href="https://www.google.com/maps/place/2681+Commons+Blvd,+Beavercreek,+OH+45431/@39.76859,-84.060064,19z/" class="linkified">https://www.google.com/maps/place/2681+Commons+Blvd,+Beavercreek,+OH+45431/@39.76859,-84.060064,19z/</a></a></p>'
    events_list_event_37.local_start = dateutil.parser.parse("2015-08-13T11:30:00")
    events_list_event_37.local_end = dateutil.parser.parse("2015-08-13T13:00:00")
    events_list_event_37.utc_offset = -14400L
    events_list_event_37.is_applicable = True
    events_list_event_37 = importer.save_or_locate(events_list_event_37)

    events_list_event_37.hashtags.add(events_list_hashtag_1)

    events_list_event_38 = Event()
    events_list_event_38.name = u'Salt River Tubing'
    events_list_event_38.event_url = u'http://www.meetup.com/GetOutGaySingleMen/events/223979202/'
    events_list_event_38.group = events_list_group_37
    events_list_event_38.meetupID = u'223979202'
    events_list_event_38.description = u'<p>Tubing down the Salt River is an Arizona tradition. Salt River Tubing (Salt River Recreation) is the company that most people use to tube on the Lower Salt River. Here\'s the short version: You park your vehicle, take a bus to a higher elevation of the river, rent inner tubes, and float down the river. Families, adventure groups, college students--all kinds of people from all walks of life join this floating party.</p> <p>The event fee, payable to Salt River Recreation, is $17 -- <b>cash only</b>.\xa0 This covers both tube rental and shuttle service.\xa0 We\'ll carpool from the Loop 101 &amp; Apache Blvd Park &amp; Ride at\xa02235 E Apache Blvd promptly at 8:30 AM.\xa0 We\'re doing an early float to avoid the heat and crowds as much as possible.\xa0 Float time is approximately 5 hours, depending on weather and water flow conditions.</p> <p><b>Be sure to review the <a href="http://www.saltrivertubing.com/">Salt River Tubing website</a>, especially the TIPS and FAQs, before the trip.</b></p> <p>If you become lost or are delayed the morning of the float trip, please contact TC at 623.521.3129.</p>'
    events_list_event_38.local_start = dateutil.parser.parse("2015-08-15T08:30:00")
    events_list_event_38.local_end = dateutil.parser.parse("2015-08-15T08:30:00")
    events_list_event_38.utc_offset = -25200L
    events_list_event_38.is_applicable = True
    events_list_event_38 = importer.save_or_locate(events_list_event_38)

    events_list_event_38.hashtags.add(events_list_hashtag_1)

    events_list_event_39 = Event()
    events_list_event_39.name = u'Summer Late session: Badminton 19:30!'
    events_list_event_39.event_url = u'http://www.meetup.com/stockholmsportypeople/events/222731545/'
    events_list_event_39.group = events_list_group_76
    events_list_event_39.meetupID = u'nqbwhlytlbqb'
    events_list_event_39.description = u'<p>Summer Sessions start!</p> <p>Badminton stadion shuts down at 9, so the former "Early session" at 19:30 becomes now the "Late session".</p> <p>I guess we will continue playing in the court 17 as the "really early session" does.</p> <p>So if you are on the waitlist and a multiple of 2, post up as\xa0It will be very easy to get additional courts.\xa0</p> <p>I think fees are 100kr for the hour. so 25 kr/ person</p>'
    events_list_event_39.local_start = dateutil.parser.parse("2015-08-12T19:30:00")
    events_list_event_39.local_end = dateutil.parser.parse("2015-08-12T20:30:00")
    events_list_event_39.utc_offset = 7200L
    events_list_event_39.is_applicable = False
    events_list_event_39 = importer.save_or_locate(events_list_event_39)

    events_list_event_39.hashtags.add(events_list_hashtag_1)

    events_list_event_40 = Event()
    events_list_event_40.name = u'New members meet and share our love of gardening!'
    events_list_event_40.event_url = u'http://www.meetup.com/East-Valley-Desert-Gardening/events/223987867/'
    events_list_event_40.group = events_list_group_80
    events_list_event_40.meetupID = u'wwbtclytlbtb'
    events_list_event_40.description = u'<p>New members meet the organizer at Starbuck\'s for a "meet and greet"; then we\'ll go up to Shady Way Nursery in Apache Jct. and look at plants!</p> <p>\xa0</p>'
    events_list_event_40.local_start = dateutil.parser.parse("2015-08-15T10:00:00")
    events_list_event_40.local_end = dateutil.parser.parse("2015-08-15T10:00:00")
    events_list_event_40.utc_offset = -25200L
    events_list_event_40.is_applicable = False
    events_list_event_40 = importer.save_or_locate(events_list_event_40)

    events_list_event_40.hashtags.add(events_list_hashtag_1)

    events_list_event_41 = Event()
    events_list_event_41.name = u'Enterprise Dataflow with Apache NiFi'
    events_list_event_41.event_url = u'http://www.meetup.com/Code-Brew/events/223935951/'
    events_list_event_41.group = events_list_group_25
    events_list_event_41.meetupID = u'223935951'
    events_list_event_41.description = u'<p>Beyond Messaging: Enterprise Dataflow with Apache NiFi</p> <p>- Agenda:</p> <p>5:30pm: \xa0Meet &amp; Greet</p> <p>6:00pm: \xa0Speaker</p> <p>7:00pm: \xa0Q &amp; A</p> <p>-Summary:</p> <p>If your organization is addressing the challenges and opportunities that Big Data presents then you\u2019re also an organization wrestling with dataflow. Dataflow is all about connecting systems. But in large organizations that are highly distributed these systems almost certainly speak different protocols, understand different data formats, and that nature of connectivity changes all the time. Messaging-based solutions are a popular answer these days but they don\u2019t address many of the fundamental challenges of enterprise dataflow.</p> <p>This talk will outline the broad range of capabilities needed in an end-to-end dataflow strategy and will put the value of messaging-based solutions in context. Systems throughout an enterprise evolve at different rates. Architectures are in a constant state of transformation. Ensuring compliance of distributed systems at scale requires new lineage tracking techniques. The idea of \u2018real-time\u2019 is more than just the delivery latency of a message. It is critical that organizations understand and have total control of their information supply chain.</p> <p>In late 2014 the National Security Agency (NSA) donated to the Apache Software Foundation the project now known as Apache NiFi (incubating). NiFi resulted from more than eight years of lessons learned and development designed to tackle the complex and broad challenges of dataflow at scale. This talk details those lessons learned and the key features of NiFi.</p> <p>- Bio:</p> <p>Joe Witt Onyara Inc. In 2006, Joe Witt created a dataflow framework that grew into a community and evolved over eight years into what became Apache NiFi (incubating). Following NiFi\u2019s open source release by the NSA in 2014, Joe has become an active committer and member of the Apache NiFi PPMC. Joe remains focused on solving global scale dataflow challenges and is a regular speaker on NiFi and data provenance.</p>'
    events_list_event_41.local_start = dateutil.parser.parse("2015-08-13T17:30:00")
    events_list_event_41.local_end = dateutil.parser.parse("2015-08-13T17:30:00")
    events_list_event_41.utc_offset = -14400L
    events_list_event_41.is_applicable = True
    events_list_event_41 = importer.save_or_locate(events_list_event_41)

    events_list_event_41.hashtags.add(events_list_hashtag_1)

    events_list_event_42 = Event()
    events_list_event_42.name = u'Happy Hour for Java Professionals'
    events_list_event_42.event_url = u'http://www.meetup.com/dc-java/events/223996187/'
    events_list_event_42.group = events_list_group_26
    events_list_event_42.meetupID = u'223996187'
    events_list_event_42.description = u"<p>Let's get together for an after-work happy hour and network! No formal program, just a fun time to chat and catch up with everyone!</p>"
    events_list_event_42.local_start = dateutil.parser.parse("2015-08-13T17:30:00")
    events_list_event_42.local_end = dateutil.parser.parse("2015-08-13T20:30:00")
    events_list_event_42.utc_offset = -14400L
    events_list_event_42.is_applicable = True
    events_list_event_42 = importer.save_or_locate(events_list_event_42)

    events_list_event_42.hashtags.add(events_list_hashtag_1)

    events_list_event_43 = Event()
    events_list_event_43.name = u'Monthly Meetup: Apache Cordova and Maker.js'
    events_list_event_43.event_url = u'http://www.meetup.com/seattlejs/events/220102652/'
    events_list_event_43.group = events_list_group_27
    events_list_event_43.meetupID = u'dczsvkytlbrb'
    events_list_event_43.description = u'<p>Hello hello! We\'re back from our CascadiaJS break with another amazing SeattleJS at Galvanize in Pioneer Square. Thank you Galvanize for hosting us this month and to DoubleDown Interact for the food!</p> <p>We have two great talks planned:</p> <p><img src="http://photos3.meetupstatic.com/photos/event/a/3/2/4/600_440321764.jpeg" /></p> <p><b>Topic 1<br/><i>Apache Cordova, Ionic, TACO, Jasmine, and more</i><br/>Ryan Salva</b></p> <p>First, Ryan Salva is a JavaScript developer, Apache Cordova committer, Visual Studio program manager, CrossFitter, sci-fi connoisseur and whiskey enthusiast. With over a decade of experience in software development, you could exhaust two Scrabble\u2122 bags accounting for all the acronyms and technologies Ryan has influenced, but the important thing to know is this: Ryan is a passionate storyteller with deep insight into market forces, technology, user experience and design. Today, he owns tooling for cross-platform app development at Microsoft. Tomorrow, the world.</p> <p>You\u2019ve got an app idea and a weekend to code it. This month, we\u2019ll learn what tools, tips and tricks you need to bootstrap an MVP in no time at all using client-side code (HTML, CSS and JS).</p> <p>We\u2019ll start by getting the dev environment configured. Then we\u2019ll move to the UI and talk about iterating quickly \u2013 first in a browser, then in an emulator and finally on a mobile device. Next, we\u2019ll tackle app logic and \u2013 GASP! \u2013 learn how to use unit testing to make rapid prototyping easy and breezy. Along the way, we\u2019ll talk about a variety of app frameworks and tools you can use in your mobile development workflow including Cordova, Ionic, TACO, Jasmine and more. You\u2019ll learn how to:</p> <p>\u2022\xa0Configure your dev environment for speed</p> <p>\u2022\xa0Iterate on your app\u2019s UI and logic quickly without breaking !@#$</p> <p>\u2022\xa0Make it look good \u2013 so good \u2013 on iOS and Android</p> <p>\u2022\xa0Debug your code on devices</p> <p>\n\n\n<img src="http://photos1.meetupstatic.com/photos/event/a/3/2/b/600_440321771.jpeg" /></p> <p><b>Topic 2<br/></b><i><b>Maker.js<br/></b></i><b>Dan Marshall</b></p> <p>Dan Marshall is a self-taught programmer who made his first drawing-creation software program at the age of 13. Thirty three years later he\u2019s back to doing that same thing. Dan has been enjoying coding in JavaScript since 1995 and currently works for Microsoft.</p> <p>Maker.js is a JavaScript library focused on the needs of people who create line drawings for 2D CNC machines. Learn how maker.js uses plain objects and an open recursive schema to represent a drawing which can be reused in others\u2019 drawings. See how Maker.js can eliminate current drawing toolchains and modernize the delivery and creation of customized drawings by leveraging HTML5, Node.js, and NPM.</p>'
    events_list_event_43.local_start = dateutil.parser.parse("2015-08-13T18:00:00")
    events_list_event_43.local_end = dateutil.parser.parse("2015-08-13T21:00:00")
    events_list_event_43.utc_offset = -25200L
    events_list_event_43.is_applicable = True
    events_list_event_43 = importer.save_or_locate(events_list_event_43)

    events_list_event_43.hashtags.add(events_list_hashtag_1)

    events_list_event_44 = Event()
    events_list_event_44.name = u'Study Session: Angular.JS & Ionic Framework With Troy Miles'
    events_list_event_44.event_url = u'http://www.meetup.com/javascriptla/events/223847981/'
    events_list_event_44.group = events_list_group_35
    events_list_event_44.meetupID = u'223847981'
    events_list_event_44.description = u'<p><img src="http://photos1.meetupstatic.com/photos/event/b/6/f/6/600_439606838.jpeg" /></p> <p>Cross Platform Mobile Apps with the <b>Ionic Framework </b><br/>What happens when you combine <b>Google\'s AngularJS,</b> the super cool J<b>avaScript MVC Framework with Apache Cordova</b>, the cross platform mobile framework using web technology? You get the Ionic Framework.\xa0</p> <p><br/>With Ionic you build mobile apps using the web technology you already know. Think the apps will be slow and clunky? Think again, <b>Ionic comes out of the box with well design CSS3 classes to make beautiful and fluid apps. </b>Using Cordova and jQuery Mobile already?\xa0</p> <p>Well, with Ionic <b>you will learn to love mobile development again. No more write-\xadonly spaghetti code</b>, Ionic makes it easy to create clean, testable, logical mobile apps. Need to support tablet and phone in the same app? Ionic has you covered. You can create one app which uses responsive design to change its look based on the device\'s screen dimensions.\xa0</p> <p>In this session, <b>we will build an app together to show many of Ionic\'s major features including CollectionRepeat, UI Widgets, Modals, and Slide Boxes. </b>We will also discuss development workflow, debugging, CSS customization, and tools.</p> <p><img src="http://photos3.meetupstatic.com/photos/event/b/7/2/e/600_439606894.jpeg" /></p> <p>\n\n\nA huge <b>THANK YOU</b> to Troy Miles for putting this together! Check out his blog here at: <a href="http://therockncoder.blogspot.com/"><a href="http://therockncoder.blogspot.com/" class="linkified">http://therockncoder.blogspot.com/</a></a>.\xa0 \xa0Twitter here: <a href="https://twitter.com/therockncoder"><a href="https://twitter.com/therockncoder" class="linkified">https://twitter.com/therockncoder</a></a>\xa0Github here:\xa0<a href="https://github.com/Rockncoder/"><a href="https://github.com/Rockncoder/" class="linkified">https://github.com/Rockncoder/</a>\xa0</a></p> <p>Troy also teaches Angular.JS, MEAN Stack at CodeDistrict. \xa0<a href="http://codedistrict.io/"><a href="http://codedistrict.io/" class="linkified">http://codedistrict.io/</a> </a>If you like his talk, definitely check out his class schedule. \xa0As usual, food and drink will be served. \xa0 Parking is around $3 in the Culver City Promenade Mall next door. \xa0 <b>Come hungry to eat and hungry to learn! </b>\xa0See you at the meetup!\xa0</p>'
    events_list_event_44.local_start = dateutil.parser.parse("2015-08-13T19:00:00")
    events_list_event_44.local_end = dateutil.parser.parse("2015-08-13T21:00:00")
    events_list_event_44.utc_offset = -25200L
    events_list_event_44.is_applicable = True
    events_list_event_44 = importer.save_or_locate(events_list_event_44)

    events_list_event_44.hashtags.add(events_list_hashtag_1)

    events_list_event_45 = Event()
    events_list_event_45.name = u'SWIHA HA Laughter Club'
    events_list_event_45.event_url = u'http://www.meetup.com/Phoenix-Laughter-Club/events/224178587/'
    events_list_event_45.group = events_list_group_74
    events_list_event_45.meetupID = u'qpdmscytlbsb'
    events_list_event_45.description = u'<p>SWIHA HA Laughter Club meets the 2nd &amp; 4th Friday of each month at the Southwest Institute of Healing Arts, 1100 E. Apache Blvd. in Tempe. The meeting is free and lasts approximately an hour. Join others for laughter exercises, laughter meditation and discussion of the Principles of Good-Hearted Living, which will help you make more room in your life for laughter.</p> <p>Hosted by Linda Scharf and Laurie Nathanson</p>'
    events_list_event_45.local_start = dateutil.parser.parse("2015-08-14T18:00:00")
    events_list_event_45.local_end = dateutil.parser.parse("2015-08-14T18:00:00")
    events_list_event_45.utc_offset = -25200L
    events_list_event_45.is_applicable = True
    events_list_event_45 = importer.save_or_locate(events_list_event_45)

    events_list_event_45.hashtags.add(events_list_hashtag_1)

    events_list_event_46 = Event()
    events_list_event_46.name = u'Data science y visualizaci\xf3n de informaci\xf3n: experiencias y demostraciones'
    events_list_event_46.event_url = u'http://www.meetup.com/TIDChile/events/224432806/'
    events_list_event_46.group = events_list_group_36
    events_list_event_46.meetupID = u'224432806'
    events_list_event_46.description = u'<p>Te invitamos a participar como expositor de este encuentro en un ambiente informal y ameno, donde habr\xe1 bebestibles y comestibles.<b> Para participar, adem\xe1s de confirmar tu asistencia en este meetup, debe inscribirte en este formulario </b><a href="http://goo.gl/forms/ETMHlUlnDw" class="linkified">http://goo.gl/forms/ETMHlUlnDw</a></p> <p>Como exigencia de este meetup, cada uno de los asistentes debe hacer una presentaci\xf3n de su experiencia aplicada o investigaci\xf3n en Data science y visualizaci\xf3n de informaci\xf3n.</p> <p><b>Formato de Participaci\xf3n </b><br/>- Cada expositor tendr\xe1 un tiempo m\xe1ximo de 6 minutos y 40 segundos para su presentaci\xf3n<br/>- <b>Deben inscribirse en el siguiente formulario</b> <a href="http://goo.gl/forms/ETMHlUlnDw" class="linkified">http://goo.gl/forms/ETMHlUlnDw</a><br/>- Enviar la ppt 24 horas antes del evento a [masked]</p> <p><b><i>Artistas Invitados</i></b></p> <p><b>Michele Trevisiol </b><br/>My background includes Data Mining/Web Mining, Multimedia and Information Retrieval, User Modeling, Recommendation Systems and Online Computational Advertising. I have worked with many different large data collections such as Flickr, Yahoo News, Yahoo query- and web-logs, and as well on Twitter data. I have also done various researches on credit card user\'s transactions, Sentiment Analysis with Yahoo and Yelp data, and geographic localization of images and videos. I am a Mac/Unix user, and my specialities are Apache Hadoop/PIG, Java, Python and R.</p> <p><b>Pablo Horacio Paladino </b><br/>Analista Desarrollador Senior con varios a\xf1os de experiencia en el \xe1rea de Sistemas y en diferentes proyectos y tecnolog\xedas. Capacidades de dise\xf1o Web y programaci\xf3n en varios lenguajes y plataformas. Entusiasta openSource, openData, openGov &amp; DataDrivenJournalism.<br/>Especialidades: Data Visualization - Mapas - AngularJS - JavaScript - PHP - MySQL - jQuery - HTML - CSS - Web scraping</p>'
    events_list_event_46.local_start = dateutil.parser.parse("2015-08-14T18:00:00")
    events_list_event_46.local_end = dateutil.parser.parse("2015-08-14T18:00:00")
    events_list_event_46.utc_offset = -14400L
    events_list_event_46.is_applicable = True
    events_list_event_46 = importer.save_or_locate(events_list_event_46)

    events_list_event_46.hashtags.add(events_list_hashtag_1)

    events_list_event_47 = Event()
    events_list_event_47.name = u'Thursday 13-August 2015 meetup, 6pm @ DU'
    events_list_event_47.event_url = u'http://www.meetup.com/RMOUG-Big-Data-SIG-Meetup/events/224088883/'
    events_list_event_47.group = events_list_group_28
    events_list_event_47.meetupID = u'224088883'
    events_list_event_47.description = u'<p><b>Address, building, and room:</b><br/>University Hall,<br/>Room 306<br/>University of Denver</p> <p><br/><b>Directions:</b></p> <p><br/>1. From E Warren Ave and S University Blvd intersection, walk towards roundabout towards University of Denver<br/>2. Make a right turn<br/>3. After passing the curve, you see a building to your right hand side. The name of the building is University Hall. We are meeting in Room # 306.</p> <p><b>NOTE:</b> Second building is \'University Hall\'.</p> <p><br/><b>Presentation Title:</b> Data Disruption and Innovation</p> <p><b>Presentation abstract:</b> Big Data holds much promise for innovative forward thinking, while at the same time disrupting some time-honored business practices and beliefs. Big Data changes how we interact with information and encourages a reimagining of how we think about our data and what we can do with it. This session takes a look forward toward best use cases for data-driven environments.</p> <p><b>Presenter name, Title and company:</b> John O\'Brien, Principal Advisor and CEO of\xa0Radiant Advisors</p> <p><b>Presenter Bio:</b> With over 25 years of experience delivering value through data warehousing and BI programs, John O\u2019Brien\u2019s unique perspective comes from the combination of his roles as a practitioner, consultant, and vendor in the BI industry. His knowledge in designing, building, and growing enterprise BI systems and teams brings real world insights to each role and phase within a BI program. Today, through Radiant Advisors John provides research and advisory services that guide companies in meeting the demands of next generation information management, architecture, and emerging technologies.<br/><b>Twitter:</b> @obrienjw</p> <p><br/><b>Agenda and timing for the meetup:</b><br/>6:00 - 6:30 - Food / Socializing<br/>6:30 - 6:45 - Announcements, Upcoming Events<br/>6:45 - 7:45 - Presentation: Data Warehousing in the Cloud \u2013 Speeding up the journey from data to insight<br/>7:45 - 8:00 - Open discussion / Socializing</p> <p><b>Free parking can be found at:</b><br/>Chamberlin Observatory<br/>2930 E Warren Ave<br/>Denver, CO 80210</p> <p>Free parking is available when you park near Chamberlin Observatory at one of the following intersections:</p> <p>1. E Illiff Ave and S Filmore St or<br/>2. S Filmore St and E Warren Ave or<br/>3. E Warren Ave and S Milwaukee St</p> <p>Paid Parking - DU Parking Map: <a href="https://www.parking.du.edu/documents/pdf/parking_map.pdf"><a href="https://www.parking.du.edu/documents/pdf/parking_map.pdf" class="linkified">https://www.parking.du.edu/documents/pdf/parking_map.pdf</a></a></p> <p>Please check the maps to make sure you won\'t be lost as University Hall does not have a specific address to post.</p> <p>Refreshments will be provided.</p>'
    events_list_event_47.local_start = dateutil.parser.parse("2015-08-13T18:00:00")
    events_list_event_47.local_end = dateutil.parser.parse("2015-08-13T20:00:00")
    events_list_event_47.utc_offset = -21600L
    events_list_event_47.is_applicable = True
    events_list_event_47 = importer.save_or_locate(events_list_event_47)

    events_list_event_47.hashtags.add(events_list_hashtag_1)

    events_list_event_48 = Event()
    events_list_event_48.name = u'Taste Beer and talk about Building a Streaming Data Plat w/Kafka and Scala'
    events_list_event_48.event_url = u'http://www.meetup.com/ATL-Tech-Tastings-Meetup/events/224379605/'
    events_list_event_48.group = events_list_group_29
    events_list_event_48.meetupID = u'224379605'
    events_list_event_48.description = u'<p>Hello fellow members! Our first meetup has been scheduled.<br/>We will meet at the Wrecking Bar Brew Pub to taste some of their best brews and learn about the brewing process from the brewmaster. They will be presenting 4-5 of their beloved brews and a cash bar will be open to purchase your favorites. <a href="http://www.wreckingbarbrewpub.com/" class="linkified">http://www.wreckingbarbrewpub.com/</a></p> <p>After the tastings, grab a beer and stick around for a 20 minute presentation by Sean Sawyer of MailChimp. Building on our open source leanings, he will talk about some the new technologies they are developing at MailChimp. His topic will be "Building a Streaming Data Platform with Apache Kafka and Scala". <a href="http://mailchimp.com/" class="linkified">http://mailchimp.com/</a></p>'
    events_list_event_48.local_start = dateutil.parser.parse("2015-08-13T18:00:00")
    events_list_event_48.local_end = dateutil.parser.parse("2015-08-13T18:00:00")
    events_list_event_48.utc_offset = -14400L
    events_list_event_48.is_applicable = True
    events_list_event_48 = importer.save_or_locate(events_list_event_48)

    events_list_event_48.hashtags.add(events_list_hashtag_1)

    events_list_event_49 = Event()
    events_list_event_49.name = u"Let's get together to talk about C*."
    events_list_event_49.event_url = u'http://www.meetup.com/Utah-Cassandra-Meetup/events/224032836/'
    events_list_event_49.group = events_list_group_30
    events_list_event_49.meetupID = u'224032836'
    events_list_event_49.description = u"<p>This is the first of what we hope to be many meetups on topics relating to Apache Cassandra. SaltStack have been gracious enough to host us. We'll have at least one speaker. But we'll also spend time discussing how this Meetup group can be most useful to the members. Contact me if you'd like to be a speaker at this or a future meetup.</p>"
    events_list_event_49.local_start = dateutil.parser.parse("2015-08-13T18:00:00")
    events_list_event_49.local_end = dateutil.parser.parse("2015-08-13T20:00:00")
    events_list_event_49.utc_offset = -21600L
    events_list_event_49.is_applicable = True
    events_list_event_49 = importer.save_or_locate(events_list_event_49)

    events_list_event_49.hashtags.add(events_list_hashtag_1)

    events_list_event_50 = Event()
    events_list_event_50.name = u'Think your software is fault tolerant? Prove it! - Christopher Batey'
    events_list_event_50.event_url = u'http://www.meetup.com/Londonjavacommunity/events/224097883/'
    events_list_event_50.group = events_list_group_31
    events_list_event_50.meetupID = u'224097883'
    events_list_event_50.description = u'<p>Think your service is fault tolerant? Well this talk is about proving it with protocol level test doubles.\xa0</p> <p>This talk will not be about in-process mocking, spying or stubbing. Instead, we will describe the benefits of using test doubles at the *protocol* level.\xa0</p> <p>When you are building a service, either monolithic or micro, you will have external dependences such as databases, message queues and/or HTTP services. The key idea is that in order to achieve fault-tolerance you must test failure scenarios across all your external dependencies and, crucially, network failures that may occur between your application and these other services.</p> <p>The talk will be structured as follows:</p> <p>- Concept and motivation: prepare to be convinced you should be testing this stuff!</p> <p>- Two specific examples:</p> <p>\xa0 1. Using Wiremock for HTTP dependencies with examples of how to test malformed responses, delays and invalid HTTP</p> <p>\xa0 2. Database: Stubbed Cassandra - a test double I built for Apache Cassandra to allow the simulation of faults typically only found in large multi data centre clusters.\xa0</p> <p>- How to simulate network faults using tools like saboteur, tc and iptables.\xa0</p> <p>My hope is by the end of this talk you\'ll want to go and build a test double for all your dependencies.\xa0</p> <p>I\'ll cover the above topics via slides and short demos.</p> <p><b>Who should attend:</b></p> <p>Any hands on technical person: developers, QAs, architects</p> <p><b>Bio:\xa0</b></p> <p><br/>Christopher Batey (@chbatey) is a Software Engineer by trade and is currently employed by DataStax as a Technical Advocate. Chris has also worked for Sky, where he helped build their online television platform, and IBM, where he helped develop a variety of messaging products.</p> <p>He spends a lot of his own time contributing back to the software community and is a active member of the London Java Community, London Software Craftsmanship Community and Cassandra London. Christopher has a particular interest in building effective automated tests for every scenario, including network failures, database faults and services returning junk. For that reason he built an open source test double for Apache Cassandra: Stubbed Cassandra. He also blogs regularly at: <a href="http://christopher-batey.blogspot.co.uk/"><a href="http://christopher-batey.blogspot.co.uk/" class="linkified">http://christopher-batey.blogspot.co.uk/</a></a>.\xa0</p> <p><b>Agenda: \xa0</b></p> <p><br/>18:15: Doors open</p> <p><br/>18:30: Main presentation (1 hour approx.)</p> <p><br/><b>Please Note:\xa0</b></p> <p><br/>Nearest tube: Barbican\xa0<br/>Nearest Coffee Shop: Sun Coffee Shop, 55-63 Goswell Road, London, EC1V 7EN for if you arrive early\xa0</p> <p><b>*Please note this is an LJC event. Skills Matter are hosting this event and are handling the attendance - it is essential that you confirm your place at this link:\xa0<a href="https://skillsmatter.com/meetups/7252-think-your-software-is-fault-tolerant-prove-it"><a href="https://skillsmatter.com/meetups/7252-think-your-software-is-fault-tolerant-prove-it" class="linkified">https://skillsmatter.com/meetups/7252-think-your-software-is-fault-tolerant-prove-it</a></a></b></p> <p><b>Event organised by the awesome folk at RecWorks - check out the blog here:\xa0<a href="http://recworks.co.uk/"><a href="http://blog.recworks.co.uk/" class="linkified">http://blog.recworks.co.uk/</a></a></b></p> <p><br/><b>Continue the conversation at our Slack Group:<a href="http://londonjavacommunity.slack.com/">londonjavacommunity.slack.com</a>\xa0- Sign up here if you\'re not a member:<a href="https://barrycranford.typeform.com/to/IIyQxd"><a href="https://barrycranford.typeform.com/to/IIyQxd" class="linkified">https://barrycranford.typeform.com/to/IIyQxd</a></a></b></p> <p><br/><img src="http://photos3.meetupstatic.com/photos/event/c/5/0/0/600_140270432.jpeg" /></p> <p>&lt;a href="https://skillsmatter.com/meetups/6710-domain-driven-design-nosql"&gt;&lt;/a&gt;</p>'
    events_list_event_50.local_start = dateutil.parser.parse("2015-08-13T18:15:00")
    events_list_event_50.local_end = dateutil.parser.parse("2015-08-13T18:15:00")
    events_list_event_50.utc_offset = 3600L
    events_list_event_50.is_applicable = True
    events_list_event_50 = importer.save_or_locate(events_list_event_50)

    events_list_event_50.hashtags.add(events_list_hashtag_1)

    events_list_event_51 = Event()
    events_list_event_51.name = u'Join us to enjoy messages from "Ephraim" Spirit Teachers channeled thru Fran M.'
    events_list_event_51.event_url = u'http://www.meetup.com/Mesa-Channeled-Messages-Meetup/events/223882102/'
    events_list_event_51.group = events_list_group_81
    events_list_event_51.meetupID = u'223882102'
    events_list_event_51.description = u'<p>Click on Pages to learn more!</p>'
    events_list_event_51.local_start = dateutil.parser.parse("2015-08-13T18:00:00")
    events_list_event_51.local_end = dateutil.parser.parse("2015-08-13T18:00:00")
    events_list_event_51.utc_offset = -25200L
    events_list_event_51.is_applicable = False
    events_list_event_51 = importer.save_or_locate(events_list_event_51)

    events_list_event_51.hashtags.add(events_list_hashtag_1)

    events_list_event_52 = Event()
    events_list_event_52.name = u'Spark Streaming'
    events_list_event_52.event_url = u'http://www.meetup.com/nj-datascience/events/222851584/'
    events_list_event_52.group = events_list_group_33
    events_list_event_52.meetupID = u'222851584'
    events_list_event_52.description = u'<p><b>Agenda</b></p> <p><b>Spark Streaming Concepts</b></p> <p><b>Spark Streaming architecture</b></p> <p><b>Spark Streaming API</b></p> <p><b>Demo / Workshop</b></p>'
    events_list_event_52.local_start = dateutil.parser.parse("2015-08-13T19:00:00")
    events_list_event_52.local_end = dateutil.parser.parse("2015-08-13T19:00:00")
    events_list_event_52.utc_offset = -14400L
    events_list_event_52.is_applicable = True
    events_list_event_52 = importer.save_or_locate(events_list_event_52)

    events_list_event_52.hashtags.add(events_list_hashtag_1)

    events_list_event_53 = Event()
    events_list_event_53.name = u'Spark at Akanoo'
    events_list_event_53.event_url = u'http://www.meetup.com/BDNSHH/events/223963763/'
    events_list_event_53.group = events_list_group_34
    events_list_event_53.meetupID = u'223963763'
    events_list_event_53.description = u'<p>Most (user-generated) data of the internet, but also genomics data, weather data, business or industrial process data etc. is sequential in nature. Finding frequent sequential patterns is key to many business and research applications. The PrefixSpan algorithm is an efficient way to calculate frequent patterns from huge sets of patterns. Akanoo has implemented the PrefixSpan algorithm in Scala using Apache Spark.</p> <p>Presented by:<br/>Frank Wolf<br/>Dr. Gundula Meckenh\xe4user</p>'
    events_list_event_53.local_start = dateutil.parser.parse("2015-08-13T19:00:00")
    events_list_event_53.local_end = dateutil.parser.parse("2015-08-13T19:00:00")
    events_list_event_53.utc_offset = 7200L
    events_list_event_53.is_applicable = True
    events_list_event_53 = importer.save_or_locate(events_list_event_53)

    events_list_event_53.hashtags.add(events_list_hashtag_1)

    events_list_event_54 = Event()
    events_list_event_54.name = u'Beta Test Apache Cassandra Certification'
    events_list_event_54.event_url = u'http://www.meetup.com/DataStax-Cassandra-South-Bay-Users/events/224269417/'
    events_list_event_54.group = events_list_group_39
    events_list_event_54.meetupID = u'224269417'
    events_list_event_54.description = u'<p><b>The meetup will be a bit different for this month. Please keep in mind it is not geared towards Apache Cassandra beginners or people interested in learning more, it is for individuals who feel like they are proficient with Apache Cassandra. If you are a beginner and or are just interested in learning more, join us for our free Cassandra Summit 2015 in September, you can find more details <a href="http://cassandrasummit-datastax.com/">here</a>.\xa0</b></p> <p>As most of you know at Cassandra Summit 2015 DataStax will be partnering with O\'Reilly Media to administer the first ever certification program for Apache Cassandra, with Administrator and Developer certification available. This is the very first time we are doing this, so we are taking every step to ensure it is done properly. One part of this is beta testing the actual certification test and this is where we\'d like to enlist your help to provide feedback on the beta; and in return you will get a voucher to take the certification test for free when it\'s generally available to the public in late September.</p> <p>For the beta test we are looking for Administrators and Developers who are proficient in Cassandra because we will not be offering training at this event, only the beta test. If you would like to prep in advance, we will be sending the materials needed two weeks prior to the event. If you have any questions or concerns, email Lina at [masked].</p> <p>Seats are limited so if you feel like you are proficient in Cassandra and would like to take part in the beta testing, you can rsvp <a href="https://www.eventbrite.com/e/beta-test-apache-cassandra-certification-tickets-17802115607">here</a>.</p> <p>*PLEASE NOTE: This is not the actual certification test, if you do well on the beta you do not get certified. You will have to take the actual certification test at a later date in order to get certified.</p> <p><b>Addtional Information:</b></p> <p>What to bring: Please bring yourself, along with a laptop. Nothing needs to be downloaded prior but you will need to bring a laptop.</p> <p>Parking: There is plenty of parking available in the parking structure behind the building as well as street parking.</p> <p>Duration: The event will be 2 hours long, 90 mins for the testing and 30 mins for you to provide feedback.</p> <p>Food and drink will be served.</p> <p>For more info on Cassandra Summit 2015 please go <a href="http://cassandrasummit-datastax.com/">here</a></p>'
    events_list_event_54.local_start = dateutil.parser.parse("2015-08-17T18:00:00")
    events_list_event_54.local_end = dateutil.parser.parse("2015-08-17T21:00:00")
    events_list_event_54.utc_offset = -25200L
    events_list_event_54.is_applicable = True
    events_list_event_54 = importer.save_or_locate(events_list_event_54)

    events_list_event_54.hashtags.add(events_list_hashtag_1)

    events_list_event_55 = Event()
    events_list_event_55.name = u'Deep Learning & Real World Experiences'
    events_list_event_55.event_url = u'http://www.meetup.com/Data-Science-Melbourne/events/221969060/'
    events_list_event_55.group = events_list_group_40
    events_list_event_55.meetupID = u'221969060'
    events_list_event_55.description = u'<p>Were back at Inspire9 for what promises to be another great evening...\xa0</p> <p><b>Schedule:</b></p> <p>6:00pm arrive and have pizza and beer\xa0<br/>6:25pm introductions\xa0<br/>6:35pm\xa0Zhen\'s talk<br/>7:20pm\xa0Q &amp; A for Zhen\xa0<br/>7:30pm 10 min break\xa0<br/>7:40pm\xa0Patrick\'s talk<br/>8:30pm\xa0Q &amp; A for Patrick<br/>9:00pm Continue debate @ Post Office Hotel on Bridge Road</p> <p>\n\n<b>Zhen He: Recent Advances in the Field of Deep Learning</b></p> <p>The area of neural networks has undergone revolutionary changes in the past 4 years.\xa0This has resulted in moving neural networks from the fringes of the machine learning community to center stage. Recently researchers have discovered effective ways of training neural networks that are 10 layers deep that contain billions of parameters. These deep neural networks have produced\xa0outstanding results in the area of image recognition, speech recognition, natural language processing, multi-modal learning, reinforcement learning, etc. For example in the area of image recognition the state-of-the-art deep learning system can achieve an error rate under 5%, which is more accurate than most humans can achieve.\xa0</p> <p>In this talk I will present some recent applications of deep learning to solve very interesting problems. I will explain how deep learning works in an easy and approachable manner. I will present programming tools for implementing deep learning solutions to solve machine learning problems. \xa0I will also present tips on how to train deep learning algorithms to achieve high accuracy.\xa0</p> <p><b>Zhen\'s Biography:</b></p> <p>Dr Zhen He is an Associate Professor in the department of computer science and computer engineering in La Trobe University. He received his undergraduate and PhD degrees in\xa0 the area of computer science from the Australian National University. His main research interest is in large scale machine learning. In particular he and his research team are exploring various ways of using the Apache Spark Big Data framework to scale out machine learning algorithms. A current focus is on scaling out deep learning algorithms using the Apache Spark framework.\xa0</p> <p>\n\n<b>Patrick Hall: Real World Machine Learning Experiences</b></p> <p>\n\nWe all know that\xa0Silicon Valley tech. firms are\xa0using machine learning, but\xa0what about the broader economy\xa0around the world? Are\xa0governments and companies in more traditional\xa0verticals\xa0like finance, healthcare, manufacturing, and oil\xa0production able to turn the ultra-hyped opportunities presented by\xa0machine learning into real-life value?\xa0In this talk, I will discuss my experiences with SAS customers in the U.S., Europe, Asia, and Australia as they\xa0seek to incorporate distributed computing, machine learning, and deep learning into their production data infrastructures. I will also point out some SAS resources for machine learning and deep learning, and how to integrate\xa0SAS\xa0with\xa0your favorite open-source packages. For a sneak peek, take a look here:</p> <p><a href="https://github.com/sassoftware/enlighten-apply"><a href="https://github.com/sassoftware/enlighten-apply" class="linkified">https://github.com/sassoftware/enlighten-apply</a></a><br/><a href="https://github.com/sassoftware/enlighten-deep"><a href="https://github.com/sassoftware/enlighten-integration" class="linkified">https://github.com/sassoftware/enlighten-integration</a></a><br/><a href="https://github.com/sassoftware/enlighten-deep"><a href="https://github.com/sassoftware/enlighten-deep" class="linkified">https://github.com/sassoftware/enlighten-deep</a></a></p> <p><b>Patrick\'s Biography:</b></p> <p>Patrick designs new data mining and machine learning technologies for SAS. He is a Cloudera certified data scientist and a certified SAS Enterprise Miner predictive modeler. Patrick is also a co-author of two recent patent applications regarding unsupervised learning. He studied computational chemistry at the University of Illinois before graduating from the Institute for Advanced Analytics at North Carolina State University</p>'
    events_list_event_55.local_start = dateutil.parser.parse("2015-08-17T18:00:00")
    events_list_event_55.local_end = dateutil.parser.parse("2015-08-17T18:00:00")
    events_list_event_55.utc_offset = 36000L
    events_list_event_55.is_applicable = True
    events_list_event_55 = importer.save_or_locate(events_list_event_55)

    events_list_event_55.hashtags.add(events_list_hashtag_1)

    events_list_event_56 = Event()
    events_list_event_56.name = u'Chef in anger!'
    events_list_event_56.event_url = u'http://www.meetup.com/Melbourne-Chef/events/224087484/'
    events_list_event_56.group = events_list_group_41
    events_list_event_56.meetupID = u'224087484'
    events_list_event_56.description = u'<p>Coming soon....\xa0</p>'
    events_list_event_56.local_start = dateutil.parser.parse("2015-08-17T18:00:00")
    events_list_event_56.local_end = dateutil.parser.parse("2015-08-17T18:00:00")
    events_list_event_56.utc_offset = 36000L
    events_list_event_56.is_applicable = True
    events_list_event_56 = importer.save_or_locate(events_list_event_56)

    events_list_event_56.hashtags.add(events_list_hashtag_1)

    events_list_event_57 = Event()
    events_list_event_57.name = u'Using CoreLocation at Scale'
    events_list_event_57.event_url = u'http://www.meetup.com/Skyway-Software-Symposium/events/224476924/'
    events_list_event_57.group = events_list_group_42
    events_list_event_57.meetupID = u'224476924'
    events_list_event_57.description = u'<p><i><b>Please bring your ID for entrance into Target Plaza Commons, this is a 21+ event.</b></i></p> <p>Core Location is one of the most important (and oldest!) frameworks in iOS, and over the years has seen many added capabilities from geofencing to background updates to iBeacons. You probably know the basics of how these work, but coordinating regions and beacon hardware across 1800 stores presents unique challenges few have ever faced. Come hear how the Target iOS App uses location features to help everything from welcoming guests at the parking lot to deals in the freezer section, and some of the more interesting challenges faced along the way.\xa0</p> <p><i>Food and Drink will be available starting at 6:00 PM, the presentation will start at 6:30 PM.</i></p>'
    events_list_event_57.local_start = dateutil.parser.parse("2015-08-17T18:00:00")
    events_list_event_57.local_end = dateutil.parser.parse("2015-08-17T21:00:00")
    events_list_event_57.utc_offset = -18000L
    events_list_event_57.is_applicable = True
    events_list_event_57 = importer.save_or_locate(events_list_event_57)

    events_list_event_57.hashtags.add(events_list_hashtag_1)

    events_list_event_58 = Event()
    events_list_event_58.name = u'Moar logs! Moar Linux!'
    events_list_event_58.event_url = u'http://www.meetup.com/Jozi-Linux-User-Group-JLUG/events/224395260/'
    events_list_event_58.group = events_list_group_43
    events_list_event_58.meetupID = u'224395260'
    events_list_event_58.description = u"<p>Come one come all! We have all the Linux you'll ever need!</p> <p>Meetup topics</p> <p>- Elkstack (Elastic Search, Log Stash, Kibana)</p> <p><br/>\xa0\xa0 Presented by Jurgens Du Toit</p> <p>- Network Namespaces</p> <p><br/>\xa0\xa0 Presented by Mark Clarke</p> <p>- Unconference session\xa0</p> <p>- Updates from committee members</p> <p><br/>\xa0\xa0\xa0 Bring all your Linux questions and get community help</p> <p>We are always on the hunt for speakers and venue hosts. Feel free to drop me a message and I will get back to you as soon as I can.</p>"
    events_list_event_58.local_start = dateutil.parser.parse("2015-08-17T19:00:00")
    events_list_event_58.local_end = dateutil.parser.parse("2015-08-17T19:00:00")
    events_list_event_58.utc_offset = 7200L
    events_list_event_58.is_applicable = True
    events_list_event_58 = importer.save_or_locate(events_list_event_58)

    events_list_event_58.hashtags.add(events_list_hashtag_1)

    events_list_event_59 = Event()
    events_list_event_59.name = u'Enterprise Integration Patterns'
    events_list_event_59.event_url = u'http://www.meetup.com/integration-stockholm/events/222660232/'
    events_list_event_59.group = events_list_group_44
    events_list_event_59.meetupID = u'222660232'
    events_list_event_59.description = u'<p>Welcome to the Enterprise Integration Patterns\xa0(EIP)\xa0seminar and workshop at R2M. Featured speaker is Bj\xf6rn Frantz\xe9n with many years of experience from the integration field.\xa0</p> <p>There are many pitfalls in enterprise integration and many books have been written about it. Enterprise Integration Patterns can be said to be a map over best-practices when it comes to enterprise integration. As with all patterns they are not meant to be perfect, nor should they be followed relentlessly without proper analysis. The seminar will focus on collaborative workshops where attendees will discuss and share experiences. To start the seminar there will be a short presentation on EIP and after the workshops there will be a demonstration on how to apply EIP with Apache Camel.</p> <p>Apache Camel is an open source integration framework that is based on the EIP patterns. Apache Camel is part of RedHat\'s strategic integration platform, RedHat Fuse, but can also be used stand alone.\xa0</p> <p>See these links for Enterprise Integration Patterns:</p> <p><a href="http://www.enterpriseintegrationpatterns.com/"><a href="http://www.enterpriseintegrationpatterns.com/" class="linkified">http://www.enterpriseintegrationpatterns.com/</a></a></p> <p><a href="http://camel.apache.org/enterprise-integration-patterns.html"><a href="http://camel.apache.org/enterprise-integration-patterns.html" class="linkified">http://camel.apache.org/enterprise-integration-patterns.html</a></a></p> <p>Recommended knowledge: System development, system architecture, integration development or integration architecture</p> <p>Looking forward to meet you at the event!</p> <p>Agenda:</p> <p>\xa0 * Welcome and Introduction to EIP</p> <p>\xa0 * EIP Overview</p> <p>\xa0 * Group Discussions on EIP</p> <p>\xa0 - Instructions</p> <p>\xa0 - Experiences and Best Practices</p> <p>\xa0 - Group Presentations with general discussion</p> <p>\xa0 * Apache Camel EIP demo</p> <p>\xa0 * Summary</p> <p>There will be lighter food and refreshments available.</p>'
    events_list_event_59.local_start = dateutil.parser.parse("2015-08-18T17:00:00")
    events_list_event_59.local_end = dateutil.parser.parse("2015-08-18T17:00:00")
    events_list_event_59.utc_offset = 7200L
    events_list_event_59.is_applicable = True
    events_list_event_59 = importer.save_or_locate(events_list_event_59)

    events_list_event_59.hashtags.add(events_list_hashtag_1)

    events_list_event_60 = Event()
    events_list_event_60.name = u'Interactively Search & Visualize Your Big Data and NLP for Lucene'
    events_list_event_60.event_url = u'http://www.meetup.com/Downtown-SF-Apache-Lucene-Solr-Meetup/events/223899054/'
    events_list_event_60.group = events_list_group_45
    events_list_event_60.meetupID = u'223899054'
    events_list_event_60.description = u"<p>Join us for the monthly San Francisco Solr Meetup, with the below talks from Cloudera's Romain Rigaux and Lucene/Solr Committer, Koji Sekiguchi. Food and drinks will be provided.</p> <p><i><b>Interactively Search and Visualize Your Big Data</b></i>, Presented by Romain Rigaux, Cloudera</p> <p>Open up your user base to the data! Contrary to programming and SQL, almost everybody knows how to search. This talk describes through an interactive demo based on open source Hue how users can graphically search their data in Hadoop. The underlying technical details of the application and its interaction with Apache Solr will be clarified.</p> <p>The session will detail how to get started with data indexing in just a few clicks as well as explore several data analysis scenarios with the latest Solr Analytics Facets and Spark Streaming. Through a Web browser, attendees will be shown how to explore and visualize data for quick answers. The search dashboard in Hue, with its draggable charts and dynamic interface, lets any non-technical user look for documents or patterns.</p> <p>Attendees of this talk will learn how to get started with interactive search visualization in their Solr cluster.</p> <p>Speaker: Romain is the Lead of Hue and an engineer at Cloudera. Before he worked on distributed systems at Yahoo! and Google and has been building Web apps since the early days.</p> <p><b><i>An Introduction to NLP4L: Natural Language Processing Tool for Apache Lucene</i></b>, Presented by Koji Sekiguchi, RONDHUIT</p> <p>NLP4L is a natural language processing tool for Apache Lucene written in Scala. The main objective of this OSS project is to use NLP technologies to improve Lucene users' search experience. The unique difference between NLP4L and other NLP tools is that NLP4L itself references Lucene index instead of raw text as its processing target. The session will describe how to use Scala to obtain word statistics and N-gram statistics from Lucene index and introduces various tools including the Hidden Markov model that are developed using these functions.</p> <p>Speaker: Koji Sekiguchi is a Lucene/Solr committer and PMC member. He enrolled in the Japan Advanced Institute of Science and Technology in 2012 to major in natural language processing and received a master's degree in information science in 2014. He is the founder of RONDHUIT, an Apache Lucene/Solr consulting/training service provider based in Japan.</p>"
    events_list_event_60.local_start = dateutil.parser.parse("2015-08-18T18:00:00")
    events_list_event_60.local_end = dateutil.parser.parse("2015-08-18T20:00:00")
    events_list_event_60.utc_offset = -25200L
    events_list_event_60.is_applicable = True
    events_list_event_60 = importer.save_or_locate(events_list_event_60)

    events_list_event_60.hashtags.add(events_list_hashtag_1)

    events_list_event_61 = Event()
    events_list_event_61.name = u'Spark Jeopardy at Zoomdata!'
    events_list_event_61.event_url = u'http://www.meetup.com/Washington-DC-Area-Spark-Interactive/events/223939521/'
    events_list_event_61.group = events_list_group_46
    events_list_event_61.meetupID = u'223939521'
    events_list_event_61.description = u'<p>Come out and join us for a fun filled evening of Spark Jeopardy at Zoomdata!\xa0 We\u2019ll divide up in groups to support and back Spark experts / Jeopardy contestants for a fun way to learn Spark.\xa0 Databricks has kindly helped craft questions and videos to make it interesting (thanks Denny!).\xa0 Join a team and get to meet some of the most progressive individuals working on Spark solutions today.\xa0 Surprise guest from Databricks also expected to pop in\u2026\xa0</p> <p>Winning team gets cool prizes!\xa0 We\u2019ll also do a raffle for a free ticket to Strata Hadoop NYC Sep 29-Oct 1. \xa0</p> <p>As you come in, you\u2019ll be assigned to one of the below teams led by a Spark expert:</p> <p><b>TEAM BAUD - Justin Langseth</b> is CEO of Zoomdata, developers of the fastest visual analytics for Big Data.\xa0 Zoomdata is Justin\'s 5th startup--he previously founded Strategy.com, Claraview, Clarabridge, and Augaroo. Justin is an expert in big data, business intelligence, text analytics, sentiment analytics, and real-time data processing.\xa0 He graduated from MIT with a degree in Management of Information Technology, and holds 14 patents. He is eagerly awaiting the singularity to increase his personal I/O rate which is currently frustratingly pegged at about 300 baud.</p> <p><b>TEAM MARVEL - Ted Malaska</b> is a Principal Solutions Architect with Cloudera.\xa0 He has spent the last four years working with Hadoop and supporting over 40 clients with their Big Data implementations, some with over 200 clusters.\xa0 He is the co-author of the O\u2019Reilly book "Hadoop Application Architecture" which features Apache Spark in three of the nine chapters.\xa0 He is also an active contributor to over nine Hadoop Ecosystem projects including two minor contributions to Spark.\xa0 At Cloudera, he has been very involved with multiple Spark applications for customers and he has gained experience with Spark, Spark-GraphX, and Spark Streaming.\xa0 Ted is also a Marvel Fan Boy and runner.\xa0</p> <p><b>TEAM NEURO - Jeremy Freeman</b> is a neuroscientist at the intersection of biology, computation, data science, and visualization. He wants to understand how the brain supports complex behavior, and how it might inform the design of intelligent systems. He\u2019s also passionate about open source and open science, contributing to major open source big data technologies, building platforms for collaborative data sharing and analysis, and advising scientists and developers across a range of fields.\xa0 Jeremy is an avid supporter of Spark and has presented in many Spark events.\xa0</p> <p>And serving as Alex Trebek:</p> <p><b>Andrew Psaltis</b> has a wealth of experience in software design, and in the construction of large-scale data-intensive systems. He is deeply entrenched in streaming systems and obsessed with delivering insight at the speed of thought. As the author of Streaming Data (<a href="http://manning.com/psaltis/" class="linkified">http://manning.com/psaltis/</a>) by Manning and an international speaker he spends most of his waking hours thinking about, writing about, and building streaming systems. He was the primary architect of Webtrends Streams -- the first scalable streaming architecture pushing real-time visitor and event-level digital intelligence into the marketing ecosystem. Andrew currently supports MetiStream as a Sr. Architect and Spark Trainer.\xa0 When he\'s not busy being busy, he\'s spending time with his lovely wife, two kids, coaching and watching as much Lacrosse as possible.</p> <p>\n\n\n================</p> <p>We\'re proud to partner w/ #StrataHadoop NYC Sep 29-Oct 1. Save 20% w/code UGDCSPARK <a href="http://oreil.ly/1KC2sCB"><a href="http://oreil.ly/1KC2sCB" class="linkified">http://oreil.ly/1KC2sCB</a></a></p> <p>\n\n\n&lt;a href="http://oreil.ly/1KC2sCB"&gt;&lt;/a&gt;</p>'
    events_list_event_61.local_start = dateutil.parser.parse("2015-08-18T18:00:00")
    events_list_event_61.local_end = dateutil.parser.parse("2015-08-18T21:00:00")
    events_list_event_61.utc_offset = -14400L
    events_list_event_61.is_applicable = True
    events_list_event_61 = importer.save_or_locate(events_list_event_61)

    events_list_event_61.hashtags.add(events_list_hashtag_1)

    events_list_event_62 = Event()
    events_list_event_62.name = u'Let\'s "Spark" a Conversation!!'
    events_list_event_62.event_url = u'http://www.meetup.com/Pepperdata-NYC/events/223819462/'
    events_list_event_62.group = events_list_group_22
    events_list_event_62.meetupID = u'223819462'
    events_list_event_62.description = u'<p>A learning session for users of Spark and other Big Data technologies!! \xa0The main format will be a panel discussion discussion with distinguished Spark experts - both providers and users. \xa0We will be talking about how to\xa0monitor Spark to get the best performance and to avoid issues. Learn how you can gain real-time insight into Spark jobs across CPU, RAM, I/O and network.</p> <p>This Meetup is sponsored by\xa0<a href="http://pepperdata.com">Pepperdata</a>, the leader in real-time performance optimization for Hadoop and Spark, and\xa0<a href="http://www.onx.com">OnX Enterprise Solutions</a>, a leading global provider of technology services and solutions.<b> \xa0FREE PIZZA, BEER, AND WINE will be provided :)</b></p> <p><br/>If you\'re using Spark now or just considering how/if to deploy it, you will have the chance to talk to others in the same situation and learn best practices from the experts!</p>'
    events_list_event_62.local_start = dateutil.parser.parse("2015-08-19T18:00:00")
    events_list_event_62.local_end = dateutil.parser.parse("2015-08-19T18:00:00")
    events_list_event_62.utc_offset = -14400L
    events_list_event_62.is_applicable = True
    events_list_event_62 = importer.save_or_locate(events_list_event_62)

    events_list_event_62.hashtags.add(events_list_hashtag_1)

    events_list_event_63 = Event()
    events_list_event_63.name = u'Prof. Andrew Ng "What\'s New in Deep Learning: Perspectives from Baidu Research"'
    events_list_event_63.event_url = u'http://www.meetup.com/SF-Big-Analytics/events/223612485/'
    events_list_event_63.group = events_list_group_61
    events_list_event_63.meetupID = u'223612485'
    events_list_event_63.description = u'<p>Refreshments: A light dinner will be served</p> <p>Agenda<br/>6:00-6:30 - Welcome and Dinner<br/>6:30-7:00 - Dr. Andrew Ng on current trends and topics in deep learning<br/>7:00-7:45 - Update on speech recognition and HPC systems research by Baidu<br/>Research team members<br/>7:45-8:00 - Q &amp; A</p>'
    events_list_event_63.local_start = dateutil.parser.parse("2015-08-19T18:00:00")
    events_list_event_63.local_end = dateutil.parser.parse("2015-08-19T20:00:00")
    events_list_event_63.utc_offset = -25200L
    events_list_event_63.is_applicable = True
    events_list_event_63 = importer.save_or_locate(events_list_event_63)

    events_list_event_63.hashtags.add(events_list_hashtag_1)

    events_list_event_64 = Event()
    events_list_event_64.name = u'[Advanced] Data Science Reading Group'
    events_list_event_64.event_url = u'http://www.meetup.com/LearnDataScience/events/223671877/'
    events_list_event_64.group = events_list_group_63
    events_list_event_64.meetupID = u'wdcshlytlbzb'
    events_list_event_64.description = u'<p>The next reading is "<b>Sparse autoencoder</b>"\xa0<a href="http://web.stanford.edu/class/cs294a/sparseAutoencoder.pdf"><a href="http://web.stanford.edu/class/cs294a/sparseAutoencoder.pdf" class="linkified">http://web.stanford.edu/class/cs294a/sparseAutoencoder.pdf</a></a></p> <p>We\'re not reading the whole thing. We\'re starting at section 3 on "Autoencoders and sparsity". (Which means the reading is a lot shorter than it actually looks.)</p> <p>\n\n\nPlease try to read it before the meetup. It\'s OK if you don\'t understand it all. The meetup is for questions and discussion.\xa0</p> <p><b>Schedule:</b></p> <p>\u2022 6:00PM Doors are open, feel free to mingle\xa0<br/>\u2022 6:30\xa0Reading Group starts<br/>\u2022 ~7:45 Off to a nearby restaurant for food, drinks, and breakout discussions\xa0</p> <p>\n\n\n\n----------\xa0</p> <p><b>What is the Data Science Reading Group about?:\xa0</b></p> <p>We will meet every other Wednesday of every month and present/discuss a topic of interest.</p>'
    events_list_event_64.local_start = dateutil.parser.parse("2015-08-19T18:00:00")
    events_list_event_64.local_end = dateutil.parser.parse("2015-08-19T20:00:00")
    events_list_event_64.utc_offset = -25200L
    events_list_event_64.is_applicable = True
    events_list_event_64 = importer.save_or_locate(events_list_event_64)

    events_list_event_64.hashtags.add(events_list_hashtag_1)

    events_list_event_65 = Event()
    events_list_event_65.name = u'[Intermediate] DS Practice With Kaggle Competitions'
    events_list_event_65.event_url = u'http://www.meetup.com/LearnDataScience/events/223316797/'
    events_list_event_65.group = events_list_group_63
    events_list_event_65.meetupID = u'zprbhlytlbzb'
    events_list_event_65.description = u"<p>As a group, we've decided to pursue Kaggle competitions as a way to practice data science skills.\xa0</p> <p>The competition for the upcoming week is still TBD. Same goes with location =]</p>"
    events_list_event_65.local_start = dateutil.parser.parse("2015-08-19T18:00:00")
    events_list_event_65.local_end = dateutil.parser.parse("2015-08-19T20:30:00")
    events_list_event_65.utc_offset = -25200L
    events_list_event_65.is_applicable = True
    events_list_event_65 = importer.save_or_locate(events_list_event_65)

    events_list_event_65.hashtags.add(events_list_hashtag_1)

    events_list_event_66 = Event()
    events_list_event_66.name = u'Introduction into Apache Spark'
    events_list_event_66.event_url = u'http://www.meetup.com/dev-070/events/223649096/'
    events_list_event_66.group = events_list_group_47
    events_list_event_66.meetupID = u'223649096'
    events_list_event_66.description = u'<p>For the people on the waiting list and other enthusiasts we are hosting the July session also in August.\xa0</p> <p>This will be a workshop so bring your own device! :)\xa0</p> <p><b>Schedule</b>\xa0</p> <p>\u2022 18:15 - 19:00: Doors open, food &amp; drinks</p> <p>\u2022 19:00 - 22:00: Introduction into Apache Spark (workshop)</p> <p><b>Introduction </b>into Apache Spark\xa0</p> <p>We will give a general introduction into Apache Spark and look at ways of running it and introduce the basic Spark API. We will briefly cover Spark components: Spark Core, Spark SQL, Spark Streaming, Spark GraphX and Spark MLlib. After the short presentation you\xa0will\xa0work on practical examples.</p> <p><b>About\xa0Apache Spark</b>:\xa0is an\xa0open-source\xa0cluster computing framework originally developed in the AMPLab at\xa0UC Berkeley. In contrast to\xa0Hadoop\'s two-stage disk-based\xa0MapReduce\xa0paradigm, Spark\'s in-memory primitives provide performance up to 100 times faster for certain applications.\xa0By allowing user programs to load data into a cluster\'s memory and query it repeatedly, Spark is well suited to machine learning algorithms.\xa0-\xa0<i>source</i>:\xa0<a href="http://en.wikipedia.org/wiki/Apache_Spark">Wikipedia</a></p> <p><img src="http://photos4.meetupstatic.com/photos/event/c/7/4/4/600_438231012.jpeg" /></p> <p><b>Prerequisites</b>:\xa0</p> <p>-JDK 8\xa0</p> <p>-Scala[masked](or higher)</p> <p>-SBT[masked]</p> <p>-Apache Spark 1.4.0</p> <p>-your favourite IDE</p> <p>Workshop led by:\xa0<a href="https://nl.linkedin.com/in/rvanrijn">Robert van Rijn</a>\xa0from NCIM Groep &amp;\xa0<a href="https://www.linkedin.com/profile/view?id=343288808&amp;authType=NAME_SEARCH&amp;authToken=CBdf&amp;locale=en_US&amp;trk=tyah&amp;trkInfo=clickedVertical%3Amynetwork%2Cidx%3A2-1-2%2CtarId%3A1433404312666%2Ctas%3Acas">Casper Koning</a>\xa0from Ordina</p>'
    events_list_event_66.local_start = dateutil.parser.parse("2015-08-18T18:00:00")
    events_list_event_66.local_end = dateutil.parser.parse("2015-08-18T18:00:00")
    events_list_event_66.utc_offset = 7200L
    events_list_event_66.is_applicable = True
    events_list_event_66 = importer.save_or_locate(events_list_event_66)

    events_list_event_66.hashtags.add(events_list_hashtag_1)

    events_list_event_67 = Event()
    events_list_event_67.name = u'Apache Placemaking  |  Community Workshop'
    events_list_event_67.event_url = u'http://www.meetup.com/Tempe-Character-Areas-Meetup/events/222510111/'
    events_list_event_67.group = events_list_group_48
    events_list_event_67.meetupID = u'222510111'
    events_list_event_67.description = u'<p><img src="http://photos4.meetupstatic.com/photos/event/4/d/c/f/600_437419919.jpeg" /></p> <p><b>Character Area 4 - Apache \xa0<br/>Placemaking Community Workshop </b>#<b>2</b></p> <p>Ratified by voters through the <i>Tempe General Plan 2040</i> in May 2014, Tempe\u2019s vision for itself is one of livability:</p> <p>\u2022 A city with a diverse, active, and engaged community<br/>\u2022 A city that is visually attractive and accessible by multiple modes of transportation<br/>\u2022 A city with parks and cultural amenities that provides the quality of life that attracts and retains residents and businesses\xa0</p> <p>Please join us our Character Area Planning process and we evolve Placemaking for the <b>Apache </b>area. This workshop will be the second of three community workshops to create locally-tailored design guidelines to implement Tempe\u2019s 20-Minute City vision.</p> <p>For more information, including a maps and the 2015 Placemaking Workshop Series, please visit:\xa0</p> <p><a href="http://www.tempe.gov/city-hall/community-development/character-areas/apache">www.tempe.gov/city-hall/community-development/character-areas/apache</a></p> <p><a href="https://www.tempe.gov/home/showdocument?id=32007">Apache Placemaking Community Workshops poster</a> [.pdf]\xa0</p> <p><img src="http://photos4.meetupstatic.com/photos/event/4/d/3/5/600_437419765.jpeg" /></p> <p><img src="http://photos4.meetupstatic.com/photos/event/c/0/6/600_437403078.jpeg" /></p>'
    events_list_event_67.local_start = dateutil.parser.parse("2015-08-18T18:00:00")
    events_list_event_67.local_end = dateutil.parser.parse("2015-08-18T20:00:00")
    events_list_event_67.utc_offset = -25200L
    events_list_event_67.is_applicable = True
    events_list_event_67 = importer.save_or_locate(events_list_event_67)

    events_list_event_67.hashtags.add(events_list_hashtag_1)

    events_list_event_68 = Event()
    events_list_event_68.name = u'PHP+Beer DT'
    events_list_event_68.event_url = u'http://www.meetup.com/indyphp/events/223840611/'
    events_list_event_68.group = events_list_group_49
    events_list_event_68.meetupID = u'kfsxdlytlbxb'
    events_list_event_68.description = u'<p>Join us upstairs at Tomlinson Tap Room at the far big wood table \xa0- we gather at 6:30 to 7:00 for beer and pizza and informal PHP discussions.</p>'
    events_list_event_68.local_start = dateutil.parser.parse("2015-08-18T18:30:00")
    events_list_event_68.local_end = dateutil.parser.parse("2015-08-18T18:30:00")
    events_list_event_68.utc_offset = -14400L
    events_list_event_68.is_applicable = True
    events_list_event_68 = importer.save_or_locate(events_list_event_68)

    events_list_event_68.hashtags.add(events_list_hashtag_1)

    events_list_event_69 = Event()
    events_list_event_69.name = u'SOLR and Cloudera Search'
    events_list_event_69.event_url = u'http://www.meetup.com/St-Louis-Hadoop-Users-Group/events/223440380/'
    events_list_event_69.group = events_list_group_50
    events_list_event_69.meetupID = u'dcjgjcytlbxb'
    events_list_event_69.description = u"<p>During the last several presentations, including those from Monsanto and Mercy Health Systems, presenters mentioned that they were using Apache Solr on Hadoop in order to quickly search the data they've stored.\xa0</p> <p>For our August meeting, Tom Wheeler will explain and demonstrate Cloudera Search, an open source product that makes it easy to run Solr at scale. This talk (which assumes no prior knowledge of Solr) will describe its use cases, explain the indexing process, and demonstrate how Solr can be used for analytics.\xa0</p> <p>Food and drink for this meeting will be sponsored by Cloudera. Special thanks for BJC for providing the space for this meeting.</p>"
    events_list_event_69.local_start = dateutil.parser.parse("2015-08-18T18:30:00")
    events_list_event_69.local_end = dateutil.parser.parse("2015-08-18T18:30:00")
    events_list_event_69.utc_offset = -18000L
    events_list_event_69.is_applicable = True
    events_list_event_69 = importer.save_or_locate(events_list_event_69)

    events_list_event_69.hashtags.add(events_list_hashtag_1)

    events_list_event_70 = Event()
    events_list_event_70.name = u'Intro to Cordova/Ionic mobile application development'
    events_list_event_70.event_url = u'http://www.meetup.com/Denver-Cordova-Ionic-Meetup/events/224457613/'
    events_list_event_70.group = events_list_group_51
    events_list_event_70.meetupID = u'224457613'
    events_list_event_70.description = u'<p>We will be conducting a hands on meetup to introduce people to hybrid mobile application development using Cordova, Ionic, and AngularJS. Please bring your laptops and we will walk you through the steps to create your first mobile application.</p>'
    events_list_event_70.local_start = dateutil.parser.parse("2015-08-18T18:30:00")
    events_list_event_70.local_end = dateutil.parser.parse("2015-08-18T18:30:00")
    events_list_event_70.utc_offset = -21600L
    events_list_event_70.is_applicable = True
    events_list_event_70 = importer.save_or_locate(events_list_event_70)

    events_list_event_70.hashtags.add(events_list_hashtag_1)

    events_list_event_71 = Event()
    events_list_event_71.name = u'Ionic + Firebase: Building Real-time Applications'
    events_list_event_71.event_url = u'http://www.meetup.com/Ionic-AZ/events/224062431/'
    events_list_event_71.group = events_list_group_52
    events_list_event_71.meetupID = u'224062431'
    events_list_event_71.description = u'<p>Bring your laptop so you can follow along on how to build real-time apps using Ionic + Firebase. More about the presentation and speaker will be available soon!<br/>Free beer &amp; pizza will be provided!!!</p>'
    events_list_event_71.local_start = dateutil.parser.parse("2015-08-18T19:00:00")
    events_list_event_71.local_end = dateutil.parser.parse("2015-08-18T19:00:00")
    events_list_event_71.utc_offset = -25200L
    events_list_event_71.is_applicable = True
    events_list_event_71 = importer.save_or_locate(events_list_event_71)

    events_list_event_71.hashtags.add(events_list_hashtag_1)

    events_list_event_72 = Event()
    events_list_event_72.name = u'Breakfast Meeting - Business Leads Group'
    events_list_event_72.event_url = u'http://www.meetup.com/Business-Leads-Group/events/224284797/'
    events_list_event_72.group = events_list_group_53
    events_list_event_72.meetupID = u'dvlvzdytlbzb'
    events_list_event_72.description = u'<p>Business Leads Group is an independent professional business leads organization that meets at Mimi\'s in Summerlin Las Vegas\xa0Nevada. We build business success through personal referrals.</p> <p>Business Leads Group structure set the standard in the word-of-mouth referral industry. Members are known for their professionalism, dedication, and loyalty to one another.</p> <p>Business Leads Group meet weekly to exchange qualified leads, build solid business relationships, develop strong presentation skills and become proficient net-workers. Only one representative of any given profession is accepted, and members are chosen for their occupational expertise.</p> <p>Meeting Times: Every Wednesday (Summerlin)</p> <p><b>(7:00am Sharp - 8:30am)</b></p> <p><b>Cost:</b> $14.00 for an Excellent Breakfast\xa0<i><b>(Cash Only)</b></i></p> <p>Weekly Meeting located at Mimi\'s Cafe in Summerlin.</p> <p><b>Mimi\'s Cafe</b> <a href="http://maps.google.com/maps?oe=utf-8&amp;rls=org.mozilla:en-US:official&amp;client=firefox-a&amp;um=1&amp;ie=UTF-8&amp;cid=0,0,1953440017319352890&amp;fb=1&amp;split=1&amp;gl=us&amp;dq=1121+S.+Fort+Apache+Rd.,las+vegas,+nv&amp;daddr=1121+S+Fort+Apache+Rd,+Las+Vegas,+NV+89117&amp;geocode=11458847154916060578,36.158701,-115.291436&amp;sa=X&amp;oi=local_result&amp;resnum=1&amp;ct=directions-to">1121 S. Fort Apache Rd.</a> Las Vegas, NV 89117 <a href="http://maps.google.com/maps?oe=utf-8&amp;rls=org.mozilla:en-US:official&amp;client=firefox-a&amp;um=1&amp;ie=UTF-8&amp;cid=0,0,1953440017319352890&amp;fb=1&amp;split=1&amp;gl=us&amp;dq=1121+S.+Fort+Apache+Rd.,las+vegas,+nv&amp;daddr=1121+S+Fort+Apache+Rd,+Las+Vegas,+NV+89117&amp;geocode=11458847154916060578,36.158701,-115.291436&amp;sa=X&amp;oi=local_result&amp;resnum=1&amp;ct=directions-to">(Southwest Corner of Fort Apache and Rampart)</a> <b>Walkins Welcome!</b></p> <p>\xa0</p>'
    events_list_event_72.local_start = dateutil.parser.parse("2015-08-19T07:00:00")
    events_list_event_72.local_end = dateutil.parser.parse("2015-08-19T08:30:00")
    events_list_event_72.utc_offset = -25200L
    events_list_event_72.is_applicable = True
    events_list_event_72 = importer.save_or_locate(events_list_event_72)

    events_list_event_72.hashtags.add(events_list_hashtag_1)

    events_list_event_73 = Event()
    events_list_event_73.name = u'Spark DataFrames: Simple and Fast Analysis of Structured Data'
    events_list_event_73.event_url = u'http://www.meetup.com/spark-online/events/223364987/'
    events_list_event_73.group = events_list_group_54
    events_list_event_73.meetupID = u'223364987'
    events_list_event_73.description = u'<p>Spark DataFrames: Simple and Fast Analysis of Structured Data<br/>Michael Armbrust</p> <p>This session will provide an introductory and technical overview of Spark\u2019s DataFrame API. First, we\u2019ll review the DataFrame API and show how to create DataFrames from a variety of data sources such as Hive, RDBMS databases, or other external data sources</p> <p>To join the session, please register at BrightTalk:\xa0<a href="https://www.brighttalk.com/webcast/12891/166495"><a href="https://www.brighttalk.com/webcast/12891/166495" class="linkified">https://www.brighttalk.com/webcast/12891/166495</a></a></p>'
    events_list_event_73.local_start = dateutil.parser.parse("2015-08-19T10:00:00")
    events_list_event_73.local_end = dateutil.parser.parse("2015-08-19T11:00:00")
    events_list_event_73.utc_offset = -25200L
    events_list_event_73.is_applicable = True
    events_list_event_73 = importer.save_or_locate(events_list_event_73)

    events_list_event_73.hashtags.add(events_list_hashtag_1)

    events_list_event_74 = Event()
    events_list_event_74.name = u'August Tech Confluence'
    events_list_event_74.event_url = u'http://www.meetup.com/TechConfluence/events/221882105/'
    events_list_event_74.group = events_list_group_55
    events_list_event_74.meetupID = u'nxcfhlytlbzb'
    events_list_event_74.description = u'<p>Dylan Koji-Cheslin: Propositional logic Aiko Cheslin: Power of mentorship Joe Fitzgerald: Cloud Foundry Topic Matt Conger-Eldeen: Moving from poll to push</p>'
    events_list_event_74.local_start = dateutil.parser.parse("2015-08-19T12:30:00")
    events_list_event_74.local_end = dateutil.parser.parse("2015-08-19T13:30:00")
    events_list_event_74.utc_offset = -21600L
    events_list_event_74.is_applicable = True
    events_list_event_74 = importer.save_or_locate(events_list_event_74)

    events_list_event_74.hashtags.add(events_list_hashtag_1)

    events_list_event_75 = Event()
    events_list_event_75.name = u'Mobile Meetup Oslo: Introducing Red Hat Mobile Application Platform'
    events_list_event_75.event_url = u'http://www.meetup.com/RedHatOslo/events/224279744/'
    events_list_event_75.group = events_list_group_56
    events_list_event_75.meetupID = u'224279744'
    events_list_event_75.description = u'<p>***************************************************</p> <p>You may RSVP here, but please visit the host\'s below <b>Mobile Meetup Oslo </b></p> <p><a href="http://www.meetup.com/Mobile-Meetup-Oslo/events/223556909/"><a href="http://www.meetup.com/Mobile-Meetup-Oslo/events/223556909/" class="linkified">http://www.meetup.com/Mobile-Meetup-Oslo/events/223556909/</a></a></p> <p>***************************************************</p> <p>Hi dear Mobile Meetup member!</p> <p>Just before main vacation period starts in Norway I\'m happy to introduce our August\'s event. Traditionally we start a new season by collaboration with world\'s leading company. Red Hat - world\'s open source leader -\xa0has launched its <a href="https://www.redhat.com/en/technologies/mobile/application-platform">Mobile Application Platform</a> and Mobile Meetup Oslo can\'t miss this milestone!</p> <p>=============<br/><b>Delicious pizza, refreshing beverages and amazing Red Hat \u201cswag\u201d will be available for attendees.</b><br/>=============</p> <p>The\xa0Mobile Application Platform\xa0consists of tools and templates for building mobile applications combined with back-end services to handle features including authentication, data, and integration with existing systems.\xa0Supported mobile platforms include <i>iOS, Android, Windows Phone and Apache Cordova</i>.</p> <p><img src="http://photos3.meetupstatic.com/photos/event/5/6/e/5/600_439162245.jpeg" /></p> <p>Curious to see how it works?</p> <p><b>Vikram Singh, Solution Architect for Red Hat, will conduct a session on this new technology from Red Hat.</b></p> <p>Vikram will give a detailed technology review and offer a demonstration / hands on, to create an enterprise grade app on just a few minutes.</p> <p><b>Shashin Shinde, Head of business development for xPaaS, will continue presentation.</b></p> <p><i>We start at 17:30. Here is the agenda:</i></p> <p><b>\u2022\xa0Red Hat Mobile Application Platform - Overview<br/>- Key Features<br/>- \u201cHow it Works\u201d<br/>- What\u2019s Next &amp; Roadmap</b></p> <p><b>\u2022\xa0Hands on demo</b></p> <p><b>\u2022\xa0Preview of related technologies - Red Hat JBoss Fuse<br/>- OpenShift xPaaS</b></p> <p><b>See you in Teknologihuset! </b></p> <p>=============</p> <p><b>More details about Red Hat Mobile Application Platform</b></p> <p>Red Hat supports the native SDKs for iOS, Android, Windows Phone and Apache Cordova as well as popular tools from companies including Xamarin, Sencha and Appcelerator. A hosted build farm provides builds for iOS, Android and Windows Phone. The server platform is based on node.js.</p> <p>Red Hat has added three things to the platform, on top of what it acquired from FeedHenry.</p> <p>\u2022\xa0The first is integration with OpenShift, Red Hat\u2019s public (or on premise) cloud application platform. OpenShift customers now have immediate access to the Mobile Application Platform.</p> <p>\u2022\xa0Second, there are new node.js adapters to integrate with JBoss, Red Hat\u2019s Java middleware product.</p> <p>\u2022\xa0Third, the company has added a push notification service from\xa0<a href="https://aerogear.org/">Aerogear</a>, another Red Hat project.</p> <p>***************************************************</p> <p>To register to this event please visit</p> <p><a href="http://www.meetup.com/Mobile-Meetup-Oslo/events/223556909/"><a href="http://www.meetup.com/Mobile-Meetup-Oslo/events/223556909/" class="linkified">http://www.meetup.com/Mobile-Meetup-Oslo/events/223556909/</a></a></p> <p>***************************************************</p>'
    events_list_event_75.local_start = dateutil.parser.parse("2015-08-19T17:30:00")
    events_list_event_75.local_end = dateutil.parser.parse("2015-08-19T17:30:00")
    events_list_event_75.utc_offset = 7200L
    events_list_event_75.is_applicable = True
    events_list_event_75 = importer.save_or_locate(events_list_event_75)

    events_list_event_75.hashtags.add(events_list_hashtag_1)

    events_list_event_76 = Event()
    events_list_event_76.name = u'Mobile Meetup Red Hat Edition: Introducing Red Hat Mobile Application Platform'
    events_list_event_76.event_url = u'http://www.meetup.com/Mobile-Meetup-Oslo/events/223556909/'
    events_list_event_76.group = events_list_group_57
    events_list_event_76.meetupID = u'223556909'
    events_list_event_76.description = u'<p>Hi dear Mobile Meetup member!</p> <p>Just before main vacation period starts in Norway I\'m happy to introduce our August\'s event. Traditionally we start a new season by collaboration with world\'s leading company. Red Hat - world\'s open source leader -\xa0has launched its <a href="https://www.redhat.com/en/technologies/mobile/application-platform">Mobile Application Platform</a> and Mobile Meetup Oslo can\'t miss this milestone!</p> <p>=============<br/><b>Delicious pizza, refreshing beverages and amazing Red Hat \u201cswag\u201d will be available for attendees.</b><br/>=============</p> <p>The\xa0Mobile Application Platform\xa0consists of tools and templates for building mobile applications combined with back-end services to handle features including authentication, data, and integration with existing systems.\xa0Supported mobile platforms include <i>iOS, Android, Windows Phone and Apache Cordova</i>.</p> <p><img src="http://photos3.meetupstatic.com/photos/event/5/6/e/5/600_439162245.jpeg" /></p> <p>Curious to see how it works?</p> <p><b>Vikram Singh, Solution Architect for Red Hat, will conduct a session on this new technology from Red Hat.</b></p> <p>Vikram will give a detailed technology review and offer a demonstration / hands on, to create an enterprise grade app on just a few minutes.</p> <p><b>Shashin Shinde, Head of business development for xPaaS, will continue presentation.</b></p> <p><br/><i>We start at 17:30. Here is the agenda:</i></p> <p><b>\u2022\xa0Red Hat Mobile Application Platform<br/></b>- Overview<br/>- Key Features<br/>- \u201cHow it Works\u201d<br/>- What\u2019s Next &amp; Roadmap</p> <p><b>\u2022\xa0Hands on demo</b></p> <p><b>\u2022\xa0Preview of related technologies<br/></b>- Red Hat JBoss Fuse<br/>- OpenShift xPaaS</p> <p>See you in Teknologihuset!</p> <p><br/>=============</p> <p><br/><b>More details about Red Hat Mobile Application Platform</b></p> <p>Red Hat supports the native SDKs for iOS, Android, Windows Phone and Apache Cordova as well as popular tools from companies including Xamarin, Sencha and Appcelerator. A hosted build farm provides builds for iOS, Android and Windows Phone. The server platform is based on node.js.</p> <p>Red Hat has added three things to the platform, on top of what it acquired from FeedHenry.</p> <p>\u2022\xa0The first is integration with OpenShift, Red Hat\u2019s public (or on premise) cloud application platform. OpenShift customers now have immediate access to the Mobile Application Platform.</p> <p>\u2022\xa0Second, there are new node.js adapters to integrate with JBoss, Red Hat\u2019s Java middleware product.</p> <p>\u2022\xa0Third, the company has added a push notification service from\xa0<a href="https://aerogear.org/">Aerogear</a>, another Red Hat project.</p>'
    events_list_event_76.local_start = dateutil.parser.parse("2015-08-19T17:30:00")
    events_list_event_76.local_end = dateutil.parser.parse("2015-08-19T17:30:00")
    events_list_event_76.utc_offset = 7200L
    events_list_event_76.is_applicable = True
    events_list_event_76 = importer.save_or_locate(events_list_event_76)

    events_list_event_76.hashtags.add(events_list_hashtag_1)

    events_list_event_77 = Event()
    events_list_event_77.name = u'#OCBigData Monthly Meetup #13'
    events_list_event_77.event_url = u'http://www.meetup.com/OCBigData/events/223360776/'
    events_list_event_77.group = events_list_group_58
    events_list_event_77.meetupID = u'223360776'
    events_list_event_77.description = u'<p><b>Hello all! We won\'t be having the OC Big Data Meetup in July. We are moving it to August. See you guys then?</b></p> <p><b>5:45 - 6:45<br/></b>Socialize over food and adult beverages</p> <p><b>6:45 - 7:30\xa0</b>\xa0<br/>TBD<br/>TBD @ <a href="http://www.snowflake.net">Snowflake Computing</a></p> <p><b>7:30 - 8:15\xa0</b><br/>TBD<br/>TBD @ <a href="http://www.datatorrent.com/">DataTorrent</a></p> <p><a href="http://www.snowflake.net">Snowflake Computing</a> will be sponsoring the food for this event.</p>'
    events_list_event_77.local_start = dateutil.parser.parse("2015-08-19T17:45:00")
    events_list_event_77.local_end = dateutil.parser.parse("2015-08-19T17:45:00")
    events_list_event_77.utc_offset = -25200L
    events_list_event_77.is_applicable = True
    events_list_event_77 = importer.save_or_locate(events_list_event_77)

    events_list_event_77.hashtags.add(events_list_hashtag_1)

    events_list_event_78 = Event()
    events_list_event_78.name = u'2nd Big Data Application Meetup'
    events_list_event_78.event_url = u'http://www.meetup.com/BigDataApps/events/224152189/'
    events_list_event_78.group = events_list_group_59
    events_list_event_78.meetupID = u'224152189'
    events_list_event_78.description = u'<p>Next meetup will be on August 19, 2015 at Cask Data HQ, Palo Alto.</p> <p>Mark your calendar and hope to see you all!</p> <p><b>Topics and Speakers</b></p> <p>\u2022\xa0Using Apache Kylin for large scale data analytics at eBay: Realtime Cube Updates with Kylin/Kafka Integration\xa0-\xa0Seshu Adunuthula, Director of Analytics Platform at eBay and Branky Shao, Software Engineer at eBay</p> <p><i>Abstract</i></p> <p>Apache Kylin is an open source Distributed Analytics Engine contributed from eBay that\xa0provides SQL interface and multi-dimensional analysis (OLAP) on Hadoop\xa0with support for extremely large data sets.\xa0</p> <p>Kylin has traditionally\xa0supported end of the day processing of the cubes resulting in large\xa0multi-hour cube build times depending on the number of rows added and<br/>dimension cardinality.\xa0</p> <p>In this talk we will introduce the concept of "Cube<br/>Segments\u201d the ability to build cubes on micro batches of data subscribed\xa0from Kakfa Topics.\xa0</p> <p>We will also present an internal usecase where SEO\xa0Attribution report with a 24+ hour processing window is now available\xa0within minutes.</p> <p><br/>\u2022 High Volume Streaming Analytics with CDAP - Jialong Wu from Lotame</p> <p><i>Abstract</i></p> <p>In this talk, we\u2019ll present the design of our new data stream processing application at Lotame and describe how we achieve significant reduction in cluster resource utilization while allowing faster updates of client audience data and better ad-hoc query support with the new platform.</p> <p>We will examine the challenges faced in counting uniques in a high volume stream processing environment, and present a novel approach using time windowed HyperLogLog aggregates. We\u2019ll also discuss how CDAP enable us to roll out this new platform quickly and share some valuable lessons and best practices we learned during the development cycle.</p> <p>\n\n\u2022 Introducing Athena -\xa0Yuanchi Ning from Uber</p> <p><br/><i>Abstract</i></p> <p><br/>Athena is a stream processing platform for Uber\'s near real time analytics applications, built using Samza. We will be discussing some of the existing and upcoming use cases and how they impact the Uber partners / riders. The talk will go through the tooling built around Samza for easier user on-boarding - such as deployment manager, integration with typesafe config system, unit test framework, Graphite integration, metric whitelisting and so on. We\'ll also go over some of the issues observed during this process.</p> <p>\n\n<b>Speakers Bio</b></p> <p>\u2022\xa0\xa0Seshu\xa0Adunuthula is Director of Analytics Platform at eBay responsible for managing some of the world\xb9s largest deployments of Hadoop, Teradata and ETL Ingest infrastructure. He is an industry veteran with over 20 years of Distributed Computing and Analytics Experience. Most recently he was managing the San Jose Development Team of MapR responsible for MapReduce, MapR-DB and MapR Control System Teams. Prior to that he was with Microsoft and Oracle in individual contributor and managerial roles in Microsoft SQL Server BI and at Oracle BPEL Workflow teams.</p> <p>\u2022\xa0\xa0Jialong\xa0Wu is a big data architect at Lotame, where he works on the core data platform that provides valuable insights to client\'s audience data and links users across mobile and desktop devices.\xa0</p> <p><br/>\u2022\xa0Yuanchi Ning is a Software Engineer in Data Engineering (Streaming Platform) at Uber Technologies. She is working on near-realtime data analytics services and application on top of Samza and is also building a generic streaming platform with Samza called Athena. This platform is built to empower other teams at Uber to develop reliable, scalable, and high-performing stream processing applications. Yuanchi received her Master\'s degree from Carnegie Mellon University.</p> <p><br/><b>Tentative schedule:</b></p> <p>Food &amp; socializing 6pm-6:30pm</p> <p>Talks 6:30pm-8pm</p>'
    events_list_event_78.local_start = dateutil.parser.parse("2015-08-19T18:00:00")
    events_list_event_78.local_end = dateutil.parser.parse("2015-08-19T20:00:00")
    events_list_event_78.utc_offset = -25200L
    events_list_event_78.is_applicable = True
    events_list_event_78 = importer.save_or_locate(events_list_event_78)

    events_list_event_78.hashtags.add(events_list_hashtag_1)

    events_list_event_79 = Event()
    events_list_event_79.name = u'The Colorado Springs Open Source Software Meetup Group Monthly Meetup'
    events_list_event_79.event_url = u'http://www.meetup.com/csopensource/events/224138823/'
    events_list_event_79.group = events_list_group_60
    events_list_event_79.meetupID = u'qzkxhhytlbzb'
    events_list_event_79.description = u'<p><b><i>AGENDA</i><br/></b> <b>6:00 - 6:30 PM</b> - Food, Drinks &amp; Networking<br/><b>6:30 - 6:35 PM</b> - Announcements<br/><b>6:35 - 7:15 PM</b> - Basic Concepts<br/><b>7:15 - 7:20 PM</b> - Break<br/><b>7:20 - 8:40 PM</b> - Main Speaker<br/><b>8:40 - 8:55 PM</b> - Door Prize Drawings</p> <p>\n\n\n<b><i>MAIN TOPIC ABSTRACT</i></b><br/><b>Apache Camel &amp; JBoss Fuse</b></p> <p>The Apache Camel mediation framework implements the defacto standard Enterprise Integration Patterns defined by Gregor Hohpe and Bobby Wolf in their treatise publication,\xa0<a href="http://www.enterpriseintegrationpatterns.com/eaipatterns.html"><a href="http://www.enterpriseintegrationpatterns.com/eaipatterns.html" class="linkified">http://www.enterpriseintegrationpatterns.com/eaipatterns.html</a></a>. Learn how Camel implements these design patterns in Camel processors and how Camel integrates with the enterprise with Camel components. Presentation will provide and overview of the Camel framework and how Camel is deployed as an ESB in the Fuse OSGi container and the JBoss EAP JEE container. We will build a couple of demo apps using the Fuse Integration Eclipse plugins deployed in JBoss Developer Studio. The Fuse Integration tooling provides a graphical editor to build Camel routes and can be deployed into any Eclipse installation. Presentation will also touch on using A-MQ in the Fuse runtime and will show how to configure and monitor Camel routes using Hawt.io and JBoss Operations Network.\xa0</p> <p><br/><b><i>MAIN SPEAKER BIOGRAPHY<br/></i>Bill Kemp</b></p> <p>Bill Kemp is a Senior Middleware Solutions Architect with Red Hat. He currently develops Proof of Concept applications based on JBoss SOA-P, JBoss Enterprise Data Services, and JBoss Fuse for Red Hat\'s middleware customers. He is the lead SOA SME for the middleware Solutions Architects at Red Hat. He has over 25 years experience in software development, design, support, and evangelism with Red Hat, Oracle, BEA Systems, SRA, Lockheed Martin, ISS, Verizon/MCI, and Digital Equipment Corp.\xa0</p> <p><br/><b><i>OUR SPONSORS</i></b></p> <p><br/><b>Website Sponsor:\xa0<a href="http://hsccareers.com">HSC Careers</a><br/></b> <b>Food Sponsor: <a href="http://apexsystemsinc.com">Apex Systems</a></b><b><br/></b> <b>Door Prize Sponsors:\xa0</b><a href="http://www.jetbrains.com"><b>Jetbrains</b></a> - Software license (Several products to choose from)<br/><b>Book Sponsor:\xa0</b><a href="http://www.oreilly.com"><b>OReilly Publishing</b></a> - Technical books</p>'
    events_list_event_79.local_start = dateutil.parser.parse("2015-08-19T18:00:00")
    events_list_event_79.local_end = dateutil.parser.parse("2015-08-19T18:00:00")
    events_list_event_79.utc_offset = -21600L
    events_list_event_79.is_applicable = True
    events_list_event_79 = importer.save_or_locate(events_list_event_79)

    events_list_event_79.hashtags.add(events_list_hashtag_1)

    events_list_event_80 = Event()
    events_list_event_80.name = u'Experiences with Spark 1.4 and R'
    events_list_event_80.event_url = u'http://www.meetup.com/Cincinnati-Apache-Spark-Meetup/events/224144550/'
    events_list_event_80.group = events_list_group_62
    events_list_event_80.meetupID = u'224144550'
    events_list_event_80.description = u"<p>Summer may be winding down, but Apache Spark is still going strong.\xa0 Spark version 1.4 was released in mid-June and included a number of major new features including 'R' integration. Join us again on the 19th to share Spark experiences, make new contacts, and learn about Spark and 'R'.\xa0 Once again, IlluminationWorks has graciously offered to host our meeting and provide pizza and drinks.</p> <p>Agenda:</p> <p>6:00 - 6:30 - Social Hour - Pizza and Drinks\xa0</p> <p>6:30 - 7:30 - Corrine Schlachter and Eugene\xa0Pyatigorsky from local tech startup, Ahalogy will be presenting on their experience with Spark and its 'R' integration.</p> <p><br/>7:30 - 8:00 - Open discussion:\xa0 people's experience with the Edx's Spark course, things we've encountered, other things in the latest release, etc.</p> <p><br/>Hope to see you on the 19th.</p> <p>\n\n\nSpeaker Bios:</p> <p><br/>Corinne is a Data Scientist at a Cincy internet tech startup, Ahalogy. She uses machine learning and other analytical methods to build new data driven product features and to help the company make informed, data-backed strategic decisions. As Ahalogy grows, Spark has emerged as the most promising way for our data scientists to work with the growing data. Corinne studied Applied Mathematics and Statistics at UC Berkeley and has been using R since college.</p> <p>Eugene works at Ahalogy \u2014 a local internet tech startup focusing on Pinterest \u2014 where he uses data to help with marketing, client management, and product development. He\u2019s a strong advocate of R, having used the platform on and off for 10 years. Eugene studied Applied Math at UC Berkeley for undergrad and Quantitative Marketing in the MBA Program at the Wharton School.</p>"
    events_list_event_80.local_start = dateutil.parser.parse("2015-08-19T18:30:00")
    events_list_event_80.local_end = dateutil.parser.parse("2015-08-19T18:30:00")
    events_list_event_80.utc_offset = -14400L
    events_list_event_80.is_applicable = True
    events_list_event_80 = importer.save_or_locate(events_list_event_80)

    events_list_event_80.hashtags.add(events_list_hashtag_1)

    events_list_event_81 = Event()
    events_list_event_81.name = u'Apex - An Enterprise Grade, Unified Batch & Stream Native Hadoop platform'
    events_list_event_81.event_url = u'http://www.meetup.com/Apex-Bay-Area-Chapter/events/224458241/'
    events_list_event_81.group = events_list_group_64
    events_list_event_81.meetupID = u'224458241'
    events_list_event_81.description = u'<p>Agenda\xa0<br/>6:30\xa0Pizza and networking\xa0<br/>7:00\xa0Announcements\xa0<br/>7:05\xa0Presentation by Chetan Narsude, Thomas Weise and \xa0Pramod Immaneni<br/>8:30\xa0Questions and Networking</p> <p>Join us at Cap One 360 Cafe in SF, where the DataTorrent lead architects will present and introduce you to Project Apex, the industry\u2019s only enterprise grade, fault tolerant batch and stream processing engine.\xa0</p> <p>In this meeting you will learn:</p> <p>-Batch and Streaming in a unified architecture- SAY WHAT?</p> <p>-Show you how DataTorrent and APEX drive ease of use, ease of operability and ease of management\xa0</p> <p>- Show you the benefits of using a truly enterprise grade platform and \xa0reduce time to business insight</p> <p>- You dont have to rewrite or redo your existing code or operational processes and be up and running with new applications in hours and days. NOT weeks and months. YOU GOT TO BE KIDDING...</p> <p>\n\n\nSee you all there. And big shout out to Capital1 Team for sponsoring Pizza and Hosting us.</p>'
    events_list_event_81.local_start = dateutil.parser.parse("2015-08-19T18:30:00")
    events_list_event_81.local_end = dateutil.parser.parse("2015-08-19T21:00:00")
    events_list_event_81.utc_offset = -25200L
    events_list_event_81.is_applicable = True
    events_list_event_81 = importer.save_or_locate(events_list_event_81)

    events_list_event_81.hashtags.add(events_list_hashtag_1)

    events_list_event_82 = Event()
    events_list_event_82.name = u'High Availability by Design'
    events_list_event_82.event_url = u'http://www.meetup.com/HackerLab/events/224051335/'
    events_list_event_82.group = events_list_group_65
    events_list_event_82.meetupID = u'224051335'
    events_list_event_82.description = u'<p>Things fail. It\u2019s a fact of life. But that doesn\u2019t mean that your applications and services need to fail. In this talk, David Prinzing will describe a solution architecture that has been proven to deliver amazing performance at scale with continuous availability on Amazon Web Services. You can\u2019t just move your application to the cloud and expect this \u2013 you need to design for it. Technology selections include Amazon Web Services, Ubuntu Linux, Apache Cassandra for the database, Dropwizard (a lightweight Java framework) for providing RESTful web services, and AngularJS as the foundation for an HTML5 web application. Pizza and beer will be served!</p> <p><br/><b>Please RSVP at the AWS Sacramento meetup group:\xa0</b><a href="http://www.meetup.com/AWS-SACRAMENTO/events/223964330/?a=ea1_grp&amp;rv=ea1&amp;_af=event&amp;_af_eid=223964330"><a href="http://www.meetup.com/AWS-SACRAMENTO/events/223964330/?a=ea1_grp&amp;rv=ea1&amp;_af=event&amp;_af_eid=223964330" class="linkified">http://www.meetup.com/AWS-SACRAMENTO/events/223964330/?a=ea1_grp&amp;rv=ea1&amp;_af=event&amp;_af_eid=223964330</a></a></p> <p><br/><b>Guest speaker:</b></p> <p>David Prinzing is currently the Chief Technology Officer of Algorithmic Ads. He has a passion for performance, scalability, availability, and security, and he\u2019s used this technology stack on three different major projects over the last several years. A more complete profile is available on LinkedIn.</p>'
    events_list_event_82.local_start = dateutil.parser.parse("2015-08-19T18:30:00")
    events_list_event_82.local_end = dateutil.parser.parse("2015-08-19T18:30:00")
    events_list_event_82.utc_offset = -25200L
    events_list_event_82.is_applicable = True
    events_list_event_82 = importer.save_or_locate(events_list_event_82)

    events_list_event_82.hashtags.add(events_list_hashtag_1)

    events_list_event_83 = Event()
    events_list_event_83.name = u'The Internet of Things'
    events_list_event_83.event_url = u'http://www.meetup.com/Triangle-JavaScript/events/224050506/'
    events_list_event_83.group = events_list_group_68
    events_list_event_83.meetupID = u'224050506'
    events_list_event_83.description = u'<p>The current hype around the Internet of Things (IoT) has led to a substantial amount of innovation thanks to open source software, open hardware, open standards, and community inspiration. In this session, we will explore how you can use open source software to incorporate the physical world (the \u201cThings\u201d) into your traditional enterprise IT infrastructure. We will walk the path from a typical enterprise developer\u2019s current focus on web desktop applications to mobile and devices, specifically developer prototyping platforms like Raspberry Pi, Intel Edison, Arduino, Particle Core, TI SensorTag, LightBlue Bean and others. Learn how to connect the physical world to your enterprise backbone via sensors and actuators with MQTT\xa0</p> <p>About the Speaker:</p> <p>Burr Sutter\xa0is responsible for Red Hat JBoss middleware developer tooling and frameworks and is specifically focused on technologies such as Java EE, Spring, PaaS, HTML5 and Apache Cordova. Burr\u2019s passion is learning, teaching and demonstrating developer facing technologies. He has previously been the President of the Atlanta Java Users Group, founder of the DevNexus conference, founder of the Atlanta chapter of the IASA and an Oracle Java Champion.\xa0</p> <p><br/>A big thanks to MetLife for hosting us again.</p>'
    events_list_event_83.local_start = dateutil.parser.parse("2015-08-19T19:00:00")
    events_list_event_83.local_end = dateutil.parser.parse("2015-08-19T19:00:00")
    events_list_event_83.utc_offset = -14400L
    events_list_event_83.is_applicable = True
    events_list_event_83 = importer.save_or_locate(events_list_event_83)

    events_list_event_83.hashtags.add(events_list_hashtag_1)

    events_list_event_84 = Event()
    events_list_event_84.name = u'ELK Stack Presentations'
    events_list_event_84.event_url = u'http://www.meetup.com/Elasticsearch-Los-Angeles/events/222201655/'
    events_list_event_84.group = events_list_group_69
    events_list_event_84.meetupID = u'222201655'
    events_list_event_84.description = u'<p>Anyone interested in Hosting or presenting at this meetup?</p>'
    events_list_event_84.local_start = dateutil.parser.parse("2015-08-19T19:00:00")
    events_list_event_84.local_end = dateutil.parser.parse("2015-08-19T19:00:00")
    events_list_event_84.utc_offset = -25200L
    events_list_event_84.is_applicable = True
    events_list_event_84 = importer.save_or_locate(events_list_event_84)

    events_list_event_84.hashtags.add(events_list_hashtag_1)

    events_list_event_85 = Event()
    events_list_event_85.name = u'Fall Early Session 19:30 Closed sessions'
    events_list_event_85.event_url = u'http://www.meetup.com/stockholmsportypeople/events/224469673/'
    events_list_event_85.group = events_list_group_76
    events_list_event_85.meetupID = u'grgtjlytlbzb'
    events_list_event_85.description = u'<p>Fall / Winter Contract sessions.</p> <p>Hi all.</p> <p>Due to several No shows last season.\xa0We have had to make some changes.</p> <p>There are 4 spots for the 7:30 to 8:30 sessions.\xa0</p> <p>These will always be reserved by 4 memebers that have paid the courts for the season.</p> <p>If you are interested and commited to attending, Join the waiting list.</p> <p><br/>If the per-paying members cannot join, they will contact you and assign you the spot.</p> <p><br/>Sorry for the drastic/tough rules, however this is the most fair way.\xa0</p> <p>BR</p> <p>Jeff</p>'
    events_list_event_85.local_start = dateutil.parser.parse("2015-08-19T19:30:00")
    events_list_event_85.local_end = dateutil.parser.parse("2015-08-19T20:30:00")
    events_list_event_85.utc_offset = 7200L
    events_list_event_85.is_applicable = False
    events_list_event_85 = importer.save_or_locate(events_list_event_85)

    events_list_event_85.hashtags.add(events_list_hashtag_1)

    events_list_event_86 = Event()
    events_list_event_86.name = u'Document Classification on Apache Spark'
    events_list_event_86.event_url = u'http://www.meetup.com/Atlanta-Hadoop-Users-Group/events/224454272/'
    events_list_event_86.group = events_list_group_66
    events_list_event_86.meetupID = u'224454272'
    events_list_event_86.description = u'<p>There are copious tuts, demos and walk-throughs that illustrate how to apply machine learning algorithms to perfectly-manicured data sets. But this doesn\u2019t reflect real-life situations for those who have big opportunities to find big value. What happens when your dataset is massive and unformatted, such as the internet search history for\u2026<i>everyone</i>? Maybe you built some very good models - now what?\xa0</p> <p><br/>This session takes place at the busy intersection of Big Data, Machine Learning and Business Problems. Being exposed to Apache Spark and its quickly maturing set of machine learning tools, you\u2019ll see how to 1) generate powerful modeling features, 2) apply the appropriate ML algorithms and 3) be able to generate value\xa0every time. You\u2019ll also leave with the code to reproduce the results and start creating your own value.\xa0</p> <p>\n\n\nPresented by <b>Joe Blue of MapR</b></p> <p><i>Event will be recorded</i>\xa0and posted after editing.</p> <p><b>Parking Instructions:</b></p> <p>It is most convenient if you enter the parking lot on the North Ave side of the building (across the street from Southern Dairies), park in the surface lot (lot that you pull into from the street) and if\xa0 you are facing the building (from North Ave) walk down the right side of the building towards the flats entrance, pass the flats entrance and you will dead end into the lobby for the suites. Please sign in in the lobby, take the elevator to the sixth floor and you will see our front (blue) doors upon exiting. Amber will be at the front desk to greet you and she will inform the appropriate parties that you have arrived on site. Please write down my contact information should you have any questions upon arriving on site.</p> <p><b>Food will be provided by D.B.A. BBQ</b></p>'
    events_list_event_86.local_start = dateutil.parser.parse("2015-08-19T19:00:00")
    events_list_event_86.local_end = dateutil.parser.parse("2015-08-19T19:00:00")
    events_list_event_86.utc_offset = -14400L
    events_list_event_86.is_applicable = True
    events_list_event_86 = importer.save_or_locate(events_list_event_86)

    events_list_event_86.hashtags.add(events_list_hashtag_1)

    events_list_event_87 = Event()
    events_list_event_87.name = u'Charlas sobre ElasticSearch'
    events_list_event_87.event_url = u'http://www.meetup.com/Montevideo-BigData-DataScience-Meetup/events/223833509/'
    events_list_event_87.group = events_list_group_67
    events_list_event_87.meetupID = u'223833509'
    events_list_event_87.description = u'<p>ElasticSearch es un servidor de b\xfasqueda Open Source basado en Lucene que provee b\xfasqueda sobre texto en forma distribuida.</p> <p>--- Charla 1 - Introducci\xf3n a Elasticsearch ---</p> <p>En esta charla vamos a ver una introducci\xf3n general a Elasticsearch, recorriendo sus funcionalidades principales para entender qu\xe9 es y qu\xe9 cosas puede hacer.</p> <p>Charla de Agust\xedn Azzinnari</p> <p>"Soy estudiante de Ingenier\xeda en Computaci\xf3n de la UdelaR. Empec\xe9 utilizando Elasticsearch para proyectos de Tryolabs hace m\xe1s de un a\xf1o, y vengo siguiendo el desarrollo de esta herramienta desde entonces. Hace un mes particip\xe9 del entrenamiento oficial de Elastic en San Pablo, donde vimos los fundamentos para dise\xf1ar y construir aplicaciones que aprovechen esta tecnolog\xeda."</p> <p>--- Charla 2 - Elasticsearch aggregations ---</p> <p>Una de las herramientas m\xe1s poderosas de Elasticsearch son las aggregations. En esta charla la idea es dar un pantallazo de algunos ejemplos pr\xe1cticos para ver el gran potencial de estas.</p> <p>Charla de Javier Rey</p> <p>"Ingeniero en Computaci\xf3n de la UdelaR. Trabajo con Elasticsearch desde hace dos a\xf1os y hace uno en Tryolabs, desarrollando aplicaciones escalables con componentes de machine learning y NLP."</p> <p>--- Charla 3: El stack ELK (Logstash + Elasticsearch + Kibana) ---</p> <p>Charla de Gabriel Moskovicz -\xa0@gmoskovicz.</p> <p>"Consultor y Soporte en Elastic, ha estado trabajando con el full stack de elasticsearch (ELK - Elasticsearch, Logstash &amp; Kibana) por mas de 2 a\xf1os. Actualmente se desarrolla tambien como docente de Paradigmas de Programaci\xf3n no convencionales en ORT"</p>'
    events_list_event_87.local_start = dateutil.parser.parse("2015-08-19T19:00:00")
    events_list_event_87.local_end = dateutil.parser.parse("2015-08-19T19:00:00")
    events_list_event_87.utc_offset = -10800L
    events_list_event_87.is_applicable = True
    events_list_event_87 = importer.save_or_locate(events_list_event_87)

    events_list_event_87.hashtags.add(events_list_hashtag_1)

    events_list_event_88 = Event()
    events_list_event_88.name = u'Monitor Web Performance - lets write an app for that !!'
    events_list_event_88.event_url = u'http://www.meetup.com/Geekfest-Seattle/events/223160364/'
    events_list_event_88.group = events_list_group_71
    events_list_event_88.meetupID = u'cdjhglytlbbc'
    events_list_event_88.description = u'<p>Testing and fixing the smoothness of your site\'s user interaction is painful and slow. In this talk, we\'ll look at creating a performance testing tool that automates a lot of the busy work, surfaces trouble spots, and gives you insight into probable causes.</p> <p><b>Talk Structure</b></p> <p>We will look at the process of using existing browser developer tools to identify code that makes a website jittery.We will explore parts of this process that can be automated.We will put our scripts together to create a tool that can be run on every commit to gather performance data.We will finally generate graphs from the data that can point to exact commits that may have caused performance issues.The audience will come away with strategies and tools to build a faster, more effective, and less painful workflow that will deliver consistently smoother user experiences and happier developers.</p> <p><br/><b>About the Speaker</b></p> <p>Parashuram is a Senior Program Manager with Microsoft Open Technologies Inc and works on many interesting open source projects including Apache Cordova and Chromium. He is a front end developer passionate about web performance and like to talk about performance practices at conferences.</p> <p><br/><b>Geekfest Events</b></p> <p>Food is always provided!</p> <p>All Geekfest events are recorded and will be published on the\xa0<a href="https://vimeo.com/grouponengineering">Groupon Engineering vimeo channel</a>. When this video is published, the link will be added to this event as a comment! Geekfest is always looking for speakers! Email us at\xa0[masked]\xa0if you are interested in giving a talk.</p>'
    events_list_event_88.local_start = dateutil.parser.parse("2015-08-20T12:00:00")
    events_list_event_88.local_end = dateutil.parser.parse("2015-08-20T13:00:00")
    events_list_event_88.utc_offset = -25200L
    events_list_event_88.is_applicable = True
    events_list_event_88 = importer.save_or_locate(events_list_event_88)

    events_list_event_88.hashtags.add(events_list_hashtag_1)

    events_list_event_89 = Event()
    events_list_event_89.name = u'Recommender Systems on Apache Spark'
    events_list_event_89.event_url = u'http://www.meetup.com/Oz-Big-Data-Melbourne/events/224443558/'
    events_list_event_89.group = events_list_group_70
    events_list_event_89.meetupID = u'224443558'
    events_list_event_89.description = u"<p>Please join us for an after-work talk (Melbourne CBD) on Recommender Systems, covering:<br/>- how Recommender Systems help the business<br/>- the information they consume<br/>- how you can design and tune one using Apache Spark.</p> <p>Recommender Systems drive the personalised website features and call-centre activities which push you the offers and suggestions that you are most likely to take. Amazon, Google, and Netflix have capitalised on them but they should be in your business too.</p> <p>The talk will be given by Maksud Ibrahimov, Chief Data Scientist at InfoReady Analytics.</p> <p><br/>It's been a while since the last Oz Big Data meetup, so we'll bring the pizza and drinks from 5:30pm with a 45-minute presentation starting after 6pm.</p> <p>As a fellow analytics professional, I look forward to seeing you again, or meeting you for the first time!</p>"
    events_list_event_89.local_start = dateutil.parser.parse("2015-08-20T17:30:00")
    events_list_event_89.local_end = dateutil.parser.parse("2015-08-20T19:00:00")
    events_list_event_89.utc_offset = 36000L
    events_list_event_89.is_applicable = True
    events_list_event_89 = importer.save_or_locate(events_list_event_89)

    events_list_event_89.hashtags.add(events_list_hashtag_1)

    events_list_event_90 = Event()
    events_list_event_90.name = u'"R for Solr", "Blacklight/GeoBlacklight for Discovery & Spatial Search in Solr"'
    events_list_event_90.event_url = u'http://www.meetup.com/SFBay-Lucene-Solr-Meetup/events/224315905/'
    events_list_event_90.group = events_list_group_85
    events_list_event_90.meetupID = u'224315905'
    events_list_event_90.description = u'<p>Parking and venue map can be found here: <a href="http://bit.ly/1eHsJEP"><a href="http://bit.ly/1eHsJEP" class="linkified">http://bit.ly/1eHsJEP</a></a></p> <p>Join us for an evening of networking, food &amp; drinks, and the below Solr talks from the Stanford Library team.<i><b><br/></b></i></p> <p><i><b>Blacklight: A discovery platform framework:</b></i> Presented by Chris Beer and Jessie Keck, Stanford Library</p> <p>Libraries, archives and museums are custodians of cultural heritage material in a wide variety of formats, metadata standards, and user interaction models. In this presentation, we will discuss how the Stanford University Libraries, along with many other libraries and cultural heritage institutions, use Blacklight [1], an open source discovery platform for Ruby on Rails that helps institutions around the world provide access to their knowledge repositories and assets using Apache Solr.</p> <p>[1] projectblacklight.org</p> <p>Speaker Bios: Coming soon</p> <p><br/><i><b>Spatial search in Solr; GeoBlacklight and Solr Facet Heatmaps:</b></i> Presented by Jack Reed, Stanford Library</p> <p>This presentation will talk about spatial search capabilities of Apache Solr and how they are used at Stanford University. GeoBlacklight, an open source spatial discovery application, will be discussed focusing on spatial search and discovery problems. In addition, a fairly new feature in Solr 5, Facet Heatmaps will be explored and put to task using Leaflet.js and the GeoNames.org corpus.</p> <p>Speaker Bio: Jack works on increasing access to geospatial data at Stanford University Libraries. A contributor to open-source software, Jack is active in the GIS, library, and open-data communities. He also serves on the executive committee of The International Association for Geoscience Diversity.</p> <p>\n\n\n<b><i>R client for Solr</i></b><br/>Scott Chamberlain, rOpenSci/UC Berkeley</p> <p><br/>Solr is a widely used search engine tool. As such, the R community needs a client to talk to Solr - to simplify searching Solr installations, and even managing configurations, cores, collections, and documents. This talk will go over the R client in development, and run through a couple of use cases that should provide good reasons to interact with Solr from R.</p> <p><br/>Speaker Bio:\xa0Scott co-founded rOpenSci (<a href="http://ropensci.org" class="linkified">http://ropensci.org</a> housed within UC Berkeley), a developer collective building R tools for open and reproducible science. Scott was an ecologist in a former life, but now makes open source software, mostly in R, and dabbles in Python and Ruby.</p>'
    events_list_event_90.local_start = dateutil.parser.parse("2015-08-20T18:00:00")
    events_list_event_90.local_end = dateutil.parser.parse("2015-08-20T18:00:00")
    events_list_event_90.utc_offset = -25200L
    events_list_event_90.is_applicable = True
    events_list_event_90 = importer.save_or_locate(events_list_event_90)

    events_list_event_90.hashtags.add(events_list_hashtag_1)

    events_list_event_91 = Event()
    events_list_event_91.name = u'Last Session of Summer'
    events_list_event_91.event_url = u'http://www.meetup.com/stockholmsportypeople/events/224469704/'
    events_list_event_91.group = events_list_group_76
    events_list_event_91.meetupID = u'224469704'
    events_list_event_91.description = u"<p>Last Session</p> <p>Badminton stadion shuts down at 9, so we'll move our time slots forward.</p> <p>We start at 6:30!\xa0at court 17.</p> <p>So if you are on the waitlist and a multiple of 2, post up as\xa0It will be very easy to get additional courts.\xa0</p> <p><br/>fees are I think fees are 110kr for the hour. so 30 kr/ person</p>"
    events_list_event_91.local_start = dateutil.parser.parse("2015-08-21T18:30:00")
    events_list_event_91.local_end = dateutil.parser.parse("2015-08-21T19:30:00")
    events_list_event_91.utc_offset = 7200L
    events_list_event_91.is_applicable = False
    events_list_event_91 = importer.save_or_locate(events_list_event_91)

    events_list_event_91.hashtags.add(events_list_hashtag_1)

    events_list_event_92 = Event()
    events_list_event_92.name = u'Introducing POSH Unplugged!'
    events_list_event_92.event_url = u'http://www.meetup.com/Pivotal-Open-Source-Hub/events/223990673/'
    events_list_event_92.group = events_list_group_86
    events_list_event_92.meetupID = u'223990673'
    events_list_event_92.description = u'<p>NOTE: THIS MEETUP IS IN SAN FRANCISCO at 5:45pm PDT</p> <p><b>Lightning Talks</b><br/>We\u2019re looking for your new and fresh ideas to liven up the POSH experience. Would you like to pitch a startup to the group? Interested in testing a conference talk? Want to share a topic idea? Anyone who has something interesting to say about an open source topic may apply.</p> <p>\u2022 Slides are allowed, but not required<br/>\u2022 5-minute talk/5-minute questions<br/>\u2022 Only one lightning talk may be submitted per person/group</p> <p>Submit your three-bullet abstract <a href="http://goo.gl/forms/EoGseOOcmN">here</a> and we\u2019ll choose six people/groups to deliver a 10-minute lightening talk at the next POSH Unplugged. We want to hear from you!</p> <p>6:00-6:30 pm Food and networking<br/>6:30-8:00 pm Talk and Q&amp;A \n<br/>8:00-8:30 pm Wind down</p> <p>\n\n\n* <i>Food for this meetup is provided by Guerilla Catering of San Francisco.\xa0 Guerilla provides some of the most authentic latin food San Francisco has to offer.\xa0 Empanadas, three ways:\xa0 prather ranch organic dry-aged grass feed beef with pimiento stuffed olives and raisins and fulton valley all natural chicken with organic sweet corn and roasted red bell peppers.\xa0 Taco Bar includes fresh homemade street style chips, tacos, salsa, guacamole, assorted amazing hot sauces, onions/cilantro with fresh chicken.\xa0 Fresh, organic green salad with walnuts, apricots and avocados, yummy!</i></p>'
    events_list_event_92.local_start = dateutil.parser.parse("2015-08-20T18:00:00")
    events_list_event_92.local_end = dateutil.parser.parse("2015-08-20T21:00:00")
    events_list_event_92.utc_offset = -25200L
    events_list_event_92.is_applicable = True
    events_list_event_92 = importer.save_or_locate(events_list_event_92)

    events_list_event_92.hashtags.add(events_list_hashtag_1)

    events_list_event_93 = Event()
    events_list_event_93.name = u'Spark Streaming& Kafka-The Future of Stream Processing-Hari Shreedharan/Cloudera'
    events_list_event_93.event_url = u'http://www.meetup.com/Los-Angeles-Apache-Spark-Users-Group/events/223927337/'
    events_list_event_93.group = events_list_group_87
    events_list_event_93.meetupID = u'223927337'
    events_list_event_93.description = u'<p>Abstract:-<br/>With its easy to use interfaces and native integration with some of the most popular ingest tools, such as Kafka, Flume, Kinesis etc, Spark Streaming has become go-to tool for stream processing. Code sharing with Spark also makes it attractive. In this talk, we will discuss the latest features in Spark Streaming and how it integrates with Kafka natively with no data loss, and even do exactly once processing!</p> <p>Bio:-<br/>Hari Shreedharan is a PMC member and committer on the Apache Flume Project. As a PMC member, he is involved in making decisions on the direction of the project. Author of the O\u2019Reilly book Using Flume, Hari is also a software engineer at Cloudera, where he works on Apache Flume, Apache Spark, and Apache Sqoop. He also ensures that customers can successfully deploy and manage Flume, Spark, and Sqoop on their clusters, by helping them resolve any issues they are facing.</p>'
    events_list_event_93.local_start = dateutil.parser.parse("2015-08-20T18:30:00")
    events_list_event_93.local_end = dateutil.parser.parse("2015-08-20T18:30:00")
    events_list_event_93.utc_offset = -25200L
    events_list_event_93.is_applicable = True
    events_list_event_93 = importer.save_or_locate(events_list_event_93)

    events_list_event_93.hashtags.add(events_list_hashtag_1)

    events_list_event_94 = Event()
    events_list_event_94.name = u'Large scale Distributed ML on Spark'
    events_list_event_94.event_url = u'http://www.meetup.com/spark-users/events/223361529/'
    events_list_event_94.group = events_list_group_108
    events_list_event_94.meetupID = u'223361529'
    events_list_event_94.description = u'<p><b>This meetup will focus on Large scale Distributed ML on Spark. Title abstract and speaker bio below.\xa0The talk will be published on the <a href="https://www.youtube.com/user/TheApacheSpark">Apache Spark</a>\xa0channel on YouTube.</b></p> <p><b><br/></b></p> <p><b>Agenda:</b></p> <p><b>6:30 - 7:00 :: Mingling</b></p> <p><b>7:00 - 7:05 :: Welcome\xa0</b></p> <p><b>7:05 - 8:15 :: Technical talk\xa0</b></p> <p><b>8:15 - 9:00 :: Mingling</b></p> <p><b><br/></b></p> <p><b>Title:</b>\xa0Large scale Distributed ML on Spark</p> <p><b>Abstract:</b>\xa0Hadoop brought MapReduce and Big Data to mainstream; however, as requirements and usage models expand, new big data analysis paradigms beyond MapReduce have inevitably emerged. In particular, there is increasing demand from organizations to discover and explore data using advanced analytics algorithms (e.g., large-scale machine learning, graph analysis, statistic modeling) for deep insights. In this talk, we will present our efforts on building large scale distributed ML on Apache Spark with many "web-scale" companies, including very complex and advanced analytics applications/algorithms (e.g., topic modeling, deep neural network, etc.), as well as massively scalable learning system/platform leveraging both application and infrastructure specific optimizations (exploring data sparsity, parameter server, etc.).</p> <p><b>Our speaker</b>. Jason Dai is currently the Chief Architect of Big Data Technologies at Intel. Prior to that, he was a Principle Architect in Microsoft, responsible for building large-scale Cloud and Big Data platform that powers some of the largest Internet services in the company. Before joining Microsoft, he was an Engineering Director and Principal Engineer in Intel, responsible for advanced research and development of Big Data platforms in Intel, including joint-development with UC Berkeley on the next generations of Big Data technologies (e.g., Apache Spark stack), and building next-gen Big Data platforms for some of the largest websites in the world. Jason is an internationally recognized expert on big data, cloud, parallel computing and compiler technologies. He is a PMC member of the Apache Spark project, and has published over 15 technical papers, filed over 20 patents, and taught computer classes in top universities.)</p>'
    events_list_event_94.local_start = dateutil.parser.parse("2015-08-20T18:30:00")
    events_list_event_94.local_end = dateutil.parser.parse("2015-08-20T21:00:00")
    events_list_event_94.utc_offset = -25200L
    events_list_event_94.is_applicable = True
    events_list_event_94 = importer.save_or_locate(events_list_event_94)

    events_list_event_94.hashtags.add(events_list_hashtag_1)

    events_list_event_95 = Event()
    events_list_event_95.name = u'Lucia Gjeltema presents SparkR - distributed computing in R using Spark clusters'
    events_list_event_95.event_url = u'http://www.meetup.com/Research-Triangle-Analysts/events/224408368/'
    events_list_event_95.group = events_list_group_89
    events_list_event_95.meetupID = u'224408368'
    events_list_event_95.description = u'<p>Data processing and machine learning tasks in R are usually limited to data sets that fit in the memory of one single machine. The new R frontend to Apache Spark, called SparkR, harnesses Spark\u2019s distributed computing powers to run large-scale data analysis directly in R. Originally an R package, SparkR is now officially merged into Apache Spark (since release 1.4 in June 2015).<br/>This talk introduces SparkR and one of its core components - the SparkR DataFrame, a way of bringing distributed computing capabilities to the world of data frames.</p>'
    events_list_event_95.local_start = dateutil.parser.parse("2015-08-20T18:30:00")
    events_list_event_95.local_end = dateutil.parser.parse("2015-08-20T20:00:00")
    events_list_event_95.utc_offset = -14400L
    events_list_event_95.is_applicable = True
    events_list_event_95 = importer.save_or_locate(events_list_event_95)

    events_list_event_95.hashtags.add(events_list_hashtag_1)

    events_list_event_96 = Event()
    events_list_event_96.name = u'Shanghai Big Data Streaming 1st Meetup'
    events_list_event_96.event_url = u'http://www.meetup.com/Shanghai-Big-Data-Streaming-Meetup/events/224418388/'
    events_list_event_96.group = events_list_group_97
    events_list_event_96.meetupID = u'224418388'
    events_list_event_96.description = u'<p><b>\u65e5\u7a0b</b><b>:</b></p> <p>12:45 \u2013 13:00 \u7b7e\u5230</p> <p>13:00 \u2013 13:15 \u5f00\u573a\u767d (Intel + \u592a\u5e93\u4ecb\u7ecd)</p> <p>13:15 \u2013 14:00 JStorm/Storm\u5728\u963f\u91cc\u7684\u5b9e\u8df5\u548c\u793e\u533a\u8fdb\u5c55 (\u963f\u91cc\u5df4\u5df4)</p> <p>14:00 \u2013 14:30 StreamingCQL - \u6784\u5efa\u5728\u5206\u5e03\u5f0f\u6d41\u5904\u7406\u5e73\u53f0\u4e0a\u7684\u67e5\u8be2\u8bed\u8a00 \uff08\u534e\u4e3a\uff09</p> <p>14:30 \u2013 14:50 \u8336\u6b47</p> <p>14:50 \u2013 15:35 Pulsar\u2013 Real-time analytics at Scale (eBay)</p> <p>15:35 \u2013 16:15 Gearpump \u2013\xa0\u57fa\u4e8eAkka\u7684\u5f00\u6e90\u6d41\u5904\u7406\u5f15\u64ce (Intel)</p> <p>16:20 \u2013 17:00 \u7ee7\u7eed\u8ba8\u8bba</p> <p>\n\n\n\u4e3b\u529e\uff1aIntel</p> <p><img src="http://photos3.meetupstatic.com/photos/event/d/5/0/f/600_440574543.jpeg" /></p> <p>\n\n\n\u91d1\u724c\u8d5e\u52a9\u4f19\u4f34\uff1a \u592a\u5e93</p> <p><img src="http://photos4.meetupstatic.com/photos/event/d/5/1/9/600_440574553.jpeg" /></p> <p><b><br/></b></p> <p><b>Speaker List:</b></p> <p><br/>Speaker1:</p> <p><b>\u5c01\u4ef2\u6df9</b>(\u6dd8\u5b9d\u82b1\u540d: \u7eaa\u541b\u7965) \u963f\u91cc\u5df4\u5df4\u963f\u91cc\u4e2d\u95f4\u4ef6\u56e2\u961f\u9ad8\u7ea7\u6280\u672f\u4e13\u5bb6</p> <p>\u963f\u91cc\u5df4\u5df4JStorm \u6838\u5fc3\u4f5c\u8005\u4e4b\u4e00\uff0c\u6d41\u5f0f\u8ba1\u7b97\u6743\u5a01\u4eba\u58eb\u4e4b\u4e00\uff0c\u66fe\u4ece\u4e8b\u5206\u5e03\u5f0f\u8ba1\u7b97\uff0c\u5206\u5e03\u5f0f\u5b58\u50a8\u591a\u5e74\uff0c \u4e13\u5229\u9887\u591a\uff0c\u76ee\u524d\u4e13\u6ce8\u4e8e\u5b9e\u65f6\u8ba1\u7b97\u548c\u6d41\u5f0f\u8ba1\u7b97\u3002 \u68a6\u60f3\u6709\u671d\u4e00\u65e5\u80fd\u5b9e\u73b0\u7c7b\u4f3cHadoop\u7684\u7cfb\u7edf\u3002\u66fe\u5c31\u804c\u4e8eEMC\uff0cVIA\u3002</p> <p><b>\u5206\u4eab\u4e3b\u9898: JStorm/Storm</b><b>\u5728\u963f\u91cc\u7684\u5b9e\u8df5\u548c\u793e\u533a\u8fdb\u5c55 </b>(45\u5206\u949f)</p> <p>\u968f\u65f6\u4e1a\u52a1\u5bf9\u6570\u636e\u7684\u5b9e\u65f6\u6027\u8981\u6c42\u8d8a\u6765\u8d8a\u4e25\u683c\uff0c \u8d8a\u6765\u8d8a\u591a\u7684\u5e94\u7528\u5f00\u59cb\u4f7f\u7528JStorm\u3001Storm\u8fdb\u884c\u5b9e\u65f6\u8ba1\u7b97\uff0c \u672c\u6b21\u6f14\u8bb2\u5c06\u4ecb\u7ecdjstorm\u5728\u963f\u91cc\u7684\u73b0\u72b6\uff0c\u548cjstorm\u6b63\u5728\u5f00\u53d1\u7684\u7279\u6027\uff0c\u4ee5\u53caJstorm \u5e76\u5165storm\u540e\u7684\u8ba1\u5212\u4e0e\u5b89\u6392(STORM-717\uff09\u3002</p> <p>\n\n\nSpeaker2:</p> <p><b>\u6c6a\u5174\u6717\xa0</b>eBay\u8d44\u6df1\u67b6\u6784\u5e08</p> <p>\u6bd5\u4e1a\u4e8e\u4e0a\u6d77\u4ea4\u901a\u5927\u5b66\u8ba1\u7b97\u673a\u7cfb\uff0c\u4e8e2013\u5e744\u6708\u52a0\u5165eBay, \u76ee\u524d\u662febay Cloud Service\u7684\u8d44\u6df1\u67b6\u6784\u5e08\uff0ceBay CCOE technical board\u4e3b\u5e2d\u3002\u52a0\u5165ebay\u4e4b\u524d\uff0c\u5728HP\u4e13\u6ce8\u4e8e\u7535\u4fe1\u884c\u4e1a\u7684\u5b9e\u65f6\u7cfb\u7edf\u5e73\u53f0, \xa0\u66fe\u62c5\u4efbHP\u7535\u4fe1\u4e1a\u52a1\u5b9e\u65f6\u5e73\u53f0\u7684\u9996\u5e2d\u67b6\u6784\u5e08\u3002\u5177\u6709\u4e30\u5bcc\u7684\u5206\u5e03\u5f0f\u5b9e\u65f6\u7cfb\u7edf\u7684\u7ecf\u9a8c\uff0c\u5728eBay\u6210\u529f\u7684\u5c06\u5b9e\u65f6\u7cfb\u7edf\u548c\u7528\u6237\u884c\u4e3a\u6570\u636e\u7ed3\u5408\u8d77\u6765\uff0c\u642d\u5efa\u4e86\u4e00\u4e2a\u5b9e\u65f6\u7684\u7528\u6237\u884c\u4e3a\u6570\u636e\u7684\u5904\u7406\u7684\u5e73\u53f0\uff0c\u5927\u5927\u7f29\u77ed\u4e86\u4e1a\u52a1\u90e8\u95e8\u7684\u51b3\u7b56\u65f6\u95f4\uff0c\u63a8\u52a8\u4e86eBay\u7528\u6237\u884c\u4e3a\u6570\u636e\u5206\u6790\u4ecehadoop\u6279\u5904\u7406\u8f6c\u5411\u5b9e\u65f6\u5904\u7406</p> <p><b>\u5206\u4eab\u4e3b\u9898</b><b>: Pulsar \u2013 Real-time analytics at Scale.</b> (45\u5206\u949f)</p> <p>Pulsar \u2013 \u6765\u81eaeBay\u7684\u4e00\u4e2a\u5206\u5e03\u5f0f\u590d\u6742\u4e8b\u4ef6\u6d41\u5904\u7406\u5e73\u53f0\uff0c\u5728eBay\u5185\u90e8\u7528\u4e8e\u5bf9\u4e8e\u7528\u6237\u884c\u4e3a\u6570\u636e\u7684\u6570\u636e\u5206\u6790\u3002\u901a\u8fc7\u5bf9\u7528\u6237\u884c\u4e3a\u6570\u636e\u6d41\u7684\u5b9e\u65f6\u5206\u6790\uff0c\u7ed9\u5ba2\u6237\u5e26\u6765\u66f4\u597d\u7684\u4e2a\u6027\u5316\u4f53\u9a8c\uff0c\u5e2e\u52a9\u5ba2\u6237\u76d1\u63a7\u5b9e\u65f6\u4e1a\u52a1\u4fe1\u606f\u5e76\u5b9a\u5236\u5b9e\u65f6\u8425\u9500\u7b56\u8def\uff0c\u53ca\u65f6\u76d1\u6d4b\u7f51\u7edc\u6b3a\u8bc8\u884c\u4e3a\u5e76\u51cf\u5c11\u673a\u5668\u4eba\u5e72\u9884\u3002\u5e76\u4e14Pulsar\u662f\u57fa\u4e8e\u6807\u51c6\u7684\u5206\u5e03\u5f0f\u4e91\u67b6\u6784\u90e8\u7f72\u5e76\u8de8\u8d8a\u591a\u4e2a\u6570\u636e\u4e2d\u5fc3\uff0c\u4ece\u800c\u4fdd\u8bc1\u4e86\u5728\u7cfb\u7edf\u5347\u7ea7\u548c\u62d3\u6251\u66f4\u65b0\u65f6\u6ca1\u6709\u96c6\u7fa4\u505c\u673a\u65f6\u95f4\u3002</p> <p>\n\n\nSpeaker3:</p> <p><b>\u4f55\u5fd7\u5f3a</b>\xa0\u534e\u4e3a\u5b9e\u65f6\u5206\u6790\u56e2\u961f\u9ad8\u7ea7\u6280\u672f\u4e13\u5bb6</p> <p>StreamingCQL\u6838\u5fc3\u4f5c\u8005\u4e4b\u4e00\uff0c\u5b9e\u65f6\u5904\u7406\u8d44\u6df1\u67b6\u6784\u5e08\u30022011\u5e744\u6708\u52a0\u5165\u534e\u4e3a\uff0c\u76ee\u524d\u5728\u534e\u4e3a\u8fdb\u884c\u5b9e\u65f6\u5206\u6790\u5f00\u53d1\u3002\u4e00\u76f4\u4ece\u4e8b\u5927\u6570\u636e\u5206\u6790\u3001\u5206\u5e03\u5f0f\u8ba1\u7b97\u3001\u6d41\u5f0f\u5904\u7406\u7b49\u65b9\u9762\u7684\u7814\u7a76\u53ca\u5f00\u53d1\u3002</p> <p><b>\u5206\u4eab\u4e3b\u9898</b><b>: StreamingCQL</b><b>\u2014\u2014\u6784\u5efa\u5728\u5206\u5e03\u5f0f\u6d41\u5904\u7406\u5e73\u53f0\u4e0a\u7684\u67e5\u8be2\u8bed\u8a00 </b>(30\u5206\u949f)</p> <p>StreamingCQL(Streaming Continuous Query Language)\u662f\u5efa\u7acb\u5728\u5206\u5e03\u5f0f\u6d41\u5904\u7406\u5e73\u53f0\u57fa\u7840\u4e0a\u7684\u7c7bSQL\u67e5\u8be2\u8bed\u8a00\uff0c\u67b6\u6784\u652f\u6301\u6784\u5efa\u5728\u591a\u79cd\u6d41\u5904\u7406\u5f15\u64ce\u4e4b\u4e0a\uff0c\u76ee\u524d\u4e3b\u8981\u9002\u914dStorm\u3002\u5f53\u524d\u591a\u6570\u6d41\u5904\u7406\u5e73\u53f0\u4ec5\u63d0\u4f9b\u5206\u5e03\u5f0f\u5904\u7406\u80fd\u529b\uff0c\u4e1a\u52a1\u903b\u8f91\u5f00\u53d1\u590d\u6742\uff0c\u6d41\u8ba1\u7b97\u4e1a\u52a1\u529f\u80fd\u8f83\u5f31\uff0c\u5b58\u5728\u4e1a\u52a1\u903b\u8f91\u91cd\u7528\u6027\u4e0d\u9ad8\u3001\u91cd\u590d\u5f00\u53d1\u3001\u5f00\u53d1\u6548\u7387\u4f4e\u4e0b\u7b49\u95ee\u9898\u3002StreamingCQL\u63d0\u4f9b\u4e86\u8f83\u4e30\u5bcc\u7684\u5206\u5e03\u5f0f\u6d41\u8ba1\u7b97\u529f\u80fd\uff0c\u9664\u4e86\u5177\u6709\u8fc7\u6ee4\u3001\u8f6c\u6362\u7b49\u4f20\u7edf\u7684SQL\u57fa\u672c\u80fd\u529b\u4e4b\u5916\uff0cStreamingCQL\u5f15\u5165\u57fa\u4e8e\u7a97\u53e3\u7684\u8ba1\u7b97\uff0c\u63d0\u4f9b\u7a97\u53e3\u6570\u636e\u7684\u7edf\u8ba1\u3001\u5173\u8054\u7b49\u80fd\u529b\uff0c\u4ee5\u53ca\u6d41\u6570\u636e\u7684\u62c6\u5206\u3001\u5408\u5e76\u7b49\u529f\u80fd\u3002\u672c\u6b21\u6f14\u8bb2\u5c06\u4ecb\u7ecdCQL\u529f\u80fd\uff0c\u76ee\u524d\u73b0\u72b6\u548c\u540e\u671f\u53d1\u5c55\u8ba1\u5212\u3002</p> <p>\n\n\nSpeaker4:</p> <p><b>\u949f\u7fd4\xa0</b>Intel\u5927\u6570\u636e\u6280\u672f\u90e8\u5de5\u7a0b\u5e08</p> <p>2011\u5e74\u52a0\u5165Intel\uff0c2014\u5e74\u524d\u662fIntel\u5927\u6570\u636e\u53d1\u884c\u7248\u5f00\u53d1(IDH)\u7684\u6838\u5fc3\u529b\u91cf\uff0c\u5f00\u53d1\u4e86IDH\u7684\u51e0\u4e2a\u6838\u5fc3\u529f\u80fd\uff0c\u6bd4\u5982MapReduce NativeTask\uff0cHBase \u5927\u5bf9\u8c61\u5b58\u50a8\u7b49\u3002\u73b0\u5728\u4e3b\u8981\u5173\u6ce8\u5b9e\u65f6\u6d41\u5904\u7406\uff0c\u521b\u7acb\u4e86\u57fa\u4e8eAkka\u7684\u65b0\u578b\u6d41\u5904\u7406\u5f15\u64ceGearpump(<a href="http://www.gearpump.io/"><a href="http://www.gearpump.io/" class="linkified">http://www.gearpump.io/</a></a>)\u3002\u949f\u7fd4\u662fApache Storm\u7684PMC\u6210\u5458\u3002</p> <p><b>\u5206\u4eab\u4e3b\u9898: \xa0Gearpump \u2013\xa0</b><b>\u57fa\u4e8eAkka</b><b>\u7684\u5f00\u6e90\u6d41\u5904\u7406\u5f15\u64ce </b>(40\u5206\u949f)</p> <p>Akka\u662f\u4e00\u4e2a\u5206\u5e03\u5f0f\u8f6f\u4ef6\u5f00\u53d1\u7684\u4e2d\u95f4\u4ef6\uff0c\u57fa\u4e8eActor\u6a21\u578b\u63d0\u4f9b\u4e86\u901a\u4fe1\u3001\u5e76\u53d1\u3001\u9694\u79bb\u3001\u5bb9\u9519\u7b49\u57fa\u7840\u8bbe\u65bd\u3002\u672c\u6b21\u6f14\u8bb2\u5c06\u4ecb\u7ecdIntel\u600e\u6837\u4f7f\u7528Akka Actor\u62bd\u8c61\uff0c\u89e3\u51b3\u6d41\u5904\u7406\u7684\u5404\u79cd\u95ee\u9898\uff0c\u5b9e\u73b0\u4e00\u4e2a\u6bcf\u79d2\u949f\u5904\u7406\u5343\u4e07\u6d88\u606f\u7684\u6d41\u5904\u7406\u5f15\u64ceGearpump\u3002\u89e3\u51b3\u7684\u95ee\u9898\u5305\u62ec:</p> <p>1\uff09\xa0 \u5b9e\u65f6\u6027\uff0c\u6beb\u79d2\u7ea7\u5ef6\u65f6\u3002</p> <p>2\uff09\xa0 \u4e00\u81f4\u6027\uff0cExactly once \u7684\u6d88\u606f\u5904\u7406\uff0c\u6570\u636e\u4e0d\u4e22\u4e0d\u91cd\u3002</p> <p>3\uff09\u541e\u5410\u91cf\uff0c\u6bcf\u79d2\u80fd\u5904\u7406\u767e\u4e07\u751a\u81f3\u5343\u4e07\u6761\u6d88\u606f\u3002</p> <p>4\uff09\u53ef\u7528\u6027, \xa0\u6ca1\u6709\u5355\u70b9\u5931\u6548\u3002</p> <p>5\uff09\u7075\u6d3b\u6027\uff0c\u652f\u6301\u8ba1\u7b97\u56fe\u7684\u52a8\u6001\u5347\u7ea7\u66ff\u6362\uff0c\u652f\u6301\u5f39\u6027\u6269\u5c55\uff0c\u652f\u6301\u65f6\u95f4\u4e71\u5e8f\u7684\u6d88\u606f\u3002</p>'
    events_list_event_96.local_start = dateutil.parser.parse("2015-08-22T12:45:00")
    events_list_event_96.local_end = dateutil.parser.parse("2015-08-22T17:00:00")
    events_list_event_96.utc_offset = 28800L
    events_list_event_96.is_applicable = True
    events_list_event_96 = importer.save_or_locate(events_list_event_96)

    events_list_event_96.hashtags.add(events_list_hashtag_1)

    events_list_event_97 = Event()
    events_list_event_97.name = u"Apache Spark Startup In Xi'an--2015\u542f\u822a"
    events_list_event_97.event_url = u'http://www.meetup.com/Xian-Apache-Spark-Meetup/events/224326895/'
    events_list_event_97.group = events_list_group_98
    events_list_event_97.meetupID = u'224326895'
    events_list_event_97.description = u'<p>\u897f\u5b89\u4e91\u5f00\u6e90\u793e\u533a\u7ecf\u8fc7\u4e00\u5e74\u7684\u98ce\u96e8\u5386\u7a0b\uff0c\u4ea4\u6d41\u4e86\u6280\u672f\u7ecf\u9a8c\uff0c\u7ed3\u8bc6\u4e86\u5fd7\u8da3\u76f8\u6295\u7684\u4f19\u4f34\uff0c\u5efa\u7acb\u4e86\u4f01\u4e1a\u95f4\u7684\u975e\u5b98\u65b9\u8054\u7cfb\uff0c\u6bcf\u4e00\u4f4d\u53c2\u4e0e\u8005\u90fd\u6709\u7740\u4e0d\u540c\u7a0b\u5ea6\u7684\u6536\u83b7\u2026\u65f6\u81f3\u4eca\u65e5\uff0c\u897f\u5b89\u4e91\u5f00\u6e90\u793e\u533a\u63a8\u51faApache\u65d7\u4e0b\u53c8\u4e00\u7cbe\u54c1\u9879\u76eeSpark\u7684Meetup\uff0c\u9996\u79c0\u65e5\u671f\u5b9a\u5728\u91d1\u79cb\uff0d8.22\uff0c\u6211\u4eec\u671f\u5f85\u7740\u60a8\u7684\u5149\u4e34\uff5e</p> <p>\u4eba\u4eec\u5728\u65e5\u5e38\u751f\u6d3b\u4e2d\u6240\u505a\u7684\u4e00\u5207\u90fd\u4f1a\u7559\u4e0b\u6570\u5b57\u75d5\u8ff9\u6216\u8005\u6570\u636e\uff0c\u4e5f\u5c31\u662f\u5927\u6570\u636e\uff0c\u4eba\u4eec\u53ef\u4ee5\u5229\u7528\u548c\u5206\u6790\u8fd9\u4e9b\u6570\u636e\u6765\u8ba9\u751f\u6d3b\u66f4\u52a0\u4fbf\u5229\u3002\u6bd4\u5982\u5f53\u6211\u4eec\u53bb\u8d2d\u7269\u65f6\uff0c\u6211\u4eec\u7684\u6570\u636e\u4f1a\u7ed3\u5408\u5386\u53f2\u8d2d\u4e70\u8bb0\u5f55\u548c\u793e\u4ea4\u5a92\u4f53\u6570\u636e\u6765\u63d0\u4f9b\u4f18\u60e0\u5238\u3001\u6298\u6263\u548c\u4e2a\u6027\u5316\u4f18\u60e0\u2026\u60f3\u77e5\u9053\u5927\u6570\u636e\u80cc\u540e\u7684\u771f\u76f8\u5417\uff1f\u5230\u5e95\u5de5\u7a0b\u5e08\u4eec\u662f\u600e\u6837\u4ece\u6d77\u91cf\u6570\u636e\u4e2d\u6316\u6398\u6709\u4ef7\u503c\u7684\u4fe1\u606f\uff1f\u8fd9\u4e00\u5207\u53c8\u4f1a\u5bf9\u6211\u4eec\u7684\u751f\u6d3b\uff0c\u5de5\u4f5c\uff0c\u601d\u7ef4\u4ea7\u751f\u4ec0\u4e48\u5f71\u54cd\uff0c\u5e26\u6765\u600e\u6837\u7684\u53d8\u9769\uff1f</p> <p>\u5feb\u6765\u52a0\u51658.22 \u201cXi\u2019an Apache Spark Meet up\u201d \u4f60\u4f1a\u627e\u5230\u5f88\u597d\u7684\u7b54\u6848\uff5e</p> <p>\u6ce8\u610f\uff1a\u5ea7\u4f4d\u6709\u9650\uff0c\u524d60\u540d\u5728meetup\u6ce8\u518c\u62a5\u540d\u4f1a\u5458\uff0c\u9884\u7559\u5ea7\u4f4d\uff5e</p> <p>\u6d3b\u52a8\u8be6\u60c5\uff1a</p> <p>\u65e5\u671f\uff1a2015. 08.22</p> <p>\u65f6\u95f4\uff1a1:45\u2014\u20145:00</p> <p>\u5730\u70b9\uff1a \u9ad8\u65b0\u56db\u8def\u521b\u4e1a\u5e7f\u573aC\u5ea7\u4e00\u5c42DO+\u5496\u5561(\u573a\u5730\u8d5e\u52a9\u8d39\u7528\u7531\u4e9a\u4fe1\u6570\u636e\u63d0\u4f9b)</p> <p><br/>1.Hadoop\u751f\u6001\u5708\u53caSpark\u6280\u672f\u5728\u4f01\u4e1a\u7ea7\u5e02\u573a\u7684\u53d1\u5c55\u65b9\u5411</p> <p>\u4e3b\u8bb2\u4eba\uff1a \u6731\u519b \u4e9a\u4fe1\u6570\u636e\u8d44\u6df1\u4ea7\u54c1\u7ecf\u7406</p> <p>\u7b80\u4ecb\uff1a\u539fIBM Platform Computing\u9ad8\u7ea7\u7814\u53d1\u7ecf\u7406\uff0c\u897f\u5b89\u4e91\u5f00\u6e90\u793e\u533a\u53d1\u8d77\u4eba\u3002<br/>\u81ea1999\u5e74\u4e2d\u79d1\u9662\u8f6f\u4ef6\u6240\u535a\u58eb\u6bd5\u4e1a\u4ee5\u6765\uff0c\u957f\u671f\u81f4\u529b\u4e8e\u5206\u5e03\u5f0f\u6280\u672f\u7814\u7a76\u53ca\u76f8\u5173HPC,\u4e91\u8ba1\u7b97\u53ca\u5927\u6570\u636e\u4ea7\u54c1\u7684\u5f00\u53d1\u8bbe\u8ba1\u3002</p> <p>\u5185\u5bb9\uff1a\u901a\u8fc7\u5bf9Hadoop\u751f\u6001\u5708\u5404\u79cd\u7ec4\u4ef6\u5728\u4f01\u4e1a\u5e94\u7528\u4e2d\u7684\u5b9e\u9645\u60c5\u51b5\uff0c\u63ed\u793aSpark\u7684\u5730\u4f4d\u53ca\u53d1\u5c55\u65b9\u5411\u3002</p> <p>2.\u57fa\u4e8eMllib\u7684\u63a8\u8350\u7cfb\u7edf\u5206\u6790</p> <p>\u4e3b\u8bb2\u4eba\uff1a \u6298\u5efa\u5cf0 \u5168\u901a\u5927\u6570\u636e\u67b6\u6784\u5e08</p> <p>\u7b80\u4ecb\uff1a \u66fe\u4efb\u804c\u4e8eIBM\u8f6f\u4ef6\u90e8\uff0c\u8d1f\u8d23SPSS Analytics Server\u4ea7\u54c1\u7684\u5f00\u53d1\u5de5\u4f5c\u3002\u73b0\u4efb\u804c\u4e0e\u5168\u901a\u6559\u80b2\uff0c\u4ece\u4e8b\u5927\u6570\u636e\u5e73\u53f0\u76f8\u5173\u5de5\u4f5c\u3002\u5177\u6709\u4e30\u5bcc\u7684\u5927\u6570\u636e\u5206\u6790\u53caHadoop\u5f00\u53d1\u7ecf\u9a8c\uff0c\u5bf9\u5206\u5e03\u5f0f\u7cfb\u7edf\uff0c\u6570\u636e\u6316\u6398\u4e0e\u673a\u5668\u5b66\u4e60\u5177\u6709\u6d53\u539a\u5174\u8da3\u3002\u540c\u65f6\u4e5f\u662fApache Spark\u897f\u5b89Meet up\u7684\u53d1\u8d77\u548c\u7ec4\u7ec7\u8005\u3002</p> <p>\u5185\u5bb9\uff1a\u57fa\u4e8esparkmllib\u4e2d\u63a8\u8350\u7cfb\u7edfALS\u7b97\u6cd5\u7684\u5b9e\u73b0\u539f\u7406\u7684\u5206\u6790\uff0c\u4e3e\u4f8b\u6f14\u793a\u3002</p> <p>3.Spark Cloud On Platform Symphony</p> <p>\u4e3b\u8bb2\u4eba\uff1a\u5218\u4fca\u5cf0 IBM platform computing\u67b6\u6784\u5e08</p> <p>\u7b80\u4ecb\uff1bIBM platform computing\u67b6\u6784\u5e08\u3002\u8d1f\u8d23\u8bbe\u8ba1\u5b9e\u65bd\u591a\u4e2aspark\u4e91\u670d\u52a1\uff0c\u5982bluemix super vessel power cloud\u7b49\u3002</p> <p>\u5185\u5bb9\uff1aspark\u5728platform symphony\u5e73\u53f0\u4e0a\u7684\u5b9e\u65bd\u548c\u589e\u5f3a\uff0cbluemix spark service\u662fibm\u9996\u4e2aspark\u5171\u6709\u4e91\u670d\u52a1\uff0c\u5c06\u5728\u4f1a\u8bae\u4e0a\u5206\u4eab\u6280\u672f\u67b6\u6784\u548c\u5fc3\u5f97\u3002</p> <p><b>\u573a\u5730\u8d5e\u52a9\uff1a</b>\u5317\u4eac\u4e9a\u4fe1\u6570\u636e\u6709\u9650\u516c\u53f8\u3002\u96b6\u5c5e\u4e8e\u4e9a\u4fe1\u96c6\u56e2\uff0c\u4ee5\u6570\u636e\u8d44\u4ea7\u4e3a\u6838\u5fc3\uff0c\u4ee5\u201c\u6570\u636e\u3001\u80fd\u529b\u3001\u8d44\u672c\u201d\u4e3a\u7ebd\u5e26\uff0c\u9886\u822a\u4ea7\u4e1a\u5347\u7ea7\uff0c\u521b\u5efa\u4ea7\u4e1a\u751f\u6001\u3002\u4e9a\u4fe1\u6570\u636e\u8fd1\u671f\u63a8\u51fa\u6a58\u4e91\u6570\u636e\u64cd\u4f5c\u5e73\u53f0OCDC3.5, \u4e3a\u7528\u6237\u5728\u5927\u6570\u636e\u4e2d\u5fc3\u642d\u5efa\u7edf\u4e00\u7684\u5206\u5e03\u5f0f\u64cd\u4f5c\u5e73\u53f0\uff0c\u5168\u9762\u5b9e\u73b0\u8d44\u6e90\u5206\u914d\u3001\u5e94\u7528\u7ba1\u7406\u53ca\u6570\u636e\u6cbb\u7406\u63d0\u4f9b\u4e86\u4f01\u4e1a\u7ea7\u4ea7\u54c1\u548c\u670d\u52a1\u3002OCDC\u7684\u4ea7\u54c1\u8bbe\u8ba1\u76ee\u6807\u4e3a\u652f\u6301\u5927\u6570\u636e\u5e94\u7528\u7684\u654f\u6377\u5f00\u53d1\u548c\u667a\u80fd\u8fd0\u7ef4\u3002</p>'
    events_list_event_97.local_start = dateutil.parser.parse("2015-08-22T13:45:00")
    events_list_event_97.local_end = dateutil.parser.parse("2015-08-22T13:45:00")
    events_list_event_97.utc_offset = 28800L
    events_list_event_97.is_applicable = True
    events_list_event_97 = importer.save_or_locate(events_list_event_97)

    events_list_event_97.hashtags.add(events_list_hashtag_1)

    events_list_event_98 = Event()
    events_list_event_98.name = u'Practical tips on running Spark on Hadoop & Machine Learning in the Wild'
    events_list_event_98.event_url = u'http://www.meetup.com/Michigan-Spark-Users-Group/events/224251488/'
    events_list_event_98.group = events_list_group_90
    events_list_event_98.meetupID = u'224251488'
    events_list_event_98.description = u'<p>A frequently asked question in the Big Data community is: "Should I go for Hadoop or Spark?". The focus of this meeting is to address this question and provide some insights into where these systems are headed. In addition, we have a talk on Machine Learning.</p> <p><b>Talk 1 (30 Minutes)</b></p> <p><b>Practical Tips for successfully running Spark in a Hadoop Cluster</b></p> <p>The meeting will start with a talk by <b>Chris Putnam of Cloudera</b>, who will talk about running Spark on Yarn and tips on how to successfully run Spark on a Hadoop Cluster. His\xa0presentation takes a high level look at Spark from a Administrator\u2019s perspective and provides key concepts and tips to support Spark users on the cluster. \xa0\xa0</p> <p>His talk will be followed by a talk on Machine Learning by <b>Chuck Anderson.</b></p> <p><b>Talk 2 (40 Minutes)</b></p> <p><b>Machine learning in the wild: a cautionary tale<br/></b></p> <p>This talk compares logistic regression performance of 5 different open source packages, primarily focusing on Spark. We cover specific cases, applying Spark 1.4 binary classification logisticSGD to different example datasets. We examine these results to illustrate pitfalls that can arise, how to be mindful of them, and ways to avoid them. \xa0<i>There will be\xa0a live demonstration running Spark and processing the example data.</i></p> <p><br/><b>About Speakers:</b></p> <p><b>Chris Putnam</b> is a Systems Engineer with Cloudera.\xa0 He has over 10 years of experience in operational analytics focused in the areas of Customer Analytics and Analytics for IT Operations.\xa0 He is currently working to help demystify Hadoop and Big Data for organizations and help their IT teams operationalize their big data applications and systems.\xa0</p> <p><br/><b>Chuck Anderson</b> -- Chuck\'s career has spanned research, engineering, and product development in pure physical sciences, nonlinear laser spectroscopy, applied sensors, medical device instrumentation and predictive analytics. For as long as he can recall Chuck has enjoyed building and breaking models. He currently uses predictive analytics, applied mathematics, data science, and other tools to build models for UFALLC, based in downtown Ann Arbor.\xa0</p> <p>\n\n\n\n\n\n\n<b>Many thanks to Cloudera and Masco Cabinetry for co-sponsoring this event.</b></p>'
    events_list_event_98.local_start = dateutil.parser.parse("2015-08-20T18:30:00")
    events_list_event_98.local_end = dateutil.parser.parse("2015-08-20T21:00:00")
    events_list_event_98.utc_offset = -14400L
    events_list_event_98.is_applicable = True
    events_list_event_98 = importer.save_or_locate(events_list_event_98)

    events_list_event_98.hashtags.add(events_list_hashtag_1)

    events_list_event_99 = Event()
    events_list_event_99.name = u'August Meetup - Elastic 2.0 (TBC)'
    events_list_event_99.event_url = u'http://www.meetup.com/South-West-ElasticSearch-Community/events/221889219/'
    events_list_event_99.group = events_list_group_91
    events_list_event_99.meetupID = u'221889219'
    events_list_event_99.description = u'<p>Details TBC</p>'
    events_list_event_99.local_start = dateutil.parser.parse("2015-08-20T18:30:00")
    events_list_event_99.local_end = dateutil.parser.parse("2015-08-20T18:30:00")
    events_list_event_99.utc_offset = 3600L
    events_list_event_99.is_applicable = True
    events_list_event_99 = importer.save_or_locate(events_list_event_99)

    events_list_event_99.hashtags.add(events_list_hashtag_1)

    events_list_event_100 = Event()
    events_list_event_100.name = u'Fighting Fraud with Reactive Systems built on Akka, Cassandra, and Spray'
    events_list_event_100.event_url = u'http://www.meetup.com/Toronto-Scala-Typesafe-User-Group/events/224034596/'
    events_list_event_100.group = events_list_group_92
    events_list_event_100.meetupID = u'224034596'
    events_list_event_100.description = u"<p>Join us for another meetup at Paytm Labs.\xa0 This time a member of their Platform Engineering team will present.\xa0 Jacob Park will give us a sneak peak at Paytm's real-time fraud engine platform built with reactive design patterns.\xa0</p> <p><br/>Our second speaker is a stranger to none.\xa0 Katrin from BoldRadius will be returning to present on using Scala.js on the web front end and how to convince your boss to try using it in production!</p> <p><br/><b>Talks</b></p> <p><b>Building a Real-time Fraud Engine at Paytm Labs</b></p> <p>Jacob Park, Platform Engineering, Paytm Labs</p> <p>Paytm Labs has developed a real-time fraud engine utilizing Akka, Cassandra, and Spray at its basis. To suite the requirements of the integrating services, the real-time engine was built to abide by the characteristics defined in the Reactive Manifesto to ensure responsiveness and resiliency.</p> <p>\u2022This talk will explore how Akka, Cassandra, and Spray are candidate technologies to build a Reactive System.</p> <p>\u2022\xa0This talk will explore a basic and a simple design for a real-time engine utilizing HTTP, Environment, and Executor layers inspired by Apache Spark.</p> <p>\u2022\xa0This talk will explore various Akka, Cassandra, and Spray patterns to build such layers effectively.</p> <p>\u2022\xa0This talk will explain various abstractions for concurrency in Scala and the advantages and disadvantages in creating a highly-performant yet predictable Executor layer with considerations of the assumption enforced upon the unit of execution.</p> <p><b>How you convince your manager to adopt Scala.js in production: Take 1.</b></p> <p>Katrin Shechtman, Senior Software Engineer, BoldRadius</p> <p>The talk will present fully functional sample application developed with Scala.js, scalatags, scalacss and other Scala and Typesafe technologies. We aim to show all the pros and cons for having Scala coast-to-coast approach to web-application development and encourage people not to shy away from asking difficult questions challenging this approach. Participants can expect to gain a clear view on the current state of the Scala based client side technologies and take away an activator template with application code that could be used as a base for technical discussions with their peers and managers.</p> <p><b>Tentative schedule</b></p> <p><br/>6:30 Doors Open</p> <p>7:00 Introduction</p> <p>7:05 A message from our hosts.</p> <p>7:10 Jacob Park, Paytm Labs, Building a Real-time Fraud Engine at Paytm Labs</p> <p>7:55 Katrin Shechtman, Senior Software Engineer, BoldRadius, How you convince your manager to adopt Scala.js in production: Take 1</p> <p>8:40 Raffle for IntelliJ license</p> <p>8:45 Social.\xa0 Stick around and get to know your fellow Scala peers</p> <p>Hope to see you there!</p>"
    events_list_event_100.local_start = dateutil.parser.parse("2015-08-20T19:00:00")
    events_list_event_100.local_end = dateutil.parser.parse("2015-08-20T19:00:00")
    events_list_event_100.utc_offset = -14400L
    events_list_event_100.is_applicable = True
    events_list_event_100 = importer.save_or_locate(events_list_event_100)

    events_list_event_100.hashtags.add(events_list_hashtag_1)

    events_list_event_101 = Event()
    events_list_event_101.name = u'The Reverse Grip Knife Training'
    events_list_event_101.event_url = u'http://www.meetup.com/san-antonio-wilderness-living-and-survival/events/222532084/'
    events_list_event_101.group = events_list_group_94
    events_list_event_101.meetupID = u'222532084'
    events_list_event_101.description = u'<p>The reverse grip is often a misunderstood method of using the blade. It is frequently referred to as the grip of the "expert knife fighter." People who have very little knowledge of the knife make statements like that.</p> <p>The reverse grip has its strengths and weaknesses. It\'s important to know both because the reverse grip is an important part of the overall toolbox of those who study the blade. Module 4 of the Patriot Knife Fighting System focuses on Reverse grip knife.</p> <p>In this course the student will learn the Apache Method, drills from the Filipino martial arts, and techniques from the Raven Method of Fernan Vargas.</p> <p>===========================================<br/>The course is part of the full Patriot Knife Fighting certification system, taught by martial arts instructor Tom Howanic. This is Module #4, but there are no pre-requisites to take this course.</p> <p>=============================================<br/><b>Course Information</b><br/>Date: August 22nd, 8 am - 1 pm<br/>Tuition: $40 in advance or $50 at the start of the class. *Pre-registered students will have priority on available spaces in the class.<br/>Pairs\' Discount: 2 for $65, save $15.<br/>Location: San Antonio campus</p>'
    events_list_event_101.local_start = dateutil.parser.parse("2015-08-22T08:00:00")
    events_list_event_101.local_end = dateutil.parser.parse("2015-08-22T13:00:00")
    events_list_event_101.utc_offset = -18000L
    events_list_event_101.is_applicable = True
    events_list_event_101 = importer.save_or_locate(events_list_event_101)

    events_list_event_101.hashtags.add(events_list_hashtag_1)

    events_list_event_102 = Event()
    events_list_event_102.name = u'Spark/Zeppelin \u9a87\u5ba2\u5468\u672b - \u514d\u8d39\u5348\u9910\u8fd8\u6709\u5956\u54c1\uff01'
    events_list_event_102.event_url = u'http://www.meetup.com/spark-user-beijing-Meetup/events/224304959/'
    events_list_event_102.group = events_list_group_99
    events_list_event_102.meetupID = u'224304959'
    events_list_event_102.description = u'<p>\u6b22\u8fce\u53c2\u52a0\u7531\u5317\u4eacSpark\u548cZeppelin\u793e\u533a\u4e3e\u529e\u7684\u9a87\u5ba2\u5468\u672b\uff01\u8ba9\u6211\u4eec\u5728\u8fd9\u4e24\u5929\u4e2dhack\u51fa\u6700cool\u7684Spark\u548cZeppelin\u9879\u76ee\uff01</p> <p>\u65e0\u8bba\u662f\u8981\u62db\u52df\u9879\u76ee\u6210\u5458\u8fd8\u662f\u60f3\u53c2\u52a0\u5230\u4ed6\u4eba\u7684\u9879\u76ee\u4e2d\uff0c\u6b22\u8fce\u6765\u5230\u73b0\u573a\uff01</p> <p>Sejun Ra (NFLabs CEO), Anthony Corbacho (NFLabs &amp; top Zeppelin committer) \u548c Jeff Markham (Hortonworks) \u5c06\u4f1a\u8385\u4e34\u73b0\u573a\uff01</p> <p>\u672c\u6b21\u6d3b\u52a8\u7531\u5fae\u8f6f\u8d5e\u52a9\uff0c\u6211\u4eec\u5c06\u5728\u8fd9\u4e24\u5929\u4e2d\u4e3a\u6240\u6709\u53c2\u4e0e\u8005\u63d0\u4f9b\u514d\u8d39\u5348\u9910\u548c\u96f6\u98df\u996e\u6599\u3002</p> <p>\u524d\u4e09\u540d\u5956\u54c1\uff1a</p> <p>\u7b2c\u4e00\u540d\uff1a\u5fae\u8f6fSculpt\u952e\u9f20\u5957\u88c5</p> <p><img src="http://photos1.meetupstatic.com/photos/event/5/a/d/3/600_440363251.jpeg" /></p> <p>\n\n\n\u7b2c\u4e8c\u540d\uff1a\u8bfa\u57fa\u4e9aX\u624b\u673a</p> <p><img src="http://photos1.meetupstatic.com/photos/event/5/a/d/7/600_440363255.jpeg" /></p> <p>\n\n\n\u7b2c\u4e09\u540d\uff1a\u7f57\u6280H600\u65e0\u7ebf\u8033\u673a</p> <p><img src="http://photos1.meetupstatic.com/photos/event/5/a/d/f/600_440363263.jpeg" /></p> <p>\n\n\n\u8be6\u7ec6\u6d3b\u52a8\u5b89\u6392\u8bf7\u8bbf\u95ee\uff1a <a href="http://beijingsparkcommunity.azurewebsites.net/"><a href="http://beijingsparkcommunity.azurewebsites.net/" class="linkified">http://beijingsparkcommunity.azurewebsites.net/</a></a></p> <p>\u6ce8\u518c\u4f60\u7684\u9879\u76ee\uff1a <a href="https://hackdash.org/dashboards/bj0815"><a href="https://hackdash.org/dashboards/bj0815" class="linkified">https://hackdash.org/dashboards/bj0815</a></a></p> <p>*\u7279\u522b\u63d0\u9192\uff1a\u5c4a\u65f6\u5728\u76f8\u90bb\u7684\u4f1a\u8bae\u5ba4\u5c06\u4e3e\u884cSpark Beijing Meet Up\uff08\u53e6\u884c\u901a\u77e5\uff09\uff0c\u53c2\u8d5b\u9009\u624b\u53ef\u4ee5\u81ea\u7531\u5728Meet Up\u8bb2\u5ea7\u671f\u95f4\u524d\u5f80\u53c2\u52a0\u3002</p> <p><br/>English</p> <p><b>Join the Beijing Spark and Zeppelin community over this 2 day hackathon to hack cool Zeppelin and/or Spark features.</b></p> <p>Whether you have an idea and want to find hackers or have no ideas in mind but want to participate to someone else\u2019s project, join us!</p> <p>Sejun Ra (NFLabs CEO), Anthony Corbacho (NFLabs &amp; top Zeppelin committer) and Jeff Markham (Hortonworks) will attend the event.</p> <p>This event is hosted and sponsored by Microsoft.</p> <p>All hackers will be provided free lunch and refreshments (morning and afternoon) during the event.</p> <p>The best 3 hacks will receive prizes:<br/>1st:\xa0 Microsoft sculpt keyboard and mouse set</p> <p><img src="http://photos1.meetupstatic.com/photos/event/5/a/d/3/600_440363251.jpeg" /></p> <p>\n\n\n2nd: Nokia X phone</p> <p><img src="http://photos1.meetupstatic.com/photos/event/5/a/d/7/600_440363255.jpeg" /></p> <p>\n\n\n3rd : Logitech h600 wireless headset</p> <p><img src="http://photos1.meetupstatic.com/photos/event/5/a/d/f/600_440363263.jpeg" /></p> <p>\n\n\nFull schedule is available here: <a href="http://beijingsparkcommunity.azurewebsites.net/"><a href="http://beijingsparkcommunity.azurewebsites.net/" class="linkified">http://beijingsparkcommunity.azurewebsites.net/</a></a><br/>Register your hack ideas here: <a href="https://hackdash.org/dashboards/bj0815"><a href="https://hackdash.org/dashboards/bj0815" class="linkified">https://hackdash.org/dashboards/bj0815</a></a></p> <p>Note: There will be a Spark/Zeppelin meetup on Saturday at the same location announced separately.</p>'
    events_list_event_102.local_start = dateutil.parser.parse("2015-08-22T08:30:00")
    events_list_event_102.local_end = dateutil.parser.parse("2015-08-23T16:30:00")
    events_list_event_102.utc_offset = 28800L
    events_list_event_102.is_applicable = True
    events_list_event_102 = importer.save_or_locate(events_list_event_102)

    events_list_event_102.hashtags.add(events_list_hashtag_1)

    events_list_event_103 = Event()
    events_list_event_103.name = u'Encontro Grupy-SP de Agosto - G4 Solutions'
    events_list_event_103.event_url = u'http://www.meetup.com/Grupy-SP/events/224049253/'
    events_list_event_103.group = events_list_group_95
    events_list_event_103.meetupID = u'224049253'
    events_list_event_103.description = u'<p>A <b><a href="http://www.g4solutions.com.br/">G4 Solutions</a></b> convida a todos para o pr\xf3ximo encontro do <b>GruPy-SP</b>. Esse encontro ser\xe1 no dia <b>22/08, s\xe1bado, das 9 \xe0s 13 horas</b>.</p> <p>O evento ocorrer\xe1 no audit\xf3rio da Impacta Treinamentos, na Barra Funda.</p> <p><b>Sugerimos a doa\xe7\xe3o de um quilo de alimento n\xe3o perec\xedvel ou uma roupa de frio em bom bom estado.\xa0</b></p> <p><br/><b>Para nosso controle, criamos um simples formul\xe1rio onde deve ser colocado seu nome e o que ser\xe1 doado.\xa0</b></p> <p><b><a href="http://goo.gl/forms/25BJZkGFTc"><a href="http://goo.gl/forms/25BJZkGFTc" class="linkified">http://goo.gl/forms/25BJZkGFTc</a></a><br/></b></p> <p><b>As doa\xe7\xf5es ser\xe3o destinadas ao <a href="https://www.facebook.com/pages/Minist%C3%A9rio-Internacional-Sem-fronteiras/197581793621972?fref=ts">Projeto Social do Minist\xe9rio Internacional Sem Fronteiras</a>.</b></p> <p><br/><b><i>Contamos com sua colabora\xe7\xe3o para ajudar o pr\xf3ximo.</i><br/></b></p> <p>Mais informa\xe7\xf5es sobre a grade de palestras, em breve.</p> <p><b>Submeta sua palestra em: \xa0 </b></p> <p><b><a href="http://call4paperz.com/events/encontro-grupy-sp-agosto-2015" class="linkified">http://call4paperz.com/events/encontro-grupy-sp-agosto-2015</a> </b></p> <p>~ N\xe3o esque\xe7a de informar a dura\xe7\xe3o na descri\xe7\xe3o da submiss\xe3o ~</p> <p>------------------------------------------------------------------</p> <p><b>Grade preliminar do conte\xfado do encontro:</b></p> <p><br/><b>Crawleando dados - Danilo Vaz</b></p> <p>Prova de conceito de como vota\xe7\xf5es e sistemas onlines que utilizam captcha podem ser burladas a fim de consumir servi\xe7os p\xfablicos tais como Receita Federal e Sefaz, utilizando o mesmo m\xe9todo tamb\xe9m para manipular vota\xe7\xf5es que utilizam captcha como prote\xe7\xe3o ou at\xe9 mesmo paginas sem captchas.</p> <p><br/><b>[30 min] (in)Seguran\xe7a Python: SQL Injection like a Pro\' OR \'2\' = \'2 - Rafael Lucas</b></p> <p>Python App Webs geralmente persistem seus dados em SGBDs. O objetivo deste talk \xe9 discutir os cuidados que devem ser tomados contra fragilidades de inje\xe7\xe3o maliciosa de comandos SQL, que podem explorar e comprometer todos os dados de uma aplica\xe7\xe3o. Sendo este o segundo cap\xedtulo sobre valida\xe7\xe3o de dados, ser\xe1 apresentado o Chop\xe3o, um e-commerce divertidamente vulner\xe1vel.Mais SecPy? br.secpy.org</p> <p><br/><b>Computa\xe7\xe3o cient\xedfica com Python - Alexandre Fioravante de Siqueira</b></p> <p>Nesta palestra ser\xe3o abordadas no\xe7\xf5es preliminares de Python voltado \xe0 computa\xe7\xe3o cient\xedfica. Pacotes de extens\xe3o, como numpy, scipy, matplotlib, scikit-learn, scikit-image, entre outros, tamb\xe9m ser\xe3o apresentados. O objetivo \xe9 disseminar o uso de software livre em aplica\xe7\xf5es cient\xedficas por meio de universidades, laborat\xf3rios e institui\xe7\xf5es de ensino.</p> <p><br/><b>Jogando Trabalho pra os outros com ESI - Breno Zan Huke</b></p> <p>Utilizando ESI para -montar o conteudo na borda (akamai,varnish,nginx,apache,CDNs...) -diminuir reprocessamento e consumo desnecess\xe1rio de rede e memoria -jogar a responsabilidade sobre os dados exibidos para... quem fornece eles...</p> <p><br/><b>[30 min] Deploy automatizado no OpenShift com Flask, MongoDB, github e WerckerCI - Bruno Rocha</b></p> <p>Irei mostrar uma aplica\xe7\xe3o web feita com Flask acessando um banco de dados MongoDB sendo "deployada" automaticamente para o OpenShift usando github+werckerCI. Usaremos o plano free do OpenShift.</p> <p><b>[30min] Coffee - Break\xa0</b></p> <p><b>[30 min] Mesa redonda</b></p> <p><b>[30 min]Testes com Selenium - Jayme Neto</b></p> <p>Pretendo mostrar como automatizar testes funcionais rapidamente usando Selenium IDE, Webdriver e Grid e algumas pr\xe1ticas para deixar seu c\xf3digo mais limpo e organizado.</p> <p>\n\n\n<b>[15 min] MongoDB CRUD (Create, Read, Update e Delete) com Pymongo - Rafael Henrique da Silva Correia</b></p> <p>Pretendo explicar o funcionamento das opera\xe7\xf5es b\xe1sicas de CRUD no MongoDB utilizando a biblioteca Pymongo. Nesta LT n\xe3o pretendo abordar vantagens e desvantagens de se usar MongoDB!</p> <p>\n\n\n<b>[30 min] Long polling com Tornado - M\xe1rio Guedes</b></p> <p>Para monitorar mudan\xe7as no lado servidor muitas vezes lan\xe7amos m\xe3o do polling ou seja, v\xe1rias chamadas subsequentes ao servidor, onerando toda a estrutura envolvida. Mostrarei uma forma de implementar o long polling usando o Tornado (n\xe3o blocante) e a facilidade PUB\\SUB do REDIS. Com long polling a chamada REST s\xf3 retorna se houver resposta (200 OK) ou por time-out (304 NOT MODIFIED).</p> <p><br/><b>[15 min]Rob\xf4 JUDITO - A ideia e porqu\xea escolhi o Python - Cleiton Fermino</b></p> <p>Sempre gostei de Intelig\xeancia Artificial, e sempre sonhei em ter meu pr\xf3prio J.A.R.V.I.S, ent\xe3o pensei em iniciar um usando Arduino. Mas pesquisando vi que iria gastar um alto valor com shields e etc. Ent\xe3o pensei em Python + Rasp PI, nisto iniciei os estudos e o desenvolvimento do rob\xf4. Ainda em fase de desenvolvimento, mas espero que consiga demonstrar a ideia e algumas funcionalidades.</p> <p><br/><b>Javascript Para Adultos - Diego Rafael Perin Honorio</b></p> <p>No javascript existem alguns conceitos que nem sempre s\xe3o conhecidos a fundo, diante dessa falta de conhecimento existem v\xe1rias pessoas que passam por v\xe1rios problemas. o seguintes temas: - Hist\xf3rico do javascript; - Fundamentos Javascript; - NodeJS; - ES 6 (Grandes Aprimoramentos na Linguagem);</p> <p><b>[15 min]N\xe3o fa\xe7a isso em casa: um keylogger em Python - Luiz Antonio de Menezes Filho (Joca)</b></p> <p>Nesta palestra mostrarei como criar um keylogger em Python utilizando a biblioteca PyCaptura (criada por mim) que, por sua vez, utiliza a Xlib para realizar a captura do teclado (funciona para as distros linux em geral).</p> <p><br/><b><br/></b></p> <p><b>-------------------------------------------------------------------</b></p> <p><b>Agradecimentos</b></p> <p>Gostar\xedamos de agradecer a G4 Solutions por estar auxiliando na organiza\xe7\xe3o e patroc\xednio desse encontro.</p> <p><b>Datas e hor\xe1rios importantes</b></p> <p>A priori, a submiss\xe3o de palestras e inscri\xe7\xf5es para o pr\xf3ximo encontro se encerrar\xe3o as 12h do dia 20/08. Fiquem atentos.</p> <p><b>Informa\xe7\xf5es</b></p> <p><b>Grupy-SP</b></p> <p><b>Github -</b>\xa0<a href="https://github.com/grupy-sp/encontros"><a href="https://github.com/grupy-sp/encontros" class="linkified">https://github.com/grupy-sp/encontros</a></a><br/><b>Facebook -</b>\xa0<a href="https://www.facebook.com/grupysp"><a href="https://www.facebook.com/grupysp" class="linkified">https://www.facebook.com/grupysp</a></a><br/><b>Twitter -</b>\xa0<a href="https://twitter.com/grupysp"><a href="https://twitter.com/grupysp" class="linkified">https://twitter.com/grupysp</a></a><br/><b>Slack -</b> <a href="https://grupysp.herokuapp.com"><a href="https://grupysp.herokuapp.com" class="linkified">https://grupysp.herokuapp.com</a></a></p> <p><b>Google Groups -</b>\xa0<a href="https://groups.google.com/forum/#!forum/grupy-sp"><a href="https://groups.google.com/forum/#!forum/grupy-sp" class="linkified">https://groups.google.com/forum/#!forum/grupy-sp</a></a></p> <p><b>Python Brasil</b></p> <p><b>Facebook -</b>\xa0<a href="https://www.facebook.com/pythonbrasil"><a href="https://www.facebook.com/pythonbrasil" class="linkified">https://www.facebook.com/pythonbrasil</a></a><br/><b>Twitter -\xa0</b><a href="https://twitter.com/pythonbrasil"><a href="https://twitter.com/pythonbrasil" class="linkified">https://twitter.com/pythonbrasil</a></a><br/><b>Google Groups -\xa0</b><a href="https://groups.google.com/forum/#!forum/python-brasil"><a href="https://groups.google.com/forum/#!forum/python-brasil" class="linkified">https://groups.google.com/forum/#!forum/python-brasil</a></a></p> <p><b>Contatos</b></p> <p><b>Eric Hideki \xa0-</b>\xa0<a href="mailto:[masked]">[masked]</a><br/><b>Diego Garcia -\xa0</b><a href="mailto:[masked]">[masked] </a></p>'
    events_list_event_103.local_start = dateutil.parser.parse("2015-08-22T09:00:00")
    events_list_event_103.local_end = dateutil.parser.parse("2015-08-22T13:00:00")
    events_list_event_103.utc_offset = -10800L
    events_list_event_103.is_applicable = True
    events_list_event_103 = importer.save_or_locate(events_list_event_103)

    events_list_event_103.hashtags.add(events_list_hashtag_1)

    events_list_event_104 = Event()
    events_list_event_104.name = u'A Deep dive into Apache Spark Internals'
    events_list_event_104.event_url = u'http://www.meetup.com/Big-Data-Hyderabad/events/223277944/'
    events_list_event_104.group = events_list_group_157
    events_list_event_104.meetupID = u'223277944'
    events_list_event_104.description = u'<p>As per request from community\xa0members, we have decided to have a Deep dive session of Spark internals.</p> <p>This is going to be a advance level talk/session.</p> <p>Agenda coming soon.</p>'
    events_list_event_104.local_start = dateutil.parser.parse("2015-08-22T09:45:00")
    events_list_event_104.local_end = dateutil.parser.parse("2015-08-22T09:45:00")
    events_list_event_104.utc_offset = 19800L
    events_list_event_104.is_applicable = True
    events_list_event_104 = importer.save_or_locate(events_list_event_104)

    events_list_event_104.hashtags.add(events_list_hashtag_1)

    events_list_event_105 = Event()
    events_list_event_105.name = u'1st London Kaggle meetup hackday'
    events_list_event_105.event_url = u'http://www.meetup.com/London-Kaggle-Meetup/events/223076741/'
    events_list_event_105.group = events_list_group_96
    events_list_event_105.meetupID = u'223076741'
    events_list_event_105.description = u'<p>Welcome to the first London Kaggle meetup. The plan is to get data enthusiasts together to form groups and collaborate on Kaggle competitions.</p> <p><br/>Check out the current competitions\xa0<a href="https://www.kaggle.com/competitions">here</a>.</p> <p>All levels from complete novices to experienced data scientists are welcome at the meetup.</p> <p><br/>If you are a complete novice check out the <a href="https://www.kaggle.com/c/titanic">Titanic tutorials</a></p> <p><br/><b>Agenda</b></p> <p>\u2022 Start arriving from 10:30am</p> <p>\u2022 A short introduction from the organisers</p> <p>\u2022 Hack away</p> <p>\u2022 Break for pizza at 1pm</p> <p>\u2022 Start hacking again!</p> <p><br/>\u2022 Lightning talks from 5pm.</p>'
    events_list_event_105.local_start = dateutil.parser.parse("2015-08-22T10:30:00")
    events_list_event_105.local_end = dateutil.parser.parse("2015-08-22T18:00:00")
    events_list_event_105.utc_offset = 3600L
    events_list_event_105.is_applicable = True
    events_list_event_105 = importer.save_or_locate(events_list_event_105)

    events_list_event_105.hashtags.add(events_list_hashtag_1)

    events_list_event_106 = Event()
    events_list_event_106.name = u'Spark\u5317\u4eacMeetup\u7b2c\u4e5d\u6b21\u6d3b\u52a8\uff0d\uff0dZeppelin\u4e3b\u9898'
    events_list_event_106.event_url = u'http://www.meetup.com/spark-user-beijing-Meetup/events/224469625/'
    events_list_event_106.group = events_list_group_99
    events_list_event_106.meetupID = u'224469625'
    events_list_event_106.description = u'<p>\u65f6\u95f4/Time:\xa0</p> <p>[masked]:00-18:00</p> <p>\u5730\u70b9/Location:\xa0</p> <p>\u5fae\u8f6f\u4e9a\u592a\u7814\u53d1\u96c6\u56e2\u603b\u90e8\u5927\u53a61\u53f7\u697c</p> <p><br/>Microsoft Research Asia (MSR Asia)</p> <p>No.5, Danling Street Haidian</p> <p>\u767e\u5ea6\u5730\u56fe/Online Map: \xa0</p> <p><a href="http://j.map.baidu.com/yVWh0"><a href="http://j.map.baidu.com/yVWh0" class="linkified">http://j.map.baidu.com/yVWh0</a></a>\xa0</p> <p>\u5185\u5bb9/Schedule:</p> <p>\u2022\xa0Keynote</p> <p>\xa0 \xa0 \xa0 Sejun Ra</p> <p>\xa0 \xa0 \xa0 CEO of NFLabs.com</p> <p>\u2022\xa0An introduction to Zeppelin with a demo</p> <p>\xa0 \xa0 \xa0 Anthony Corbacho</p> <p>\xa0 \xa0 \xa0 Engineer from NFLabs and Apache Zeppelin committer</p> <p>\u2022\xa0Apache Kylin introduction and Zeppelin integration</p> <p>\xa0 \xa0 \xa0 Luke Han</p> <p>\xa0 \xa0 \xa0 Apache Kylin committer and PMC member</p> <p>\u2022\xa0Spark on HDP</p> <p>\xa0 \xa0 \xa0 Jeff Markham</p> <p>\xa0 \xa0 \xa0 Technical Director, APAC, Hortonworks</p> <p>\u8bf7\u53c2\u4e0e\u7684\u540c\u5b66\u8ba4\u771f\u586b\u5199\u59d3\u540d\u548c\u5355\u4f4d\u4fe1\u606f, \u8c22\u8c22\u5408\u4f5c</p> <p>Please give us the real name and company for the RSVP Questions, Thanks</p>'
    events_list_event_106.local_start = dateutil.parser.parse("2015-08-22T14:00:00")
    events_list_event_106.local_end = dateutil.parser.parse("2015-08-22T14:00:00")
    events_list_event_106.utc_offset = 28800L
    events_list_event_106.is_applicable = True
    events_list_event_106 = importer.save_or_locate(events_list_event_106)

    events_list_event_106.hashtags.add(events_list_hashtag_1)

    events_list_event_107 = Event()
    events_list_event_107.name = u'Karaoke, Board Game Potluck Lunch'
    events_list_event_107.event_url = u'http://www.meetup.com/South-East-Valley-Filipino-American-Families-and-Friends/events/224411501/'
    events_list_event_107.group = events_list_group_100
    events_list_event_107.meetupID = u'224411501'
    events_list_event_107.description = u"<p>Let's have fun Singing to your hearts delight.. If you rather not sing, you can eat, drink or play any of our board games - Poker, majong, card games, bingo. Feel free to bring your own game. Bring one dollar bills for poker and bingo. Location to be\xa0emailed to you\xa01 to 2 days prior to the event or call Maria at (480)[masked] for location and direction.\xa0 Each family to bring one main dish or one side dish<b> and</b> a dessert. RSVP with a dish to share so we don't all bring the same food and we come home with happy tummies.</p> <p>Btw, the pool is open for swimming or dipping. Bring your friends and family!!!</p> <p>Lastly, a SEVFAF meeting will follow after the event to plan for the Christmas Party. If you are in the core group, please plan on staying. The meeting is open to all.</p> <p>\n\n\n<b>Suggested Menu:</b></p> <p><b>Main Dish</b></p> <p>Chicken, beef or pork adobo</p> <p>Tosino</p> <p>Pancit</p> <p>Lumpia</p> <p>Pizza</p> <p>Lasagna or Pasta dish</p> <p>Fish Dish</p> <p>Barbecue</p> <p>Menudo</p> <p>Sinigang</p> <p>Ribs</p> <p><b>Side Dish</b></p> <p>Rice</p> <p>Bread/Rolls</p> <p>Vegetable Dish</p> <p>Fruit Plate</p> <p><b>Dessert</b></p> <p>Macaroni Salad</p> <p>Palitaw</p> <p>Buko Pie</p> <p>Halo-Halo</p> <p>Turon</p> <p>Cassava Cake</p> <p>Ice Cream</p>"
    events_list_event_107.local_start = dateutil.parser.parse("2015-08-23T12:00:00")
    events_list_event_107.local_end = dateutil.parser.parse("2015-08-23T12:00:00")
    events_list_event_107.utc_offset = -25200L
    events_list_event_107.is_applicable = True
    events_list_event_107 = importer.save_or_locate(events_list_event_107)

    events_list_event_107.hashtags.add(events_list_hashtag_1)

    events_list_event_108 = Event()
    events_list_event_108.name = u'Work on homework in advance; Algorithms: Design and Analysis Week 4'
    events_list_event_108.event_url = u'http://www.meetup.com/StudyGroups/events/224225646/'
    events_list_event_108.group = events_list_group_72
    events_list_event_108.meetupID = u'224225646'
    events_list_event_108.description = u'<p>Algorithm is the foundation of hacking skill. Work on homework in advance. Come to discuss homework:<br/><a href="https://class.coursera.org/algo-008/wiki/Syllabus" class="linkified">https://class.coursera.org/algo-008/wiki/Syllabus</a></p>'
    events_list_event_108.local_start = dateutil.parser.parse("2015-08-23T13:00:00")
    events_list_event_108.local_end = dateutil.parser.parse("2015-08-23T15:00:00")
    events_list_event_108.utc_offset = -25200L
    events_list_event_108.is_applicable = True
    events_list_event_108 = importer.save_or_locate(events_list_event_108)

    events_list_event_108.hashtags.add(events_list_hashtag_1)

    events_list_event_109 = Event()
    events_list_event_109.name = u'Apache Phoenix'
    events_list_event_109.event_url = u'http://www.meetup.com/ambariCloud-Big-Data-Meetup/events/223891255/'
    events_list_event_109.group = events_list_group_101
    events_list_event_109.meetupID = u'223891255'
    events_list_event_109.description = u'<p>1. Why Phoenix on Hbase<br/>2. Demo You will learn how to build SQL on NoSQL Hbase database.</p>'
    events_list_event_109.local_start = dateutil.parser.parse("2015-08-23T14:00:00")
    events_list_event_109.local_end = dateutil.parser.parse("2015-08-23T14:00:00")
    events_list_event_109.utc_offset = -18000L
    events_list_event_109.is_applicable = True
    events_list_event_109 = importer.save_or_locate(events_list_event_109)

    events_list_event_109.hashtags.add(events_list_hashtag_1)

    events_list_event_110 = Event()
    events_list_event_110.name = u'Work on a Data Science Project Together'
    events_list_event_110.event_url = u'http://www.meetup.com/StudyGroups/events/223605568/'
    events_list_event_110.group = events_list_group_72
    events_list_event_110.meetupID = u'223605568'
    events_list_event_110.description = u'<p>Why not form a group and work on a data science project together?</p> <p>Please bring your laptop and work\xa0on a project for a couple of hours, whether it is\xa0<a href="https://docs.google.com/document/d/1jKgqR944e0Ak8idLz8r3l6GkXtZzOjyb5meBIyIZCek/edit?usp=sharing">a self designed project</a>\xa0or a Kaggle project.</p>'
    events_list_event_110.local_start = dateutil.parser.parse("2015-08-23T14:30:00")
    events_list_event_110.local_end = dateutil.parser.parse("2015-08-23T16:30:00")
    events_list_event_110.utc_offset = -25200L
    events_list_event_110.is_applicable = True
    events_list_event_110 = importer.save_or_locate(events_list_event_110)

    events_list_event_110.hashtags.add(events_list_hashtag_1)

    events_list_event_111 = Event()
    events_list_event_111.name = u'Apache Spark 101 and Smart Cities and Big Data'
    events_list_event_111.event_url = u'http://www.meetup.com/Sydney-Big-Data-and-Analytics/events/224418400/'
    events_list_event_111.group = events_list_group_102
    events_list_event_111.meetupID = u'224418400'
    events_list_event_111.description = u'<p>In this meetup we will cover two separate topics.</p> <p><br/>The first one will introduce Apache Spark one of the fast developing <a href="https://en.wikipedia.org/wiki/Open-source_software">open-source</a> cluster computing frameworks.</p> <p><br/>The second one will show an example how Big Data could help us build smart cities. We will share an end to end architectural overview of a potential live solution with live demo.</p>'
    events_list_event_111.local_start = dateutil.parser.parse("2015-08-24T18:30:00")
    events_list_event_111.local_end = dateutil.parser.parse("2015-08-24T18:30:00")
    events_list_event_111.utc_offset = 36000L
    events_list_event_111.is_applicable = True
    events_list_event_111 = importer.save_or_locate(events_list_event_111)

    events_list_event_111.hashtags.add(events_list_hashtag_1)

    events_list_event_112 = Event()
    events_list_event_112.name = u'See how Propeller Health utilizes Big Data'
    events_list_event_112.event_url = u'http://www.meetup.com/BigDataMadison/events/220142969/'
    events_list_event_112.group = events_list_group_104
    events_list_event_112.meetupID = u'220142969'
    events_list_event_112.description = u'<p>Propeller Health will present on a use case of how they use Big Data at their organization.\xa0</p> <p>Anurati Mathur is a Data Scientist who works with Propeller Health\u2019s clinical and product data. She will be sharing the process of analyzing and visualizing geospatial data from Propeller Health\u2019s program in Louisville, Kentucky; including how the team:</p> <p><br/>- Collected, cleansed, and de-identified data\xa0</p> <p>- Discovered trends &amp; correlations with relevant external data layers</p> <p>- Visualized a compelling story to share with the public. \xa0We combined our raw inhaler use data with publicly available geo-shapefiles. We were able to prototype using QGIS &amp; Tableau, and then build out a time-lapsed visualization using D3 &amp; Mapbox.</p> <p><br/>Headquartered in Madison, Propeller Health is the leading digital health platform for asthma and COPD. Through sensors, mobile apps, analytics, and services, Propeller Health continuously tracks inhaler use &amp; helps reduce the cost of care while delivering better quality of life for individuals with chronic respiratory disease.\xa0</p> <p><br/>Cloudera is sponsoring food and drink for this meetup.</p>'
    events_list_event_112.local_start = dateutil.parser.parse("2015-08-25T18:00:00")
    events_list_event_112.local_end = dateutil.parser.parse("2015-08-25T18:00:00")
    events_list_event_112.utc_offset = -18000L
    events_list_event_112.is_applicable = True
    events_list_event_112 = importer.save_or_locate(events_list_event_112)

    events_list_event_112.hashtags.add(events_list_hashtag_1)

    events_list_event_113 = Event()
    events_list_event_113.name = u'Hands On Intro to Machine Learning with Spark'
    events_list_event_113.event_url = u'http://www.meetup.com/Melbourne-Apache-Spark-Meetup/events/224245425/'
    events_list_event_113.group = events_list_group_105
    events_list_event_113.meetupID = u'224245425'
    events_list_event_113.description = u"<p>Spark is creating a lot of excitement in the machine learning community because the integrated nature of the ecosystem seems to offer true support for the end-to-end analytical lifecycle on big data volumes - from exploration and visualisation through training to scoring - in a way that nothing else does.\xa0</p> <p>During the evening, you will explore a dataset, train a simple machine learning model and test it's predictions on a holdout set - all in Spark.</p> <p>Prerequisites to enjoy the Meetup</p> <p>\u2022 Some familiarity with the basic concepts of machine learning (e.g. linear regression, simple decision trees)</p> <p>\u2022 Some hands on experience\xa0with basic data wrangling in Spark</p> <p>More details to follow.</p>"
    events_list_event_113.local_start = dateutil.parser.parse("2015-08-25T18:00:00")
    events_list_event_113.local_end = dateutil.parser.parse("2015-08-25T18:00:00")
    events_list_event_113.utc_offset = 36000L
    events_list_event_113.is_applicable = True
    events_list_event_113 = importer.save_or_locate(events_list_event_113)

    events_list_event_113.hashtags.add(events_list_hashtag_1)

    events_list_event_114 = Event()
    events_list_event_114.name = u'Intro to Meteor'
    events_list_event_114.event_url = u'http://www.meetup.com/Houston-Meteor-Meetup/events/224055402/'
    events_list_event_114.group = events_list_group_106
    events_list_event_114.meetupID = u'224055402'
    events_list_event_114.description = u'<p>6:30 Intro to Meteor - Covers the basics of what Meteor is, why it was created, and why to use it.</p> <p><br/>7:00 Q&amp;A or Meteor Tutorial walk through, this will be at crowd request. \xa0</p>'
    events_list_event_114.local_start = dateutil.parser.parse("2015-08-25T18:00:00")
    events_list_event_114.local_end = dateutil.parser.parse("2015-08-25T18:00:00")
    events_list_event_114.utc_offset = -18000L
    events_list_event_114.is_applicable = True
    events_list_event_114 = importer.save_or_locate(events_list_event_114)

    events_list_event_114.hashtags.add(events_list_hashtag_1)

    events_list_event_115 = Event()
    events_list_event_115.name = u'Our First Solr Meetup - Plus a talk on Autosuggest!'
    events_list_event_115.event_url = u'http://www.meetup.com/solr-sg/events/224369520/'
    events_list_event_115.group = events_list_group_107
    events_list_event_115.meetupID = u'224369520'
    events_list_event_115.description = u"<p>Hey everyone, our first Solr SG meetup is here!\xa0This'll be a great chance to get to meet more people in the search community.</p> <p>Plus, I'll give a talk on a couple of ways to add autosuggest in Solr, the pros &amp; cons of each, and an example of what we did for a recent client in Singapore.\xa0</p> <p>I'm currently still looking for a venue to host this event. If you know anyone that can help out let me know. I'll send an update when a venue is confirmed.</p> <p>Looking forward!</p>"
    events_list_event_115.local_start = dateutil.parser.parse("2015-08-25T18:30:00")
    events_list_event_115.local_end = dateutil.parser.parse("2015-08-25T20:30:00")
    events_list_event_115.utc_offset = 28800L
    events_list_event_115.is_applicable = True
    events_list_event_115 = importer.save_or_locate(events_list_event_115)

    events_list_event_115.hashtags.add(events_list_hashtag_1)

    events_list_event_116 = Event()
    events_list_event_116.name = u'Tomcat Overview with Mark Thomas'
    events_list_event_116.event_url = u'http://www.meetup.com/Toronto-Pivotal-User-Group/events/222492685/'
    events_list_event_116.group = events_list_group_119
    events_list_event_116.meetupID = u'222492685'
    events_list_event_116.description = u"<p>We are lucky to get Mark Thomas in town for this meeting. Mark is one of the premier Tomcat experts in the world. The details of the session will be posted as we approach the date, however you can expect a Tomcat 9 overview and a Q &amp; A period with Mark where you can ask all your Tomcat related questions. Hope to see you all there.</p> <p>Here is Mark's bio:</p> <p>I have been an Apache Tomcat committer since November 2003. I initially worked on Tomcat in my free time but since August 2008 I have been employed by Pivotal (formerly SpringSource). I spend most of my time on Tomcat but I also work on tc Server, Pivotal's Servlet &amp; JSP container based on Tomcat. Additionally, I lead the Pivotal security team.<br/>I am the Tomcat 8 release manager and I try to release every month. I am currently focused on Tomcat 9 development which will support Servlet 4.0 (including HTTP/2) and is expected to also include updated JSP, EL and WebSocket support (I am a member of the relevant JCP expert groups). Elsewhere at the ASF, I am a member of the ASF security and infrastructure teams and I am on the Commons PMC where I focus on Commons Pool and DBCP. I am a member of the ASF.\xa0</p>"
    events_list_event_116.local_start = dateutil.parser.parse("2015-08-26T19:00:00")
    events_list_event_116.local_end = dateutil.parser.parse("2015-08-26T19:00:00")
    events_list_event_116.utc_offset = -14400L
    events_list_event_116.is_applicable = True
    events_list_event_116 = importer.save_or_locate(events_list_event_116)

    events_list_event_116.hashtags.add(events_list_hashtag_1)

    events_list_event_117 = Event()
    events_list_event_117.name = u'Elasticsearch Meetup'
    events_list_event_117.event_url = u'http://www.meetup.com/ElasticSearch-Usergroup-Frankfurt/events/223558349/'
    events_list_event_117.group = events_list_group_120
    events_list_event_117.meetupID = u'223558349'
    events_list_event_117.description = u'<p>Hallo zusammen,</p> <p>ich freue mich sehr, das n\xe4chste Meetup der Elasticsearch Usergroup Frankfurt anzuk\xfcndigen, wenn auch vorerst nur den Termin.</p> <p><br/>Nach aktueller Planung werden wir drei Talks rund um das Thema Elasticsearch anbieten, die exakten Themen werden aktuell noch festgezurrt und bald nachgereicht.</p> <p>Eine Location hat uns freundlicherweise die codecentric AG\xa0 angeboten.</p> <p><br/>F\xfcr alle denen Ende August noch zu lange hin ist wird es zwischendurch noch ein "Social Meetup" ohne Talks geben, dass zum Kennenlernen und Erfahrungsaustausch gedacht ist. Der Termin wird in K\xfcrze bekanntgegeben.</p> <p><br/>Ich w\xfcrde mich freuen viele von euch wiederzusehen, aber nat\xfcrlich auch, viele neue Gesichter zu sehen!</p> <p>\n\n\nBeste Gr\xfc\xdfe,</p> <p>\xa0S\xf6nke</p> <p>------</p> <p>Hi all,</p> <p>it is with great pleasure that I announce the date of the next Elasticsearch Frankfurt Usergroup meetup.</p> <p>We will have at least three talks on topics from the Elasticsearch ecosystem, the precise titles are still being worked out, but will be announced soon.</p> <p>The meetup will take place in the offices of the codecentric AG.</p> <p><br/>And finally, if the end of August seems a long time to wait, we will have a social gathering in the interim, with no talks but a focus on getting to know each other and swapping experiences.</p> <p>I look forward to seeing lots of you again as well as meeting many new people!</p> <p>Regards,</p> <p>S\xf6nke</p>'
    events_list_event_117.local_start = dateutil.parser.parse("2015-08-26T19:00:00")
    events_list_event_117.local_end = dateutil.parser.parse("2015-08-26T19:00:00")
    events_list_event_117.utc_offset = 7200L
    events_list_event_117.is_applicable = True
    events_list_event_117 = importer.save_or_locate(events_list_event_117)

    events_list_event_117.hashtags.add(events_list_hashtag_1)

    events_list_event_118 = Event()
    events_list_event_118.name = u'Developer Meetup: Why understanding how Spark is built helps the community'
    events_list_event_118.event_url = u'http://www.meetup.com/spark-users/events/223632544/'
    events_list_event_118.group = events_list_group_108
    events_list_event_118.meetupID = u'223632544'
    events_list_event_118.description = u"<p>Developer Talk: Why understanding how Spark is built helps the developer community. Detailed abstract and speaker bio below. This talk will be filmed and posted on the Apache Spark YouTube page.</p> <p><br/>Agenda:</p> <p>6:30 - 7:00 :: Mingling</p> <p>7:00 - 7:05 :: Welcome</p> <p>7:05 - 8:15 :: Technical talk</p> <p>8:15 - 9:00 :: Mingling</p> <p>To enter the building: At security \u2013 let them know you are there for the Spark Meetup and need to go to Capital One \u2013 5th\xa0Floor. All guests must register once on the 5th floor.</p> <p><br/>Abstract: Ever wonder what goes into building, testing, and maintaining a codebase such as Spark? Building a system that others can contribute to pain-free out of the box is a daunting task, but one that, when done right, engages the community and fosters long term growth. In this talk we'll discuss how Spark has conquered those problems, lessons learned along the way, and how we're moving forward to continue making development for Spark easier within the community.</p> <p><br/>Specifically we'll discuss:* Why understanding how Spark is built helps the developer community* The tools that've been created to ease the build burden* A walk through of the `dev/run-tests(-jenkins)` scripts and how to diagnose errors</p> <p><br/>This talk will be aimed primarily at developers seeking to contribute to Spark, anyone wanting to better understand Spark's build and CI environment, or anyone (developer or otherwise) looking at the possibility of building custom Spark forks for their organization.</p> <p>\n\n\nBrennon York will be our speaker, he is an aspiring aerobatic pilot moonlighting as a data engineer at Capital One. His true loves are distributed computing, scalable architectures, and programming languages. He's been working hard to make Spark a stronger community and inspire collaboration through his efforts on GraphX and the core build environment.</p>"
    events_list_event_118.local_start = dateutil.parser.parse("2015-08-25T18:30:00")
    events_list_event_118.local_end = dateutil.parser.parse("2015-08-25T18:30:00")
    events_list_event_118.utc_offset = -25200L
    events_list_event_118.is_applicable = True
    events_list_event_118 = importer.save_or_locate(events_list_event_118)

    events_list_event_118.hashtags.add(events_list_hashtag_1)

    events_list_event_119 = Event()
    events_list_event_119.name = u'DrupalGap'
    events_list_event_119.event_url = u'http://www.meetup.com/laphonegap/events/223542898/'
    events_list_event_119.group = events_list_group_32
    events_list_event_119.meetupID = u'223542898'
    events_list_event_119.description = u'<p><a href="http://www.drupalgap.org/u/tylerfrankenstein" class="linkified">http://www.drupalgap.org/u/tylerfrankenstein</a></p>'
    events_list_event_119.local_start = dateutil.parser.parse("2015-08-25T18:30:00")
    events_list_event_119.local_end = dateutil.parser.parse("2015-08-25T21:30:00")
    events_list_event_119.utc_offset = -25200L
    events_list_event_119.is_applicable = True
    events_list_event_119 = importer.save_or_locate(events_list_event_119)

    events_list_event_119.hashtags.add(events_list_hashtag_1)

    events_list_event_120 = Event()
    events_list_event_120.name = u'Talk: Apache Storm Vs. Apache Spark'
    events_list_event_120.event_url = u'http://www.meetup.com/south-west-data/events/224285174/'
    events_list_event_120.group = events_list_group_109
    events_list_event_120.meetupID = u'224285174'
    events_list_event_120.description = u"<p>There has been lots of excitement recently around stream and real time processing with Big Data. \xa0Two great stream processing technologies are Apache Storm and Apache Spark.</p> <p>But which one should you choose, and what are the differences?</p> <p>Our speaker on the topic will be Andrew Carr, CEO of automated data analytics software Claritize.</p> <p>We'll be based in the Pervasive Media Studios (located in the Watershed) for the talk and questions, which will be followed by a more relaxed discussion over a drink or two at the Watershed bar.</p>"
    events_list_event_120.local_start = dateutil.parser.parse("2015-08-25T19:00:00")
    events_list_event_120.local_end = dateutil.parser.parse("2015-08-25T19:00:00")
    events_list_event_120.utc_offset = 3600L
    events_list_event_120.is_applicable = True
    events_list_event_120 = importer.save_or_locate(events_list_event_120)

    events_list_event_120.hashtags.add(events_list_hashtag_1)

    events_list_event_121 = Event()
    events_list_event_121.name = u'MongoDB 3.0 Deep Dive + Riak'
    events_list_event_121.event_url = u'http://www.meetup.com/Seattle-Scalability-Meetup/events/222229243/'
    events_list_event_121.group = events_list_group_121
    events_list_event_121.meetupID = u'krbrflytlbjc'
    events_list_event_121.description = u'<p>This meetup focuses on Scalability and technologies to enable handling large amounts of data: Hadoop, HBase, distributed NoSQL databases, and more!</p> <p>There\'s not only a focus on technology, but also everything surrounding it including operations, management, business use cases, and more.</p> <p>We\'ve had great success in the past, and are growing quickly! Previous guests were from Twitter, LinkedIn, Amazon, Cloudant, Microsoft, 10gen/MongoDB, and more.</p> <p><b>This month\'s guests:</b></p> <p><b>Bryan Reinero is a Developer Advocate for MongoDB,<br/></b></p> <p>MongoDB Version 3.0: A Deep Dive.\xa0Released last March, version 3.0 brings a host of new capability to MongoDB including the Wired Tiger storage engine and the pluggable storage engine API. MongoDB 3.0 features improvements in concurrency as well as compression and lock-free algorithms via Wired Tiger. We\'ll explore all these new features, their impact on performance, and dive into the mechanics of MongoDB\'s latest release.\xa0</p> <p>\n\nBryan Reinero is a Developer Advocate for MongoDB, helping the community of users grow. Formerly a Senior Consulting Engineer at MongoDB, Bryan helped users optimize MongoDB for scale and performance and a was contributor to the Java Driver. Earlier, Bryan was Software Engineering Manager at Valueclick, building and managing large scale marketing applications for advertising, retargeting, real-time bidding and campaign optimization. Earlier still, Bryan specialized in software for embedded systems at Ricoh Corporation and developed data analysis and signal processing software at the Experimental Physics Branch of Ames Research Center.\xa0</p> <p>\n\n\n<b>Sargun Dhillon is a Software Engineer for Riak.\xa0</b></p> <p>In this talk I will dive into the coming challenges with the datacenter as a computer. Why we need massively distributed databases that are fault tolerant to node failure--and how geodiversity has an effect upon how we build the Riak database. Specifically, we will walk through. \xa0</p> <p>1. What are the coming challenges with databases?<br/>2.\xa0Why do AP, distributed databases make sense?<br/>3.\xa0Why do we need certain tools (CRDTs) to help us use these AP databases in a reasonable fashion?</p> <p>\n\nSargun Dhillon (@sargun) has a background in operations, and distributed systems, specifically in the area of infrastructure. Previous to this, he\'s worked at companies such as Microsoft, Yammer, and deCarta, which was later acquired by Uber. There he was responsible for operations, as well as infrastructure. In addition to this, he\'s built out systems that operate at warehouse scale across multiple datacenters. Given this background, he spends much of his time thinking about how to make massively distributed, scalable systems friendlier to run.\xa0</p> <p><br/>Our format is flexible: We usually have 2 speakers who talk for ~30 minutes each and then do Q+A plus discussion (about 45 minutes each talk) finish by 8:45.</p> <p>There\'ll be beer afterwards, of course!</p> <p>Meetup Location:</p> <p><a href="http://maps.google.com/maps?q=1301+5th+Avenue+%231700%2C+Seattle%2C+WA">Whitepages</a>,[masked]th Avenue #1600, Seattle, WA</p> <p>After-beer Location: Rock Bottom\xa0Rainier Square (same building)</p> <p>Doors open 30 minutes ahead of show-time. Please show up at least 15 minutes early out of respect for our first speaker.</p>'
    events_list_event_121.local_start = dateutil.parser.parse("2015-08-26T19:00:00")
    events_list_event_121.local_end = dateutil.parser.parse("2015-08-26T19:00:00")
    events_list_event_121.utc_offset = -25200L
    events_list_event_121.is_applicable = True
    events_list_event_121 = importer.save_or_locate(events_list_event_121)

    events_list_event_121.hashtags.add(events_list_hashtag_1)

    events_list_event_122 = Event()
    events_list_event_122.name = u'Big Data - No Fluff - lets get started with Hadoop #2'
    events_list_event_122.event_url = u'http://www.meetup.com/Oslo-Hadoop-Big-Data-Meetup/events/222587835/'
    events_list_event_122.group = events_list_group_122
    events_list_event_122.meetupID = u'mmpzglytkbdb'
    events_list_event_122.description = u'<p>Meetup #2: At the second Oslo Hadoop Big Data meetup we will build on the last meetup experience! With not only even nicer soup ;-) but presenting even more knowledge and information along with more practical examples and introduction to Big Data via Hadoop! Also we will have much more fun with French keyboards!!</p> <p>We are also interested to find some core Big Data Vikings to help support the group and ensure we build a healthy open community. Just contact me if you have any questions or would like to contribute or support. Lars(Nitro) also has an open challenge if anyone can beat his intro video!!</p> <p>And of course Scotsman and the famous Big Data Ninja Quiz and Beer!!! Its time to knock Nitro(Lars) off his top spot!!!!!</p> <p>Agenda: (under construction as we Speak)</p> <p>1. Introduction and Welcome</p> <p>2. Big Data - No Fluff</p> <p>3. Hortonworks Full Pack!!! Everything you always wanted to know but were too afraid to ask!</p> <p>4. Klarna Sweden - 2 years with Hadoop and onwards - Erik shares all</p> <p>5. More how to get started<br/>i. Setting up your first Sandbox<br/>ii. Building your first Cluster</p> <p>5. Open Discussion Panel</p> <p>Big Data Quiz and Beer @ Scotsman</p>'
    events_list_event_122.local_start = dateutil.parser.parse("2015-08-27T17:30:00")
    events_list_event_122.local_end = dateutil.parser.parse("2015-08-27T20:15:00")
    events_list_event_122.utc_offset = 7200L
    events_list_event_122.is_applicable = True
    events_list_event_122 = importer.save_or_locate(events_list_event_122)

    events_list_event_122.hashtags.add(events_list_hashtag_1)

    events_list_event_123 = Event()
    events_list_event_123.name = u'TRAINING - Be the next top Cassandra Model-ler'
    events_list_event_123.event_url = u'http://www.meetup.com/Melbourne-Cassandra-Users/events/223688798/'
    events_list_event_123.group = events_list_group_123
    events_list_event_123.meetupID = u'223688798'
    events_list_event_123.description = u'<p><img src="http://photos2.meetupstatic.com/photos/event/4/3/c/0/600_440357344.jpeg" /></p> <p>This will be run as a training session aimed at developers but also caters to ops engineers who would like to understand how Cassandra works under the hood.</p> <p><br/>Pizza, beer and softdrinks will be served.</p> <p>More details to follow. Please feel free to post a comment if you have any questions.</p>'
    events_list_event_123.local_start = dateutil.parser.parse("2015-08-27T18:00:00")
    events_list_event_123.local_end = dateutil.parser.parse("2015-08-27T18:00:00")
    events_list_event_123.utc_offset = 36000L
    events_list_event_123.is_applicable = True
    events_list_event_123 = importer.save_or_locate(events_list_event_123)

    events_list_event_123.hashtags.add(events_list_hashtag_1)

    events_list_event_124 = Event()
    events_list_event_124.name = u'August CHUG Event: Overview of the upcoming Apache Atlas project'
    events_list_event_124.event_url = u'http://www.meetup.com/CharlotteHUG/events/219153236/'
    events_list_event_124.group = events_list_group_110
    events_list_event_124.meetupID = u'219153236'
    events_list_event_124.description = u"<p>Dave Callahan (2C data) is teaming up with Hortonworks for this month's presentation on the upcoming Apache Atlas, a part of the Data Governance Initiative.\xa0</p> <p>Discussion Topic:\xa0</p> <p>As enterprises across all major industries deploy Hadoop into corporate data and processing environments, a common approach to working with metadata and data governance becomes a necessity. \xa0Apache Atlas was created by a consortium of enterprises to meet this need. Atlas enhances governance capabilities in Hadoop for both prescriptive and forensic models enriched by taxonomical metadata. Atlas, at its core, is designed to exchange metadata with other tools and processes within and outside of the Hadoop stack. Atlas enables platform-agnostic governance controls that effectively address enterprise compliance requirements.</p> <p>\n\n\nSpeaker's bio:\xa0</p> <p>Dave Callaghan is a\xa0Modern Data Innovator at 2C Data.</p> <p>He is responsible for helping companies successfully implement and realize measurable value from their Big Data, Fast Data and NoSQL implementations.</p> <p>On the Big Data batch process\xa0side, he's certified in and worked extensively with, and occasionally extend,\xa0the entire\xa0Hadoop ecosystem as well as Cassandra.\xa0</p> <p>On the Fast Data streaming side, he's implemented solutions\xa0using Storm, Spark and Kafka streaming with both\xa0Java and Scala\xa0</p> <p>He is currently focused on\xa0working with and contributing to the new data governance initiative platform applications like Falcon and Ranger and ultimately Apache Atlas.\xa0</p> <p>He also brings modest\xa0data science skills, mostly using R, Weka and Watson.\xa0</p>"
    events_list_event_124.local_start = dateutil.parser.parse("2015-08-26T18:00:00")
    events_list_event_124.local_end = dateutil.parser.parse("2015-08-26T18:00:00")
    events_list_event_124.utc_offset = -14400L
    events_list_event_124.is_applicable = True
    events_list_event_124 = importer.save_or_locate(events_list_event_124)

    events_list_event_124.hashtags.add(events_list_hashtag_1)

    events_list_event_125 = Event()
    events_list_event_125.name = u'Spark and Hadoop in Production - Real Life Stories'
    events_list_event_125.event_url = u'http://www.meetup.com/Pepperdata/events/224407137/'
    events_list_event_125.group = events_list_group_111
    events_list_event_125.meetupID = u'224407137'
    events_list_event_125.description = u'<p>This meetup will feature a series of short presentations by industry experts, highlighting real life use cases where Spark and Hadoop have been used together in production environments. We\'ll touch on some of the drivers behind using these 2 platforms together, as well as key considerations and best practices to ensure you have a successful deployment.</p> <p>Speakers will include technical experts from MAPR, Altiscale, and Pepperdata.</p> <p>After the short presentation round-robin, we will open it up to Q&amp;A from the audience. Come prepared with any questions you want answered from the experts!</p> <p>Food &amp; drinks will be provided. \xa0</p> <p>Hope to see you there!</p> <p>\n\n\n<img src="http://photos1.meetupstatic.com/photos/event/9/5/7/7/600_440558263.jpeg" /></p> <p><img src="http://photos1.meetupstatic.com/photos/event/9/5/9/d/600_440558301.jpeg" /></p>'
    events_list_event_125.local_start = dateutil.parser.parse("2015-08-26T18:00:00")
    events_list_event_125.local_end = dateutil.parser.parse("2015-08-26T18:00:00")
    events_list_event_125.utc_offset = -25200L
    events_list_event_125.is_applicable = True
    events_list_event_125 = importer.save_or_locate(events_list_event_125)

    events_list_event_125.hashtags.add(events_list_hashtag_1)

    events_list_event_126 = Event()
    events_list_event_126.name = u'Google Cloud Platform Roadshow Ha Noi'
    events_list_event_126.event_url = u'http://www.meetup.com/Google-Developer-Group-Ha-Noi/events/224324654/'
    events_list_event_126.group = events_list_group_112
    events_list_event_126.meetupID = u'224324654'
    events_list_event_126.description = u'<p><img src="http://photos4.meetupstatic.com/photos/event/9/c/1/a/600_440379962.jpeg" /></p> <p>\u2022\xa0<b><i>\u2022\xa0</i>Agenda:</b></p> <p><b><br/></b></p> <p>\u2022\xa0<b>15 min: Registration</b></p> <p><br/>\u2022\xa0<b>10 min: Welcome\xa0</b></p> <p><br/><b>\u2022\xa045 min: Firebase - Build Extraordinary Apps</b></p> <p><b><br/></b></p> <p>Firebase is a new member of Google Cloud Platform, but a proven tool for creating real-time experiences. Firebase is the fastest way to build your app. Come and learn how you can build applications quickly without managing complex infrastructure.</p> <p>\n\n\n\u2022\xa0<b>45 min: Modern DevOps with GCP</b></p> <p><b><br/></b></p> <p>In this talk I will discuss different ways of developing and operating infrastructures for web services, also referred to as DevOps. This will include topics such as infrastructure provisioning, continuous integration, application deployment, and monitoring. GCP services such as load-balancing and BigQuery, which are useful for improving efficiency of various DevOps processes, will also be covered. Finally, I will introduce Mackerel, a server monitoring SaaS that functions as a hub of actions pertaining to DevOps.</p> <p>\n\n\n\u2022\xa0<b>45 min: Your Data and the World Beyond MapReduce</b></p> <p><br/>Google\'s MapReduce has been the most important innovation in the Big Data industry in last decade, which provided the technical foundation for Apache Hadoop MapReduce and other solutions. But at Google, we have moved to next generation technologies such as Dremel, Flume and MillWheel that replace the classic MapReduce infrastructure. In this session, we will introduce two products from Google Cloud Platform, BigQuery and Cloud Dataflow, that allow developers to leverage the power of the Google\'s latest Big Data technologies.</p> <p><br/>\u2022\xa0<b>20 min: Q&amp;A and Networking</b></p> <p><b><br/></b></p> <p>\u2022\xa0<b>\u2022\xa0Speakers for Vietnam events</b></p> <p><img src="http://photos3.meetupstatic.com/photos/event/9/b/f/9/600_440379929.jpeg" /></p> <p><b><br/></b></p> <p>\u2022\xa0<b>Kazunori Sato</b> is a Developer Advocate at Cloud Platform team, Google Inc. He works as an advocate for Google Cloud Platform developer communities in Asia for, such as GCP User Group (GCPUG), #bq_sushi, and gcp ja night. He also supports Big Data product launch such as Cloud Dataflow and BigQuery.</p> <p><br/><img src="http://photos1.meetupstatic.com/photos/event/9/c/0/c/600_440379948.jpeg" /></p> <p>\u2022\xa0<b>Shinji Tanaka</b> is the Chief Technology Officer at Hatena Co., Ltd. Hatena provides a variety of web-based services including Hatena Blog, and Hatena Bookmark. Launched in 2014, Hatena\u2019s newest service, Mackerel, is a cloud management SaaS.Shinji is responsible for the technology behind all of Hatena\u2019s services from front-end to infrastructure.</p>'
    events_list_event_126.local_start = dateutil.parser.parse("2015-08-26T18:00:00")
    events_list_event_126.local_end = dateutil.parser.parse("2015-08-26T21:00:00")
    events_list_event_126.utc_offset = 25200L
    events_list_event_126.is_applicable = True
    events_list_event_126 = importer.save_or_locate(events_list_event_126)

    events_list_event_126.hashtags.add(events_list_hashtag_1)

    events_list_event_127 = Event()
    events_list_event_127.name = u'Infinite Session Clustering with Cassandra'
    events_list_event_127.event_url = u'http://www.meetup.com/CassandraSF/events/222667575/'
    events_list_event_127.group = events_list_group_113
    events_list_event_127.meetupID = u'dtnrggytlbjc'
    events_list_event_127.description = u'<p>For this meetup we are excited to be joined by Les Hazlewood,\xa0Stormpath co-founder and CTO and the Apache Shiro PMC Chair who will be discussing infinite session clustering with Cassandra.</p> <p><b>What You\'ll Learn At This Meetup:</b></p> <p>Les Hazlewood, the Apache Shiro PMC Chair, will cover Shiro\'s enterprise session management capabilities, how it can be used across any application (not just web or JEE applications) and how to use\xa0Cassandra as Shiro\'s session store, enabling a distributed session cluster supporting hundreds of thousands or even millions of concurrent sessions. As a working example, Les will show how to set up a session cluster in under 10 minutes using\xa0Cassandra. If you need to scale user session load, you won\'t want to miss this!</p> <p><br/><b>About Les Hazlewood:</b></p> <p>Les Hazlewood is Stormpath co-founder and CTO and the Apache Shiro PMC Chair.\xa0Prior to forming Stormpath, Les held senior architectural positions at Bloomberg and Delta Airlines and he was former CTO of a software engineering firm supporting educational and government agencies. Les has been actively involved in Open Source for more than 10 years, committing or contributing to projects like the Spring Framework, JBoss, and Apache Shiro. Les has a BS in Computer Science from Georgia Tech, and practices Kendo and studies Japanese when he\'s not coding.</p> <p><br/>*Thank you Stormpath for sponsoring food and drinks and to Disqus for hosting!</p> <p>*Cassandra Summit is less than 2 months away! For those of you who haven\'t registered yet, you can find more info and register <a href="http://cassandrasummit-datastax.com">here</a>. You can also use the code MeetupPromo to get 50% off priority passes!</p>'
    events_list_event_127.local_start = dateutil.parser.parse("2015-08-26T18:30:00")
    events_list_event_127.local_end = dateutil.parser.parse("2015-08-26T18:30:00")
    events_list_event_127.utc_offset = -25200L
    events_list_event_127.is_applicable = True
    events_list_event_127 = importer.save_or_locate(events_list_event_127)

    events_list_event_127.hashtags.add(events_list_hashtag_1)

    events_list_event_128 = Event()
    events_list_event_128.name = u'Apache Ignite\u2122 (incubating) - In-Memory Data Fabric'
    events_list_event_128.event_url = u'http://www.meetup.com/eastbayjug/events/223440590/'
    events_list_event_128.group = events_list_group_114
    events_list_event_128.meetupID = u'223440590'
    events_list_event_128.description = u'<p>Agenda:</p> <p>\u2022\xa06.30-7pm - networking and pizza\xa0</p> <p>\u2022\xa07pm-9pm - presentation\xa0</p> <p>This presentation will provide a deep dive into new Apache project:\xa0<a href="https://ignite.incubator.apache.org/">Apache Ignite</a>.\xa0Apache Ignite is the in-memory data fabric that combines in-memory cluster &amp; computing, in-memory data grid and in-memory streaming under one umbrella of a fabric. In-memory data fabric slides between applications and various data sources and provides ultimate performance and scalability to the applications. Apache Ignite is the first general purpose in-memory computing platform in Apache Software Foundation family. We believe it will have same effect on Fast Data processing as Hadoop has on Big Data processing. Better understanding of inner details behind Apache Ignite will hopefully encourage more companies and individual committers to join the project.</p> <p><b>Bio:</b></p> <p>Nikita Ivanov is founder of Apache Ignite project and CTO of GridGain Systems, started in 2007. Nikita has led GridGain to develop advanced and distributed in-memory data processing technologies \u2013 the top Java in-memory data fabric starting every 10 seconds around the world today.</p> <p>Nikita has over 20 years of experience in software application development, building HPC and middleware platforms, contributing to the efforts of other startups and notable companies including Adaptec, Visa and BEA Systems. Nikita was one of the pioneers in using Java technology for server side middleware development while working for one of Europe\u2019s largest system integrators in 1996.</p> <p>He is an active member of Java middleware community, contributor to the Java specification. He\u2019s also frequent international speaker with over two dozens of talks on various developers conferences globally in the last 3 years.</p>'
    events_list_event_128.local_start = dateutil.parser.parse("2015-08-26T18:30:00")
    events_list_event_128.local_end = dateutil.parser.parse("2015-08-26T18:30:00")
    events_list_event_128.utc_offset = -25200L
    events_list_event_128.is_applicable = True
    events_list_event_128 = importer.save_or_locate(events_list_event_128)

    events_list_event_128.hashtags.add(events_list_hashtag_1)

    events_list_event_129 = Event()
    events_list_event_129.name = u'Using Composer for WordPress Site Setup'
    events_list_event_129.event_url = u'http://www.meetup.com/atlanta-wordpress-coders-guild/events/221439272/'
    events_list_event_129.group = events_list_group_115
    events_list_event_129.meetupID = u'221439272'
    events_list_event_129.description = u'<p>For our August 2015 workshop we will cover using Composer for Site Setup.</p> <p><b>Date/Time/Location T.B.D. : Please make suggestions in the comments below for date, time, area of town, and facility(especially if you can host.)\xa0</b></p> <p>You can <b>RSVP to reserve a spot </b>and <b>cancel for full refund</b> if our date/time/location does not work for you. After we set date/time/location we will not refund on cancellation.</p> <p><b>16 attendees max</b> - So RSVP early.</p>'
    events_list_event_129.local_start = dateutil.parser.parse("2015-08-26T18:30:00")
    events_list_event_129.local_end = dateutil.parser.parse("2015-08-26T18:30:00")
    events_list_event_129.utc_offset = -14400L
    events_list_event_129.is_applicable = True
    events_list_event_129 = importer.save_or_locate(events_list_event_129)

    events_list_event_129.hashtags.add(events_list_hashtag_1)

    events_list_event_130 = Event()
    events_list_event_130.name = u'Bay Area Search'
    events_list_event_130.event_url = u'http://www.meetup.com/Bay-Area-Search/events/220396634/'
    events_list_event_130.group = events_list_group_116
    events_list_event_130.meetupID = u'lgjpclytlbjc'
    events_list_event_130.description = u'<p>6:30 Eat &amp; Greet</p> <p>7:00 Talk -\xa0Great speakers, good food, free beer.</p> <p>Event will be held at the eBay campus just off 17/880 @ Hamilton in the main Community building. \xa0Look for lobby/flagpole.</p> <p>Wifi: eBayGuest/#WeAreeBay</p> <p>We are always looking for speakers. \xa0Please suggest speakers or topics you would like to hear.</p> <p>Recordings for past talks on our youtube channel :\xa0<a href="https://www.youtube.com/channel/UCbv6D3Wwfp0qMI7nRD1V-Gw" class="embedded">https://www.youtube.com/channel/UCbv6D3Wwfp0qMI7nRD1V-Gw</a></p>'
    events_list_event_130.local_start = dateutil.parser.parse("2015-08-26T18:30:00")
    events_list_event_130.local_end = dateutil.parser.parse("2015-08-26T18:30:00")
    events_list_event_130.utc_offset = -25200L
    events_list_event_130.is_applicable = True
    events_list_event_130 = importer.save_or_locate(events_list_event_130)

    events_list_event_130.hashtags.add(events_list_hashtag_1)

    events_list_event_131 = Event()
    events_list_event_131.name = u'Flink Meetup #10 Cluster Deployment on Docker, Flink - Gelly, Community Update'
    events_list_event_131.event_url = u'http://www.meetup.com/Apache-Flink-Meetup/events/223913365/'
    events_list_event_131.group = events_list_group_117
    events_list_event_131.meetupID = u'223913365'
    events_list_event_131.description = u'<p><b><img src="http://photos2.meetupstatic.com/photos/event/7/9/d/0/600_438691184.jpeg" /></b></p> <p>Join us at the 10th <a href="https://flink.apache.org/">Apache Flink</a> Meetup, drinks and sandwiches sponsored by <a href="http://data-artisans.com/">data Artisans</a>.</p> <p><b>Talks:</b></p> <p><b>1. Flink Community Update</b><br/>By Robert Metzger</p> <p><b>2. Apache Flink cluster deployment on Docker using Docker-Compose<br/></b>By Romeo Kienzler</p> <p>Often resource requirements on Data Processing Clusters exhibit high variation. So in this case elastic deployments reduce total cost of ownership. In this talk we will introduce the basic concepts on container isolation exemplified on Docker and explain how Apache Flink is made elastic using Docker-Compose. Finally we push the cluster to the cloud exemplified on the IBM Docker Cloud.</p> <p><b>3. Graph Processing with Apache Flink </b><br/>By Andra Lungu</p> <p>Gelly is Flink\'s large-scale graph processing API which leverages Flink\'s efficient delta iterations to map various graph processing models (vertex-centric and gather-sum-apply) to dataflows. Gelly allows Flink users to perform end-to-end data analysis, without having to build complex pipelines and combine different systems. It can be seamlessly combined with Flink\'s DataSet API, which means that pre-processing, graph creation, graph analysis and post-processing can be done in the same application.</p> <p><br/>--------</p> <p><br/><b>Bring your data </b></p> <p>After the talks, while having a drink, there\'s the opportunity to work together with Flink committers on an interesting data problem you\'re facing.</p> <p>Please contact Kostas Tzoumas at kostas@data-<br/>artisans.com if you\'re interested in taking part in this!</p> <p><br/>--------</p> <p><b>About Robert</b></p> <p>Robert Metzger is a PMC member at Apache Flink and co-founder and software engineer at data Artisans. Robert studied Computer Science at TU Berlin and worked at IBM Germany and at the IBM Almaden Research Center in San Jose.</p> <p><b><br/>About Romeo</b></p> <p>Romeo Kienzler holds a Master Degree in Information Systems, Applied Statistics and Bioinformatics from the Swiss Federal Institute of Technology. He works for IBM Zurich as a Data Scientist and Architect.</p> <p><b>About Andra</b></p> <p>Andra Lungu is one of the committers behind Flink\'s graph processing API, Gelly. She is a student research assistant at TU-Berlin (DIMA), currently working on her master thesis, which proposes a set of operators meant to scale up computations on highly skewed graphs while minimizing the number of messages sent from one vertex to another. Andra began her first year of Master studies in Rennes, France and completed her Bachelor studies at the Technical University of Bucharest, Romania. During her university years, she interned for Adobe Systems and Endava.</p> <p><br/>---------</p>'
    events_list_event_131.local_start = dateutil.parser.parse("2015-08-26T19:00:00")
    events_list_event_131.local_end = dateutil.parser.parse("2015-08-26T22:00:00")
    events_list_event_131.utc_offset = 7200L
    events_list_event_131.is_applicable = True
    events_list_event_131 = importer.save_or_locate(events_list_event_131)

    events_list_event_131.hashtags.add(events_list_hashtag_1)

    events_list_event_132 = Event()
    events_list_event_132.name = u'Indy Big Data Monthly Meetup'
    events_list_event_132.event_url = u'http://www.meetup.com/IndyBigData/events/224258916/'
    events_list_event_132.group = events_list_group_118
    events_list_event_132.meetupID = u'dlqcwjytlbjc'
    events_list_event_132.description = u'<p>Agenda coming...</p>'
    events_list_event_132.local_start = dateutil.parser.parse("2015-08-26T19:00:00")
    events_list_event_132.local_end = dateutil.parser.parse("2015-08-26T19:00:00")
    events_list_event_132.utc_offset = -14400L
    events_list_event_132.is_applicable = True
    events_list_event_132 = importer.save_or_locate(events_list_event_132)

    events_list_event_132.hashtags.add(events_list_hashtag_1)

    events_list_event_133 = Event()
    events_list_event_133.name = u'Apache Tomcat 9 Preview'
    events_list_event_133.event_url = u'http://www.meetup.com/Toronto-Java-Users-Group/events/223134356/'
    events_list_event_133.group = events_list_group_124
    events_list_event_133.meetupID = u'dmscthytlbkc'
    events_list_event_133.description = u"<p>Our Presenter this moth is Mark Thomas Apache Tomcat Committer who will be giving us a Preview of Tomcat 9.</p> <p>Development of the next major release of Tomcat 9 is well underway with significant improvements to TLS support, basic support for HTTP/2 and a host of other improvements. In addition, Tomcat 9 will support the new JavaEE 8 specifications including the possible inclusion of Reactive Streams support in Servlet 4.0. This presentation will provide an overview of what these new features and enhancements mean for users of Tomcat and provide an insight into the current roadmap for Tomcat 9 development.</p> <p><br/>Here is Mark introducing himself in his own words.</p> <p><br/>I have been an Apache Tomcat committer since November 2003. I initially worked on Tomcat in my free time but since August 2008 I have been employed by Pivotal (formerly SpringSource). I spend most of my time on Tomcat but I also work on tc Server, Pivotal's Servlet &amp; JSP container based on Tomcat. Additionally, I lead the Pivotal security team.<br/>I am the Tomcat 8 release manager and I try to release every month. I am currently focused on Tomcat 9 development which will support Servlet 4.0 (including HTTP/2) and is expected to also include updated JSP, EL and WebSocket support (I am a member of the relevant JCP expert groups). Elsewhere at the ASF, I am a member of the ASF security and infrastructure teams and I am on the Commons PMC where I focus on Commons Pool and DBCP. I am a member of the ASF.\xa0</p>"
    events_list_event_133.local_start = dateutil.parser.parse("2015-08-27T18:30:00")
    events_list_event_133.local_end = dateutil.parser.parse("2015-08-27T18:30:00")
    events_list_event_133.utc_offset = -14400L
    events_list_event_133.is_applicable = True
    events_list_event_133 = importer.save_or_locate(events_list_event_133)

    events_list_event_133.hashtags.add(events_list_hashtag_1)

    events_list_event_134 = Event()
    events_list_event_134.name = u'Kick-off  Social at The Winery Restaurant Tustin'
    events_list_event_134.event_url = u'http://www.meetup.com/SoCal-Talend-Meetup/events/224277064/'
    events_list_event_134.group = events_list_group_125
    events_list_event_134.meetupID = u'224277064'
    events_list_event_134.description = u'<p>Please join us for drinks and appetizers as we celebrate the start of the SoCal Talend Meetup.</p> <p><br/>This will be an opportunity for members to meet each other in a casual environment and discuss future Meetup topics and agendas.</p>'
    events_list_event_134.local_start = dateutil.parser.parse("2015-08-27T18:30:00")
    events_list_event_134.local_end = dateutil.parser.parse("2015-08-27T20:30:00")
    events_list_event_134.utc_offset = -25200L
    events_list_event_134.is_applicable = True
    events_list_event_134 = importer.save_or_locate(events_list_event_134)

    events_list_event_134.hashtags.add(events_list_hashtag_1)

    events_list_event_135 = Event()
    events_list_event_135.name = u'\u0418\u043d\u0434\u0435\u043a\u0441\u043d\u044b\u0435 \u0441\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u044b \u0434\u0430\u043d\u043d\u044b\u0445 \u0432 \u0440\u0435\u043b\u044f\u0446\u0438\u043e\u043d\u043d\u044b\u0445 \u0421\u0423\u0411\u0414 \u0438 \u043f\u043e\u0438\u0441\u043a\u043e\u0432\u044b\u0445 \u0441\u0438\u0441\u0442\u0435\u043c\u0430\u0445'
    events_list_event_135.event_url = u'http://www.meetup.com/bigmoscow/events/224231490/'
    events_list_event_135.group = events_list_group_126
    events_list_event_135.meetupID = u'224231490'
    events_list_event_135.description = u'<p>\u0412\u0441\u0435 \u043c\u044b \u0437\u043d\u0430\u0435\u043c, \u0447\u0442\u043e \u0438\u043d\u0434\u0435\u043a\u0441\u044b \u043d\u0435\u043e\u0442\u0435\u043c\u043b\u0438\u043c\u0430\u044f \u0447\u0430\u0441\u0442\u044c \u043b\u044e\u0431\u043e\u0439 \u0440\u0435\u043b\u044f\u0446\u0438\u043e\u043d\u043d\u043e\u0439 \u0421\u0423\u0411\u0414. \u0424\u0430\u043a\u0442 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u044f \u0438\u043d\u0434\u0435\u043a\u0441\u043e\u0432 \u0432 \u043f\u043e\u0438\u0441\u043a\u043e\u0432\u0438\u043a\u0430\u0445 \u0442\u0430\u043a \u0436\u0435 \u043d\u0438 \u0434\u043b\u044f \u043a\u043e\u0433\u043e \u043d\u0435 \u0441\u0435\u043a\u0440\u0435\u0442.</p> <p>\u0422\u0435\u043c \u043d\u0435 \u043c\u0435\u043d\u0435\u0435,\xa0 \u0435\u0441\u043b\u0438 \u043a\u043e\u043f\u043d\u0443\u0442\u044c \u0433\u043b\u0443\u0431\u0436\u0435, \u0441\u0440\u0430\u0437\u0443 \u0432\u0441\u043f\u043b\u044b\u0432\u0430\u044e\u0442 \u0432\u043e\u043f\u0440\u043e\u0441\u044b, \u043e\u0442\u0432\u0435\u0442\u044b \u043d\u0430 \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u043e\u0442\u043d\u044e\u0434\u044c \u043d\u0435 \u0442\u0430\u043a \u0448\u0438\u0440\u043e\u043a\u043e \u0438\u0437\u0432\u0435\u0441\u0442\u043d\u044b.</p> <p>\u2022\xa0\u041a\u0430\u043a\u0438\u0435 \u0432\u0438\u0434\u044b \u0438\u043d\u0434\u0435\u043a\u0441\u043e\u0432 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u044e\u0442\u0441\u044f \u0434\u043b\u044f \u0440\u0430\u0437\u043b\u0438\u0447\u043d\u044b\u0445 \u0437\u0430\u0434\u0430\u0447?\xa0</p> <p>\u2022\xa0\u041a\u0430\u043a\u0438\u0435 \u0441\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u044b \u0434\u0430\u043d\u043d\u044b\u0445 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u044e\u0442\u0441\u044f \u0434\u043b\u044f \u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f \u0438\u043d\u0434\u0435\u043a\u0441\u043e\u0432?</p> <p>\u2022\xa0\u041a\u0430\u043a \u0438\u043c\u0435\u043d\u043d\u043e \u0438\u043d\u0434\u0435\u043a\u0441\u044b \u0443\u0447\u0430\u0441\u0442\u0432\u0443\u044e\u0442 \u0432 \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u0435 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f \u0437\u0430\u043f\u0440\u043e\u0441\u0430?</p> <p>\u0412 \u044d\u0442\u043e\u043c \u0434\u043e\u043a\u043b\u0430\u0434\u0435 \u043c\u044b \u043e\u0441\u0432\u0435\u0442\u0438\u043c \u043e\u0441\u043e\u0431\u0435\u043d\u043d\u043e\u0441\u0442\u0438 \u0440\u0435\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u0438 \u0438\u043d\u0434\u0435\u043a\u0441\u043e\u0432 \u0432 \u0440\u0430\u0437\u043b\u0438\u0447\u043d\u044b\u0445 \u0441\u0438\u0441\u0442\u0435\u043c\u0430\u0445.</p> <p><i>\u0414\u043c\u0438\u0442\u0440\u0438\u0439 \u0420\u0435\u043c\u0438\u0437\u043e\u0432</i> \u0440\u0430\u0441\u0441\u043a\u0430\u0436\u0435\u0442 \u043f\u0440\u043e \u0441\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u0443 \u0438\u043d\u0434\u0435\u043a\u0441\u043e\u0432 \u0432 \u0421\u0423\u0411\u0414 Oracle.</p> <p><i>\u0410\u043b\u0435\u043a\u0441\u0435\u0439 \u0420\u0430\u0433\u043e\u0437\u0438\u043d</i> \u0440\u0430\u0441\u0441\u043a\u0430\u0436\u0435\u0442 \u043f\u0440\u043e \u0438\u043d\u0434\u0435\u043a\u0441\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0434\u0430\u043d\u043d\u044b\u0445 \u0432 key-value \u0445\u0440\u0430\u043d\u0438\u043b\u0438\u0449\u0430\u0445 (\u043d\u0430 \u043f\u0440\u0438\u043c\u0435\u0440\u0435 Oracle Coherence) \u0438 \u043f\u043e\u043b\u043d\u043e\u0442\u0435\u043a\u0441\u0442\u043e\u0432\u043e\u043c \u043f\u043e\u0438\u0441\u043a\u0435 (Apache Lucene)</p>'
    events_list_event_135.local_start = dateutil.parser.parse("2015-08-27T18:30:00")
    events_list_event_135.local_end = dateutil.parser.parse("2015-08-27T18:30:00")
    events_list_event_135.utc_offset = 14400L
    events_list_event_135.is_applicable = True
    events_list_event_135 = importer.save_or_locate(events_list_event_135)

    events_list_event_135.hashtags.add(events_list_hashtag_1)

    events_list_event_136 = Event()
    events_list_event_136.name = u'Come learn about PigPen - Data Engineering with Clojure and Hadoop'
    events_list_event_136.event_url = u'http://www.meetup.com/cascading/events/224050557/'
    events_list_event_136.group = events_list_group_127
    events_list_event_136.meetupID = u'224050557'
    events_list_event_136.description = u"<p>PigPen is <b>Clojure</b> for big data, or distributed Clojure. You write idiomatic Clojure code, we translate it to Cascading (or Apache Pig) and run it on thousands of machines. PigPen provides a seamless mesh between the code used to build your pipeline and the code running remotely. It does this by capturing lexical closures and packaging them for evaluation later, so your map-reduce applications now look and feel like they're running on a single machine. Gone are the days of verbose UDFs being defined elsewhere and manual context sharing. PigPen allows you develop your jobs iteratively (and locally) using the Clojure REPL and also to write unit and generative tests using the existing Clojure frameworks.</p> <p><br/>PigPen brings the simplicity and elegance of Clojure to big data.</p> <p>About the Speaker:</p> <p>Matt Bossenbroek works at <b>Netflix</b> on the Personalization &amp; Search team. He helps to manage the data pipelines that deliver the Netflix you know &amp; love. He is a Clojure enthusiast, writing PigPen and other internal Netflix libraries in Clojure, working to spread the language throughout the company. Previously he worked at Microsoft, doing basically the same thing in c# (sans OSS).</p> <p><br/><i>Agenda:\xa0</i></p> <p>\u2022\xa0<i>6:30pm-Registration</i></p> <p><i>\u2022\xa07pm- Talks Start</i></p> <p><i>(Food and Drinks provided)</i></p>"
    events_list_event_136.local_start = dateutil.parser.parse("2015-08-27T18:30:00")
    events_list_event_136.local_end = dateutil.parser.parse("2015-08-27T21:00:00")
    events_list_event_136.utc_offset = -25200L
    events_list_event_136.is_applicable = True
    events_list_event_136 = importer.save_or_locate(events_list_event_136)

    events_list_event_136.hashtags.add(events_list_hashtag_1)

    events_list_event_137 = Event()
    events_list_event_137.name = u'Bill Ayers - Mobile Development with Visual Studio 2015'
    events_list_event_137.event_url = u'http://www.meetup.com/Derbyshire-Dot-Net/events/223681560/'
    events_list_event_137.group = events_list_group_128
    events_list_event_137.meetupID = u'223681560'
    events_list_event_137.description = u'<p>Users are going mobile and they don\u2019t want to browse websites \u2013 they want apps! And they want them on their Android and iOS and, yes, Windows phones and tablets. So what are the options? Do you need to get the Java books out again? Or take a trip back to the 1990s and learn Objective C? Or are you going to chase the \u201cwrite once, run everywhere\u201d dream?</p> <p>I\u2019m going to run through the options for mobile development using Visual Studio including the Windows Universal Platform, Xamarin and Apache Cordova, without the need to learn how to use native development environments. With cross-platform development there is an element of compromise and there is no ideal solution for all situations, so I will help you make some choices. I will show how to get the most out of the tooling and get as near as possible to cross-platform Nirvana with minimum effort. And I\'ll show some tips, tricks and traps that will save you hours of frustration when it comes to getting your apps published.</p> <p>Bill Ayers is a consultant developer and solution architect who specializes in collaboration and Intranet portals and mobile solutions with a particular focus on agile software development practices. He is a Microsoft Certified Master and Charter MCSM for SharePoint, and a Microsoft Certified Trainer. He has over 20 years\u2019 experience in the software industry, and speaks regularly at international conferences and user groups. He is also a moderator on SharePoint.StackExchange.com, and blogs at\xa0<a href="http://spdoctor.net/"><a href="http://SPDoctor.net/" class="linkified">http://SPDoctor.net/</a></a>. He is based in Sheffield, UK.</p>'
    events_list_event_137.local_start = dateutil.parser.parse("2015-08-27T18:30:00")
    events_list_event_137.local_end = dateutil.parser.parse("2015-08-27T18:30:00")
    events_list_event_137.utc_offset = 3600L
    events_list_event_137.is_applicable = True
    events_list_event_137 = importer.save_or_locate(events_list_event_137)

    events_list_event_137.hashtags.add(events_list_hashtag_1)

    events_list_event_138 = Event()
    events_list_event_138.name = u'Distributed Stream and Graph Processing with Apache Flink'
    events_list_event_138.event_url = u'http://www.meetup.com/Bay-Area-Apache-Flink-Meetup/events/224189524/'
    events_list_event_138.group = events_list_group_73
    events_list_event_138.meetupID = u'224189524'
    events_list_event_138.description = u'<p>In this meetup we will present talks about real streaming an graph processing with Apache Flink. Also will present research and future projects related to Apache Flink.</p> <p>Please join us on this great opportunity to learn more about Apache Flink</p> <p><b>Apache Flink community update\xa0- Henry</b></p> <p>Will present the current community updates for Apache Flink including releases, community growth, new features, adoptions, and meetups happening.</p> <p><b>Stateful distributed stream processing</b>\xa0<b>-</b>\xa0<b>Gyula</b></p> <p>More complex streaming applications generally need to store some state of the running computations in a fault-tolerant manner. This talk discusses the concept of operator state and compares state management in current stream processing frameworks such as Apache Flink Streaming, Apache Spark Streaming, Apache Storm and Apache Samza.</p> <p>We will go over the recent changes in Flink streaming that introduce a unique set of tools to manage state in a scalable, fault-tolerant way backed by a lightweight asynchronous checkpointing algorithm.</p> <p><b>When Micro-batching Isn\'t Good Enough - Ted</b></p> <p>I will describe several use cases where batch and micro batch processing is not appropriate and describe why this is so. \xa0</p> <p>I will also describe what a true streaming solution needs to provide for solving these problems.</p> <p>These use cases will be taken from real industrial situations, but the descriptions will drive down to technical details as well.</p> <p>\n\n<b>Large-Scale Graph Analysis with Apache Flink</b> <b>- Vasia</b></p> <p>This talk will give an ove\xa0rview of Flink\u2019s Graph processing API, Gelly. We will discuss how iterative operators and other unique features of Flink make it a competitive alternative for large-scale graph processing. We will show how one can elegantly express graph analysis tasks, using common Flink operators and how different graph processing models, like vertex-centric and gather-sum-apply, can be easily mapped to Flink dataflows.</p> <p><br/><b>Looking Forward - Apahe Flink research preview/roadmap</b> <b>- Paris</b></p> <p>In this talk we will give a broad preview of the research behind Flink and the fundamentals we are working on to make Flink a use-case complete system for data processing. The topics we will cover will be incremental checkpointing, windowing optimisations, machine learning pipeline design and streaming graph analytics on Flink.</p> <p>Finally, we will introduce Karamel (<a href="http://karamel.io/">karamel.io</a>), a new way of deploying and reproducing experiments with Flink on EC2, GCC, Openstack and bare metal.</p> <p><br/><b>Proposed Schedule</b></p> <p>6:30pm-7pm Door open and socialize</p> <p>7pm-9pm Talks</p> <p><br/><b>Bio of Speakers</b></p> <p>\u2022\xa0Henry Saputra</p> <p>Henry is a PMC member for the Apache Flink and also member of the Apache Software Foundation. Henry also member of Apache Incubator PMC and former mentor of Apache Flink while still in incubation.</p> <p>Currently Henry is working on distributed systems and big data application platforms.</p> <p>\u2022\xa0Gyula F\xf3ra</p> <p>Gyula is a PMC member for the Apache Flink project, currently working as a researcher at the Swedish Institute of Computer Science. His main expertise and interest is real-time distributed data processing frameworks, and their connections to other big data applications. He is a core architect of Apache Flink Streaming. His current work includes research and development on several aspects of stream processing, including fault-tolerance, efficient windowing computations and streaming machine learning.</p> <p>\u2022\xa0Vasia Kalavri</p> <p>Vasia Kalavri is a PhD student at KTH, Stockholm, doing research on distributed data processing, systems optimization and large\xad-scale graph analysis. She is also a \xa0PMC member of Apache Flink, mainly working on Flink\'s graph processing API, Gelly.</p> <p>\u2022\xa0Paris Carbone</p> <p>Paris is a PhD student in distributed computing at the Royal Institute of Technology in Sweden and a committer for Apache Flink. His work is focused on abstractions, domain specific languages and architectures towards scalable, expressive and cost-effective distributed data stream processing.</p> <p>\u2022\xa0Ted Dunning - Chief Application Architect, MapR\xa0</p> <p>Ted Dunning is Chief Application Architect at MapR Technologies and committer and PMC member of the Apache Mahout, Apache ZooKeeper, and Apache Drill projects . Ted has been very active in mentoring new Apache projects and is currently serving as vice president of incubation for the Apache Software Foundation . \xa0Ted was the chief architect behind the MusicMatch (now Yahoo Music) and Veoh recommendation systems. He built fraud detection systems for ID Analytics (LifeLock) and he has 24 patents issued to date and a dozen pending. Ted has a PhD in computing science from the University of Sheffield. When he\u2019s not doing data science, he plays guitar and mandolin. He also bought the beer at the first Hadoop user group meeting.</p>'
    events_list_event_138.local_start = dateutil.parser.parse("2015-08-27T19:00:00")
    events_list_event_138.local_end = dateutil.parser.parse("2015-08-27T19:00:00")
    events_list_event_138.utc_offset = -25200L
    events_list_event_138.is_applicable = True
    events_list_event_138 = importer.save_or_locate(events_list_event_138)

    events_list_event_138.hashtags.add(events_list_hashtag_1)

    events_list_event_139 = Event()
    events_list_event_139.name = u'Data Science meets Software Development AND Is Apache Spark Ready for the Cloud?'
    events_list_event_139.event_url = u'http://www.meetup.com/bigdatadc/events/223863127/'
    events_list_event_139.group = events_list_group_129
    events_list_event_139.meetupID = u'223863127'
    events_list_event_139.description = u'<p>Hi Big Data DC, we have a double feature co-organized with\xa0<a href="http://www.meetup.com/Washington-DC-Area-Spark-Interactive/">Washington DC Area Apache Spark Interactive</a>\xa0for you.\xa0</p> <p><b>Summary:\xa0</b>Data Science meets Software Development</p> <p><br/>Alexis works in a Data Innovation Lab with a horde of Data Scientists. Data Scientists gather data, clean data, apply Machine Learning algorithms and produce results, all of that with specialized tools (Dataiku, Scikit-Learn, R...). These processes run on a single machine, on data that is fixed in time, and they have no constraint on execution speed.</p> <p>With his fellow Developers, Alexis\' goal is to bring these processes to production. Developers and Scientists have very different constraints: developers want the code to be versioned, to be tested, to be deployed automatically and to produce logs. Developers also need it to run in production on distributed architectures(Spark, Hadoop, \u2026), with fixed versions of languages and frameworks (Scala\u2026), and with data that changes every day.</p> <p>In this talk, Alexis will explain how Developers work hand-in-hand with Data Scientists to shorten the path to running data workflows in production.</p> <p><b>Biography: </b>Alexis Seigneurin @ASeigneurin</p> <p>Software engineer for 15 years and consultant for <a href="http://www.ipponusa.com">Ippon Technologies</a>. Ippon delivers Digital, Big Data and Cloud applications on top of proven Java expertise in the US and France.</p> <p>Throughout many projects, Alexis explored many aspects of data management - cleansing, processing, indexing, reporting\u2026 - with many languages, frameworks, systems and databases. Alexis has used Spark since early 2014 and specifically Spark with Cassandra when working on real-time reporting applications.</p> <p><b>Summary</b>: Is Apache Spark Ready for the Cloud?\xa0</p> <p><br/>Many technology companies are turning to the cloud for scalable, elastic infrastructure to store and analyze user behavior data, information from wearables, sensor data, and more. However, running big data tools, like Apache Spark, in the cloud presents a host of challenges. Spark is typically deployed in a dedicated data center as a next step in an organizations big data deployment strategy to gain deeper and faster insights. However, as the advantages of big data in the cloud become more apparent and gain wider adoption, can organizations also reap the benefits of Spark as a service without sacrificing its primary benefit\u2014speed? In other words, is Spark ready for the cloud?\xa0</p> <p>In this presentation, Praveen Seluka, a software engineer and Apache Spark expert at Qubole, will outline how the combination of Apache Spark and AWS can be implemented to ensure high performance, based on real-world experience. The audience will learn\xa0how to effectively deploy Spark in the cloud, key technological challenges with delivering it as a service that can scale and deliver the performance Spark was designed to deliver, and the important benefits that can be achieved through Spark as a Service.</p> <p><b>Speaker Bio</b>:<br/>Praveen Seluka is a software engineer at Qubole. Prior to Qubole, Praveen worked as a software engineer at Microsoft and Yahoo. Praveen has won several coding competitions such as Kaggle and Codechef. He has a master\u2019s degree in information systems from the Birla Institute of Technology and Science, Pilani.</p> <p><b>Agenda</b>:\xa0<br/>6:30 - Drinks/Apps and Networking\xa0<br/>7 \xa0 \xa0 \xa0 - Introduction\xa0<br/>7:15 \xa0- Talks\xa0<br/>8:30 - Wrap up/shut down</p> <p><br/><b>Getting Here</b>:\xa0<br/>AddThis HQ is located next to the Silver lines\' Spring Hill Metro station. Free parking is also available. If you have trouble getting in please call Brad at[masked]</p> <p><b>Food</b>:\xa0<br/>AddThis will provide beer and sodas and Ippon and Qubole will provide food. \xa0There are plenty of local bars available if people would like to continue the discussion after the talk.\xa0</p> <p><b>Sponsors</b>:\xa0<a href="http://www.addthis.com/">AddThis</a>,\xa0<a href="http://www.ippon.fr/">Ippon</a>,\xa0<a href="http://www.qubole.com/">Qubole</a></p>'
    events_list_event_139.local_start = dateutil.parser.parse("2015-08-27T19:00:00")
    events_list_event_139.local_end = dateutil.parser.parse("2015-08-27T19:00:00")
    events_list_event_139.utc_offset = -14400L
    events_list_event_139.is_applicable = True
    events_list_event_139 = importer.save_or_locate(events_list_event_139)

    events_list_event_139.hashtags.add(events_list_hashtag_1)

    events_list_event_140 = Event()
    events_list_event_140.name = u'4. Hybrid Cordova Meetup'
    events_list_event_140.event_url = u'http://www.meetup.com/Berliner-Apache-Cordova-Network/events/224444437/'
    events_list_event_140.group = events_list_group_130
    events_list_event_140.meetupID = u'224444437'
    events_list_event_140.description = u'<p>Review Cordova and AWS Setup, REST API, Typescript class structure.</p>'
    events_list_event_140.local_start = dateutil.parser.parse("2015-08-27T19:00:00")
    events_list_event_140.local_end = dateutil.parser.parse("2015-08-27T20:45:00")
    events_list_event_140.utc_offset = 7200L
    events_list_event_140.is_applicable = True
    events_list_event_140 = importer.save_or_locate(events_list_event_140)

    events_list_event_140.hashtags.add(events_list_hashtag_1)

    events_list_event_141 = Event()
    events_list_event_141.name = u'Yarn vs Mesos Deathmatch - (second session deep dive explaination)'
    events_list_event_141.event_url = u'http://www.meetup.com/Big-things-are-happening-here/events/223599573/'
    events_list_event_141.group = events_list_group_139
    events_list_event_141.meetupID = u'223599573'
    events_list_event_141.description = u'<p><b>this is the second session continued the first one:\xa0<br/><a href="http://www.meetup.com/Big-things-are-happening-here/events/223012442/">first session - Yarn vs Mesos Deathmatch </a><br/></b><b><br/>18:00 -18:30\xa0- Mingling</b><b><br/></b></p> <p><b>18:30 -20:00\xa0</b>-\xa0<b>Avishai Ish-Sahlom\xa0</b>(Infrastructure expert and systems architect @ fewbytes)-\xa0<b>Yarn vs Mesos Deathmatch\xa0</b>- <b>(second session deep dive explaination)</b> In recent years hadoop has evolved to become an ecosystem of various data processing projects.\xa0As part of this evolution is has attained a grid component - Yarn.\xa0However,\xa0Yarn isn\'t the only grid that can run data oriented jobs and many people are interested in Mesos.This session will give an overview of grids in general, Yarn and Mesos in particular and compare them in the context of data oriented workloads .\xa0The things that we are going to focus on Yarn and Mesos and the difference about them.</p> <p><b>20:00 - 20:10 -\xa0Coffee Break\xa0</b></p> <p><br/><b>20:10 - 20:40 -\xa0Open Question from the audience - Be ready with some :)\xa0</b></p>'
    events_list_event_141.local_start = dateutil.parser.parse("2015-08-31T18:00:00")
    events_list_event_141.local_end = dateutil.parser.parse("2015-08-31T21:00:00")
    events_list_event_141.utc_offset = 10800L
    events_list_event_141.is_applicable = True
    events_list_event_141 = importer.save_or_locate(events_list_event_141)

    events_list_event_141.hashtags.add(events_list_hashtag_1)

    events_list_event_142 = Event()
    events_list_event_142.name = u'Adobe Extension Builder'
    events_list_event_142.event_url = u'http://www.meetup.com/Adobe-developers-designers-sydney/events/224114922/'
    events_list_event_142.group = events_list_group_140
    events_list_event_142.meetupID = u'224114922'
    events_list_event_142.description = u"<p>Meet at 6pm for 6:30 start. (note: the building is locked at 6:30pm).</p> <p><br/>Presenter: Richard Turner-Jones of Adobe.</p> <p>Richard will showing us how to build extensions for the Creative Cloud applications and will be discussing how the differences between the various releases of Creative Cloud applicaitons affects the way extensions are build.</p> <p>Also, we'll giving away a one year subscription to Adobe Creative Cloud to one lucky attendee.</p> <p>We'll strive to finish by 7:30 to retire to the Lord Nelson for food and drinks.</p> <p><br/>Venue provided by RocketBoots.</p>"
    events_list_event_142.local_start = dateutil.parser.parse("2015-08-31T18:00:00")
    events_list_event_142.local_end = dateutil.parser.parse("2015-08-31T18:00:00")
    events_list_event_142.utc_offset = 36000L
    events_list_event_142.is_applicable = True
    events_list_event_142 = importer.save_or_locate(events_list_event_142)

    events_list_event_142.hashtags.add(events_list_hashtag_1)

    events_list_event_143 = Event()
    events_list_event_143.name = u"Toronto Apache Spark's first event!!"
    events_list_event_143.event_url = u'http://www.meetup.com/Toronto-Apache-Spark/events/224035398/'
    events_list_event_143.group = events_list_group_141
    events_list_event_143.meetupID = u'224035398'
    events_list_event_143.description = u'<p>--- Date and Agenda Updated ---</p> <p><br/>I am very excited to announce that we will have our first event on <b>August 31st, 2015</b>.</p> <p>We are going to have a great start with our guest <b>Reza Zadeh</b> giving talk at The first Toronto Apache Spark meetup.</p> <p>Toronto Hadoop User Group (THUG) and Toronto Apache Spark meetup group are both listing and organizing this event.</p> <p>Description for this event will be updated with more details about the talk and the timing.</p> <p><br/>Note:</p> <p><br/>\u2022 <i>Please inform us in advance if you require any assistance because of mobility issues.</i></p> <p>\u2022 <i>Parking: some across the street in the green p. Close access to St. Andrew TTC Station. </i></p>'
    events_list_event_143.local_start = dateutil.parser.parse("2015-08-31T19:00:00")
    events_list_event_143.local_end = dateutil.parser.parse("2015-08-31T19:00:00")
    events_list_event_143.utc_offset = -14400L
    events_list_event_143.is_applicable = True
    events_list_event_143 = importer.save_or_locate(events_list_event_143)

    events_list_event_143.hashtags.add(events_list_hashtag_1)

    events_list_event_144 = Event()
    events_list_event_144.name = u'Data analytics with NOSQL'
    events_list_event_144.event_url = u'http://www.meetup.com/Lansing-Hadoop-Users-Group-Meetup/events/224387460/'
    events_list_event_144.group = events_list_group_131
    events_list_event_144.meetupID = u'224387460'
    events_list_event_144.description = u"<p><b>Presenters: </b>Mukundan Agaram and Chris Weiss</p> <p><b>Mukundan Agaram is the Chief Enterprise Architect at Delta Dental.</b> Prior to this he was a Senior Program Manager at Microsoft. Mukundan has over 20 years of diverse, international IT experience \xa0architecting and developing large scale distributed systems spanning several industry verticals. He is deeply passionate about bringing technology, elegant architecture, innovation and lasting value to bear on the systems he builds. He is a strong believer in developing knowledge capital on emerging technologies and paradigms. He is a recognized and published practitioner in the arena of Business Rules and Decision Management. His current interests revolve around technologies that can make systems smart and differentiating. Mukundan has a Masters degree in Computer Applications and a Bachelors degree in Mathematics and Statistics.</p> <p><br/><b>Chris Weiss is the Practice Lead for Architectural Services at Dewpoint Inc.</b>\xa0Over the past 18 years, Chris has architected medium to large systems that have spanned application, software, database, and system architecture. He has also led web development for a variety of projects, including the Ohio Department of Youth Services, Calhoun Intermediate School District, the State of Michigan, and many other clients, using technologies such as PHP, Java/JEE, and .NET. One of his key focuses has been solution architecture, looking at the full technology stack and identifying the personnel necessary to deliver projects on time and on budget.\xa0Chris's approach to information technology can be summarized as pragmatic problem solving through sustainable means.\xa0</p> <p>\n\nThis session will provide an overview of the various types of NOSQL databases and how they can be leveraged for data analytics.</p> <p><br/><b>Agenda:</b></p> <p>1. Introduction \xa0(5 mins)</p> <p>2. NOSQL Databases (45 mins)</p> <p>\xa0 \xa0 - Definition and introduction of topic</p> <p>\xa0 \xa0 - What are the various variants of NOSQL Databases?</p> <p>\xa0 \xa0 - Key Use Cases\xa0</p> <p>\xa0 \xa0 - Applications for Data Analytics</p> <p>\xa0 \xa0 - NOSQL Landscape</p> <p>3. Demo and Code Walk-thru (45 mins)</p> <p>4. Closing Discussions and Q/A (15 mins)</p>"
    events_list_event_144.local_start = dateutil.parser.parse("2015-08-27T19:00:00")
    events_list_event_144.local_end = dateutil.parser.parse("2015-08-27T21:00:00")
    events_list_event_144.utc_offset = -14400L
    events_list_event_144.is_applicable = True
    events_list_event_144 = importer.save_or_locate(events_list_event_144)

    events_list_event_144.hashtags.add(events_list_hashtag_1)

    events_list_event_145 = Event()
    events_list_event_145.name = u'8\uc6d4 Tajo \uc0ac\uc6a9\uc790 \ubaa8\uc784'
    events_list_event_145.event_url = u'http://www.meetup.com/seoul-apache-tajo-meetup/events/224450142/'
    events_list_event_145.group = events_list_group_132
    events_list_event_145.meetupID = u'224450142'
    events_list_event_145.description = u'<p>\uc548\ub155\ud558\uc138\uc694~\xa0</p> <p><br/>8\uc6d4 Tajo \uc0ac\uc6a9\uc790 \ubaa8\uc784\uc744 \uc544\ub798\uc640 \uac19\uc774 \uc9c4\ud589\ud558\uace0\uc790 \ud569\ub2c8\ub2e4.</p> <p>- \ubc1c\ud45c \uc8fc\uc81c : Flamingo \ud504\ub85c\uc81d\ud2b8 \uc18c\uac1c \ubc0f Tajo \uc5f0\ub3d9 \uac1c\ubc1c \ud6c4\uae30 (\ud074\ub77c\uc6b0\ub2e4\uc778 \ubc15\ud6a8\uadfc \ucee8\uc124\ud134\ud2b8)</p> <p><br/>- \uc77c\uc815 : 8/27(\ubaa9) \uc624\ud6c4 7\uc2dc 30\ubd84</p> <p>- \uc7a5\uc18c : \ubbf8\uc815 (\ucd94\ud6c4 \uacf5\uc9c0 \uc608\uc815)\xa0</p> <p>- \ubaa8\uc784 \ud6c4 \uac00\ubcbc\uc6b4 Beer \ub4b7\ud480\uc774</p> <p>Tajo \uc0ac\uc6a9\uc790 \ubaa8\uc784\uc740 Tajo \ub9cc\uc744 \uc8fc\uc81c\ub85c \ud558\ub294 \uac83\uc774 \uc544\ub2c8\ub77c, \ub2e4\uc591\ud55c \ub370\uc774\ud130 \ucc98\ub9ac \uae30\uc220\uacfc \uc5d0\ucf54 \uc2dc\uc2a4\ud15c \ub4f1\uc744 \ub2e4\ub8e8\uace0\uc790 \ud569\ub2c8\ub2e4. \ubc1c\ud45c\uc5d0 \uad00\uc2ec\uc788\uc73c\uc2e0 \ubd84\ub4e4\uc740 \uc5b8\uc81c\ub4e0\uc9c0 \ud3b8\ud558\uac8c [masked] \uc73c\ub85c \ubb38\uc758 \uc8fc\uc2dc\uba74 \ub429\ub2c8\ub2e4. *^^*</p> <p>\uadf8\ub7fc \ub9ce\uc740 \uad00\uc2ec \ubd80\ud0c1\ub4dc\ub9ac\uaca0\uc2b5\ub2c8\ub2e4~\xa0</p> <p>[\uc774 \ubaa8\uc784\uc740\xa0<a href="http://developer.naver.com/wiki/pages/community">\ub124\uc774\ubc84 D2 \uac1c\ubc1c\uc790 \ucee4\ubba4\ub2c8\ud2f0 \uc9c0\uc6d0 \ud504\ub85c\uadf8\ub7a8</a>\xa0\uc5d0\uc11c \ud6c4\uc6d0\ud569\ub2c8\ub2e4.]\xa0</p>'
    events_list_event_145.local_start = dateutil.parser.parse("2015-08-27T19:30:00")
    events_list_event_145.local_end = dateutil.parser.parse("2015-08-27T19:30:00")
    events_list_event_145.utc_offset = 32400L
    events_list_event_145.is_applicable = True
    events_list_event_145 = importer.save_or_locate(events_list_event_145)

    events_list_event_145.hashtags.add(events_list_hashtag_1)

    events_list_event_146 = Event()
    events_list_event_146.name = u'Mount Baldy Loop (Intermediate Hike)'
    events_list_event_146.event_url = u'http://www.meetup.com/Arizona-Backpacking/events/224083339/'
    events_list_event_146.group = events_list_group_133
    events_list_event_146.meetupID = u'224083339'
    events_list_event_146.description = u'<p>This challenging hike will enjoy the scenic Mount Baldy Loop in the White Mountains. Mt Baldy is the second highest mountain in Arizona (highest is Mt Humphreys). The best description can be found at <a href="http://hikearizona.com/decoder.php?ZTN=531">HikeArizona.com</a>\xa0and we\'ll be starting at the West Baldy trailhead (also<a href="http://hikearizona.com/decoder.php?ZTN=2309"> described here</a>), going counter-clockwise.</p> <p>We will plan to leave the Phoenix area before 4:00 PM on Friday, 8/28, and arrive at the Sheeps Crossing trailhead in the early evening. My goal is to then hike in no more than a couple of miles to find a nice campsite along the West Fork of the Lower Colorado River. This will give us the chance to acclimate to the altitude before hiking on Saturday.</p> <p>We\'ll leave our gear on Saturday morning and do the entire 17-mile loop, returning to the campsite for a relaxing evening, weather permitting, before driving back to Phoenix on Sunday AM.\xa0</p> <p><b><i>10 spots total for this hike.\xa0</i></b><b>Sorry, no dogs.\xa0</b></p> <p><b>Carpooling:</b></p> <p>We\'ll meet at the Apache/Loop 101 Park and Ride and leave from there, arranging carpools at the time of departure. A contribution of $10 or more (gas costs) is recommended if you are a rider.</p> <p><b>Recommended experience:</b> This will be my first time on this trail, but trusted sources confirm that it is <b><i>not </i></b>a beginner hike. I do my best to not be a trail-taskmaster but the entire loop is a challenging 17 miles with 2000 ft accumulated gain (the peak reaches over 11,300 ft), so I expect we will be hiking the entire day. <i>You should be fit and capable enough to complete the loop</i>. I am listing this as "intermediate," but if you have concerns about your ability, please contact me and we\'ll discuss that.</p> <p><b>For those not used to high altitudes, please note:</b></p> <p><i>This is a high altitude hike; we are shooting for the second highest mountain in Arizona, so be prepared. You WILL need wind and sun protection, and summer afternoons mean a thunderstorm isn\'t out of the question; bring rain gear. A serious pair of shoes or boots is another necessity, and the Forest Service notes that the trail is "not cleared of hazards." Expect that you will dehydrate more rapidly at high altitude, so bring even more water, not to mention calories to burn, and substantial snacks. </i></p> <p><br/><b>Water available:</b></p> <p>Water should be available but will need to be filtered/treated.</p> <p><b>Other helpful information:</b></p> <p>\u2022\xa0Be sure to bring appropriate gear based on the forecast for the weekend (I\'ll be posting weather reports in the days leading up to the trip).</p> <p>\u2022\xa0The summit itself is on the White Mountain Apache reservation, and I will be asking for permission for our group to enter and spend a few minutes on the summit. If we are not able to obtain permission, we\'ll just continue on the crossover section of the loop.</p>'
    events_list_event_146.local_start = dateutil.parser.parse("2015-08-28T16:00:00")
    events_list_event_146.local_end = dateutil.parser.parse("2015-08-30T14:00:00")
    events_list_event_146.utc_offset = -25200L
    events_list_event_146.is_applicable = True
    events_list_event_146 = importer.save_or_locate(events_list_event_146)

    events_list_event_146.hashtags.add(events_list_hashtag_1)

    events_list_event_147 = Event()
    events_list_event_147.name = u'Before Sunset Suzi Stern & Rich Harney live at the Smiling Wolf Music Studio.'
    events_list_event_147.event_url = u'http://www.meetup.com/Composers-Lyricists-Songwriters-Workshop-and-Showcase/events/223485154/'
    events_list_event_147.group = events_list_group_134
    events_list_event_147.meetupID = u'223485154'
    events_list_event_147.description = u'<p><b>100% of all donations go directly to the performing artists.</b></p> <p><b>Please only RSVP if you are completely confident you can attend.</b> With very limited seating these performing artists are counting on RSVP commitments. Of course stuff can happen but if you must cancel please provide at least 48 hour notice so the seat can be filled by another member.</p> <p>There is a requested door donation of $10 per attendee.</p> <p><br/>To prevent group sabotage those who cancel or no show RSVPs 3 times within a year will be removed from the group.</p> <p><b>Performing Artist</b></p> <p>Once again here at the Smiling Wolf Music Studio we\'ve struck gold!</p> <p>What can be said that isn\'t already well known in the Austin jazz community about Suzi Stern\'s innovative jazz style and exceptional talent?</p> <p>She\'s among Austin\'s jazz royalty up there at the top right along with Donna Menthol, Rich Harney, Madie Kay and many others soon to join us.</p> <p>When you hear <a href="http://suzistern.com/">Suzi Stern</a> you think Jazz, New Music, Singer Songwriter</p> <p><br/>"Grace and Elegance" / Jazz Times</p> <p>"Wonderful, soaring with jazzy lyricism" / Downbeat</p> <p>"Poetic\u2026masterful\u2026control and richness\u2026poignant" /All About Jazz</p> <p>The Austin American Statesman says of jazz singer Suzi Stern; \u201cStern has learned the great secret that transcends art - that the voice from the heart is at the center of all virtuosity.\u201d</p> <p>The combination of Stern\u2019s emotional clear voice, flying over her uncatagorizable compositions with her poignant lyrics creates a magic that moves the listener and is unforgettable. Jazz pianist and Columbia Records recording artist Denny Zeitlin says of Stern "It has been years since a singer has affected me so profoundly. Suzi has it all: a fantastic vocal instrument, effortless musicality, and a special way of working with the material and evoking the deepest emotions."</p> <p>(use scroll bar at the right of page to scan the entire page down to read more and check out the reviews from Downbeat, Jazztimes, All About Jazz, Cadence and more)</p> <p>Suzi was born in Buffalo, the daughter of jazz violinist Harry Stern who toured with The Vaughn Monroe big band and was leader of his own orchestras in Western New York of which which Suzi\'s mother was the featured singer. Her maternal grandfather spent his life touring in Vaudeville as a comic acrobat sharing the bill with the likes of a young Frank Sinatra, The Marx Brothers, George Burns and Bob Hope. Growing up in a family where creative outpourings were encouraged and being able to hear her fathers musicians come over for post gig jams gave Stern a clear sense that music was her true love at a very early age.</p> <p>Stern has released 7 jazz CD\u2019s to date under her own name (Viewpoint Records, Aardvark Records and Bus Biscuit Records), and has performed on a myriad of other artists projects. Her latest 2013 release "Romancing the Dark" steps out of the jazz idiom for which she is known, and is a collection of Stern\u2019s own original compositions and arrangements.</p> <p>Jazz Times reviewer H. Allen Williams states that "Stern\u2019s musical style pallet is wide...a testament to her wide reaching command of many styles and her ability to match a musical mood to the feeling of her words."</p> <p>She is a published poet and her lyrics appear in the Bill Evans second edition fake book and David Friesen\'s book of transcriptions called " Years Through Time", both Hal Leonard publications.</p> <p>Suzi has penned lyrics to a plethora of classic jazz compositions not typically sung and has collaborated with numerous contemporary artists on their works such as Denny Zeitlin\'s "Quiet Now", Joe Henderson\'s "Black Narcissus" and Joshua Redman\'s "Hide and Seek" which have been recorded by artists worldwide.</p> <p>A few of Stern\'s musical colleagues and collaborators of note have been: Denny Zeitlin, David Friesen, Joe Henderson, Mal Waldron,Leroy Vinegar, Jesseca Williams, Helen Sung, Bud Shank, Peggy Stern, Jay Clayton, Harvie S, Stefan Karlsson, Randy Porter, Doug Hall to name only a few.</p> <p>Stern and her partner pianist-composer George Oldziey are the producers of a jazz house concert series known as Casa Karen in Austin Texas which has become known as the best venue for acoustic jazz in central Texas with it\'s 9 foot concert grand piano as the center piece. This series has attracted touring artists over the past 5 years the likes of Eddie Gomez, Alex Sipiagin, Stan Killian, Fred Hamilton, Rich Perry, Don Edwards, Ed Soph, David Amram, Roseanna Vitro, Mark Soskin, Dean Johnson, Tim Horner, Carmen Bradford and many of the best artists from the Austin area.</p> <p>When not traveling to perform, Stern teaches in her home town of Austin Texas where she is one of the most sought after vocal coaches and studio singers in the area.</p> <p>+++++++++++++++++++++++++++++++++++++++++++++++++++++++++</p> <p>Radio and Press Contact:</p> <p>KARI-ON PRODUCTIONS</p> <p>[masked]</p> <p>[masked]</p> <p><a href="http://www.karigaffney.com">www.karigaffney.com</a></p> <p>[masked]</p> <p>[masked]</p> <p>++++++++++++++++++++++++++++++++++++++++++++++++++++++</p> <p>DISCOGRAPHY:</p> <p>Romancing the Dark - Bus Biscuit Records 2013</p> <p>Peter John Stoltzman Trio &amp; Friends, Live at Casa Karen - Bus Biscuit Records 2013</p> <p>El Viento - Bus Biscuit Records 2012</p> <p>Dark River - Blue Corn Records 2010</p> <p>Leap of Heart - Aardvark Records 2009</p> <p>A Child\u2019s Christmas in Wales - Aardvark Records 2006 (winner of the 2006 Addy Award)</p> <p>Lament - Aardvark Records 2003</p> <p>Inside Stories - Viewpoint Records 2000</p> <p>Seven Stars - Mad Moon Records 1995</p> <p>Voices of the New Jazz Culture - Jazziz on Disc</p> <p>++++++++ And a few words from the press:</p> <p>CADENCE MAGAZINE - "Making artistic use of her delicate and beautiful voice, Stern parlays in-depth knowledge of the tunes and an uncanny sense of timing to create memorable interpretations of these classic melodies"</p> <p>5 Stars out of 5 ! YAHOO REVIEW by Susan Francis -\u201cSinger-songwriter Suzi Stern immerses herself into the tracks, and her personal touch translates to audiences. With music, lyrics, and arrangements written by Stern, the songs embody an intimacy that soothes the listener completely. Romancing the Dark brims with deep emotions expressing love that\'s been lost and never forgotten.\u201d</p> <p>5 out of 5 Stars!! Amazon by Grady Harp HALL OF FAME TOP 50 REVIEWERVINE VOICE "Stern not only possesses a naturally beautiful voice, capable of exploring all the emotions songs deliver to the artist, but she composed the music and lyrics and is responsible for the arrangements\u2026it is a stunning achievement! Special music from a special lady. Let it seep in!!"</p> <p>Michael Point DOWNBEAT MAGAZINE - "Her voice is wonderful, soaring with jazzy lyricism.."</p> <p>JAZZ TIMES H. Allen Williams - "Romancing the Dark keeps a strong foundation of the well-known jazz compositional techniques...but it borrows from many styles to yield a well-conceived and flowing collection of tunes that is both engaging and enjoyable. \u201cFirefly\u201d begins the romance with a beautiful and subtle waltz ballad that has Stern\u2019s clear tone and diction coupled with a haunting cello line by Douglas Harvey that is an interweaving counterpoint throughout Sterns melodic statement. Stern\u2019s lyrics are certainly poetic and the accompanying booklet really allows the listener to understand and appreciate the true talent and deeper meanings of the lyrics\u2026.Stern\u2019s phrasing is always clear and in accord with the musical environment she is singing in, never over dramatic, but keeping the energy of the melody moving forward\u2026grace and elegance\u2026a wonderful offering\u2026a delightful musical journey!"</p> <p>2013 CD REVIEW JAZZCAMERA UK -"Suzi Stern has created something really special with 11 of her own songs on this new CD. Stern...exceptional strength and eloquence...More please, Suzi!!"</p> <p>ART VOICE BUFFALO EVENING NEWS "Stern is a gifted artist who simultaneously defines and reinterprets what jazz is today"</p> <p>Brad Buchholtz AUSTIN AMERICAN STATESMAN -"Stern\'s \'Lament\' stands as one of the finest albums of the decade - a masterpiece of understatement that honors the highest aspirations of jazz."</p> <p>WILLAMETTE WEEK -"Stern\'s ease with a challenging melody is matched by her improvisational prowess..."</p> <p>Sax great JOE HENDERSON-"Suzi, you\'ve done a superb job. You made it sound and seem so easy, giving that melody (Black Narcissus) a voice. Write on!"</p> <p>ACOUSTIC MUSIC EXCHANGE review by Mark S. Tucker-\u201cBesides the pure beauty of the singing, I was rather astonished to discover that almost everything here was written and arranged by Ms. Stern resulting in a disc that has few comparatives...airs not normally found in rock, jazz, or related modes. Stern embraces the timbre of midnight, the lonely tolling of far away bells above an aching heart, the sigh of fog as it drifts over fallow meadows, an amber moon glowing starkly in arid ebon skies. Haunted Heart enfolds the sort of atmosphere the word \'bittersweet\' was invented for\u2026.a showcase for not just Ms. Stern\'s entrancing vocals and depth-encrusted compositions but her very soul as well.\u201d</p> <p>Review by Rotcod Zzaj for Improvijazzation Nation</p> <p>Suzi Stern \u2013 ROMANCING THE DARK: There are plenty of \u201cjust jazz singers\u201d in today\'s market, but I can tell you that Suzi\u2019s definitely not \u201cjust\u201d anything\u2026 listen to the opening track, \u201cFirefly\u201c, and you\u2019ll hear a singer who has \u201cbeen there\u201d already\u2026 and she paints sonic beauty that makes you want to go right along with her, no matter the cost! While this outing (she\u2019s released 7 CD\u2019s previously) isn\u2019t exactly jazz, the tunes are all originals \u2013 which in itself lends an air of excitement; at least for this listener. The percussion intro on \u201cSounds Are Louder In The Dark\u201d was the perfect way to get you to notice what she means in the title \u2013 a truly excellent tune! It was the almost-theatrical \u201cTango For Tina\u201d that got my vote for favorite of the 11 on this fine CD. I give Suzi (&amp; crew) a MOST HIGHLY RECOMMENDED, with an \u201cEQ\u201d (energy quotient) rating of 4.98.</p> <p>5 Stars out of 5 emusic review \u201c Stern has created a lasting deep and evocative offering, filled with smart lyrics that are poetic and never trite\u2026a wonderful composer/vocalist.\u201d</p> <p>All.About.Jazz review:</p> <p>ROMANCING THE DARK: SUZI STERN</p> <p>By</p> <p>GEANNINE REID,</p> <p>Published: March 11, 2014</p> <p>When a jazz singer is able to combine skills as a poet, composer, arranger and singer, what type of music is the result? Folk/Jazz/World; but of course! That is the underlying theme throughout Suzi Stern\'s CD, Romancing the Dark. The Austin based singer has a diverse history of collaborations, working with artist such as: Joe Henderson, Denny Zeitlin,David Friesen, Jerry Hahn, Leroy Vinnegar,Jessica Williams,Sheila Jordan, Jay Clayton, Peggy Stern, Stefan Karlsson, Alan Jones, Randy Porter, John Stowell, and beyond. Stern also boasts a library of seven CDs as a leader and is a published poet and lyricist. Stern has penned lyrics to numerous contemporary and classic jazz compositions such as Denny Zeitlin\'s "Quiet Now," Joe Henderson\'s "Black Narcissus" and Joshua Redman\'s "Hide and Seek," which have been recorded by artists worldwide. Stern\'s lyrics have been published in the Bill Evans Fake Book from Hal Leonard Publications.</p> <p>Romancing the Dark contains eleven selections, nine of which are Stern originals, one penned by bassist Paul Unger, "Sleepwalking Girl" and one standard, "Haunted Heart." Stern composed, orchestrated and wrote the lyrics for nine of the selections and has compiled a varying set of instruments for the project. Each selection has its own unique instrumentation and orchestration, which provides the perfect emotional setting for Stern\'s clear voice to articulate her storylines. "Romancing The Dark" starts with George Oldziey\'s fluid accordion lines that flow into an accented off beat chordal march pattern that clarinetist John Mills blows a haunting melody over. The two are joined by the marching snare work of Steve Schwelling\'s drums to complete the intro for Sterns vocal entrance. "Beautiful" is the first word of Stern\'s lyrics and that sums up the mood and overall presentation of the composition. Stern\'s singing style is clear and accurate; her lyrics are poetic in nature and give just enough information for the listener to follow the storyline while still leaving room for the imagination to fill in the details. Oldziey also plays piano on the track and Mike Sailors adds trumpet, while Randy Zimmerman\'s trombone provides a nice brass pad behind the vocals and the fills from Mills. Stern composes and orchestrates a masterful interlude with the three horn players playing counterpoint to one another leading us to the last chorus and verse which continues the three horn writing behind Stern\'s vocals. After a poetic pause on "Self-Indulgence Your Game," Stern joins the three horns with a series of vocal scats that culminate in the ending statement.</p> <p>As before mentioned, the varying instrumentation and Stern\'s ability to clearly articulate a melody over creative orchestrations is the key element to the success of Romancing the Dark. "Sounds Are Louder In The Dark" finds Stern\'s voice paired with a string quartet and percussion. On this track Stern collaborates with Oldziey, who provides a stunning string arrangement for Stern to sing with. The ballad "Hymn" is colored with piano, bass, percussion, guitar, violin and a children\'s choir. The entire first half of the song is a rubato phrasing of voice, violin, arco bass and piano. The Children\'s voices and percussion are added later to build the selection to a logical climax and ending. "Deeper Quiet" is another ballad that features more wonderful music and lyrics by Stern and spot on string orchestration from Oldziey. Sailor\'s muted trumpet opens the selection over a lush string quartet chordal pad with Oldziey\'s piano chords and single note fills rounding out the space, these intimate moments really expose Stern\'s voice and allow the listener to hear the control and richness of her singing. "Moth" finds Stern\'s voice impeccably singing each phrase of the melody with a new orchestrative color, sometimes she harmonizes with herself, other times she sings in perfect unison with the piano or in counterpoint to the guitar. Guitarist Bruce Saunders provides a very nice nylon strung guitar solo, followed by more counterpoint with the melody and violin. Stern\'s elegant singing, music and lyrics are presented in an array of colors and instrumental settings that result in a unique and poignant listen. What type of music as a poet, composer, arranger and singer make? Folk/Jazz/World; or more specifically, creative music! That is the underlying theme throughout Suzi Stern\'s beautiful CD, Romancing the Dark.</p> <p>Donation<br/>There is a requested door donation of $10 per attendee.</p> <p>This an "Adults only" show.</p> <p>Due to limited space and parking only RSVP\'s will be allowed in. Gate crashers will be turned away.</p> <p>There is an attendance cap of 12 members (plus host) so RSVP now for a spot.</p>'
    events_list_event_147.local_start = dateutil.parser.parse("2015-08-28T17:30:00")
    events_list_event_147.local_end = dateutil.parser.parse("2015-08-28T18:15:00")
    events_list_event_147.utc_offset = -18000L
    events_list_event_147.is_applicable = True
    events_list_event_147 = importer.save_or_locate(events_list_event_147)

    events_list_event_147.hashtags.add(events_list_hashtag_1)

    events_list_event_148 = Event()
    events_list_event_148.name = u'SWIHA HA Laughter Club'
    events_list_event_148.event_url = u'http://www.meetup.com/Phoenix-Laughter-Club/events/224356491/'
    events_list_event_148.group = events_list_group_74
    events_list_event_148.meetupID = u'dlwhmdytlblc'
    events_list_event_148.description = u'<p>SWIHA HA Laughter Club meets the 2nd and 4th Friday of each month at the Southwest Institute of Healing Arts, 1100 E. Apache Blvd. in Tempe. The meeting is free and lasts approximately an hour. Join others for laughter exercises, laughter meditation and discussion of the Principles of Good-Hearted Living, which will help you make more room in your life for laughter.</p> <p>Hosted by Linda Scharf on the 2nd Friday, or by Shelby McBride or Laurie Nathanson on the 4th Friday.</p>'
    events_list_event_148.local_start = dateutil.parser.parse("2015-08-28T18:00:00")
    events_list_event_148.local_end = dateutil.parser.parse("2015-08-28T18:00:00")
    events_list_event_148.utc_offset = -25200L
    events_list_event_148.is_applicable = True
    events_list_event_148 = importer.save_or_locate(events_list_event_148)

    events_list_event_148.hashtags.add(events_list_hashtag_1)

    events_list_event_149 = Event()
    events_list_event_149.name = u'Scala Manchester'
    events_list_event_149.event_url = u'http://www.meetup.com/scala-developers/events/224202231/'
    events_list_event_149.group = events_list_group_142
    events_list_event_149.meetupID = u'fcqxglytlbpc'
    events_list_event_149.description = u'<p>TBC</p>'
    events_list_event_149.local_start = dateutil.parser.parse("2015-08-31T19:00:00")
    events_list_event_149.local_end = dateutil.parser.parse("2015-08-31T19:00:00")
    events_list_event_149.utc_offset = 3600L
    events_list_event_149.is_applicable = True
    events_list_event_149 = importer.save_or_locate(events_list_event_149)

    events_list_event_149.hashtags.add(events_list_hashtag_1)

    events_list_event_150 = Event()
    events_list_event_150.name = u"Lets meet at Apache Cafe for  'The Bar Exam'"
    events_list_event_150.event_url = u'http://www.meetup.com/ALTlanta/events/224139835/'
    events_list_event_150.group = events_list_group_135
    events_list_event_150.meetupID = u'lwhpglytlblc'
    events_list_event_150.description = u'<p>In a little over 2 years The Bar Exam has grown to be recognized as Atlanta\'s definitive open-mic competition and showcase. The Bar Exam brings the excitement; inspiration, anticipation, humor and heart break from the likes of American Idol and puts it in front of a live audience. The Bar Exam is the place to develop your craft, showcase your talents, and network with like-minded people and industry professionals.</p> <p><img src="http://photos1.meetupstatic.com/photos/event/c/7/8/600_440583192.jpeg" /></p> <p>\n\n\n<img src="http://photos3.meetupstatic.com/photos/event/3/0/5/f/600_436332383.jpeg" /></p> <p>\n\n\n<b>About the show:</b></p> <p><b>16 artists battle for The Bar Exam crown before an industry panel of judges and a packed house to win $1,400 in prizes. Who will raise the bar? Ultimately, you the audience decide if they #PassTheBar or #PassTheMic<br/></b></p> <p><b>Entrance for ALTlanta Core Members is just $5 before 9pm (normally $10)</b></p> <p>More about the venue:\xa0<a href="http://www.apachecafe.info/">www.apachecafe.info</a></p> <p>Nestled next to the iconic Olympic torch of I-75 behind The Varsity off North Avenue and Spring St. in downtown Atlanta, this diamond in the rough has been a staple in the art and music community for over a dozen years. \xa0Eclectic art drape the walls and live music ranging from jazz, funk, soul , spoken word and Hip-Hop paint the room every night giving this place a unique sense of creative euphoria unlike anywhere else.\xa0</p> <p>Full menu</p> <p>Full Bar</p> <p>More from the organizer:\xa0<a href="http://www.savagefam.com/">www.savagefam.com</a></p>'
    events_list_event_150.local_start = dateutil.parser.parse("2015-08-28T20:00:00")
    events_list_event_150.local_end = dateutil.parser.parse("2015-08-28T20:00:00")
    events_list_event_150.utc_offset = -14400L
    events_list_event_150.is_applicable = True
    events_list_event_150 = importer.save_or_locate(events_list_event_150)

    events_list_event_150.hashtags.add(events_list_hashtag_1)

    events_list_event_151 = Event()
    events_list_event_151.name = u'Introduction to Machine Learning in Spark'
    events_list_event_151.event_url = u'http://www.meetup.com/Bangalore-Apache-Spark-Meetup/events/223706911/'
    events_list_event_151.group = events_list_group_136
    events_list_event_151.meetupID = u'223706911'
    events_list_event_151.description = u'<p>Agenda : To be decided</p>'
    events_list_event_151.local_start = dateutil.parser.parse("2015-08-29T10:00:00")
    events_list_event_151.local_end = dateutil.parser.parse("2015-08-29T10:00:00")
    events_list_event_151.utc_offset = 19800L
    events_list_event_151.is_applicable = True
    events_list_event_151 = importer.save_or_locate(events_list_event_151)

    events_list_event_151.hashtags.add(events_list_hashtag_1)

    events_list_event_152 = Event()
    events_list_event_152.name = u'Work on homework in advance; Algorithms: Design and Analysis Week 5'
    events_list_event_152.event_url = u'http://www.meetup.com/StudyGroups/events/224225630/'
    events_list_event_152.group = events_list_group_72
    events_list_event_152.meetupID = u'224225630'
    events_list_event_152.description = u'<p>Algorithm is the foundation of hacking skill. Work on homework in advance. Come to discuss homework:<br/><a href="https://class.coursera.org/algo-008/wiki/Syllabus" class="linkified">https://class.coursera.org/algo-008/wiki/Syllabus</a></p>'
    events_list_event_152.local_start = dateutil.parser.parse("2015-08-30T13:00:00")
    events_list_event_152.local_end = dateutil.parser.parse("2015-08-30T15:00:00")
    events_list_event_152.utc_offset = -25200L
    events_list_event_152.is_applicable = True
    events_list_event_152 = importer.save_or_locate(events_list_event_152)

    events_list_event_152.hashtags.add(events_list_hashtag_1)

    events_list_event_153 = Event()
    events_list_event_153.name = u'A tour of Hive'
    events_list_event_153.event_url = u'http://www.meetup.com/Big-Data-Denmark/events/223651150/'
    events_list_event_153.group = events_list_group_138
    events_list_event_153.meetupID = u'223651150'
    events_list_event_153.description = u'<p>Apache Hive has become a great way for people to start using Hadoop, as it it features a SQL like query language. But Hive is not a regular database, and Hive\u2019s query language is not SQL. In this talk, I will give you a tour of Hive, and try to focus in on the areas where Hive is different, and where you might get a few surprises when you start using Hive in practice. The talk will include some live demos, and some of the topics that will be touched upon include Tez vs. MR, the ORC format, window functions and transforms.</p> <p>\n\n\nSpeaker:</p> <p>Martin\xa0Qvist\xa0is an HPC Specialist at Vestas Wind Systems. He studied mathematics at Aalborg University, and worked on traffic modeling in computer networks as well as some approximation theoretic topics in subdivision surfaces. Since then he has worked as a software developer, and subsequently started his own consultancy company, which he ran until he started at Vestas.</p> <p>\n\n\n\nAs always the presentation is free and refreshments will be\xa0provided for all who sign up.\xa0</p> <p>\n\n\n\nThere are max. 40 seat available for this presentation.</p>'
    events_list_event_153.local_start = dateutil.parser.parse("2015-08-31T17:00:00")
    events_list_event_153.local_end = dateutil.parser.parse("2015-08-31T20:00:00")
    events_list_event_153.utc_offset = 7200L
    events_list_event_153.is_applicable = True
    events_list_event_153 = importer.save_or_locate(events_list_event_153)

    events_list_event_153.hashtags.add(events_list_hashtag_1)

    events_list_event_154 = Event()
    events_list_event_154.name = u'Outdoor Football'
    events_list_event_154.event_url = u'http://www.meetup.com/stockholmsportypeople/events/223782300/'
    events_list_event_154.group = events_list_group_76
    events_list_event_154.meetupID = u'kbbhhlytlbpc'
    events_list_event_154.description = u"<p>Please check the comments just before the event:\xa0maybe we decide not to play because of the weather or so...</p> <p>--------------------------------------</p> <p>GENERAL INFORMATION:</p> <p>Please note that these games are friendly games and everybody has to be\xa0fair play. In case of unappropriate behaviour (hard tackling,\xa0direct swearing, etc) you will be warned and eventually asked to leave the pitch. We play for fun so let's have fun together!</p> <p>Please take:</p> <p>\u2022\xa01 white AND 1 black\xa0t-shirt, so that we can change teams if needed.</p> <p>\u2022\xa0football shoes or normal sport shoes, but football shoes are recommended as we play on artificial grass (outdoor) and it can be slippery.</p> <p>\u2022\xa0water, as there is no access to water there.</p> <p>\u2022\xa0a ball if you have one, so that we can play with the best one</p> <p>\u2022\xa0shin pads are recommended: even if we don't play the world cup, it's always better to have good protections!</p> <p>\u2022 Location for Monday games will be posted on Sundays and location for Friday games posted on Wednesday<br/>There are no shower or changing cabins there.</p>"
    events_list_event_154.local_start = dateutil.parser.parse("2015-08-31T19:00:00")
    events_list_event_154.local_end = dateutil.parser.parse("2015-08-31T22:00:00")
    events_list_event_154.utc_offset = 7200L
    events_list_event_154.is_applicable = False
    events_list_event_154 = importer.save_or_locate(events_list_event_154)

    events_list_event_154.hashtags.add(events_list_hashtag_1)

    events_list_event_155 = Event()
    events_list_event_155.name = u'Lambda Architecture - Real Time Machine Learning'
    events_list_event_155.event_url = u'http://www.meetup.com/HUGNOFA/events/224481578/'
    events_list_event_155.group = events_list_group_143
    events_list_event_155.meetupID = u'224481578'
    events_list_event_155.description = u'<p><b><br/></b></p> <p><img src="http://photos3.meetupstatic.com/photos/event/e/5/b/0/600_440638800.jpeg" /></p> <p><b>\xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 Query = Function (All Data)</b></p> <p>Nathan Marz, the creator of Storm at Twitter quoted the above years before. In a nutshell, this is the essence of Lambda Architecture.</p> <p><br/>Lambda architectures present distinctive traits that make them particularly suitable for real-world, large-scale data products. They provide a viable answer to the need of gathering insights that are function of the entire data set. At the same time, lambda architectures are built with the capability to support data processes at different data and temporal granularity. Enterprise data pipelines, most of the time, comprise heterogeneous processing modalities: computing can be batch (e.g. Hadoop) vs. (near) real-time vs. streaming (e.g. Storm), data storage can he file-oriented (e.g. HDFS) vs. columnar (e.g. HBase). Additionally, given the distributed nature of lambda architectures, they are designed to be scalable and fault-tolerant.</p> <p>Once again, hear from my experience, another feather to your big data crown.</p> <p>See you all, and as usual register early.</p>'
    events_list_event_155.local_start = dateutil.parser.parse("2015-09-01T18:30:00")
    events_list_event_155.local_end = dateutil.parser.parse("2015-09-01T20:30:00")
    events_list_event_155.utc_offset = -14400L
    events_list_event_155.is_applicable = True
    events_list_event_155 = importer.save_or_locate(events_list_event_155)

    events_list_event_155.hashtags.add(events_list_hashtag_1)

    events_list_event_156 = Event()
    events_list_event_156.name = u'Mid-Week Football'
    events_list_event_156.event_url = u'http://www.meetup.com/stockholmsportypeople/events/224067034/'
    events_list_event_156.group = events_list_group_76
    events_list_event_156.meetupID = u'224067034'
    events_list_event_156.description = u'<p>Please note that these games are friendly games and everybody has to be\xa0fair play. KICK OFF AT 8.30PM SHARP.</p> <p>\u2022\xa01 white AND 1 black\xa0t-shirt - PLEASE BRING ONE OF EACH in case we have to swap teams to make the game fair.\xa0</p> <p>\u2022\xa0football shoes or normal sport shoes, but football shoes are recommended as we play on artificial grass (outdoor) and it can be slippery.</p> <p>\u2022\xa0water, as there is no access to water there.</p> <p>\u2022\xa0A BALL if you have one, so that we can play with the best one</p> <p>\u2022 IF YOU CAN NOT ATTEND PLEASE UPDATE YOUR RSVP SO EVERYONE ELSE CAN HAVE A CHANCE TO PLAY!</p>'
    events_list_event_156.local_start = dateutil.parser.parse("2015-08-31T20:15:00")
    events_list_event_156.local_end = dateutil.parser.parse("2015-08-31T20:15:00")
    events_list_event_156.utc_offset = 7200L
    events_list_event_156.is_applicable = False
    events_list_event_156 = importer.save_or_locate(events_list_event_156)

    events_list_event_156.hashtags.add(events_list_hashtag_1)

    events_list_event_157 = Event()
    events_list_event_157.name = u'Learn and discuss Hadoop technology'
    events_list_event_157.event_url = u'http://www.meetup.com/Cloudera-Tech-Meetup/events/223985747/'
    events_list_event_157.group = events_list_group_144
    events_list_event_157.meetupID = u'223985747'
    events_list_event_157.description = u'<p><b>Come join us on Tuesday for some great information about Hadoop.</b></p> <p><b>We are bringing many Clouderans to Budapest from around the globe. \xa0This is a great opportunity to hear some technical talks about Hadoop and related technologies. \xa0Many Hadoop experts will be here for Q&amp;A as well.</b></p> <p>Drinks and Pizza will be provided</p> <p><i>We will update the topics as we determine our speakers.</i></p> <p><b>6:30 - 7:00</b> \xa0Arrivals and Networking</p> <p><b>7:00 - 7:30</b>: \xa0Technical Discussion on Yarn/MR/Spark \xa0 \xa0 \xa0Wilfred Spiegelenburg</p> <p><b>7:40 - 8:10</b>: \xa0\xa0Technical Discussion TBD</p> <p><b>8:20 - 8:50</b>: \xa0\xa0Technical Discussion TBD</p> <p><b>9:00 - 10:00</b>:\xa0\xa0Drinks and Networking \xa0(Beer, Wine, and Pizza)</p> <p><b>About Cloudera:\xa0</b><br/>We are an open-source distributed systems business, focused on providing value added services around Hadoop, packaged via our Enterprise Data Hub (EDH) offering. Cloudera has been rapidly expanding our business in supporting our end customers around this open source software, and this team is at the forefront of the expansion of our business. (www.cloudera.com)\xa0</p>'
    events_list_event_157.local_start = dateutil.parser.parse("2015-09-01T19:00:00")
    events_list_event_157.local_end = dateutil.parser.parse("2015-09-01T22:00:00")
    events_list_event_157.utc_offset = 7200L
    events_list_event_157.is_applicable = True
    events_list_event_157 = importer.save_or_locate(events_list_event_157)

    events_list_event_157.hashtags.add(events_list_hashtag_1)

    events_list_event_158 = Event()
    events_list_event_158.name = u'Ionic Presentation: What you  need to know about 1.0, and advanced Ionic Topics.'
    events_list_event_158.event_url = u'http://www.meetup.com/Atlanta-Ionic-Developers/events/222861007/'
    events_list_event_158.group = events_list_group_158
    events_list_event_158.meetupID = u'222861007'
    events_list_event_158.description = u"<p>All,\xa0</p> <p>We are going to be putting together an advanced presentation for the next steps with Ionic. We have had two fantastic presentations on introductions to Ionic in Atlanta so far, from our group and the Atlanta HTML5 group, and now it's time to talk about what is next.\xa0</p> <p>We will be posting more details about this presentation soon. Some things you can expect from this presentation:\xa0</p> <p>- Discussion about the release of Ionic 1.0 and what you need to know.</p> <p>- Actual live coding.</p> <p>- Use of Ionic's Advanced features (Native Scrolling, View Caching, Collection-Repeat, and more!).\xa0</p> <p>- How to submit an application to Ionic View.</p> <p>- How to leverage Ionic.IO to post updates to your app without resubmitting them to the Google/Apple stores.\xa0</p> <p>- Windows Phone is coming!\xa0</p> <p>\n\n\nAnd more! Stay tuned for more details.\xa0</p>"
    events_list_event_158.local_start = dateutil.parser.parse("2015-09-01T19:30:00")
    events_list_event_158.local_end = dateutil.parser.parse("2015-09-01T21:30:00")
    events_list_event_158.utc_offset = -14400L
    events_list_event_158.is_applicable = True
    events_list_event_158 = importer.save_or_locate(events_list_event_158)

    events_list_event_158.hashtags.add(events_list_hashtag_1)

    events_list_event_159 = Event()
    events_list_event_159.name = u'Big Clinical Data: NLP with cTAKES & UIMA'
    events_list_event_159.event_url = u'http://www.meetup.com/austin-data-geeks/events/224025951/'
    events_list_event_159.group = events_list_group_146
    events_list_event_159.meetupID = u'224025951'
    events_list_event_159.description = u"<p>This is a joint meetup with Austin NLP/Text</p> <p><b>Abstract</b></p> <p>Those of you whom have visited a physician in the recent past know from experience that you are more than a check-box or a survey. \xa0In order to personalize care, physicians utilize free-text notes about specific patient conditions. \xa0However capturing these notes as a rich source of information for patient care and satisfaction can be difficult. \xa0Electronic Health Records were first started in the 1990s and now are used to pool patient information and resources on health-care specific cloud and hybrid data platforms. \xa0This data tends to be high dimensional and high volume. \xa0Thus Apache Software Foundation has incubated several open-source resource tools for Natural Language Processing of Clinical Notes.</p> <p><br/>This talk will describe the use of Clinical Text Analysis and Knowledge Extraction System (cTAKES) and Unstructured Information Management Architecture (UIMA) to mine free-text clinical notes. \xa0We will give an over-view of recent and past uses of the system as well as some suggestions for novel uses. \xa0Most importantly, there is a shift in heathcare to more individualized medicine. A number of companies are providing natural language processing capabilities on their healthcare platforms to enable information mined from unstructured textual (i.e. doctor's clinical notes), to be combined with structured clinical data.</p> <p><b>About the Speaker</b></p> <p>Jennifer\xa0Davis, Ph.D., is a senior data scientist with domain expertise in Big Data, Life Sciences and Healthcare.\xa0 Jennifer\xa0graduated from Georgetown in Washington DC, having completed her dissertation at the Medical School in 2009 (Doctorate in Tumor Biology). Since then Jennifer has completed Post-doctoral\xa0Rotations and Research\xa0Fellowships\xa0at Baylor College of Medicine, MD Anderson Cancer Center, and The University of Texas, Austin both in the\xa0College\xa0of Pharmacy and the Cockrell School of Engineering.\xa0 In\xa02013\xa0Jennifer\xa0completed a Internship\xa0in Life Sciences Computing, atone of the largest super-computing centers in the world--the Texas Advanced Computing Center. Jennifer\xa0has a combined experience of over 10 years in computational methods including machine learning, statistics and data\xa0visualization.\xa0 Jennifer\xa0has publications in international journals and is currently a reviewer for\xa0two international scientific journals, \u2018Cancer Informatics\u2019\xa0and\xa0\u2018PLoS\xa0One\u2019.\xa0She\xa0is licensed in\xa0several areas of Data Science. \xa0</p>"
    events_list_event_159.local_start = dateutil.parser.parse("2015-09-02T18:30:00")
    events_list_event_159.local_end = dateutil.parser.parse("2015-09-02T20:45:00")
    events_list_event_159.utc_offset = -18000L
    events_list_event_159.is_applicable = True
    events_list_event_159 = importer.save_or_locate(events_list_event_159)

    events_list_event_159.hashtags.add(events_list_hashtag_1)

    events_list_event_160 = Event()
    events_list_event_160.name = u'Performance Meetup!'
    events_list_event_160.event_url = u'http://www.meetup.com/Atlanta-Web-Performance-Group/events/223476866/'
    events_list_event_160.group = events_list_group_147
    events_list_event_160.meetupID = u'dbstndytmbdb'
    events_list_event_160.description = u"<p>Are you passionate about:</p> <p>Improving your website's user experience?</p> <p>Having a faster site that actually uses less resources?</p> <p>Getting more traffic, more clicks, more leads and more revenue?</p> <p>Then this Atlanta Web Performance Meetup is for you!</p> <p>I'm happy to schedule this Atlanta Web Performance Meetup! We now have\xa0a great venue with a projector and lots of space to talk provided Rigor.</p> <p>This meetup is moving to the social/presentation format as well. Show up first for free food and drinks to network with other passionate performance people. Afterwards we will have a presentation about cool web performance topics.</p>"
    events_list_event_160.local_start = dateutil.parser.parse("2015-09-02T19:00:00")
    events_list_event_160.local_end = dateutil.parser.parse("2015-09-02T19:00:00")
    events_list_event_160.utc_offset = -14400L
    events_list_event_160.is_applicable = True
    events_list_event_160 = importer.save_or_locate(events_list_event_160)

    events_list_event_160.hashtags.add(events_list_hashtag_1)

    events_list_event_161 = Event()
    events_list_event_161.name = u'R, matey!'
    events_list_event_161.event_url = u'http://www.meetup.com/SeaLang/events/222412789/'
    events_list_event_161.group = events_list_group_148
    events_list_event_161.meetupID = u'222412789'
    events_list_event_161.description = u'<p>... and just in time for "Talk Like A Pirate Day", too!</p> <p>Vishnu Vettrivel has volunteered to walk us through R, a statistical data language. In his own words:</p> <p>"R is a programming language and software environment for statistical computing and graphics. It is widely used among statisticians and data miners for developing statistical software and data analysis.</p> <p>This talk will give a brief introduction to the R Programming language and more importantly introduces Spark-R: an R package that provides a light-weight front-end to use Apache Spark: a large-scale data processing engine."</p> <p>Should be interesting! (NOTE: Pirate-speak during the meeting entirely optional, but encouraged.)</p>'
    events_list_event_161.local_start = dateutil.parser.parse("2015-09-02T19:00:00")
    events_list_event_161.local_end = dateutil.parser.parse("2015-09-02T19:00:00")
    events_list_event_161.utc_offset = -25200L
    events_list_event_161.is_applicable = True
    events_list_event_161 = importer.save_or_locate(events_list_event_161)

    events_list_event_161.hashtags.add(events_list_hashtag_1)

    events_list_event_162 = Event()
    events_list_event_162.name = u'AEM Developer Meetup #1'
    events_list_event_162.event_url = u'http://www.meetup.com/AEM-Developer-Meetup/events/223914977/'
    events_list_event_162.group = events_list_group_149
    events_list_event_162.meetupID = u'223914977'
    events_list_event_162.description = u'<p>Hello all! Welcome to the first Adobe Experience Manager Developer Meetup in The Netherlands. We are very excited to kick off in September and are looking forward to meeting the community of Adobe enthusiasts!</p> <p>This first meetup is graciously hosted and co-initiated by eFocus. We\u2019ll have a look at some first-hand experiences from Marijn Vermeulen working on the Phonak case and Gabriel Walt from Adobe will join to share some of the latest in development tooling and what lies ahead in the roadmap. There\u2019s room in the agenda to bring in your thoughts and ideas as well. Just shout out on any ideas that you may have for the unconference timeslot. It\u2019s an open discussion so please be invited to contribute and make this interesting for the community and yourself.</p> <p><b>Agenda</b></p> <p>17.00 \u2013 18.00: Welcome &amp; Pizza<br/>18.00 \u2013 18.45: AEM Integration for Phonak - Marijn Vermeulen, eFocus<br/>18.45 \u2013 19.00: break<br/>19.00 \u2013 19.45: Development Tooling + Roadmap - Gabriel Walt, Adobe<br/>19.45 \u2013 20.00: break<br/>20.00 \u2013 21.00: Unconference \u2013 bring your own topic, experiences that you want to share, open discussion - anything is possible \u263a<br/>21.00 \u2013 22.00: Drinks\xa0</p> <p>\n\n\n<b>1. AEM integration for Phonak\xa0</b></p> <p><b>About this session</b></p> <p><br/>During the last year Marijn, his colleagues and partner companies have been collaborating to create a new website with Adobe Experience Manager and Adobe Campaign for Phonak.\xa0In this session, Marijn will tell you about his personal experiences while integrating AEM and Adobe Campaign. He will share his successes, failures as well as some recommendations for future implementations.\xa0</p> <p><b>Bio</b><br/>Marijn Vermeulen is a Backend Developer at eFocus, a digital agency from The Netherlands. His specialty is creating AEM sites and he gained experience with integrating AEM and Adobe Campaign Manager. Marijn has over fifteen years of experience with building websites. He has been working with different languages such as PHP, C#, Java and multiple CMSs. He has been working for companies such as DSM, Shimano, McGregor, Sara Lee and D.E Master Blenders 1753.\xa0</p> <p><b><br/></b></p> <p><b>2. Development Tooling + Roadmap<br/></b></p> <p><b>About the session </b><br/>Gabriel will share the latest and best practices using the available development tooling. He will also share details what is coming up next for AEM.\xa0</p> <p><b>Bio</b><br/>Gabriel Walt is product manager at Adobe for Adobe Experience Manager and based in Basel, Switzerland. Gabriel drives the design-to-web innovations, developer efficiency and tooling topics for AEM. <a href="https://twitter.com/GabrielWalt" class="linkified">https://twitter.com/GabrielWalt</a></p>'
    events_list_event_162.local_start = dateutil.parser.parse("2015-09-03T17:00:00")
    events_list_event_162.local_end = dateutil.parser.parse("2015-09-03T17:00:00")
    events_list_event_162.utc_offset = 7200L
    events_list_event_162.is_applicable = True
    events_list_event_162 = importer.save_or_locate(events_list_event_162)

    events_list_event_162.hashtags.add(events_list_hashtag_1)

    events_list_event_163 = Event()
    events_list_event_163.name = u'LADataTech Monthly MixR'
    events_list_event_163.event_url = u'http://www.meetup.com/laphpdev/events/223686061/'
    events_list_event_163.group = events_list_group_150
    events_list_event_163.meetupID = u'dvsfskytmbfb'
    events_list_event_163.description = u'<p>Monthly Mixer for several Data/Tech meetups in LA.\xa0</p> <p>Join us at 31Ten Lounge in Santa Monica\xa0the 1st Thursday of every month.</p> <p>Happy Hour is 6pm-8pm!\xa0Stay as long as you like.</p> <p>Brought to you by\xa0<a href="https://www.linkedin.com/in/joedevon">Joe Devon</a>,\xa0<a href="https://www.linkedin.com/in/szilard">Szilard Pafka</a>\xa0and\xa0<a href="https://www.linkedin.com/in/sawjd">Subash D\'Souza</a>\xa0for the following meetup groups:</p> <p><a href="http://www.meetup.com/la-mysql/">The Los Angeles MySQL Meetup Group</a><br/><a href="http://www.meetup.com/LA-NewTech-Meetup/">LA NewTech Meetup\xa0</a><br/><a href="http://www.meetup.com/laphpdev/">LAPHP: The Los Angeles PHP Developers Group\xa0<br/></a><a href="http://www.meetup.com/ladmug/">Los Angeles Digital Media Usergroup\xa0<br/></a><a href="http://www.meetup.com/Los-Angeles-MongoDB-User-Group/">Los Angeles MongoDB User Group\xa0<br/></a><a href="http://www.meetup.com/lasemweb/">The Los Angeles Semantic Web Meetup\xa0<br/></a><a href="http://www.meetup.com/LAWebSpeed/">LAWebSpeed</a>\xa0<br/><a href="http://www.meetup.com/Los-Angeles-Big-Data-Users-Group/">Los Angeles Big Data Users Group</a>\xa0<br/><a href="http://www.meetup.com/LA-HUG/">Los Angeles Hadoop Users Group</a>\xa0<br/><a href="http://www.meetup.com/Los-Angeles-Apache-Spark-Users-Group/">Los Angeles Apache Spark Users Group</a>\xa0<br/><a href="http://www.meetup.com/Los-Angeles-HBase-User-group/">Los Angeles HBase Users Group</a>\xa0<br/><a href="http://www.meetup.com/Los-Angeles-R-Users-Group-Data-Science/">LA R Users Group</a>\xa0<br/><a href="http://www.meetup.com/Los-Angeles-Machine-Learning-Data-Science/">LA Data Science/Machine Learning</a>\xa0<br/><a href="http://www.meetup.com/Data-Visualization-Los-Angeles-Data-Science/">DataVis LA</a>\xa0<br/><a href="http://www.meetup.com/Python-Data-Science-Los-Angeles/">Python Data Science LA</a>\xa0<br/><a href="http://www.meetup.com/LA-Data-Warehouse-Business-Intelligence-Analytics/">LA Data Warehouse, Business Intelligence and Analytics</a>\xa0<br/><a href="http://datascience.la/">DataScience.LA</a>\xa0</p>'
    events_list_event_163.local_start = dateutil.parser.parse("2015-09-03T18:00:00")
    events_list_event_163.local_end = dateutil.parser.parse("2015-09-03T18:00:00")
    events_list_event_163.utc_offset = -25200L
    events_list_event_163.is_applicable = True
    events_list_event_163 = importer.save_or_locate(events_list_event_163)

    events_list_event_163.hashtags.add(events_list_hashtag_1)

    events_list_event_164 = Event()
    events_list_event_164.name = u'LADataTech Monthly MixR'
    events_list_event_164.event_url = u'http://www.meetup.com/Data-Science-Los-Angeles/events/220903859/'
    events_list_event_164.group = events_list_group_151
    events_list_event_164.meetupID = u'pmmnflytmbfb'
    events_list_event_164.description = u'<p>Monthly Mixer for several Data/Tech meetups in LA.\xa0</p> <p>\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nJoin us at 31Ten Lounge in Santa Monica <b>every 1st Thursday of the month</b> 6pm-10pm (happy hour 6pm-8pm)!</p> <p>\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nBrought to you by <a href="https://www.linkedin.com/in/joedevon">Joe Devon</a>, <a href="https://www.linkedin.com/in/szilard">Szilard Pafka</a> and <a href="https://www.linkedin.com/in/sawjd">Subash D\'Souza</a> for the following meetup groups:</p> <p>\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n<a href="http://www.meetup.com/Los-Angeles-Big-Data-Users-Group/">Los Angeles Big Data Users Group</a>\xa0<br/><a href="http://www.meetup.com/LA-HUG/">Los Angeles Hadoop Users Group</a>\xa0<br/><a href="http://www.meetup.com/Los-Angeles-Apache-Spark-Users-Group/">Los Angeles Apache Spark Users Group</a>\xa0<br/><a href="http://www.meetup.com/Los-Angeles-HBase-User-group/">Los Angeles HBase Users Group</a>\xa0<br/><a href="http://www.meetup.com/Los-Angeles-R-Users-Group-Data-Science/">LA R Users Group</a>\xa0<br/><a href="http://www.meetup.com/Los-Angeles-Machine-Learning-Data-Science/">LA Data Science/Machine Learning</a>\xa0<br/><a href="http://www.meetup.com/Data-Visualization-Los-Angeles-Data-Science/">DataVis LA</a>\xa0<br/><a href="http://www.meetup.com/Python-Data-Science-Los-Angeles/">Python Data Science LA</a>\xa0<br/><a href="http://www.meetup.com/LA-Data-Warehouse-Business-Intelligence-Analytics/">LA Data Warehouse, Business Intelligence and Analytics</a>\xa0<br/><a href="http://datascience.la/">DataScience.LA</a>\xa0<br/><a href="http://www.meetup.com/la-mysql/">The Los Angeles MySQL Meetup Group</a><br/><a href="http://www.meetup.com/LA-NewTech-Meetup/">LA NewTech Meetup</a><br/><a href="http://www.meetup.com/laphpdev/">LAPHP: The Los Angeles PHP Developers Group \xa0<br/></a><a href="http://www.meetup.com/ladmug/">Los Angeles Digital Media Usergroup \xa0<br/></a><a href="http://www.meetup.com/Los-Angeles-MongoDB-User-Group/">Los Angeles MongoDB User Group \xa0<br/></a><a href="http://www.meetup.com/lasemweb/">The Los Angeles Semantic Web Meetup \xa0<br/></a><a href="http://www.meetup.com/LAWebSpeed/">LAWebSpeed</a></p>'
    events_list_event_164.local_start = dateutil.parser.parse("2015-09-03T18:00:00")
    events_list_event_164.local_end = dateutil.parser.parse("2015-09-03T18:00:00")
    events_list_event_164.utc_offset = -25200L
    events_list_event_164.is_applicable = True
    events_list_event_164 = importer.save_or_locate(events_list_event_164)

    events_list_event_164.hashtags.add(events_list_hashtag_1)

    events_list_event_165 = Event()
    events_list_event_165.name = u'Introduction to Apache Drill - Self-Service Data Exploration & Nested Data'
    events_list_event_165.event_url = u'http://www.meetup.com/BIGDATAVISION/events/224209774/'
    events_list_event_165.group = events_list_group_152
    events_list_event_165.meetupID = u'224209774'
    events_list_event_165.description = u'<p><b>Introduction to Apache Drill -\xa0Self-Service Data Exploration and Nested Data Analytics on Hadoop\xa0</b></p> <p>SQL is one of the most widely used languages to access, enterprise data architectures across industries, the need for SQL for both structured and loosely-structured data on Hadoop is growing rapidly. Apache Drill started off with the audacious goal of delivering consistent, millisecond ANSI SQL query capability across wide range of data formats. At a high level, this translates to two key requirements \u2013 Schema Flexibility and Performance.</p> <p>Apache Drill provides the users the ability to interact with big data on Hadoop much faster and far more easily using the familiar SQL language. Users are no longer dependent on central IT teams and DBAs to produce schemas and then maintain them when the structure changes for a few records. Drill alleviates the pain associated with structuring unstructured data before one gains any insights by providing a simple mechanism to query any dataset on Hadoop - be it flat files, parquet or JSON files or tables within an HBase table. This session will give you an overview of several different use cases that enterprises are testing Drill for as well as the latest news on the project.</p> <p>\n\n\n<img src="http://photos1.meetupstatic.com/photos/event/9/d/c/a/600_440260394.jpeg" /></p> <p>\n\n\n<b>BIO ABOUT THE PRESENTER</b></p> <p><b>Vince Gonzalez - Systems Engineer, MapR</b>Vince Gonzalez is a Systems Engineer for MapR. \xa0He has 20 years of experience designing, implementing and automating infrastructure and applications. Previously, he was an Field Application Engineer for AMD Data Center Server Solutions (formerly SeaMicro), where he supported customers in the eastern U.S. Prior to AMD/SeaMicro, Vince worked for BlueArc Corporation. Vince held a variety of roles at BlueArc, including Field Engineer, Sales Engineer, and Director of Technical Services, where he led the Eastern region field technical team. Earlier in his career, Vince was a UNIX/Linux administrator.</p>'
    events_list_event_165.local_start = dateutil.parser.parse("2015-09-03T18:30:00")
    events_list_event_165.local_end = dateutil.parser.parse("2015-09-03T20:30:00")
    events_list_event_165.utc_offset = -14400L
    events_list_event_165.is_applicable = True
    events_list_event_165 = importer.save_or_locate(events_list_event_165)

    events_list_event_165.hashtags.add(events_list_hashtag_1)

    events_list_event_166 = Event()
    events_list_event_166.name = u'Code-level Deep Dive:  Shuffle & Network Optimizations to Win Daytona GraySort'
    events_list_event_166.event_url = u'http://www.meetup.com/Advanced-Apache-Spark-Meetup/events/223665950/'
    events_list_event_166.group = events_list_group_11
    events_list_event_166.meetupID = u'223665950'
    events_list_event_166.description = u'<p>Code-level Deep Dive into the optimizations that allowed Spark to win the Daytona GraySort Challenge: \xa0</p> <p><a href="https://databricks.com/blog/2014/10/10/spark-petabyte-sort.html"><a href="https://databricks.com/blog/2014/10/10/spark-petabyte-sort.html" class="linkified">https://databricks.com/blog/2014/10/10/spark-petabyte-sort.html</a></a></p> <p>We\'ll discuss the following at a code level:</p> <p>1) Sort-based Shuffle (less OS resources)</p> <p><a href="https://issues.apache.org/jira/browse/SPARK-2045"><a href="https://issues.apache.org/jira/browse/SPARK-2045" class="linkified">https://issues.apache.org/jira/browse/SPARK-2045</a></a></p> <p><br/>2) Netty-based Network module (epoll, async, ByteBuffer reuse)</p> <p><a href="https://issues.apache.org/jira/browse/SPARK-2468"><a href="https://issues.apache.org/jira/browse/SPARK-2468" class="linkified">https://issues.apache.org/jira/browse/SPARK-2468</a></a></p> <p><br/>3) External Shuffle Service (also allows for auto-scaling of Worker nodes)</p> <p><a href="https://issues.apache.org/jira/browse/SPARK-3796"><a href="https://issues.apache.org/jira/browse/SPARK-3796" class="linkified">https://issues.apache.org/jira/browse/SPARK-3796</a></a></p>'
    events_list_event_166.local_start = dateutil.parser.parse("2015-09-03T18:30:00")
    events_list_event_166.local_end = dateutil.parser.parse("2015-09-03T21:00:00")
    events_list_event_166.utc_offset = -25200L
    events_list_event_166.is_applicable = True
    events_list_event_166 = importer.save_or_locate(events_list_event_166)

    events_list_event_166.hashtags.add(events_list_hashtag_1)

    events_list_event_167 = Event()
    events_list_event_167.name = u'Web Performance for a Perfect Single Page Application'
    events_list_event_167.event_url = u'http://www.meetup.com/Web-Performance-NY/events/223626007/'
    events_list_event_167.group = events_list_group_153
    events_list_event_167.meetupID = u'223626007'
    events_list_event_167.description = u'<p>Web performance optimization techniques and practices are well defined, but rarely utilized to create fast, modern, single page web applications. In this tutorial <b>Chris Love</b> will demonstrate how to apply many common web performance optimization techniques and tricks to build a fast, native-like application user experience end users desire. In other words see how to apply performance best practices in a real-world application scenario.</p> <p><br/>This tutorial will demonstrate the following concepts:</p> <p><br/>\u2022\xa0Using the 14kb Rule for Instant Loading</p> <p>\u2022\xa0Markup Management</p> <p>\u2022\xa0Eliminating Excess AJAX Calls</p> <p>\u2022\xa0Working With and Around Application Cache</p> <p>\u2022\xa0Developing A Responsive Image Strategy</p> <p>\u2022\xa0Implementing A Good Touch First Strategy</p> <p>\u2022\xa0See How to Implement Small, Subtle Performance First</p> <p>\u2022\xa0Techniques to Have a Big Impact</p> <p>\u2022\xa0Code Management for good Production and Development</p> <p>\u2022\xa0Experiences</p> <p>\u2022\xa0Using Task Runners to Build &amp; Deploy Production Code\xa0</p> <p><img src="http://photos2.meetupstatic.com/photos/event/6/6/9/d/600_440006269.jpeg" /></p> <p>Chris\xa0(<a href="https://twitter.com/ChrisLove">@ChrisLove</a>) is a front-end developer for people and companies who are lost in the sea of modern web and user experience standards. Through his Blog, Speaking and books, he\u2019s here to help you shake up your approach to web development while making it all feel like fun. His insights and opinions have been featured in various magazines and popular web sites. He has helped hundreds of businesses and individuals ranging from mom and pops through major corporate brands build modern web experiences. And when he\u2019s not working on front-end development, you can find him spending time with his step-kids, learning karate and serving on his church\'s board of directors.</p> <p><br/><a href="http://www.spotify.com/">Spotify</a>\xa0is hosting us again. And they still have\xa0food and beer!</p> <p>As always, we are going to have\xa0<b>geekaways </b>with<b> awesome prizes!</b></p> <p>Agenda:</p> <p>6:30 - Arrive at\xa0Spotify, meet other members<br/>6:45 - Event starts<br/>7:00 -\xa0<b>Web Performance for a Perfect Single Page Application</b>\xa0(Chris Love)<br/>8:00 - Q&amp;A<br/>8:15 - "Books and Stuff" geekaways<br/>8:30 - Open Discussion, Networking</p> <p>Location:</p> <p>Spotify<br/><a href="http://bit.ly/1Jx2bUA">45 West 18th St<br/>7th floor<br/>New York,\xa0NY</a></p> <p>Directions on Google Maps:\xa0<a href="http://bit.ly/1Jx2bUA"><a href="http://bit.ly/1Jx2bUA" class="linkified">http://bit.ly/1Jx2bUA</a></a></p> <p>Entrance on StreetView:\xa0<a href="http://bit.ly/1QDVVyp"><a href="http://bit.ly/1QDVVyp" class="linkified">http://bit.ly/1QDVVyp</a></a></p> <p>\n\n\n<b>Our Sponsors:</b></p> <p>\u2022\xa0<a href="http://www.akamai.com/">Akamai\xae</a>\xa0is the leading cloud platform for helping enterprises provide secure, high-performing user experiences on any device, anywhere.</p> <p>\u2022\xa0<a href="http://instartlogic.com/">Instart Logic</a>\xa0replaces CDNs with intelligent streaming of web content. Users can interact with Web apps 2x faster, even for mobile devices.</p> <p>\u2022\xa0<a href="http://newrelic.com/">New Relic</a>\xa0is a software analytics company that makes sense of billions of metrics about millions of applications in real time.</p> <p>\u2022\xa0<a href="http://www.fastly.com/">Fastly</a>\xa0is the next generation in content delivery, designed to seamlessly integrate with your development stack.</p> <p>\u2022\xa0<a href="http://www.catchpoint.com/">Catchpoint</a>\xa0is sponsoring us by providing 10% discount to our members and geeky stuff to raffle off.</p> <p><a href="http://www.soasta.com/">\u2022\xa0SOASTA</a>\u2019s web and mobile app test automation solution enables developers, QA professionals, and IT Operations teams to test with unprecedented speed, scale and precision.</p>'
    events_list_event_167.local_start = dateutil.parser.parse("2015-09-03T18:30:00")
    events_list_event_167.local_end = dateutil.parser.parse("2015-09-03T18:30:00")
    events_list_event_167.utc_offset = -14400L
    events_list_event_167.is_applicable = True
    events_list_event_167 = importer.save_or_locate(events_list_event_167)

    events_list_event_167.hashtags.add(events_list_hashtag_1)

    events_list_event_168 = Event()
    events_list_event_168.name = u'Zion / Bryce / Monument Valley'
    events_list_event_168.event_url = u'http://www.meetup.com/North-Phoenix-Cruisers/events/219283813/'
    events_list_event_168.group = events_list_group_154
    events_list_event_168.meetupID = u'219283813'
    events_list_event_168.description = u"<p>I am taking my beloved Patricia to run the beautiful canyons of Southern Utah, on Labor day weekend. It would be great to share this experience, if you are available. It's a 1200-mile / 4-day ride, through a slightly different route from last year's: Zion, Bryce, Mon. Valley, with return through Snowflake and Globe. \xa0</p> <p><br/>Schedule is as follows (I've booked these hotels, but there are others available):\xa0</p> <p>Day 1 (Fri 09/04): 320 miles to Kanab, UT. Lunch at Cameron Trading Post. Parry Lodge @\xa089 East Center Street.\xa0Kanab, UT 84741.\xa0[masked]). ~$109 (brkfast included)</p> <p>Day 2 (Sat 09/05): 285 miles to Torrey, UT (through Zion). Capital Reef Inn &amp; Cafe @ 360 W Main St, Torrey, UT 84775\xa0(&lt;a&gt;[masked]&lt;/a&gt;) ~ $59 (brkfst available but separate)</p> <p>Day 3 (Sun 09/06): 290 miles to Chinle, AZ (through Bryce Canyon, and Monument Valley). Holiday Inn of Chinle @\xa0Bia Route 7, Chinle, AZ 86503\xa0[masked]) ~ $99 (brkfst available but separate)</p> <p>Day 4 (Mon 09/07): 304 miles to Apache Junction (through Holbrook and Globe).</p> <p>Hotels are filling up fast for that weekend.\xa0</p>"
    events_list_event_168.local_start = dateutil.parser.parse("2015-09-04T07:30:00")
    events_list_event_168.local_end = dateutil.parser.parse("2015-09-04T07:30:00")
    events_list_event_168.utc_offset = -25200L
    events_list_event_168.is_applicable = True
    events_list_event_168 = importer.save_or_locate(events_list_event_168)

    events_list_event_168.hashtags.add(events_list_hashtag_1)

    events_list_event_169 = Event()
    events_list_event_169.name = u'Naylin Channel with Maria Yraceburu on Google Hangout LIVE!'
    events_list_event_169.event_url = u'http://www.meetup.com/Taa-naash-kaa-da/events/223682431/'
    events_list_event_169.group = events_list_group_155
    events_list_event_169.meetupID = u'223682431'
    events_list_event_169.description = u'<p><img src="http://photos2.meetupstatic.com/photos/event/c/e/f/6/600_438772982.jpeg" /></p> <p>If you thought the first one was good, you won\'t want to miss this one!</p> <p>Share it with your friends. \xa0Plans are in the works for her to have a regular meeting, and answer personal question for people.</p> <p>9/4 \u2022 6 pm MST \u2022 Online / Lightstone Academy of Psychic ArtsDuring this online event, we will explore through breathing, guided meditation, questions and the process if channeling, PLUS Grandmother Nayline Lage channeling important messages regarding the earth changes of earth and more. She will also activate the StarEnergy that is streaming into the earth, to will help you be clearly connected with your Soul purpose.\u2014\u2014</p> <p>Naylin Channel with Maria Yraceburu on Google Hangout LIVE!</p> <p><br/>June 30 at 5pm-6pm Pacific Time, \xa0Apache medicine woman, Naylin Lage speaks for the first time via LIVE Google Hangout.<br/>For those of us who have been lucky enough to be in audience with the power of Naylin\'s medicine wisdom know how life changing just being embraced by her energy field can be. Naylin is the niece of Noch-ay-del-klinne and the great-grandmother of Maria Yraceburu, who has been channeling her wisdom for many years.<br/>Naylin will answer our questions the second half of the broadcast! This is a public event! There is no RSVP or charge to join us!\xa0<br/>Your questions must be submitted via email to [masked] by June 29 with the subject line: "Naylin Channel" to be considered. \xa0<br/>On JUNE 30 at 5pm PT ~ Watch the broadcast here:\xa0<a href="https://plus.google.com/events/cpqd0mbk19mfo1eg10ppsgkqvn4"><a href="https://plus.google.com/events/cpqd0mbk19mfo1eg10ppsgkqvn4" class="linkified">https://plus.google.com/events/cpqd0mbk19mfo1eg10ppsgkqvn4</a></a></p>'
    events_list_event_169.local_start = dateutil.parser.parse("2015-09-04T18:00:00")
    events_list_event_169.local_end = dateutil.parser.parse("2015-09-04T18:00:00")
    events_list_event_169.utc_offset = -21600L
    events_list_event_169.is_applicable = True
    events_list_event_169 = importer.save_or_locate(events_list_event_169)

    events_list_event_169.hashtags.add(events_list_hashtag_1)

    events_list_event_170 = Event()
    events_list_event_170.name = u'3rd Annual Devils Highway Run'
    events_list_event_170.event_url = u'http://www.meetup.com/PhxMRG/events/222578776/'
    events_list_event_170.group = events_list_group_156
    events_list_event_170.meetupID = u'222578776'
    events_list_event_170.description = u'<p>A weekend of riding, campfires, debauchery, and the most important RUM!!!</p> <p>Devils Highway Run\xb3</p> <p>Each year we ride the "Devils highway" on Labor Day weekend and try to make the ride a bit different each time, the only thing that is constant is us riding the "Devils Highway"</p> <p>This year our plans are to run the highway twice. Sunday we will head up it to Alpine for some grub those who wish to head home may do so at this point. For the rest after eating and maybe some exploring we head right back down to camp for another night of merriment.<br/>We are also heading a bit south to catch the 191 where it meets the I10, well, just because\u2026</p> <p><br/>The brief rundown of the trip:<br/>Sat Sept. 5th KSU 8:00am<br/>Start at Chevron Apache Junction 75 East 29th Avenue Apache Junction, AZ 85219 (Idaho and the 60) KSU at 8:00 am. There is a Waffle House there if you want to grab some grub. Make sure you get there early enough to eat.</p> <p>Fuel stop at Circle K 333 West Grant Road, Tucson, AZ 85705 (Approx 100 miles)</p> <p>Fuel Stop at TravelCenters of America 1501 Fort Grant Road, Willcox, AZ 85643 Approx 90miles)</p> <p>Then a stop in Morenci for Fuel and shoping. There is a Bashas\u2019 in town where we can/will pick up food and other items for the camp ground<br/>Bashas\' 172 Plaza Morenci, AZ 85540 (approx. 90 miles)</p> <p>Lunch we can discuss beforehand, it will be about 6-7 hours ride time including gas stops.</p> <p>Then just another 17 or so miles to the campground.</p> <p>For those of you who prefer camping with 4 \u201csolid\u201d walls and a roof there is the Rode Inn in Clifton <a href="http://rodeinnclifton.com/" class="linkified">http://rodeinnclifton.com/</a> . The last time we had someone stay there they were pretty booked up so plan accordingly.</p> <p>Saturdays Scoot Map <a href="https://goo.gl/maps/wPLvo" class="linkified">https://goo.gl/maps/wPLvo</a></p> <p>Day 2, Sunday:<br/>Head up 191 to Alpine for some grub the back down to camp</p> <p>Day 3 Monday Sept 7th<br/>Morning Grub at PJ\u2019s in Clifton, fuel up, maybe explore the town and head out</p> <p>Stop in Globe for Fuel and then home</p> <p>Mondays Scoot Map <a href="https://goo.gl/maps/o8jKh" class="linkified">https://goo.gl/maps/o8jKh</a></p> <p>More Details are to come and these may change as the date gets closer.</p> <p>We welcome suggestions and ideas</p> <p>Just some \u201cuseless\u201d trivia</p> <p>\u2022 U.S. Rt. 666 was first commissioned in 1926 with a northern terminus of Cortez, CO.<br/>\u2022 The Signage arrived to Arizona in 1938, stretching to Douglas, 30 miles of it overlapped U.S. Route 66.<br/>\u2022 1985 marked the end of U.S. Route 66 designation, leaving U.S 666 an orphan.<br/>\u2022 Dislike of the reference to the antichrist, street signs were stolen at a faster pace than they could be replaced, rerouting and complaints from superstitious drivers were a few of the reasons that lead to the gradual cessation of Route 666.<br/>\u2022 Arizona changed the numbering to U.S. 191 in 1993.<br/>\u2022 On May 31, 2013, U.S. Route 666 officially became extinct, leaving legends, scenic miles and the nickname \u201cThe Devil\u2019s Highway\u201d for posterity.</p>'
    events_list_event_170.local_start = dateutil.parser.parse("2015-09-05T07:30:00")
    events_list_event_170.local_end = dateutil.parser.parse("2015-09-07T13:00:00")
    events_list_event_170.utc_offset = -25200L
    events_list_event_170.is_applicable = True
    events_list_event_170 = importer.save_or_locate(events_list_event_170)

    events_list_event_170.hashtags.add(events_list_hashtag_1)

    events_list_event_171 = Event()
    events_list_event_171.name = u'Emerging Big Data Technologies/Frameworks'
    events_list_event_171.event_url = u'http://www.meetup.com/Big-Data-Hyderabad/events/223806896/'
    events_list_event_171.group = events_list_group_157
    events_list_event_171.meetupID = u'223806896'
    events_list_event_171.description = u'<p>We will discuss on new emerging big data technologies/frameworks:</p> <p>1. <b>Tachyon</b> :\xa0A memory-centric distributed storage system<br/>2. <b>BlinkDB</b> :\xa0Queries with Bounded Errors and Bounded Response Times on Very Large Data e.g. query on 10TB in 2sec using sampling<br/>3. <b>Presto</b> :\xa0Distributed SQL Query Engine for\xa0Big\xa0Data<br/>4. <b>Parquet</b>: Efficient columnar storage (to Hadoop/Spark)<br/>5.\xa0<b>Apache Flink</b> :\xa0scalable batch and stream data processing <b>(If time permits)</b></p>'
    events_list_event_171.local_start = dateutil.parser.parse("2015-09-05T10:00:00")
    events_list_event_171.local_end = dateutil.parser.parse("2015-09-05T10:00:00")
    events_list_event_171.utc_offset = 19800L
    events_list_event_171.is_applicable = True
    events_list_event_171 = importer.save_or_locate(events_list_event_171)

    events_list_event_171.hashtags.add(events_list_hashtag_1)

    events_list_event_172 = Event()
    events_list_event_172.name = u'Ionic Development Workshop Series: Level 1'
    events_list_event_172.event_url = u'http://www.meetup.com/Atlanta-Ionic-Developers/events/223319597/'
    events_list_event_172.group = events_list_group_158
    events_list_event_172.meetupID = u'223319597'
    events_list_event_172.description = u"<p><b>Welcome to the Ionic Workshop Level 1.\xa0</b><b>This is the first in a series of Ionic Workshops we will be conducting.</b></p> <p>This is a 5 hour workshop dedicated to getting you up to speed and building your first ever Ionic Application! We will be guiding you through the entire process, and at the end you will have your own Ionic Application that you build from scratch!</p> <p>This will be a guided workshop. The primary Instructor will be Bryan Oliver, Founder of Whitehall Technologies. Bryan has been working with Ionic since the beginning of the beta, and has built numerous Hybrid and Web Applications with the framework since it's rise. He has also presented on numerous other topics, including Test Driven Development, Sencha Touch Development, and Continuous Integration.\xa0</p> <p>We are also going to have several hands on instructors, who will be moving about the workshop to help you and answer your questions as we go along. If you get stuck, don't worry! They will get you out! Stay tuned for our list of Instructors.\xa0</p> <p>We are preparing a tailored experience for you. You will be building an Ionic application from scratch.\xa0</p> <p><b>By the end, you will be knowledgeable in the following:</b></p> <p>----</p> <p>- Use of the Ionic Command Line Tools.\xa0</p> <p>- Initial Scaffolding of an Ionic + Cordova Application.</p> <p>- How to Build, Test, Serve, and Debug an Ionic Application.</p> <p>- Implementing a basic registration and login system (we will provide you with a server api to connect to).</p> <p>- Implementing basic Facebook Login with an Ionic Application.</p> <p>- Managing and Adding Cordova Plugins for Native Features to an Ionic Application.</p> <p>- Using the Cordova Camera to take a picture with an Ionic Application.</p> <p>- Rendering basic resources in an Ionic Application (such as images you take with the camera).\xa0</p> <p>- Uploading an Ionic Application to Ionic View.\xa0</p> <p>- Packaging an Ionic Application with Cordova.</p> <p>- Packaging an Ionic Application with Cordova.</p> <p>----</p> <p><b>What we will be providing you with:\xa0</b></p> <p><br/>- A Server API to connect to. We will give you the source code to the API at the end of the course.\xa0</p> <p>- A course booklet. This will contain the following:\xa0</p> <p>1. All of the course materials.</p> <p>2. Some next steps for after the course.</p> <p>3. Some Topics on Hybrid and Ionic Development Best Practices.</p> <p>4. Code samples on some more advanced features.\xa0</p> <p>\n\n\n<b>Additional Info:\xa0</b></p> <p>1. All code and code snippets provided will be MIT licensed (open source for your use).\xa0</p> <p>2. We will be updating shortly with an Environment setup procedure that you <b>are required to do before arriving</b>. You don't want to get stuck downloading dependencies when the course starts.</p> <p>3. Please <b>SHARE </b>this MeetUp (Facebook, Twitter, etc.).\xa0</p> <p>\n\n\n<b>Final Notes:\xa0</b></p> <p>If you already know what you are doing with Ionic, don't sweat, we have a Level 2 slated for announcement very shortly</p> <p><br/>If you can't attend but still want access to the course booklet, contact the organizers. The cost for the digital booklet will be $5 if you cannot attend.</p>"
    events_list_event_172.local_start = dateutil.parser.parse("2015-09-05T13:00:00")
    events_list_event_172.local_end = dateutil.parser.parse("2015-09-05T18:00:00")
    events_list_event_172.utc_offset = -14400L
    events_list_event_172.is_applicable = True
    events_list_event_172 = importer.save_or_locate(events_list_event_172)

    events_list_event_172.hashtags.add(events_list_hashtag_1)

    events_list_event_173 = Event()
    events_list_event_173.name = u'Apache Spark'
    events_list_event_173.event_url = u'http://www.meetup.com/Haifa-Whats-new-with-BIG-DATA-Meetup/events/224285642/'
    events_list_event_173.group = events_list_group_159
    events_list_event_173.meetupID = u'224285642'
    events_list_event_173.description = u'<p>[masked] : Networking</p> <p><br/>2000:2045 : lecture "Apache Spark" by Roy Levin</p> <p>Descripton :</p> <p>Apache Spark is a popular Open Source Big Data processing framework.\xa0Among the main reasons for its popularity are it relative ease of use and its high performance (orders of 100x) when compared to Hadoop MapReduce based alternarives.In this talk I will provide an overview of Spark and focus specifically on what makes it so fast and easier to use. \xa0</p> <p>This meeting is sponserd by IBM and includes pizza and beer.</p>'
    events_list_event_173.local_start = dateutil.parser.parse("2015-09-06T19:30:00")
    events_list_event_173.local_end = dateutil.parser.parse("2015-09-06T21:00:00")
    events_list_event_173.utc_offset = 10800L
    events_list_event_173.is_applicable = True
    events_list_event_173 = importer.save_or_locate(events_list_event_173)

    events_list_event_173.hashtags.add(events_list_hashtag_1)

    events_list_event_174 = Event()
    events_list_event_174.name = u'Introduction to R programming - day 1'
    events_list_event_174.event_url = u'http://www.meetup.com/Open-Data-Innovation-Training-Hub/events/223355026/'
    events_list_event_174.group = events_list_group_160
    events_list_event_174.meetupID = u'223355026'
    events_list_event_174.description = u'<p>R for starters: duration: 2 days.\xa0This day forms one unit with day 2; it is not possible to register separately for one of the two days. The price indicated is the price per day, so registration for two days is Eur600.\xa0</p> <p>What is covered in this module:</p> <p>\u2022\xa0What is R, packages available (CRAN, R-Forge, ...), R documentation search, finding help, RStudio editor, syntax\xa0</p> <p>\u2022\xa0Data types: numeric, character, factor, logicals, NA, Dates/Times</p> <p>\u2022\xa0Data structures (vector/data.frame/matrix/lists and standard operations on these)</p> <p>\u2022\xa0Saving (RData) &amp; importing data from flat files, csv, Excel, Oracle, MS SQL Server, SAS, SPSS</p> <p>\u2022\xa0Creating functions, data manipulation (subsetting, adding variables, ifelse, control flow, recoding, rbind, cbind) and aggregating and reshaping</p> <p>\u2022\xa0Plotting in R using base and lattice functionality (dot plots, barcharts, graphical parameters, legends, devices)</p> <p>\u2022\xa0Basic statistics in R (mean, variance, crosstabs, quantile, correlation, distributions, densities, histograms, boxplot, t-tests, wilcoxon test, non-parametric tests)</p> <p>During the course, you will need to do exercises, so bring your laptop.</p> <p>Instructor: Jan Wijfels, <a href="http://www.bnosac.be/">BNOSAC</a></p> <p>Price: 600 Euro for the two days; register/pay via\xa0<a href="http://www.eventbrite.com/e/introduction-to-r-programming-tickets-17920927978">Eventbrite</a></p>'
    events_list_event_174.local_start = dateutil.parser.parse("2015-09-07T09:00:00")
    events_list_event_174.local_end = dateutil.parser.parse("2015-09-07T17:00:00")
    events_list_event_174.utc_offset = 7200L
    events_list_event_174.is_applicable = True
    events_list_event_174 = importer.save_or_locate(events_list_event_174)

    events_list_event_174.hashtags.add(events_list_hashtag_1)

    events_list_event_175 = Event()
    events_list_event_175.name = u'Google Next - Google Cloud event for developers and IT professionals'
    events_list_event_175.event_url = u'http://www.meetup.com/IGTCloud/events/224337600/'
    events_list_event_175.group = events_list_group_75
    events_list_event_175.meetupID = u'224337600'
    events_list_event_175.description = u'<p>You\'re invited to Next, an event coming to Tel Aviv from <b>Google Cloud Platform</b> where you\u2019ll be joined by hundreds of Developers and IT Professionals to \xa0learn about the next generation of Cloud.</p> <p>At the event you can:</p> <p>- Learn how to build faster with the latest Cloud technologies using mobile, big data, compute, and security.</p> <p>- Meet with peers and Google engineers to discuss the future of cloud computing and how we can push new boundaries.</p> <p>- Receive technical training via hands-on labs.</p> <p>Please complete your registration at the Google event site:</p> <p><a href="https://goo.gl/YflPsF"><a href="https://goo.gl/YflPsF" class="linkified">https://goo.gl/YflPsF</a></a></p>'
    events_list_event_175.local_start = dateutil.parser.parse("2015-09-07T10:00:00")
    events_list_event_175.local_end = dateutil.parser.parse("2015-09-07T16:30:00")
    events_list_event_175.utc_offset = 10800L
    events_list_event_175.is_applicable = True
    events_list_event_175 = importer.save_or_locate(events_list_event_175)

    events_list_event_175.hashtags.add(events_list_hashtag_1)

    events_list_event_176 = Event()
    events_list_event_176.name = u'Cassandra MSP Meetup'
    events_list_event_176.event_url = u'http://www.meetup.com/Minneapolis-St-Paul-Cassandra-Meetup/events/222866089/'
    events_list_event_176.group = events_list_group_161
    events_list_event_176.meetupID = u'crtlglytmbkb'
    events_list_event_176.description = u'<p>\u2022 6:30 - Food and Social Time<br/>\u2022 7:00 - Lightning Talks (Open to all)<br/>\u2022 Following - Main Presentation</p>'
    events_list_event_176.local_start = dateutil.parser.parse("2015-09-07T18:30:00")
    events_list_event_176.local_end = dateutil.parser.parse("2015-09-07T18:30:00")
    events_list_event_176.utc_offset = -18000L
    events_list_event_176.is_applicable = True
    events_list_event_176 = importer.save_or_locate(events_list_event_176)

    events_list_event_176.hashtags.add(events_list_hashtag_1)

    events_list_event_177 = Event()
    events_list_event_177.name = u'Machine Learning with Apache Spark and Word embeddings'
    events_list_event_177.event_url = u'http://www.meetup.com/spark-zurich/events/224213662/'
    events_list_event_177.group = events_list_group_162
    events_list_event_177.meetupID = u'224213662'
    events_list_event_177.description = u'<p>more details to come soon...</p> <p>This is a joint event with <a href="http://www.research.ibm.com/labs/zurich/">IBM Research Lab Zurich</a>, and the\xa0<a href="http://www.meetup.com/Zurich-Machine-Learning/events/223477218/">Zurich Machine Learning and Data Science Meetup</a> group</p> <p>Preliminary program:</p> <p><b>\u2022\xa0Introduction to Word-Embeddings</b><br/><a href="http://www.da.inf.ethz.ch/people/FlorianSchmidt/">Florian Schmidt</a>, ETH\xa0Z\xfcrich</p> <p><b>\u2022\xa0Leveraging word-embeddings (word2vec, and glove) for natural and semi-natural text classification and clustering<br/></b>Speaker by IBM Research</p> <p><b>\u2022 Distributed Machine Learning with Apache Spark</b><br/><a href="https://www.linkedin.com/pub/christina-heinze/a3/9b4/a71">Christina Heinze</a>, ETH Z\xfcrich</p>'
    events_list_event_177.local_start = dateutil.parser.parse("2015-09-08T18:30:00")
    events_list_event_177.local_end = dateutil.parser.parse("2015-09-08T21:30:00")
    events_list_event_177.utc_offset = 7200L
    events_list_event_177.is_applicable = True
    events_list_event_177 = importer.save_or_locate(events_list_event_177)

    events_list_event_177.hashtags.add(events_list_hashtag_1)

    events_list_event_178 = Event()
    events_list_event_178.name = u'September Meetup - Leveraging Solr for website searches and more'
    events_list_event_178.event_url = u'http://www.meetup.com/Apache-Lucene-Solr-London-User-Group/events/223986670/'
    events_list_event_178.group = events_list_group_163
    events_list_event_178.meetupID = u'223986670'
    events_list_event_178.description = u'<p>This month, BlackRock has very kindly offered to host us, sponsor drinks and pizzas AND speak at our meetup! Thank you so much to BlackRock for this!</p> <p><b>PLEASE NOTE</b><i>: You will need to RSVP with your full name, not just Meetup nickname, as a list will be given to security.\xa0</i></p> <p>First Talk:\xa0<b>Leveraging Solr to help power websites</b></p> <p><b>Speakers</b>: Ife Nkechukwu and Erica Sundberg are both a software developers at <a href="http://www.blackrock.com">BlackRock</a>.</p> <p><br/><b>Synopsis: </b>Solr is one of the main open source search engines. Ife and Erica have been evaluating how it can be used as the base technology for website search on blackrock.com; Theywill be discussing the pros and cons of Solr, in the problem domain of website search including indexing data, web crawling, and faceting</p> <p>Second talk TBC.\xa0</p>'
    events_list_event_178.local_start = dateutil.parser.parse("2015-09-08T18:30:00")
    events_list_event_178.local_end = dateutil.parser.parse("2015-09-08T18:30:00")
    events_list_event_178.utc_offset = 3600L
    events_list_event_178.is_applicable = True
    events_list_event_178 = importer.save_or_locate(events_list_event_178)

    events_list_event_178.hashtags.add(events_list_hashtag_1)

    events_list_event_179 = Event()
    events_list_event_179.name = u'Outdoor Football'
    events_list_event_179.event_url = u'http://www.meetup.com/stockholmsportypeople/events/224394664/'
    events_list_event_179.group = events_list_group_76
    events_list_event_179.meetupID = u'kbbhhlytmbkb'
    events_list_event_179.description = u"<p>Please check the comments just before the event:\xa0maybe we decide not to play because of the weather or so...</p> <p>--------------------------------------</p> <p>GENERAL INFORMATION:</p> <p>Please note that these games are friendly games and everybody has to be\xa0fair play. In case of unappropriate behaviour (hard tackling,\xa0direct swearing, etc) you will be warned and eventually asked to leave the pitch. We play for fun so let's have fun together!</p> <p>Please take:</p> <p>\u2022\xa01 white AND 1 black\xa0t-shirt, so that we can change teams if needed.</p> <p>\u2022\xa0football shoes or normal sport shoes, but football shoes are recommended as we play on artificial grass (outdoor) and it can be slippery.</p> <p>\u2022\xa0water, as there is no access to water there.</p> <p>\u2022\xa0a ball if you have one, so that we can play with the best one</p> <p>\u2022\xa0shin pads are recommended: even if we don't play the world cup, it's always better to have good protections!</p> <p>\u2022 Location for Monday games will be posted on Sundays and location for Friday games posted on Wednesday<br/>There are no shower or changing cabins there.</p>"
    events_list_event_179.local_start = dateutil.parser.parse("2015-09-07T19:00:00")
    events_list_event_179.local_end = dateutil.parser.parse("2015-09-07T22:00:00")
    events_list_event_179.utc_offset = 7200L
    events_list_event_179.is_applicable = False
    events_list_event_179 = importer.save_or_locate(events_list_event_179)

    events_list_event_179.hashtags.add(events_list_hashtag_1)

    events_list_event_180 = Event()
    events_list_event_180.name = u'Outdoor Football'
    events_list_event_180.event_url = u'http://www.meetup.com/stockholmsportypeople/events/223782307/'
    events_list_event_180.group = events_list_group_76
    events_list_event_180.meetupID = u'kbbhhlytmbgb'
    events_list_event_180.description = u"<p>Please check the comments just before the event:\xa0maybe we decide not to play because of the weather or so...</p> <p>--------------------------------------</p> <p>GENERAL INFORMATION:</p> <p>Please note that these games are friendly games and everybody has to be\xa0fair play. In case of unappropriate behaviour (hard tackling,\xa0direct swearing, etc) you will be warned and eventually asked to leave the pitch. We play for fun so let's have fun together!</p> <p>Please take:</p> <p>\u2022\xa01 white AND 1 black\xa0t-shirt, so that we can change teams if needed.</p> <p>\u2022\xa0football shoes or normal sport shoes, but football shoes are recommended as we play on artificial grass (outdoor) and it can be slippery.</p> <p>\u2022\xa0water, as there is no access to water there.</p> <p>\u2022\xa0a ball if you have one, so that we can play with the best one</p> <p>\u2022\xa0shin pads are recommended: even if we don't play the world cup, it's always better to have good protections!</p> <p>\u2022 Location for Monday games will be posted on Sundays and location for Friday games posted on Wednesday<br/>There are no shower or changing cabins there.</p>"
    events_list_event_180.local_start = dateutil.parser.parse("2015-09-04T19:00:00")
    events_list_event_180.local_end = dateutil.parser.parse("2015-09-04T22:00:00")
    events_list_event_180.utc_offset = 7200L
    events_list_event_180.is_applicable = False
    events_list_event_180 = importer.save_or_locate(events_list_event_180)

    events_list_event_180.hashtags.add(events_list_hashtag_1)

    events_list_event_181 = Event()
    events_list_event_181.name = u'Outdoor Football'
    events_list_event_181.event_url = u'http://www.meetup.com/stockholmsportypeople/events/223782298/'
    events_list_event_181.group = events_list_group_76
    events_list_event_181.meetupID = u'kbbhhlytlblc'
    events_list_event_181.description = u"<p>Please check the comments just before the event:\xa0maybe we decide not to play because of the weather or so...</p> <p>--------------------------------------</p> <p>GENERAL INFORMATION:</p> <p>Please note that these games are friendly games and everybody has to be\xa0fair play. In case of unappropriate behaviour (hard tackling,\xa0direct swearing, etc) you will be warned and eventually asked to leave the pitch. We play for fun so let's have fun together!</p> <p>Please take:</p> <p>\u2022\xa01 white AND 1 black\xa0t-shirt, so that we can change teams if needed.</p> <p>\u2022\xa0football shoes or normal sport shoes, but football shoes are recommended as we play on artificial grass (outdoor) and it can be slippery.</p> <p>\u2022\xa0water, as there is no access to water there.</p> <p>\u2022\xa0a ball if you have one, so that we can play with the best one</p> <p>\u2022\xa0shin pads are recommended: even if we don't play the world cup, it's always better to have good protections!</p> <p>\u2022 Location for Monday games will be posted on Sundays and location for Friday games posted on Wednesday<br/>There are no shower or changing cabins there.</p>"
    events_list_event_181.local_start = dateutil.parser.parse("2015-08-28T19:00:00")
    events_list_event_181.local_end = dateutil.parser.parse("2015-08-28T22:00:00")
    events_list_event_181.utc_offset = 7200L
    events_list_event_181.is_applicable = False
    events_list_event_181 = importer.save_or_locate(events_list_event_181)

    events_list_event_181.hashtags.add(events_list_hashtag_1)

    events_list_event_182 = Event()
    events_list_event_182.name = u'Afterwork Kayaking'
    events_list_event_182.event_url = u'http://www.meetup.com/stockholmsportypeople/events/223913154/'
    events_list_event_182.group = events_list_group_76
    events_list_event_182.meetupID = u'gcvphlytlbrb'
    events_list_event_182.description = u'<p>Every Thursday during summer we\u2019ll meet for a paddle around the city, often involving a stop for a drink/picnic/swim.</p> <p><img src="http://photos3.meetupstatic.com/photos/event/7/d/5/3/600_438152083.jpeg" /></p> <p><img src="http://photos4.meetupstatic.com/photos/event/d/3/6/a/600_406074122.jpeg" /></p> <p><img src="http://photos2.meetupstatic.com/photos/event/d/8/5/6/600_403555382.jpeg" /></p> <p><i>The boring bits:</i><br/>* The event is strictly for SWIMMERS ONLY<br/>* First timers are welcome but at their own risk - look out for beginner lesson events if you aren\'t confident you can keep up with the group.<br/>* The rental fee is 200SEK for 2-3 hours kayak + all necessary equipment rental.<br/>* To reserve a kayak with the group, you must pay 24 hours in advance &amp; there are no refunds. <b>The Swish code to pay is:[masked]</b>.<br/>*If you want to come along on the off chance, you are welcome but there is no guarantee there will be a kayak available for you. If you pay far in advance and have to drop out with more than 24 hours\' notice I should be able to move you to a later event, but I make the kayak reservation on Wednesday evening and after that it\'s final.<br/>*there are no lockers available at Kafe Kayak. You can bring your things with you in the kayak or else leave them in the hut with the staff.<br/>* there is no particular clothing necessary, wear roughly what you might wear to go running.</p> <p>See you on the water!</p>'
    events_list_event_182.local_start = dateutil.parser.parse("2015-08-13T18:15:00")
    events_list_event_182.local_end = dateutil.parser.parse("2015-08-13T21:15:00")
    events_list_event_182.utc_offset = 7200L
    events_list_event_182.is_applicable = False
    events_list_event_182 = importer.save_or_locate(events_list_event_182)

    events_list_event_182.hashtags.add(events_list_hashtag_1)

    events_list_event_183 = Event()
    events_list_event_183.name = u'Outdoor Football'
    events_list_event_183.event_url = u'http://www.meetup.com/stockholmsportypeople/events/222707379/'
    events_list_event_183.group = events_list_group_76
    events_list_event_183.meetupID = u'kbbhhlytlbnb'
    events_list_event_183.description = u"<p>Please check the comments just before the event:\xa0maybe we decide not to play because of the weather or so...</p> <p>--------------------------------------</p> <p>GENERAL INFORMATION:</p> <p>Please note that these games are friendly games and everybody has to be\xa0fair play. In case of unappropriate behaviour (hard tackling,\xa0direct swearing, etc) you will be warned and eventually asked to leave the pitch. We play for fun so let's have fun together!</p> <p>Please take:</p> <p>\u2022\xa01 white AND 1 black\xa0t-shirt, so that we can change teams if needed.</p> <p>\u2022\xa0football shoes or normal sport shoes, but football shoes are recommended as we play on artificial grass (outdoor) and it can be slippery.</p> <p>\u2022\xa0water, as there is no access to water there.</p> <p>\u2022\xa0a ball if you have one, so that we can play with the best one</p> <p>\u2022\xa0shin pads are recommended: even if we don't play the world cup, it's always better to have good protections!</p> <p>\u2022 Location for Monday games will be posted on Sundays and location for Friday games posted on Wednesday<br/>There are no shower or changing cabins there.</p>"
    events_list_event_183.local_start = dateutil.parser.parse("2015-08-10T19:00:00")
    events_list_event_183.local_end = dateutil.parser.parse("2015-08-10T22:00:00")
    events_list_event_183.utc_offset = 7200L
    events_list_event_183.is_applicable = False
    events_list_event_183 = importer.save_or_locate(events_list_event_183)

    events_list_event_183.hashtags.add(events_list_hashtag_1)

    events_list_event_184 = Event()
    events_list_event_184.name = u'Bohemian Circus Figure Drawing Group at Apache Cafe'
    events_list_event_184.event_url = u'http://www.meetup.com/Figure-Drawing-Group-at-Apache-Cafe/events/224411835/'
    events_list_event_184.group = events_list_group_164
    events_list_event_184.meetupID = u'gmjgqytlbnb'
    events_list_event_184.description = u'<p><img src="http://photos1.meetupstatic.com/photos/event/8/9/6/9/event_20615177.jpeg" /> <img src="http://photos3.meetupstatic.com/photos/event/3/6/e/d/event_39194061.jpeg" /></p> <p>\xa0</p> <p>\xa0</p> <p>\xa0</p> <p>\xa0</p> <p>\xa0</p> <p>\xa0</p> <p>\xa0</p> <p>\xa0</p> <p>\xa0</p> <p>Open figure drawing and photography session. Meet-up Details: Mondays from 7:30PM to 11PM Apache Cafe provides figure models for artist and photographers to casually drop in and create without a need to pre-register or commit to a multiple week drawing class. Please remember to bring your own supplies! Flow of the night: At Apache Cafe a typical figure/life drawing session (class) the attendees sit around a model either in a semicircle or a full circle. No two students have exactly the same view, thus their drawing or photography will reflect the perspective of the artist\'s unique location relative to the model. The model often poses on a stand, so attendees can more easily find an unobstructed view, depending on the type of pose, furniture and/or props used. At the beginning of the figure drawing session, the model is often requested to make a series of brief poses in rapid succession. These are called gestures poses, and are typically one to three minutes each. Gesture drawing is a warm-up exercise for many artists, although some artists sketch out the gesture as the first step in every figure drawing. Since the purpose of figure drawing classes is to learn how to draw humans of all kinds, male and female models of all ages, shapes, and ethnicities are usually sought, rather than selecting only beautiful models or those with "ideal figures". The variety of models hired may be limited by the need for them to hold a pose for extended periods. Scheduled models are posted on our Calendar events page.</p>'
    events_list_event_184.local_start = dateutil.parser.parse("2015-08-10T19:00:00")
    events_list_event_184.local_end = dateutil.parser.parse("2015-08-10T19:00:00")
    events_list_event_184.utc_offset = -14400L
    events_list_event_184.is_applicable = False
    events_list_event_184 = importer.save_or_locate(events_list_event_184)

    events_list_event_184.hashtags.add(events_list_hashtag_1)

    # Processing model: Log

    from events_list.models import Log

    events_list_log_1 = Log()
    events_list_log_1.description = u'Group (id=10) marked as not applicable '
    events_list_log_1.datetime = dateutil.parser.parse("2015-08-08T22:39:07.794287")
    events_list_log_1.action_type = u'GU'
    events_list_log_1.object_id = 10L
    events_list_log_1 = importer.save_or_locate(events_list_log_1)

    events_list_log_2 = Log()
    events_list_log_2.description = u'Group (id=5) marked as not applicable '
    events_list_log_2.datetime = dateutil.parser.parse("2015-08-08T22:34:24.062499")
    events_list_log_2.action_type = u'GU'
    events_list_log_2.object_id = 5L
    events_list_log_2 = importer.save_or_locate(events_list_log_2)

    events_list_log_3 = Log()
    events_list_log_3.description = u'Group (id=4) marked as not applicable '
    events_list_log_3.datetime = dateutil.parser.parse("2015-08-08T19:15:44.793505")
    events_list_log_3.action_type = u'GU'
    events_list_log_3.object_id = 4L
    events_list_log_3 = importer.save_or_locate(events_list_log_3)

    events_list_log_4 = Log()
    events_list_log_4.description = u'Group (id=23) marked as not applicable '
    events_list_log_4.datetime = dateutil.parser.parse("2015-08-08T07:41:07.079514")
    events_list_log_4.action_type = u'GU'
    events_list_log_4.object_id = 23L
    events_list_log_4 = importer.save_or_locate(events_list_log_4)

    events_list_log_5 = Log()
    events_list_log_5.description = u'Group (id=41) marked as not applicable '
    events_list_log_5.datetime = dateutil.parser.parse("2015-08-08T07:38:28.468544")
    events_list_log_5.action_type = u'GU'
    events_list_log_5.object_id = 41L
    events_list_log_5 = importer.save_or_locate(events_list_log_5)

    events_list_log_6 = Log()
    events_list_log_6.description = u'Group (id=52) marked as not applicable '
    events_list_log_6.datetime = dateutil.parser.parse("2015-08-08T07:38:18.641857")
    events_list_log_6.action_type = u'GU'
    events_list_log_6.object_id = 52L
    events_list_log_6 = importer.save_or_locate(events_list_log_6)

    events_list_log_7 = Log()
    events_list_log_7.description = u'Group (id=8) marked as not applicable '
    events_list_log_7.datetime = dateutil.parser.parse("2015-08-08T07:38:11.978958")
    events_list_log_7.action_type = u'GU'
    events_list_log_7.object_id = 8L
    events_list_log_7 = importer.save_or_locate(events_list_log_7)

    events_list_log_8 = Log()
    events_list_log_8.description = u'Group (id=3) marked as not applicable '
    events_list_log_8.datetime = dateutil.parser.parse("2015-08-08T07:35:35.832371")
    events_list_log_8.action_type = u'GU'
    events_list_log_8.object_id = 3L
    events_list_log_8 = importer.save_or_locate(events_list_log_8)

    events_list_log_9 = Log()
    events_list_log_9.description = u'Group (id=1) marked as not applicable '
    events_list_log_9.datetime = dateutil.parser.parse("2015-08-08T07:35:26.222618")
    events_list_log_9.action_type = u'GU'
    events_list_log_9.object_id = 1L
    events_list_log_9 = importer.save_or_locate(events_list_log_9)

    events_list_log_10 = Log()
    events_list_log_10.description = u'Group (id=11) marked as not applicable '
    events_list_log_10.datetime = dateutil.parser.parse("2015-08-08T07:35:08.711086")
    events_list_log_10.action_type = u'GU'
    events_list_log_10.object_id = 11L
    events_list_log_10 = importer.save_or_locate(events_list_log_10)

    events_list_log_11 = Log()
    events_list_log_11.description = u'Events imported'
    events_list_log_11.datetime = dateutil.parser.parse("2015-08-08T07:34:48.871882")
    events_list_log_11.action_type = u'EI'
    events_list_log_11.object_id = None
    events_list_log_11 = importer.save_or_locate(events_list_log_11)

