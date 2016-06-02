# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import os
import unittest
import start
from subprocess import call


class ApiTestCase(unittest.TestCase):
    database_file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'database/api.db'))
    database_schema_file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'database/schema.sql'))

    def _update_db(self):
        try:
            call(["rm", "-rf", self.database_file])
            update_db = "sqlite3 %s < %s" % (self.database_file, self.database_schema_file)
            os.system(update_db)
        except OSError as e:
            print(e)

    def setUp(self):
        self.app = start.app.test_client()
        self._update_db()

    def tearDown(self):
        self._update_db()

    # assets list

    def test_assets_list(self):
        response = self.app.get('/?sort_by')
        assert response.status_code == 400
        response = self.app.get('/')
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert int(response_data[0]['id']) == 1
        assert response_data[0]['title'] == "Wiredrive IOWA: Wiredrive Award Winners 2009"
        assert response_data[0]['description'] == \
               "https://iowa.wiredrive.com/present-library-gallery/token/e5d10087fd878ba5dc8ea7857495710b"
        assert response_data[0]['created_at'] == "Wed, 01 Jun 2016 00:00:00 -0000"

    def test_assets_list_asc(self):
        response = self.app.get('/?sort_by')
        assert response.status_code == 400
        response = self.app.get('/?sort_by=asc')
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert int(response_data[0]['id']) == 1
        assert response_data[0]['title'] == "Wiredrive IOWA: Wiredrive Award Winners 2009"
        assert response_data[0]['description'] == \
               "https://iowa.wiredrive.com/present-library-gallery/token/e5d10087fd878ba5dc8ea7857495710b"
        assert response_data[0]['created_at'] == "Wed, 01 Jun 2016 00:00:00 -0000"

    def test_assets_list_desc(self):
        response = self.app.get('/?sort_by')
        assert response.status_code == 400
        response = self.app.get('/?sort_by=asc')
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert int(response_data[0]['id']) == 1
        assert response_data[0]['title'] == "Wiredrive IOWA: Wiredrive Award Winners 2009"
        assert response_data[0]['description'] == \
               "https://iowa.wiredrive.com/present-library-gallery/token/e5d10087fd878ba5dc8ea7857495710b"
        assert response_data[0]['created_at'] == "Wed, 01 Jun 2016 00:00:00 -0000"

    def test_assets_list_limit(self):
        response = self.app.get('/?limit')
        assert response.status_code == 400

        response = self.app.get('/?limit=2')
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert len(response_data) == 2
        assert int(response_data[0]['id']) == 1
        assert response_data[0]['title'] == "Wiredrive IOWA: Wiredrive Award Winners 2009"
        assert response_data[0]['description'] == \
               "https://iowa.wiredrive.com/present-library-gallery/token/e5d10087fd878ba5dc8ea7857495710b"
        assert response_data[0]['created_at'] == "Wed, 01 Jun 2016 00:00:00 -0000"

        response = self.app.get('/?limit=1')
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert len(response_data) == 1
        assert int(response_data[0]['id']) == 1
        assert response_data[0]['title'] == "Wiredrive IOWA: Wiredrive Award Winners 2009"
        assert response_data[0]['description'] == \
               "https://iowa.wiredrive.com/present-library-gallery/token/e5d10087fd878ba5dc8ea7857495710b"
        assert response_data[0]['created_at'] == "Wed, 01 Jun 2016 00:00:00 -0000"

        response = self.app.get('/?limit=-1')
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert len(response_data) == 2
        assert int(response_data[0]['id']) == 1
        assert response_data[0]['title'] == "Wiredrive IOWA: Wiredrive Award Winners 2009"
        assert response_data[0]['description'] == \
               "https://iowa.wiredrive.com/present-library-gallery/token/e5d10087fd878ba5dc8ea7857495710b"
        assert response_data[0]['created_at'] == "Wed, 01 Jun 2016 00:00:00 -0000"

    def test_assets_list_sort_limit(self):
        response = self.app.get('/?limit&sort_by')
        assert response.status_code == 400

        response = self.app.get('/?limit=1&sort_by')
        assert response.status_code == 400

        response = self.app.get('/?limit1=1&sort_by1')
        assert response.status_code == 400

        response = self.app.get('/?limit&sort_by=asc')
        assert response.status_code == 400

        response = self.app.get('/?limit=2&sort_by=asc')
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert len(response_data) == 2
        assert int(response_data[0]['id']) == 1
        assert response_data[0]['title'] == "Wiredrive IOWA: Wiredrive Award Winners 2009"
        assert response_data[0]['description'] == \
               "https://iowa.wiredrive.com/present-library-gallery/token/e5d10087fd878ba5dc8ea7857495710b"
        assert response_data[0]['created_at'] == "Wed, 01 Jun 2016 00:00:00 -0000"

        response = self.app.get('/?limit=2&sort_by=desc')
        response_data = json.loads(response.data)
        assert response.status_code == 200
        assert len(response_data) == 2
        assert int(response_data[0]['id']) == 2
        assert response_data[0]['title'] == "Wiredrive IOWA: Wiredrive Award Winners 2010"
        assert response_data[0]['description'] == \
               "https://iowa.wiredrive.com/present-library-gallery/token/e5d10087fd878ba5dc8ea7857495710b1"
        assert response_data[0]['created_at'] == "Tue, 31 May 2016 00:00:00 -0000"

        response = self.app.get('/?limit=1&sort_by=asc')
        response_data = json.loads(response.data)
        assert response.status_code == 200
        assert len(response_data) == 1
        assert int(response_data[0]['id']) == 1
        assert response_data[0]['title'] == "Wiredrive IOWA: Wiredrive Award Winners 2009"
        assert response_data[0]['description'] == \
               "https://iowa.wiredrive.com/present-library-gallery/token/e5d10087fd878ba5dc8ea7857495710b"
        assert response_data[0]['created_at'] == "Wed, 01 Jun 2016 00:00:00 -0000"

        response = self.app.get('/?limit=1&sort_by=desc')
        response_data = json.loads(response.data)
        assert response.status_code == 200
        assert len(response_data) == 1
        assert int(response_data[0]['id']) == 2
        assert response_data[0]['title'] == "Wiredrive IOWA: Wiredrive Award Winners 2010"
        assert response_data[0]['description'] == \
               "https://iowa.wiredrive.com/present-library-gallery/token/e5d10087fd878ba5dc8ea7857495710b1"
        assert response_data[0]['created_at'] == "Tue, 31 May 2016 00:00:00 -0000"

    def test_assets_list_credits_filter(self):
        response = self.app.get('/?credits_filter1')
        assert response.status_code == 400

        response = self.app.get('/?credits_filter')
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert len(response_data) == 2
        assert int(response_data[0]['id']) == 1
        assert response_data[0]['title'] == "Wiredrive IOWA: Wiredrive Award Winners 2009"
        assert response_data[0]['description'] == \
               "https://iowa.wiredrive.com/present-library-gallery/token/e5d10087fd878ba5dc8ea7857495710b"
        assert response_data[0]['created_at'] == "Wed, 01 Jun 2016 00:00:00 -0000"

        response = self.app.get('/?credits_filter=angry')
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert len(response_data) == 1
        assert int(response_data[0]['id']) == 1
        assert response_data[0]['title'] == "Wiredrive IOWA: Wiredrive Award Winners 2009"
        assert response_data[0]['description'] == \
               "https://iowa.wiredrive.com/present-library-gallery/token/e5d10087fd878ba5dc8ea7857495710b"
        assert response_data[0]['created_at'] == "Wed, 01 Jun 2016 00:00:00 -0000"

        response = self.app.get('/?credits_filter=asd')
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert len(response_data) == 0

        response = self.app.get('/?credits_filter=Fozie Bear')
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert len(response_data) == 2
        assert int(response_data[0]['id']) == 1
        assert response_data[0]['title'] == "Wiredrive IOWA: Wiredrive Award Winners 2009"
        assert response_data[0]['description'] == \
               "https://iowa.wiredrive.com/present-library-gallery/token/e5d10087fd878ba5dc8ea7857495710b"
        assert response_data[0]['created_at'] == "Wed, 01 Jun 2016 00:00:00 -0000"

    def test_assets_list_limit_sort_credits(self):
        response = self.app.get('/?credits_filter=angry&limit=2&sort_by=asc')
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert len(response_data) == 1
        assert int(response_data[0]['id']) == 1
        assert response_data[0]['title'] == "Wiredrive IOWA: Wiredrive Award Winners 2009"
        assert response_data[0]['description'] == \
               "https://iowa.wiredrive.com/present-library-gallery/token/e5d10087fd878ba5dc8ea7857495710b"
        assert response_data[0]['created_at'] == "Wed, 01 Jun 2016 00:00:00 -0000"

        response = self.app.get('/?credits_filter=angry&limit=2&sort_by=desc')
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert len(response_data) == 1
        assert int(response_data[0]['id']) == 1
        assert response_data[0]['title'] == "Wiredrive IOWA: Wiredrive Award Winners 2009"
        assert response_data[0]['description'] == \
               "https://iowa.wiredrive.com/present-library-gallery/token/e5d10087fd878ba5dc8ea7857495710b"
        assert response_data[0]['created_at'] == "Wed, 01 Jun 2016 00:00:00 -0000"

        response = self.app.get('/?credits_filter=angry&limit=1&sort_by=asc')
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert len(response_data) == 1
        assert int(response_data[0]['id']) == 1
        assert response_data[0]['title'] == "Wiredrive IOWA: Wiredrive Award Winners 2009"
        assert response_data[0]['description'] == \
               "https://iowa.wiredrive.com/present-library-gallery/token/e5d10087fd878ba5dc8ea7857495710b"
        assert response_data[0]['created_at'] == "Wed, 01 Jun 2016 00:00:00 -0000"

        response = self.app.get('/?credits_filter=asd&limit=1&sort_by=asc')
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert len(response_data) == 0

        response = self.app.get('/?credits_filter=asd&limit=1&sort_by=desc')
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert len(response_data) == 0

        response = self.app.get('/?credits_filter=asd&limit1=1&sort_by=asc')
        assert response.status_code == 400

        response = self.app.get('/?credits_filter=asd&limit1=1&sort_by1=asc')
        assert response.status_code == 400

        response = self.app.get('/?credits_filter1=asd&limit1=1&sort_by1=asc')
        assert response.status_code == 400

        response = self.app.get('/?credits_filter=Foz&limit=1&sort_by=asc')
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert len(response_data) == 1
        assert int(response_data[0]['id']) == 1
        assert response_data[0]['title'] == "Wiredrive IOWA: Wiredrive Award Winners 2009"
        assert response_data[0]['description'] == \
               "https://iowa.wiredrive.com/present-library-gallery/token/e5d10087fd878ba5dc8ea7857495710b"
        assert response_data[0]['created_at'] == "Wed, 01 Jun 2016 00:00:00 -0000"

        response = self.app.get('/?credits_filter=Foz&limit=2&sort_by=asc')
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert len(response_data) == 2
        assert int(response_data[0]['id']) == 1
        assert response_data[0]['title'] == "Wiredrive IOWA: Wiredrive Award Winners 2009"
        assert response_data[0]['description'] == \
               "https://iowa.wiredrive.com/present-library-gallery/token/e5d10087fd878ba5dc8ea7857495710b"
        assert response_data[0]['created_at'] == "Wed, 01 Jun 2016 00:00:00 -0000"

        response = self.app.get('/?credits_filter=Foz&limit=2&sort_by=desc')
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert len(response_data) == 2
        assert int(response_data[0]['id']) == 2
        assert response_data[0]['title'] == "Wiredrive IOWA: Wiredrive Award Winners 2010"
        assert response_data[0]['description'] == \
               "https://iowa.wiredrive.com/present-library-gallery/token/e5d10087fd878ba5dc8ea7857495710b1"
        assert response_data[0]['created_at'] == "Tue, 31 May 2016 00:00:00 -0000"

        response = self.app.get('/?credits_filter=Foz&limit=1&sort_by=desc')
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert len(response_data) == 1
        assert int(response_data[0]['id']) == 2
        assert response_data[0]['title'] == "Wiredrive IOWA: Wiredrive Award Winners 2010"
        assert response_data[0]['description'] == \
               "https://iowa.wiredrive.com/present-library-gallery/token/e5d10087fd878ba5dc8ea7857495710b1"
        assert response_data[0]['created_at'] == "Tue, 31 May 2016 00:00:00 -0000"

    # asset item

    def test_asset_item(self):
        response = self.app.get('/assets/3')
        assert response.status_code == 301

        response = self.app.get('/assets/3/')
        assert response.status_code == 500

        response = self.app.get('/assets/3/?sort_by=asc')
        assert response.status_code == 400

        response = self.app.get('/assets/1/')
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert int(response_data['id']) == 1
        assert response_data['title'] == "Wiredrive IOWA: Wiredrive Award Winners 2009"
        assert response_data['description'] == \
               "https://iowa.wiredrive.com/present-library-gallery/token/e5d10087fd878ba5dc8ea7857495710b"
        assert response_data['created_at'] == "Wed, 01 Jun 2016 00:00:00 -0000"

        response = self.app.get('/assets/2/')
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert int(response_data['id']) == 2
        assert response_data['title'] == "Wiredrive IOWA: Wiredrive Award Winners 2010"
        assert response_data['description'] == \
               "https://iowa.wiredrive.com/present-library-gallery/token/e5d10087fd878ba5dc8ea7857495710b1"
        assert response_data['created_at'] == "Tue, 31 May 2016 00:00:00 -0000"

    def test_asset_item_update(self):
        response = self.app.put('/assets/3/', data={
            'title': 'title1', 'description': 'description1', 'created_at': 'Mon, 01 Jun 2015 00:00:00'})
        assert response.status_code == 500

        response = self.app.put('/assets/1/', data={
            'title': 'title1', 'description': 'description1', 'created_at': 'Mon, 01 Jun 2015 00:00:00'})
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert int(response_data['id']) == 1
        assert response_data['title'] == "title1"
        assert response_data['description'] == "description1"
        assert response_data['created_at'] == "Mon, 01 Jun 2015 07:00:00 -0000"

        response = self.app.get('/assets/1/')
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert int(response_data['id']) == 1
        assert response_data['title'] == "title1"
        assert response_data['description'] == "description1"
        assert response_data['created_at'] == "Mon, 01 Jun 2015 07:00:00 -0000"

        response = self.app.get('/assets/')
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert int(response_data[1]['id']) == 1
        assert response_data[1]['title'] == "title1"
        assert response_data[1]['description'] == "description1"
        assert response_data[1]['created_at'] == "Mon, 01 Jun 2015 07:00:00 -0000"

    def test_asset_item_delete(self):
        response = self.app.delete('/assets/3/')
        assert response.status_code == 500

        response = self.app.delete('/assets/1/')
        assert response.status_code == 201

        response = self.app.get('/assets/1/')
        assert response.status_code == 500

        response = self.app.get('/assets/')
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert len(response_data) == 1

    def test_asset_item_create(self):
        response = self.app.post('/assets/', data={
            'title': 'title1',
            'description': 'description1',
            'created_at': 'Mon, 01 Jun 2015 00:00:00',
            "thumbnails": [
                "https://google.com",
                "https://yahoo.com",
            ],
            "credits_names": [
                "Tom Jones",
                "Jessica Alba",
            ],
        })
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert int(response_data['id']) == 3
        assert response_data['title'] == "title1"
        assert response_data['description'] == "description1"
        assert response_data['created_at'] == "Mon, 01 Jun 2015 07:00:00 -0000"
        assert len(response_data['thumbnails']) == 2
        assert response_data['thumbnails'][0]['image_url'] == "https://google.com"
        assert response_data['thumbnails'][1]['image_url'] == "https://yahoo.com"
        assert len(response_data['credits']) == 2

        response = self.app.get('/assets/3/credits/')
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert len(response_data) == 2

        response = self.app.get('/assets/')
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert len(response_data) == 3
        assert int(response_data[2]['id']) == 3
        assert response_data[2]['title'] == "title1"
        assert response_data[2]['description'] == "description1"
        assert response_data[2]['created_at'] == "Mon, 01 Jun 2015 07:00:00 -0000"
        assert len(response_data[2]['thumbnails']) == 2
        assert response_data[2]['thumbnails'][0]['image_url'] == "https://google.com"
        assert response_data[2]['thumbnails'][1]['image_url'] == "https://yahoo.com"
        assert len(response_data[2]['credits']) == 2

        response = self.app.delete('/assets/3/')
        assert response.status_code == 201

    # assets credits

    def test_asset_credits(self):
        response = self.app.get('/assets/3/credits/')
        assert response.status_code == 500

        response = self.app.get('/assets/1/credits/')
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert len(response_data) == 3
        assert response_data[0]["name"] == "Fozie Bear"
        assert response_data[1]["name"] == "Big Bird"
        assert response_data[2]["name"] == "Angry Tiger"

        response = self.app.get('/assets/2/credits/')
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert len(response_data) == 2
        assert response_data[0]["name"] == "Fozie Bear"
        assert response_data[1]["name"] == "Big Bird"

    # credits list

    def test_credits_list(self):
        response = self.app.get('/credits')
        assert response.status_code == 301

        response = self.app.get('/credits/')
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert len(response_data) == 3
        assert response_data[0]["name"] == "Angry Tiger"
        assert response_data[1]["name"] == "Big Bird"
        assert response_data[2]["name"] == "Fozie Bear"

        response = self.app.get('/credits/?limit1=1')
        assert response.status_code == 400

        response = self.app.get('/credits/?sort_by1=asc')
        assert response.status_code == 400

        response = self.app.get('/credits/?sort_by=1')
        assert response.status_code == 400

        response = self.app.get('/credits/?sort_by=1&limit=asd')
        assert response.status_code == 400

        response = self.app.get('/credits/?sort_by=asc&limit=1')
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert len(response_data) == 1
        assert response_data[0]["name"] == "Angry Tiger"

        response = self.app.get('/credits/?sort_by=desc&limit=1')
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert len(response_data) == 1
        assert response_data[0]["name"] == "Fozie Bear"

        response = self.app.get('/credits/?sort_by=asc&limit=2')
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert len(response_data) == 2
        assert response_data[0]["name"] == "Angry Tiger"
        assert response_data[1]["name"] == "Big Bird"

        response = self.app.get('/credits/?sort_by=asc&limit=-1')
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert len(response_data) == 3
        assert response_data[0]["name"] == "Angry Tiger"
        assert response_data[1]["name"] == "Big Bird"
        assert response_data[2]["name"] == "Fozie Bear"

        response = self.app.get('/credits/?sort_by=desc&limit=-1')
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert len(response_data) == 3
        assert response_data[0]["name"] == "Fozie Bear"
        assert response_data[1]["name"] == "Big Bird"
        assert response_data[2]["name"] == "Angry Tiger"

    def test_credits_create(self):
        response = self.app.post('/credits/', data={})
        assert response.status_code == 400

        response = self.app.post('/credits/', data={"name1": "name1"})
        assert response.status_code == 400

        response = self.app.post('/credits/', data={"name": "name1"})
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert int(response_data["id"]) == 4
        assert response_data["name"] == "name1"

        response = self.app.get('/credits/')
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert len(response_data) == 4
        assert response_data[0]["name"] == "Angry Tiger"
        assert response_data[1]["name"] == "Big Bird"
        assert response_data[2]["name"] == "Fozie Bear"
        assert response_data[3]["name"] == "name1"

        response = self.app.post('/credits/', data={"name": "name2"})
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert int(response_data["id"]) == 5
        assert response_data["name"] == "name2"

        response = self.app.get('/credits/')
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert len(response_data) == 5
        assert response_data[0]["name"] == "Angry Tiger"
        assert response_data[1]["name"] == "Big Bird"
        assert response_data[2]["name"] == "Fozie Bear"
        assert response_data[3]["name"] == "name1"
        assert response_data[4]["name"] == "name2"

    def test_delete_credits(self):
        response = self.app.delete('/credits/4/')
        assert response.status_code == 500

        response = self.app.delete('/credits/1/')
        assert response.status_code == 201

        response = self.app.get('/credits/1/')
        assert response.status_code == 500

        response = self.app.get('/credits/')
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert len(response_data) == 2

    def test_get_credits_item(self):
        response = self.app.get('/credits/3')
        assert response.status_code == 301

        response = self.app.get('/credits/4/')
        assert response.status_code == 500

        response = self.app.get('/credits/4/?sort_by=asc')
        assert response.status_code == 400

        response = self.app.get('/credits/3/?sort_by=asc')
        assert response.status_code == 400

        response = self.app.get('/credits/1/')
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert int(response_data["id"]) == 1
        assert response_data["name"] == "Fozie Bear"

        response = self.app.get('/credits/2/')
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert int(response_data["id"]) == 2
        assert response_data["name"] == "Big Bird"

        response = self.app.get('/credits/3/')
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert int(response_data["id"]) == 3
        assert response_data["name"] == "Angry Tiger"

    def test_update_credits_item(self):
        response = self.app.put('/credits/4/', data={'name': 'name1'})
        assert response.status_code == 500

        response = self.app.put('/credits/1/', data={'name': 'name1'})
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert int(response_data["id"]) == 1
        assert response_data["name"] == "name1"

        response = self.app.get('/credits/')
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert len(response_data) == 3
        assert int(response_data[0]["id"]) == 3
        assert int(response_data[1]["id"]) == 2
        assert int(response_data[2]["id"]) == 1
        assert response_data[0]["name"] == "Angry Tiger"
        assert response_data[1]["name"] == "Big Bird"
        assert response_data[2]["name"] == "name1"

        response = self.app.get('/credits/?sort_by=desc')
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert len(response_data) == 3
        assert int(response_data[0]["id"]) == 1
        assert int(response_data[1]["id"]) == 2
        assert int(response_data[2]["id"]) == 3
        assert response_data[0]["name"] == "name1"
        assert response_data[1]["name"] == "Big Bird"
        assert response_data[2]["name"] == "Angry Tiger"

    def test_credits_assets_list(self):
        response = self.app.get('/credits/4/assets/')
        assert response.status_code == 500

        response = self.app.get('/credits/1/assets')
        assert response.status_code == 301

        response = self.app.get('/credits/1/assets/')
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert len(response_data) == 2

        response = self.app.get('/credits/2/assets/')
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert len(response_data) == 2

        response = self.app.get('/credits/3/assets/')
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert len(response_data) == 1
        assert int(response_data[0]['id']) == 1
        assert response_data[0]['title'] == 'Wiredrive IOWA: Wiredrive Award Winners 2009'

if __name__ == '__main__':
    unittest.main()
