# -*- coding: utf-8 -*-
'''
Load the appropriate extraction module for the question type
and extract candidate answers for verification.

'''
# desc_def is not functional
from extractors.desc import desc_def
# desc_manner is not functional
from extractors.desc import desc_manner
# desc_reason is not functional
from extractors.desc import desc_reason
# desc_hum is not functional
from extractors.desc import desc_desc
# hum_desc is not functional
from extractors.hum import hum_desc
from extractors.hum import hum_ind
from extractors.hum import hum_ind_alchemy
from extractors.hum import hum_gr
from extractors.hum import hum_gr_alchemy
# hum_title is not functional
from extractors.hum import hum_title
from extractors.num import num_count
from extractors.loc import loc_planet
from extractors.loc import loc_continent
from extractors.loc import loc_island
from extractors.loc import loc_country
from extractors.loc import loc_state
from extractors.loc import loc_county
from extractors.loc import loc_airport
from extractors.loc import loc_ocean
from extractors.loc import loc_sea
from extractors.loc import loc_desert


class Answer_extractor:

    def __init__(self):
        hum_map_alchemy = {
            'desc': hum_desc,
            'gr': hum_gr_alchemy,
            'ind': hum_ind_alchemy,
            'title': hum_title,
        }

        hum_map = {
            'desc': hum_desc,
            'gr': hum_gr,
            'ind': hum_ind,
            'title': hum_title
        }

        loc_map = {
            'address': '',
            'airport': loc_airport,
            'artificial': '',
            'biome': '',
            'bodwat': '',
            'celestial_body': '',
            'city': '',
            'constellation': '',
            'continent': loc_continent,
            'coordinate': '',
            'country': loc_country,
            'county': loc_county,
            'desert': loc_desert,
            'direction': '',
            'island': loc_island,
            'lake': '',
            'mountain': '',
            'ocean': loc_ocean,
            'other': '',
            'park': '',
            'planet': loc_planet,
            'region': '',
            'restaurant': '',
            'retail': '',
            'river': '',
            'school': '',
            'sea': loc_sea,
            'source': '',
            'state': loc_state,
            'street': '',
            'vague': '',
            'web_address': ''
        }

        num_map = {
            'code': 'num_code',
            'count': num_count,
            'date': 'num_date',
            'dist': 'num_dist',
            'money': 'num_money',
            'ord': 'num_ord',
            'other': 'num_other',
            'perc': 'num_perc',
            'period': 'num_period',
            'speed': 'num_speed',
            'temp': 'num_temp',
            'volsize': 'num_volsize',
            'weight': 'num_weight'
        }

        abbr_map = {
            'abbr': 'hum_map',
            'exp': 'num_map',
        }

        desc_map = {
            'def': desc_def,
            'desc': desc_desc,
            'manner': desc_manner,
            'reason': desc_reason,
        }

        enty_map_alchemy = {
            'animal': '',
            'body': '',
            'color': '',
            'cremat': '',
            'currency': '',
            'dismed': '',
            'event': '',
            'food': '',
            'instru': '',
            'lang': '',
            'letter': '',
            'other': '',
            'plant': '',
            'product': '',
            'religion': '',
            'sport': '',
            'substance': '',
            'symbol': '',
            'techmeth': '',
            'termeq': '',
            'veh': '',
            'word': ''
        }

        enty_map = {
            'animal': '',
            'body': '',
            'color': '',
            'cremat': '',
            'currency': '',
            'dismed': '',
            'event': '',
            'food': '',
            'instru': '',
            'lang': '',
            'letter': '',
            'other': '',
            'plant': '',
            'product': '',
            'religion': '',
            'sport': '',
            'substance': '',
            'symbol': '',
            'techmeth': '',
            'termeq': '',
            'veh': '',
            'word': ''
        }

        self.extraction_map = {
            'abbr': abbr_map,
            'desc': desc_map,
            'enty': enty_map,
            'hum': hum_map,
            'loc': loc_map,
            'num': num_map,
        }

        self.extraction_map_alchemy = {
            'abbr': abbr_map,
            'desc': desc_map,
            'enty': enty_map_alchemy,
            'hum': hum_map_alchemy,
            'loc': loc_map,
            'num': num_map,
        }

    def extract_answers(self, tokens,
                        pos_tagged_documents, ranked_docs,
                        coarse, fine, keywordsList, use_alchemy):
        if not use_alchemy:
            extractor = self.extraction_map[coarse][fine]
            ranked_answers = extractor.extract(
                tokens, pos_tagged_documents, ranked_docs)
        else:
            print('using alchemy api')
            extractor = self.extraction_map_alchemy[coarse][fine]
            ranked_answers = extractor.extract(
                tokens, pos_tagged_documents, ranked_docs)
        return ranked_answers