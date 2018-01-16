from django.apps import AppConfig

class FetchApiConfig(AppConfig):
    name = 'fetch_api'

    def ready(self):
        from paradise_papers_search.constants import COUNTRIES, JURISDICTIONS
